#!/usr/bin/env python3
"""Merge drafter staging files into the canonical data/ CSVs and meta registers.

- data/staging/*ma_deals*.csv, ma_20*.csv -> data/ma_deals.csv        key: date|acquirer|target
- data/staging/*private_funding*.csv       -> data/private_funding.csv key: company|date|round
- data/staging/*public_comps*.csv          -> data/public_comps.csv    key: ticker (latest as_of wins)
- data/staging/*company_financials*.csv    -> data/company_financials.csv key: company|fiscal_period|metric
- meta/staging/*-open-questions.md         -> appended to meta/open-questions.md
- meta/staging/*-decisions.md              -> appended to meta/decisions.md
- meta/staging/*-glossary.md               -> meta/glossary-terms.md (term registry used to build docs/glossary.md)

Rows whose notes/outcome contain "CORRECTION" replace an existing row with the same key.
Processed files are moved to */staging/merged/. Run with --dry-run to preview.
"""
from __future__ import annotations

import csv
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA, DST, MST = ROOT / "data", ROOT / "data" / "staging", ROOT / "meta" / "staging"
DRY = "--dry-run" in sys.argv

SPECS = {
    "ma_deals": (("date", "acquirer", "target"), ["*ma_deals*.csv", "ma_20*.csv"]),
    "private_funding": (("company", "date", "round"), ["*private_funding*.csv"]),
    "public_comps": (("ticker",), ["*public_comps*.csv"]),
    "company_financials": (("company", "fiscal_period", "metric"), ["*company_financials*.csv"]),
}


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def read(path: Path) -> tuple[list[str], list[dict]]:
    with path.open(newline="", encoding="utf-8") as fh:
        r = csv.DictReader(fh)
        return list(r.fieldnames or []), [dict(row) for row in r]


def move(p: Path) -> None:
    if DRY:
        return
    dest = p.parent / "merged"
    dest.mkdir(exist_ok=True)
    shutil.move(str(p), dest / p.name)


def merge_csvs() -> None:
    for name, (key, globs) in SPECS.items():
        main = DATA / f"{name}.csv"
        header, rows = read(main)
        index = {"|".join(norm(r.get(k, "")) for k in key): i for i, r in enumerate(rows)}
        files = sorted({p for g in globs for p in DST.glob(g)})
        added = replaced = 0
        for f in files:
            _, new = read(f)
            for r in new:
                r = {h: (r.get(h) or "").strip() for h in header}
                if not any(r.values()):
                    continue
                k = "|".join(norm(r.get(x, "")) for x in key)
                corr = "CORRECTION" in " ".join(r.values()).upper()
                if k in index:
                    i = index[k]
                    newer = name == "public_comps" and r.get("as_of", "") > rows[i].get("as_of", "")
                    if corr or newer:
                        rows[i] = r
                        replaced += 1
                    continue
                index[k] = len(rows)
                rows.append(r)
                added += 1
            move(f)
        sort_key = {"ma_deals": "date", "private_funding": "date"}.get(name)
        if sort_key:
            rows.sort(key=lambda r: r.get(sort_key, ""))
        if not DRY:
            with main.open("w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=header)
                w.writeheader()
                w.writerows(rows)
        print(f"{name:20} files={len(files):2} added={added:3} replaced={replaced:3} total={len(rows)}")


def merge_md() -> None:
    oq = sorted(MST.glob("*-open-questions.md"))
    dec = sorted(MST.glob("*-decisions.md"))
    gl = sorted(MST.glob("*-glossary.md"))
    if oq and not DRY:
        with (ROOT / "meta" / "open-questions.md").open("a", encoding="utf-8") as fh:
            for f in oq:
                ch = f.name.split("-")[0]
                for line in f.read_text(encoding="utf-8").splitlines():
                    line = line.strip().lstrip("-* ").strip()
                    if line and not line.startswith("#"):
                        fh.write(f"| {ch} | {line.replace('|', '/')} | open |\n")
                move(f)
    if dec and not DRY:
        with (ROOT / "meta" / "decisions.md").open("a", encoding="utf-8") as fh:
            for f in dec:
                ch = f.name.split("-")[0]
                for line in f.read_text(encoding="utf-8").splitlines():
                    line = line.strip().lstrip("-* ").strip()
                    if line and not line.startswith("#"):
                        fh.write(f"| {ch} | 2026-11-01 | {line.replace('|', '/')} | drafter judgment |\n")
                move(f)
    reg = ROOT / "meta" / "glossary-terms.md"
    existing = reg.read_text(encoding="utf-8") if reg.exists() else "# Glossary term registry (merged from drafters)\n\n"
    seen = {norm(m) for m in re.findall(r"^- \*\*(.+?)\*\*", existing, flags=re.M)}
    added = 0
    for f in gl:
        for line in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\s*[-*]\s*\*\*(.+?)\*\*\s*[—–-]+\s*(.+)$", line)
            if m and norm(m.group(1)) not in seen:
                seen.add(norm(m.group(1)))
                existing += f"- **{m.group(1).strip()}** — {m.group(2).strip()}\n"
                added += 1
        move(f)
    if not DRY:
        reg.write_text(existing, encoding="utf-8")
    print(f"open-questions files={len(oq)} decisions files={len(dec)} glossary files={len(gl)} new terms={added} total terms={len(seen)}")


if __name__ == "__main__":
    merge_csvs()
    merge_md()
