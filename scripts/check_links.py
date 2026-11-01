#!/usr/bin/env python3
"""Check internal Markdown links and anchors across the repo.

Checks every relative link in README.md, glossary.md and docs/**/*.md:
- the target file exists;
- if an #anchor is given, a heading (or explicit id / <a name>) with that slug exists.
External links (http/https/mailto) are skipped. Exit code 1 on any broken link.

Usage: scripts/check_links.py [files…]
"""
from __future__ import annotations

import re
import sys
import unicodedata
from urllib.parse import unquote
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def slugify(text: str) -> str:
    """GitHub-style slug (close to MkDocs toc default when using slugify=github style)."""
    text = re.sub(r"\{#([^}]+)\}", "", text)  # attr-list ids handled separately
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.strip().lower()
    text = unicodedata.normalize("NFKD", text)
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


@lru_cache(maxsize=None)
def anchors(path: Path) -> set[str]:
    out: set[str] = set()
    counts: dict[str, int] = {}
    in_fence = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING_RE.match(line)
        if m:
            raw = m.group(2)
            for explicit in re.findall(r"\{#([^}]+)\}", raw):
                out.add(explicit)
            s = slugify(raw)
            n = counts.get(s, 0)
            out.add(s if n == 0 else f"{s}-{n}")
            counts[s] = n + 1
        for a in re.findall(r"<a\s+(?:name|id)=\"([^\"]+)\"", line):
            out.add(a)
        for a in re.findall(r"\{#([^}]+)\}", line):
            out.add(a)
    return out


def iter_links(path: Path):
    in_fence = False
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for rx in (LINK_RE, IMG_RE):
            for m in rx.finditer(line):
                yield i, m.group(1)


def main() -> int:
    files = [Path(a).resolve() for a in sys.argv[1:]] or (
        [ROOT / "README.md", ROOT / "glossary.md"] + sorted((ROOT / "docs").rglob("*.md"))
    )
    broken = 0
    checked = 0
    for f in files:
        if not f.exists():
            continue
        for line, target in iter_links(f):
            if re.match(r"^(https?:|mailto:|tel:)", target):
                continue
            checked += 1
            target_path, _, anchor = target.partition("#")
            target_path = unquote(target_path)
            dest = f if not target_path else (f.parent / target_path).resolve()
            if not dest.exists():
                print(f"BROKEN {f.relative_to(ROOT)}:{line} → {target} (missing file)")
                broken += 1
                continue
            if anchor and dest.suffix == ".md" and anchor not in anchors(dest):
                print(f"BROKEN {f.relative_to(ROOT)}:{line} → {target} (missing anchor)")
                broken += 1
    print(f"Link check: {checked} internal links, {broken} broken.")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
