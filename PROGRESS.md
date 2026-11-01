# PROGRESS

> Memory file for the autonomous build. After any context compaction: re-read `CLAUDE.md` and this file, then continue with the next unfinished item.

## ✅ Completion summary (2026-11-01)

**Status: Definition of Done met**, except the live GitHub Pages deployment, which needs a one-time setting from the repo owner (see below).

| Definition-of-Done item | Target | Result |
|---|---|---|
| Prose words (50 chapters + Part 0) | ≥100,000 | **208,622** (`scripts/wordcount.py`) |
| Part 4 words; Databricks / Snowflake | ≥28,000; ≥4,000 each | **46,683**; Ch 25 ≈5.2k, Ch 26 ≈6.2k |
| Visuals; per chapter | ≥150; ≥3 each | **484** (193 Mermaid, 35 charts/SVG, 256 comparison tables); every chapter ≥3 and ≥2 diagrams/charts |
| Mermaid renders | all | **193 blocks, 0 failures** (`scripts/lint_mermaid.sh`) |
| Charts regenerate from `data/` | all | **29 charts, 0 failures** (`scripts/make_charts.py`) |
| Templates incl. Conversation Playbook | every chapter | **52/52 pass** `scripts/qa_report.py` (0 problems) |
| `ma_deals.csv` / `public_comps.csv` / `private_funding.csv` | ≥80 / ≥20 / ≥40 | **146 / 26 / 110** (+192 financial rows, market-size files) |
| Glossary / question bank / flashcards | ≥350 / ≥150 / ≥200 | **712 / 154 / 253** |
| Independent reviewer pass | all Parts | **Done for Parts 0–7** (8 reviewers, ~370 fixes; logs in `meta/reviews/`) |
| Internal links | 0 broken | **4,581 links, 0 broken** (`scripts/check_links.py`) |
| MkDocs site | builds | **`mkdocs build`: 0 warnings**; CI build job passes |

**Remaining `[VERIFY]` markers: 447** (Part 4: 240 · Part 3: 61 · Part 6: 41 · Part 2: 39 · Part 5: 36 · Part 1: 27 · Part 7: 3 · Part 0: 0), all logged in `meta/open-questions.md`. They concentrate in the Part 4 chapters drafted after the subagent web-search pool ran out (Ch 29, 34, 26, 28, 30, 32, 31). Most flag exact publication dates, list prices, URLs and pre-2025 background facts recalled rather than re-fetched. The highest-impact current facts were re-verified live by the integrator and collected in `meta/verified-facts.md` (22 items: Q3 2026 hyperscaler results, Snowflake/MongoDB/Everpure/Salesforce/Confluent results, MongoDB CEO change, renames, SAP–Snowflake, Workday Data Cloud, AWS–DuckLabs, Proofpoint–Varonis, Snowflake S3-compatible vendors). **Recommended next pass:** with network access, open the primary filings and clear Part 4's markers first.

**Deployment.** The workflow `.github/workflows/deploy.yml` builds successfully on every push. The deploy step returns HTTP 404 because GitHub Pages is not yet enabled for the repository. **Owner action:** Settings → Pages → Build and deployment → Source: **GitHub Actions**, then re-run the latest workflow (or push any commit). The repo already reads well on github.com (Mermaid renders natively; SVG and PNG assets are relative links).

**Key decisions** (full list in `meta/decisions.md`):
1. Repo root = atlas root; assets in `docs/assets/` so they work both on github.com and in MkDocs; canonical glossary in `docs/glossary.md` (root copy generated).
2. **Research was WebSearch-only:** WebFetch and direct HTTP were blocked by the environment's network policy, and the subagents' shared search pool ran out mid-build (from Part 4 onward). Footnotes cite primary URLs surfaced by search; anything unconfirmed is `[VERIFY]`.
3. Everpure is referred to as "Everpure (formerly Pure Storage; NYSE: P, formerly PSTG)". The ticker changed 2026-04-17, which corrects the brief's PSTG.
4. Single source of truth: `data/*.csv` plus `meta/verified-facts.md`. Drafters staged rows; the integrator merged them (`scripts/merge_staging.py`).
5. Chapters run over their word budgets (208k vs the 120k target) because drafters met scope with mechanism and worked examples. Budgets were treated as floors.

**Notable findings that changed mid-2025 conventional wisdom** (all sourced in the chapters): Pure Storage → Everpure and its 1touch acquisition ($125M, closed 2026-05-07); Databricks at $190B with a >$7B run-rate (company-stated); IBM–Confluent closed; Salesforce–Informatica closed; Fivetran–dbt merged; AWS agreed to buy DuckLabs; SAP bought Dremio; Proofpoint–Varonis pending; Snowflake CoWork/CoCo renames; Google Cloud +103% in Q3 2026; MongoDB's CEO turnover.

## Current status

- **Phase:** COMPLETE — all phases (0–3) done; awaiting owner action to enable GitHub Pages.
- **Next step:** (optional) clear `[VERIFY]` markers with network access, starting with Part 4; enable Pages.
- **Integration routine:** `scripts/integrate.sh <chapter.md> "docs(chNN): …"` (QA + Mermaid lint + merge staging + charts + PROGRESS + commit), then `git push -u origin claude/loving-brahmagupta-stqbpn`. Briefing corrections go to the bottom of `meta/research-briefing.md`.

## Phase checklist

- [x] Phase 0.1 skeleton, CLAUDE.md, style guide, templates, outline, scripts, mkdocs.yml, Pages workflow; mmdc + Python deps installed
- [x] Phase 0.2 research sweep (comps/financials, funding 79 rounds, M&A 119 deals, briefing, market sizes) — WebSearch-only (see decision 9)
- [x] Phase 0.3 outline finalized
- [x] Phase 0.4 quality-bar chapters Ch 7 and Ch 25 (QA OK)
- [x] Phase 1 batches (Part 1 → 2 → 3 → 4 → 5 → 6 → 7 → 0)
- [x] Phase 2 independent reviews (all Parts)
- [x] Phase 3 synthesis: glossary, flashcards, cheat sheets, README, final QA, deploy

## Chapter tracker

Words = prose words (`scripts/wordcount.py`). Visuals = Mermaid + images + comparison tables (`scripts/qa_report.py`).

**Totals:** 52/52 chapters drafted · 208,622 prose words · 484 visuals · 447 [VERIFY] markers.

| Ch | File | Status | Words | Budget | Visuals | VERIFY | Reviewed |
|---|---|---|---|---|---|---|---|
| 0.1 | ch00-1-how-to-use.md | reviewed | 1,760 | 1200 | 5 | 0 | yes |
| 0.2 | ch00-2-market-map.md | reviewed | 2,053 | 1800 | 4 | 0 | yes |
| 1 | ch01-data-stack-map.md | reviewed | 3,429 | 2200 | 10 | 4 | yes |
| 2 | ch02-data-models.md | reviewed | 3,230 | 1900 | 7 | 4 | yes |
| 3 | ch03-database-internals.md | reviewed | 4,485 | 2300 | 10 | 1 | yes |
| 4 | ch04-distributed-databases.md | reviewed | 4,408 | 2000 | 10 | 5 | yes |
| 5 | ch05-analytical-engines.md | reviewed | 3,437 | 2200 | 8 | 2 | yes |
| 6 | ch06-file-formats.md | reviewed | 2,993 | 1800 | 7 | 2 | yes |
| 7 | ch07-open-table-formats.md | reviewed | 3,634 | 2000 | 9 | 1 | yes |
| 8 | ch08-catalogs-and-metastores.md | reviewed | 2,660 | 1600 | 6 | 8 | yes |
| 9 | ch09-pipeline-patterns.md | reviewed | 3,503 | 2000 | 10 | 3 | yes |
| 10 | ch10-ingestion-and-integration.md | reviewed | 2,758 | 1900 | 8 | 8 | yes |
| 11 | ch11-streaming-and-event-platforms.md | reviewed | 3,681 | 2200 | 10 | 5 | yes |
| 12 | ch12-transformation-and-orchestration.md | reviewed | 3,319 | 1900 | 7 | 3 | yes |
| 13 | ch13-data-quality-observability-lineage.md | reviewed | 3,448 | 1800 | 8 | 5 | yes |
| 14 | ch14-semantic-layers-and-bi.md | reviewed | 2,900 | 2000 | 7 | 5 | yes |
| 15 | ch15-governance-security-privacy.md | reviewed | 4,434 | 2200 | 8 | 10 | yes |
| 16 | ch16-ai-data-lifecycle.md | reviewed | 3,660 | 2200 | 6 | 1 | yes |
| 17 | ch17-unstructured-data-processing.md | reviewed | 3,160 | 2100 | 10 | 11 | yes |
| 18 | ch18-embeddings-and-vector-search.md | reviewed | 4,467 | 2600 | 11 | 6 | yes |
| 19 | ch19-retrieval-architectures.md | reviewed | 3,785 | 2200 | 11 | 6 | yes |
| 20 | ch20-training-data-supply-chain.md | reviewed | 3,652 | 2200 | 8 | 20 | yes |
| 21 | ch21-ml-platforms-feature-stores-llmops.md | reviewed | 3,436 | 2100 | 9 | 0 | yes |
| 22 | ch22-agents-and-data.md | reviewed | 4,328 | 2400 | 10 | 4 | yes |
| 23 | ch23-real-time-analytics-htap.md | reviewed | 3,366 | 2000 | 9 | 10 | yes |
| 24 | ch24-data-meets-compute-and-storage.md | reviewed | 3,641 | 2200 | 11 | 3 | yes |
| 25 | ch25-databricks.md | reviewed | 5,346 | 4500 | 13 | 6 | yes |
| 26 | ch26-snowflake.md | reviewed | 6,449 | 4500 | 16 | 29 | yes |
| 27 | ch27-databricks-vs-snowflake.md | reviewed | 4,026 | 2500 | 11 | 16 | yes |
| 28 | ch28-hyperscaler-data-platforms.md | reviewed | 5,371 | 3500 | 10 | 26 | yes |
| 29 | ch29-operational-database-vendors.md | reviewed | 4,557 | 3000 | 11 | 40 | yes |
| 30 | ch30-data-movement-streaming-companies.md | reviewed | 4,371 | 3000 | 10 | 25 | yes |
| 31 | ch31-analytical-engine-challengers-legacy.md | reviewed | 4,473 | 3000 | 8 | 21 | yes |
| 32 | ch32-ai-native-data-companies.md | reviewed | 4,760 | 3500 | 11 | 24 | yes |
| 33 | ch33-governance-catalog-security-companies.md | reviewed | 3,647 | 2500 | 9 | 15 | yes |
| 34 | ch34-application-giants-data-platforms.md | reviewed | 3,827 | 2000 | 12 | 38 | yes |
| 35 | ch35-business-models.md | reviewed | 3,881 | 2500 | 9 | 1 | yes |
| 36 | ch36-unit-economics-kpis.md | reviewed | 4,124 | 2500 | 11 | 9 | yes |
| 37 | ch37-public-comps-valuation.md | reviewed | 3,412 | 2500 | 15 | 6 | yes |
| 38 | ch38-open-source-strategy.md | reviewed | 3,316 | 2000 | 8 | 6 | yes |
| 39 | ch39-ma-history.md | reviewed | 4,782 | 3500 | 11 | 1 | yes |
| 40 | ch40-gtm-partnerships.md | reviewed | 2,964 | 2000 | 9 | 7 | yes |
| 41 | ch41-market-sizing.md | reviewed | 1,782 | 1000 | 7 | 6 | yes |
| 42 | ch42-history-of-databases.md | reviewed | 4,723 | 3000 | 7 | 10 | yes |
| 43 | ch43-modern-data-stack.md | reviewed | 2,304 | 2000 | 6 | 5 | yes |
| 44 | ch44-future-trends.md | reviewed | 4,325 | 3000 | 9 | 11 | yes |
| 45 | ch45-storage-moving-up-the-stack.md | reviewed | 2,765 | 2000 | 8 | 15 | yes |
| 46 | ch46-talking-with-data-people.md | reviewed | 3,865 | 2200 | 7 | 0 | yes |
| 47 | ch47-diligence-checklist.md | reviewed | 3,671 | 2000 | 6 | 1 | yes |
| 48 | ch48-question-bank.md | reviewed | 8,292 | 2000 | 15 | 0 | yes |
| 49 | ch49-explain-in-30-seconds.md | reviewed | 4,676 | 1500 | 7 | 0 | yes |
| 50 | ch50-self-test-cheat-sheets.md | reviewed | 13,286 | 1300 | 19 | 2 | yes |

## Simplified Chinese edition (2026-11-01)

- `Chinese translation/` mirrors the atlas: README, glossary (712 terms), `docs/index.md` and all 52 chapters, with identical file names. Data, scripts, meta and chart images are shared with the English edition.
- Checks: 4,587 internal links, 0 broken (English anchors injected by `scripts/zh_postprocess.py`); 193 translated Mermaid diagrams, 0 render failures.
- Print edition: `Chinese translation/AI-Data-Atlas-zh.pdf` (A4, 903 pages, 40 MB; cover, translator's note, contents with page numbers, Part dividers, bookmarks). Rebuild with `python3 scripts/zh_build_pdf.py --fonts <node_modules/@fontsource>` (needs mmdc, Playwright/Chromium, markdown, pypdf; optional @fontsource/noto-serif-sc and noto-sans-sc for typography).
