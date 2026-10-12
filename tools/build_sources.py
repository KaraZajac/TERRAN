#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the source records in sources/*.yaml and generate SOURCES.md.

    python3 tools/build_sources.py           validate, then write SOURCES.md
    python3 tools/build_sources.py --check   validate; exit 1 if SOURCES.md is stale

A source cited by several research notes can appear in several YAML files.
Records with the same id are merged: the first file's details are kept and
gaps filled from the others, their Charter parts and "supports" lines are
combined, and the strongest check result is kept. Every [author/2024_slug]
citation in the research notes, thoughts and open questions, alone or grouped
as [id; id], must resolve to a record.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / "sources"
OUTPUT = ROOT / "SOURCES.md"
CITING_GLOBS = ("research/*.md", "thoughts/*.md", "OPEN-QUESTIONS.md")

PARTS = {
    "Preamble": "Preamble",
    "I": "Part I — Terrans",
    "II": "Part II — The Seven Principles",
    "III": "Part III — The Floor and the Ceiling",
    "IV": "Part IV — The Culture of Enough",
    "V": "Part V — Business",
    "VI": "Part VI — A Utopia of Utopias",
    "VII": "Part VII — Working Together",
    "VIII": "Part VIII — How Terrans Decide",
    "IX": "Part IX — Accountability",
    "X": "Part X — The Long View",
    "XI": "Part XI — A Living Charter",
    "XII": "Part XII — Becoming the Commonwealth",
    "OQ": "Open questions",
}
PART_ORDER = list(PARTS)
TIERS = ("primary", "secondary", "tertiary")
KINDS = ("book", "article", "report", "law", "treaty", "court", "dataset", "web", "news")
RESULTS = ("verified", "partial", "unverified")  # strongest first

SLUG = r"[a-z0-9][a-z0-9-]*/[0-9]{4}[a-z]?_[a-z0-9][a-z0-9-]*"
ID_RE = re.compile(rf"^{SLUG}$")
BRACKET_RE = re.compile(r"\[([^\[\]\n]+)\]")
DATE_RE = re.compile(r"^[0-9]{4}(-[0-9]{2}(-[0-9]{2})?)?$")


def text(value) -> str:
    """YAML turns unquoted dates and years into date and int objects; keep them as text."""
    return "" if value is None else str(value).strip()


def present(value) -> bool:
    if isinstance(value, (list, dict)):
        return bool(value)
    return bool(text(value))


def checked_on(checked: dict) -> str:
    # YAML 1.1 reads a bare `on:` key as the boolean true.
    return text(checked.get("on", checked.get(True)))


def check_record(rec: dict, where: str, errors: list[str], warnings: list[str]) -> None:
    rid = text(rec.get("id"))
    if not rid:
        errors.append(f"{where}: missing id")
        return
    where = f"{where} {rid}"
    if not ID_RE.match(rid):
        warnings.append(f"{where}: id doesn't follow <author>/<year>_<slug>")
    if not text(rec.get("title")):
        errors.append(f"{where}: missing title")
    if not text(rec.get("url")):
        warnings.append(f"{where}: no url")
    date = text(rec.get("date"))
    if date and not DATE_RE.match(date):
        warnings.append(f"{where}: date {date!r} isn't YYYY, YYYY-MM or YYYY-MM-DD")
    if rec.get("tier") not in TIERS:
        errors.append(f"{where}: tier must be one of {', '.join(TIERS)}")
    if rec.get("kind") not in KINDS:
        errors.append(f"{where}: kind must be one of {', '.join(KINDS)}")
    parts = rec.get("parts")
    if not isinstance(parts, list) or not parts:
        errors.append(f"{where}: parts must be a non-empty list")
    elif unknown := [p for p in parts if text(p) not in PARTS]:
        errors.append(f"{where}: unknown parts {unknown}")
    checked = rec.get("checked")
    if not isinstance(checked, dict):
        errors.append(f"{where}: missing checked block")
        return
    if not text(checked.get("by")):
        errors.append(f"{where}: checked.by is required")
    if not checked_on(checked):
        errors.append(f"{where}: checked.on is required")
    if checked.get("result") not in RESULTS:
        errors.append(f"{where}: checked.result must be one of {', '.join(RESULTS)}")


def load(errors: list[str], warnings: list[str]) -> dict[str, dict]:
    merged: dict[str, dict] = {}
    files: dict[str, set[str]] = defaultdict(set)
    for path in sorted(SOURCES_DIR.glob("*.yaml")):
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            errors.append(f"{path.name}: invalid YAML: {exc}")
            continue
        if data is None:
            continue
        if not isinstance(data, list):
            errors.append(f"{path.name}: expected a list of records")
            continue
        for i, rec in enumerate(data):
            where = f"{path.name}[{i}]"
            if not isinstance(rec, dict):
                errors.append(f"{where}: not a mapping")
                continue
            before = len(errors)
            check_record(rec, where, errors, warnings)
            if len(errors) > before:
                continue
            rid = text(rec["id"])
            parts = [text(p) for p in rec["parts"]]
            files[rid].add(path.name)
            if rid not in merged:
                merged[rid] = dict(rec, parts=parts)
                continue
            base = merged[rid]
            if text(base.get("url")).rstrip("/") != text(rec.get("url")).rstrip("/"):
                warnings.append(f"{where} {rid}: same id as another record but a different url")
            for key, value in rec.items():
                if key not in ("id", "parts", "supports", "checked") and present(value) and not present(base.get(key)):
                    base[key] = value
            supports = text(rec.get("supports"))
            if supports and supports not in text(base.get("supports")):
                base["supports"] = "; ".join(s for s in (text(base.get("supports")), supports) if s)
            if RESULTS.index(rec["checked"]["result"]) < RESULTS.index(base["checked"]["result"]):
                base["checked"] = rec["checked"]
            base["parts"] = base["parts"] + parts
    for rid, rec in merged.items():
        rec["parts"] = sorted(set(rec["parts"]), key=PART_ORDER.index)
        rec["files"] = sorted(files[rid])

    by_url: dict[str, set[str]] = defaultdict(set)
    for rid, rec in merged.items():
        if url := text(rec.get("url")).rstrip("/"):
            by_url[url].add(rid)
    for url, ids in sorted(by_url.items()):
        if len(ids) > 1:
            warnings.append(f"one url under {len(ids)} ids ({', '.join(sorted(ids))}): {url}")
    return merged


def citations() -> dict[str, set[str]]:
    """Ids cited as [id], or grouped as [id; id] or [id, id]."""
    cited: dict[str, set[str]] = defaultdict(set)
    for pattern in CITING_GLOBS:
        for path in sorted(ROOT.glob(pattern)):
            for group in BRACKET_RE.findall(path.read_text(encoding="utf-8")):
                for token in re.split(r"[;,]\s*", group):
                    if ID_RE.match(token.strip()):
                        cited[token.strip()].add(path.relative_to(ROOT).as_posix())
    return cited


def anchor(heading: str) -> str:
    """GitHub's heading anchors: lowercase, punctuation dropped, spaces to hyphens."""
    return re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")


def escape(value: str) -> str:
    return re.sub(r"([\\\[\]*])", r"\\\1", value)


def link_target(url: str) -> str:
    return f"<{url}>" if re.search(r"[\s()<>]", url) else url


def authors(rec: dict) -> str:
    names = [text(a) for a in rec.get("authors") or [] if text(a)]
    if len(names) > 3:
        return f"{names[0]} et al."
    return ", ".join(names)


def entry(rec: dict, cited_in: set[str]) -> str:
    title = f"**{escape(text(rec['title']))}**"
    url = text(rec.get("url"))
    head = f"[{title}]({link_target(url)})" if url else title
    byline = " · ".join(x for x in (authors(rec), text(rec.get("publisher")), text(rec.get("date"))) if x)
    checked = rec["checked"]
    status = f"{checked['result']} {checked_on(checked)} by {text(checked['by'])}"
    if checked["result"] != "verified" and (note := text(checked.get("note"))):
        status += f": {note}"
    meta = [f"`{rec['id']}`", rec["tier"], rec["kind"], status]
    if cited_in:
        meta.append("cited in " + ", ".join(f"[{Path(f).stem}]({f})" for f in sorted(cited_in)))
    lines = [f"- {head}" + (f" — {byline}" if byline else "") + "  "]
    if supports := text(rec.get("supports")):
        lines.append(f"  {supports}  ")
    lines.append(f"  <sub>{' · '.join(meta)}</sub>")
    return "\n".join(lines)


def render(records: dict[str, dict], cited: dict[str, set[str]]) -> str:
    tiers = Counter(r["tier"] for r in records.values())
    results = Counter(r["checked"]["result"] for r in records.values())
    by_part: dict[str, list[dict]] = defaultdict(list)
    for rec in records.values():
        for part in rec["parts"]:
            by_part[part].append(rec)

    out = [
        "# TERRAN — sources",
        "",
        f"Every source cited in the research behind the Terran Charter: {len(records)} records, "
        "grouped by the Part of the Charter they inform. Generated from `sources/*.yaml` by "
        "`tools/build_sources.py`; do not edit by hand.",
        "",
        f"**Tiers:** {tiers['primary']} primary · {tiers['secondary']} secondary · "
        f"{tiers['tertiary']} tertiary. **Checks:** {results['verified']} verified · "
        f"{results['partial']} partial · {results['unverified']} unverified.",
        "",
        "Every check names who made it and when. *Verified* means the cited claim was found on "
        "the fetched page; *partial* means only part of it, or only an abstract or landing page, "
        "could be confirmed; *unverified* means the page could not be opened. Checks by `claude` "
        "are machine-performed and are not Kara's own verification.",
        "",
        " · ".join(
            f"[{'Open questions' if p == 'OQ' else p}](#{anchor(PARTS[p])}) {len(by_part[p])}"
            for p in PART_ORDER
            if by_part[p]
        ),
    ]
    for part in PART_ORDER:
        if not by_part[part]:
            continue
        out += ["", f"## {PARTS[part]}", ""]
        for rec in sorted(by_part[part], key=lambda r: r["id"]):
            out.append(entry(rec, cited.get(rec["id"], set())))
    return "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="fail if SOURCES.md is out of date")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    records = load(errors, warnings)
    cited = citations()
    for rid in sorted(set(cited) - set(records)):
        errors.append(f"cited but no record: [{rid}] in {', '.join(sorted(cited[rid]))}")
    uncited = sorted(set(records) - set(cited))
    if uncited:
        warnings.append(f"{len(uncited)} records not cited anywhere: {', '.join(uncited)}")

    for message in warnings:
        print(f"warning: {message}", file=sys.stderr)
    for message in errors:
        print(f"error: {message}", file=sys.stderr)
    if errors:
        print(f"{len(errors)} errors; SOURCES.md not written", file=sys.stderr)
        return 1

    rendered = render(records, cited)
    if args.check:
        current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if current != rendered:
            print("SOURCES.md is out of date; run `make sources`", file=sys.stderr)
            return 1
        print(f"ok: {len(records)} records, SOURCES.md up to date")
        return 0
    OUTPUT.write_text(rendered, encoding="utf-8")
    print(f"wrote SOURCES.md: {len(records)} records from {len(list(SOURCES_DIR.glob('*.yaml')))} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
