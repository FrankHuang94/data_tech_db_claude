#!/usr/bin/env python3
"""Generate repo-root glossary.md from the canonical docs/glossary.md.

docs/glossary.md links to chapters as `01-data-systems-foundations/ch03-….md`;
at the repo root those links must be prefixed with `docs/`.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
src = (ROOT / "docs" / "glossary.md").read_text(encoding="utf-8")
banner = "<!-- GENERATED from docs/glossary.md by scripts/sync_root_files.py: do not edit here. -->\n"


def fix(m: re.Match) -> str:
    target = m.group(2)
    if re.match(r"^(https?:|mailto:|#)", target):
        return m.group(0)
    return f"{m.group(1)}(docs/{target})"


out = re.sub(r"(\[[^\]]*\])\(([^)\s]+)\)", fix, src)
(ROOT / "glossary.md").write_text(banner + out, encoding="utf-8")
print("glossary.md regenerated")
