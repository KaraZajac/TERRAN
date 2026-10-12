#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Check the numbers in the Articles of Terra against schedules/numbers.yaml,
and generate Schedule 1 (Safeguards) and Schedule 2 (Settings) from it.

    python3 tools/build_schedules.py           check, then write both Schedules
    python3 tools/build_schedules.py --check   check; exit 1 if a Schedule is stale

Every number in the Articles is a reference link to its entry, such as
[1,000][panel-size], with a matching definition at the foot of the file.
Numbers inside a Mermaid diagram are declared in a comment just above it:
<!-- numbers: rejected-wait="two years" -->. The check makes sure that:

- every link and declaration names an entry, and every link's definition
  points at the Schedule that holds that entry;
- the number the text shows says the same as the entry's value;
- every entry with a value is used in the Articles, and every entry without
  one says where the Articles need it;
- every setting's value sits inside its allowed range.
"""

from __future__ import annotations

import argparse
import re
import sys
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "schedules" / "numbers.yaml"
ARTICLES = ROOT / "articles"

ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
LINK_RE = re.compile(r"\[([^\[\]\n]+)\]\[([a-z0-9-]+)\]")
DEF_RE = re.compile(r"^\[([a-z0-9-]+)\]: (\S+)\s*$")
CLAUSE_RE = re.compile(r"^(\d+)\. \*\*")
ARTICLE_RE = re.compile(r"^# Article (\d+) — (.+)$")
DECLARE_RE = re.compile(r"<!-- numbers: (.*?) -->")
PAIR_RE = re.compile(r'([a-z0-9-]+)="([^"]+)"')

WORDS = {
    "a": 1, "an": 1, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "twenty-one": 21, "twenty-five": 25, "thirty": 30,
    "forty": 40, "fifty": 50, "hundred": 100,
}
FRACTIONS = {
    "half": Fraction(1, 2), "a third": Fraction(1, 3), "two-thirds": Fraction(2, 3),
    "a quarter": Fraction(1, 4), "three-quarters": Fraction(3, 4),
    "a fifth": Fraction(1, 5), "a sixth": Fraction(1, 6), "a tenth": Fraction(1, 10),
    "nine in ten": Fraction(9, 10),
}
SUFFIXES = (
    "of terrans of voting age", "of the regions", "of the council", "of the board",
    "of humanity", "the lowest pay", "terrans", "members", "delegates", "signatures",
    "judges", "stewards", "days", "day", "months", "month", "years", "year", "times", "points",
)


def quantity(phrase: str) -> float | None:
    """Read the number a phrase in the text states: '1,000', 'six-year', 'a quarter of the regions'."""
    s = phrase.strip().lower().replace(",", "").replace("$", "")
    s = re.sub(r"-(year|month|day)\b", r" \1", s)
    stripped = True
    while stripped:
        stripped = False
        for suffix in SUFFIXES:
            if s.endswith(" " + suffix):
                s, stripped = s[: -len(suffix) - 1].rstrip(), True
    s = s.replace("one-million", "one million")
    if s in FRACTIONS:
        return float(FRACTIONS[s])
    m = re.fullmatch(r"(\d+(?:\.\d+)?)%", s)
    if m:
        return float(m.group(1)) / 100
    m = re.fullmatch(r"(\S+) million", s)
    if m:
        base = quantity(m.group(1))
        return None if base is None else base * 1_000_000
    if re.fullmatch(r"\d+(?:\.\d+)?", s):
        return float(s)
    return float(WORDS[s]) if s in WORDS else None


def same(a: float, b: float) -> bool:
    return math.isclose(a, b, rel_tol=1e-3)


def load() -> tuple[dict, list[dict], list[str]]:
    data = yaml.safe_load(DATA.read_text())
    errors: list[str] = []
    schedules = data.get("schedules") or {}
    for key in ("safeguards", "settings"):
        sched = schedules.get(key)
        if not sched or not all(sched.get(f) for f in ("file", "title", "intro")):
            errors.append(f"schedules.{key}: needs file, title and intro")
    seen = set()
    for i, n in enumerate(data.get("numbers") or []):
        where = n.get("id") or f"entry {i + 1}"
        for field in ("id", "schedule", "name", "show", "why"):
            if not n.get(field):
                errors.append(f"{where}: missing {field}")
        if n.get("id") and not ID_RE.match(n["id"]):
            errors.append(f"{where}: id must be lowercase letters, digits and hyphens")
        if n.get("id") in seen:
            errors.append(f"{where}: duplicate id")
        seen.add(n.get("id"))
        if n.get("schedule") not in ("safeguards", "settings"):
            errors.append(f"{where}: schedule must be safeguards or settings")
        value = n.get("value")
        if value is None:
            if not n.get("where"):
                errors.append(f"{where}: an entry without a value must say where the Articles need it")
            continue
        q = quantity(str(n.get("show", "")))
        if q is None or not same(q, float(value)):
            errors.append(f"{where}: shown as {n.get('show')!r}, which doesn't read as {value}")
        if n.get("schedule") == "settings":
            lo, hi = n.get("min"), n.get("max")
            if lo is None or hi is None or not n.get("range"):
                errors.append(f"{where}: a setting needs min, max and range")
            elif not lo <= value <= hi:
                errors.append(f"{where}: value {value} is outside its range {lo}–{hi}")
        elif not n.get("range"):
            errors.append(f"{where}: missing range")
    return schedules, data.get("numbers") or [], errors


def scan(numbers: list[dict], schedules: dict) -> tuple[dict, dict, list[str]]:
    """Find every use of a number in the Articles, and check each one."""
    by_id = {n["id"]: n for n in numbers if n.get("id")}
    uses: dict[str, list[tuple[int, str]]] = defaultdict(list)
    titles: dict[int, str] = {}
    errors: list[str] = []
    for path in sorted(ARTICLES.glob("[0-9]*.md")):
        lines = path.read_text().splitlines()
        defs = {m.group(1): m.group(2) for line in lines if (m := DEF_RE.match(line))}
        article, clause, in_diagram, declared = None, None, False, []
        for lineno, line in enumerate(lines, 1):
            at = f"{path.relative_to(ROOT)}:{lineno}"
            if m := ARTICLE_RE.match(line):
                article = int(m.group(1))
                titles[article] = m.group(2)
            if m := CLAUSE_RE.match(line):
                clause = m.group(1)
            if m := DECLARE_RE.search(line):
                declared = PAIR_RE.findall(m.group(1))
                if not declared:
                    errors.append(f"{at}: empty numbers declaration")
            if line.startswith("```mermaid"):
                in_diagram, diagram = True, []
                continue
            if in_diagram:
                if line.startswith("```"):
                    in_diagram = False
                    body = "\n".join(diagram)
                    for nid, shown in declared:
                        check_use(nid, shown, at, by_id, errors)
                        if shown not in body:
                            errors.append(f"{at}: the diagram doesn't show {shown!r} for {nid}")
                        uses[nid].append((article, f"{article} (diagram)"))
                    declared = []
                else:
                    diagram.append(line)
                continue
            if DEF_RE.match(line):
                continue
            for m in LINK_RE.finditer(line):
                shown, nid = m.group(1), m.group(2)
                check_use(nid, shown, at, by_id, errors)
                entry = by_id.get(nid)
                target = defs.get(nid)
                if entry and schedules.get(entry.get("schedule")):
                    want = f"../schedules/{schedules[entry['schedule']]['file']}#{nid}"
                    if target != want:
                        errors.append(f"{at}: [{nid}] should be defined as {want}, not {target}")
                ref = f"{article}.{clause}" if clause else f"{article} (diagram)"
                uses[nid].append((article, ref))
        if declared:
            errors.append(f"{path.relative_to(ROOT)}: a numbers declaration with no diagram after it")
    for n in numbers:
        if n.get("value") is not None and n.get("id") not in uses:
            errors.append(f"{n.get('id')}: has a value but the Articles never use it")
        if n.get("value") is None and n.get("id") in uses:
            errors.append(f"{n.get('id')}: the Articles link to it, but it has no value")
    return uses, titles, errors


def check_use(nid: str, shown: str, at: str, by_id: dict, errors: list[str]) -> None:
    entry = by_id.get(nid)
    if entry is None:
        errors.append(f"{at}: no Schedule entry {nid!r}")
        return
    if entry.get("value") is None:
        return
    q = quantity(shown)
    if q is None or not same(q, float(entry["value"])):
        errors.append(f"{at}: shows {shown!r} for {nid}, but its value is {entry['value']}")


def cell(text) -> str:
    return " ".join(str(text).split()).replace("|", "\\|")


def render(key: str, schedules: dict, numbers: list[dict], uses: dict, titles: dict) -> str:
    sched = schedules[key]
    rows = [n for n in numbers if n.get("schedule") == key]

    def refs_of(n):
        """Clause references first, so an entry files under the clause that defines it."""
        refs = [r for _, r in uses.get(n["id"], [])] or [str(w) for w in n.get("where", [])]
        clauses = [r for r in refs if "." in r]
        return clauses or refs

    def order(n):
        major, _, minor = refs_of(n)[0].split(" ")[0].partition(".")
        return (int(major), int(minor or 0))

    def home(n):
        return order(n)[0]

    groups: dict[int, list[dict]] = defaultdict(list)
    for n in sorted(rows, key=order):
        groups[home(n)].append(n)

    range_head = "Allowed range" if key == "settings" else "Sensible range"
    out = [
        f"# {sched['title']}",
        "",
        f"*Generated from [numbers.yaml](numbers.yaml) by `make schedules`: edit the YAML, not this file · "
        f"[All Schedules](README.md) · [The Terran Charter](../CHARTER.md)*",
        "",
        " ".join(str(sched["intro"]).split()),
    ]
    for article in sorted(groups):
        title = titles.get(article, "")
        out += ["", f"## Article {article} — {title}", "",
                f"| Number | Value | {range_head} | Used in | Why |",
                "| --- | --- | --- | --- | --- |"]
        for n in groups[article]:
            refs = list(dict.fromkeys(r for _, r in uses.get(n["id"], []))) or [str(w) for w in n.get("where", [])]
            refs = [r for r in refs if "." in r] + [r for r in refs if "." not in r]
            value = cell(n["show"]) if n.get("value") is not None else "Not yet set"
            out.append(f"| <a id=\"{n['id']}\"></a>{cell(n['name'])} | {value} | {cell(n.get('range', '—'))} | "
                       f"{', '.join(refs)} | {cell(n['why'])} |")
    return "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="fail if a Schedule is out of date")
    args = parser.parse_args()

    schedules, numbers, errors = load()
    uses, titles, scan_errors = scan(numbers, schedules)
    errors += scan_errors
    for e in errors:
        print(f"error: {e}", file=sys.stderr)
    if errors:
        return 1

    stale = []
    for key in ("safeguards", "settings"):
        path = ROOT / "schedules" / schedules[key]["file"]
        text = render(key, schedules, numbers, uses, titles)
        if args.check:
            if not path.exists() or path.read_text() != text:
                stale.append(path.relative_to(ROOT))
        else:
            path.write_text(text)
    if stale:
        print(f"error: out of date: {', '.join(map(str, stale))}; run make schedules", file=sys.stderr)
        return 1
    counts = {k: sum(1 for n in numbers if n.get("schedule") == k) for k in ("safeguards", "settings")}
    unset = sum(1 for n in numbers if n.get("value") is None)
    linked = sum(len(v) for v in uses.values())
    print(f"{counts['safeguards']} safeguards and {counts['settings']} settings ({unset} not yet set); "
          f"{linked} uses in the Articles checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
