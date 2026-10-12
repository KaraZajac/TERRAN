#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Check that every relative link in the repository's Markdown resolves.

    python3 tools/check_links.py

A link resolves when its file exists and, if it names an anchor, the file has a
heading or an <a id="..."> with that anchor. Web links are not fetched; the
source records track those. Exits 1 if any link is broken.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CODE_RE = re.compile(r"```.*?```", re.S)
INLINE_RE = re.compile(r"\]\((<[^>\n]+>|[^)\s]+)\)")
REFDEF_RE = re.compile(r"(?m)^\[[^\]\n]+\]: (\S+)")
HEADING_RE = re.compile(r"(?m)^#{1,6} (.+)$")
ANCHOR_RE = re.compile(r'<a id="([^"]+)"></a>')
SCHEME_RE = re.compile(r"^[a-z][a-z0-9+.-]*:", re.I)

_anchors: dict[Path, set[str]] = {}


def slug(heading: str) -> str:
    """The anchor a forge gives a heading: lowercase, punctuation dropped, spaces to hyphens."""
    s = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return s.replace(" ", "-")


def anchors(path: Path) -> set[str]:
    if path not in _anchors:
        text = CODE_RE.sub("", path.read_text())
        _anchors[path] = {slug(h) for h in HEADING_RE.findall(text)} | set(ANCHOR_RE.findall(text))
    return _anchors[path]


def main() -> int:
    broken, checked = [], 0
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        text = CODE_RE.sub("", md.read_text())
        for target in INLINE_RE.findall(text) + REFDEF_RE.findall(text):
            target = target.strip("<>")
            if SCHEME_RE.match(target):
                continue
            checked += 1
            path, _, frag = target.partition("#")
            dest = (md.parent / path).resolve() if path else md
            where = md.relative_to(ROOT)
            if not dest.exists():
                broken.append(f"{where}: no such file: {target}")
            elif frag and dest.suffix == ".md" and frag not in anchors(dest):
                broken.append(f"{where}: no such anchor: {target}")
    for b in broken:
        print(f"error: {b}", file=sys.stderr)
    if broken:
        return 1
    print(f"ok: {checked} links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
