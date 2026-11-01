# Chapter-drafter brief (read fully before writing)

You are drafting one or more chapters of the **AI Data Atlas** (repo root: `/home/user/data_tech_db_claude`). Today is **2026-11-01**. Your training data is stale for anything after mid-2025: **research every current fact live** with WebSearch/WebFetch.

## 1. Read first (in this order)

1. `CLAUDE.md` — standing rules (accuracy, sourcing, labels, copyright, public-info-only, voice).
2. `meta/style-guide.md` — voice, number labels, fiscal years, Mermaid hygiene, captions, palette, links.
3. `meta/templates.md` — the mandatory template for your chapter type, footnote format, callout format.
4. `meta/outline.md` — every chapter's file path (use these for cross-links), budgets and planned visuals.
5. `meta/research-briefing.md` and `meta/research-notes-*.md` — verified current-state facts from the Phase 0 sweep. Treat them as a starting point; re-verify anything central to your chapter.
6. `data/*.csv` — the single source of truth for numbers (comps, funding, M&A, financials, market sizes). When your chapter cites a number that is in a CSV, use the CSV value and its source.
7. If they exist, the two quality-bar chapters: `docs/01-data-systems-foundations/ch07-open-table-formats.md` (concept) and `docs/04-company-deep-dives/ch25-databricks.md` (company). Match their depth, density and polish.

## 2. What you own (write only these)

- Your chapter file(s) at the exact path(s) given in your assignment.
- Optional per-chapter chart scripts: `scripts/charts/chNN_<name>.py`, each exposing `make()` that reads `data/*.csv` via `chartlib.load()` and saves with `chartlib.save(fig, "chNN_<name>")` → `docs/assets/charts/chNN_<name>.png`. Import with `from chartlib import load, num, save, source_note, PALETTE, SERIES, plt`. Run it with `python3 scripts/make_charts.py chNN` to check it works. Add a `source_note()` line on every chart.
- Optional chapter-specific datasets: `data/chNN_<topic>.csv` (must include `source` and `as_of` columns on every row).
- Optional SVG diagrams: `docs/assets/diagrams/chNN-<name>.svg` (original, palette colors, `<title>` and `<desc>`).
- Staging files (the integrator merges these; never edit the shared originals):
  - `data/staging/chNN-ma_deals.csv`, `data/staging/chNN-private_funding.csv`, `data/staging/chNN-public_comps.csv`, `data/staging/chNN-company_financials.csv` — same header as the main CSV; only **new or corrected** rows (put "CORRECTION of …" in notes/outcome if correcting).
  - `meta/staging/chNN-glossary.md` — one line per term: `- **Term** — one-sentence L1 definition. (chNN)`. Include every term in your "Key terms" section and any other new jargon.
  - `meta/staging/chNN-open-questions.md` — one line per `[VERIFY: …]` you leave in the text.
  - `meta/staging/chNN-decisions.md` — any judgment call worth logging (scope boundaries, conflicting sources).

**Do not edit** `README.md`, `PROGRESS.md`, `CLAUDE.md`, `docs/glossary.md`, `mkdocs.yml`, the main `data/*.csv`, other chapters, or `scripts/*.py` (other than your own `scripts/charts/chNN_*.py`). **Do not run git** (no add/commit/push); the integrator commits.

## 3. How to write

- **Word budget** = prose words counted by `python3 scripts/wordcount.py <your file>` (excludes code/Mermaid, tables, footnote definitions, headings, captions). Hit **at least the budget**, ideally +5–10%. Meet it with mechanism, worked examples, numbers, history and implications, not padding.
- **Depth:** L2 by default; L3 only inside `> **Going deeper (L3).**` callouts.
- **Bridges:** use the reader's home turf (semiconductors/memory hierarchy, datacenter infra, storage, finance/valuation). Mark as `> **Bridge: …**`.
- **Everpure lens:** Everpure = formerly Pure Storage (NYSE: PSTG), moving up the stack into data management/intelligence (Enterprise Data Cloud, intelligent control plane, 2026 acquisition of 1touch for data discovery/classification/semantic context — check `meta/research-briefing.md`). Public information only; frame strategy as "options a strategy team might evaluate, based on public information." Do not re-teach storage; use a short `> **Storage bridge.**` box instead (refer to "the companion *Everpure Tech Atlas*", no URL).
- **Every number** needs a footnote with URL, publisher, published date and "retrieved 2026-11-01", and a label: GAAP / non-GAAP / company-stated run-rate / press-reported / estimate. Fiscal years explicit. If you cannot verify: `[VERIFY: …]` and log it in your open-questions staging file. **Never invent** numbers, names, dates, customers or quotes.
- **Copyright:** your own words; quotes < 15 words, ≤1 per source.
- **Visuals:** ≥1 per ~700 prose words, ≥3 per chapter, ≥2 of them diagrams/charts (Mermaid, SVG or PNG chart), plus structured comparison tables. Each visual followed by an italic caption `*Figure N.k — <takeaway>.*`. Images need descriptive alt text. Follow the Mermaid hygiene rules in the style guide exactly (allowed diagram types, quoted labels, no `block-beta`).
- **Links:** relative links to other chapters using the paths in `meta/outline.md` (e.g., from Part 1 to Ch 25: `../04-company-deep-dives/ch25-databricks.md`). Glossary links: `../glossary.md#<slug>` where slug = lowercase term, spaces→hyphens, punctuation dropped (e.g., `LSM-tree` → `lsm-tree`, `Change data capture (CDC)` → write the term as `Change data capture` → `change-data-capture`). Keep glossary term names simple (no slashes/parentheses) so slugs are predictable, and stage every linked term.
- **Key terms** section: a bullet list of linked terms (`- [Manifest list](../glossary.md#manifest-list) — …`).
- **Sources** section: all footnote definitions, numbered/ID'd, each with URL, publisher, published date, retrieved date.
- **Conversation playbook:** 3 PM questions, 3 engineer questions (company chapters: questions for the company's PMs/execs/partners), what good answers sound like, and a "Don't say this" list (common misconceptions that would cost credibility).

## 4. Before you finish (mandatory checks)

```bash
cd /home/user/data_tech_db_claude
python3 scripts/wordcount.py docs/<part>/<your-file>.md      # ≥ budget
scripts/lint_mermaid.sh docs/<part>/<your-file>.md           # 0 failures
python3 scripts/qa_report.py docs/<part>/<your-file>.md      # Problems column should say OK (links to glossary are checked later)
python3 scripts/make_charts.py chNN                          # if you added chart scripts
```

Fix every Mermaid failure (simplify the diagram if needed). Reference each chart you create in the chapter with a relative path from your chapter (`../assets/charts/chNN_<name>.png`).

## 5. Your reply to the integrator

Reply in **≤150 words**: file(s) written, prose words, visuals count, VERIFY count, staging files created, and any cross-chapter consistency issue (e.g., a number in `data/*.csv` you believe is wrong, with the better source).
