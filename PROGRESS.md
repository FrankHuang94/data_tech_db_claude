# PROGRESS

> Memory file for the autonomous build. After any context compaction: re-read `CLAUDE.md` and this file, then continue with the next unfinished item.

## Current status

- **Phase:** 1 — Parts 1–3 drafted and integrated (QA OK); Ch 25 done; Part 4 (Ch 26–34) drafting; Part 5 launching next.
- **Next step:** integrate Part 4 as agents report; launch Part 5 (Ch 35–41), then Part 6 (42–45), then Part 7 + Part 0; then Phase 2 reviewers per Part; then Phase 3 (glossary ≥350 via scripts/build_glossary.py, README, final QA, deploy).
- **Integration routine:** `scripts/integrate.sh <chapter.md> "docs(chNN): …"` (QA + Mermaid lint + merge staging + charts + PROGRESS + commit), then `git push -u origin claude/loving-brahmagupta-stqbpn`. Briefing corrections go to the bottom of `meta/research-briefing.md`.

## Phase checklist

- [x] Phase 0.1 skeleton, CLAUDE.md, style guide, templates, outline, scripts, mkdocs.yml, Pages workflow; mmdc + Python deps installed
- [x] Phase 0.2 research sweep (comps/financials, funding 79 rounds, M&A 119 deals, briefing, market sizes) — WebSearch-only (see decision 9)
- [x] Phase 0.3 outline finalized
- [x] Phase 0.4 quality-bar chapters Ch 7 and Ch 25 (QA OK)
- [ ] Phase 1 batches (Part 1 → 2 → 3 → 4 → 5 → 6 → 7 → 0)
- [ ] Phase 2 independent reviews (all Parts)
- [ ] Phase 3 synthesis: glossary, flashcards, cheat sheets, README, final QA, deploy

## Chapter tracker

Words = prose words (`scripts/wordcount.py`). Visuals = Mermaid + images + comparison tables (`scripts/qa_report.py`).

**Totals:** 26/52 chapters drafted · 93,399 prose words · 235 visuals · 193 [VERIFY] markers.

| Ch | File | Status | Words | Budget | Visuals | VERIFY | Reviewed |
|---|---|---|---|---|---|---|---|
| 0.1 | ch00-1-how-to-use.md | not started | 0 | 1200 | 0 | 0 | no |
| 0.2 | ch00-2-market-map.md | not started | 0 | 1800 | 0 | 0 | no |
| 1 | ch01-data-stack-map.md | QA pass | 3,417 | 2200 | 10 | 4 | no |
| 2 | ch02-data-models.md | QA pass | 3,201 | 1900 | 7 | 5 | no |
| 3 | ch03-database-internals.md | QA pass | 4,376 | 2300 | 10 | 1 | no |
| 4 | ch04-distributed-databases.md | QA pass | 4,315 | 2000 | 10 | 4 | no |
| 5 | ch05-analytical-engines.md | QA pass | 3,400 | 2200 | 8 | 2 | no |
| 6 | ch06-file-formats.md | QA pass | 2,967 | 1800 | 7 | 6 | no |
| 7 | ch07-open-table-formats.md | QA pass | 3,602 | 2000 | 9 | 2 | no |
| 8 | ch08-catalogs-and-metastores.md | QA pass | 2,640 | 1600 | 6 | 8 | no |
| 9 | ch09-pipeline-patterns.md | QA pass | 3,461 | 2000 | 10 | 3 | no |
| 10 | ch10-ingestion-and-integration.md | QA pass | 2,751 | 1900 | 8 | 9 | no |
| 11 | ch11-streaming-and-event-platforms.md | QA pass | 3,593 | 2200 | 10 | 5 | no |
| 12 | ch12-transformation-and-orchestration.md | QA pass | 3,250 | 1900 | 7 | 3 | no |
| 13 | ch13-data-quality-observability-lineage.md | QA pass | 3,395 | 1800 | 8 | 6 | no |
| 14 | ch14-semantic-layers-and-bi.md | QA pass | 2,857 | 2000 | 7 | 4 | no |
| 15 | ch15-governance-security-privacy.md | QA pass | 4,343 | 2200 | 8 | 9 | no |
| 16 | ch16-ai-data-lifecycle.md | QA pass | 3,600 | 2200 | 6 | 1 | no |
| 17 | ch17-unstructured-data-processing.md | QA pass | 3,144 | 2100 | 10 | 11 | no |
| 18 | ch18-embeddings-and-vector-search.md | QA pass | 4,359 | 2600 | 11 | 5 | no |
| 19 | ch19-retrieval-architectures.md | QA pass | 3,781 | 2200 | 11 | 7 | no |
| 20 | ch20-training-data-supply-chain.md | QA pass | 3,610 | 2200 | 8 | 20 | no |
| 21 | ch21-ml-platforms-feature-stores-llmops.md | QA pass | 3,436 | 2100 | 9 | 0 | no |
| 22 | ch22-agents-and-data.md | QA pass | 4,255 | 2400 | 10 | 4 | no |
| 23 | ch23-real-time-analytics-htap.md | QA pass | 3,360 | 2000 | 9 | 13 | no |
| 24 | ch24-data-meets-compute-and-storage.md | QA pass | 3,630 | 2200 | 11 | 5 | no |
| 25 | ch25-databricks.md | QA pass | 5,237 | 4500 | 13 | 6 | no |
| 26 | ch26-snowflake.md | not started | 0 | 4500 | 0 | 0 | no |
| 27 | ch27-databricks-vs-snowflake.md | not started | 0 | 2500 | 0 | 0 | no |
| 28 | ch28-hyperscaler-data-platforms.md | not started | 0 | 3500 | 0 | 0 | no |
| 29 | ch29-operational-database-vendors.md | not started | 0 | 3000 | 0 | 0 | no |
| 30 | ch30-data-movement-streaming-companies.md | not started | 0 | 3000 | 0 | 0 | no |
| 31 | ch31-analytical-engine-challengers-legacy.md | not started | 0 | 3000 | 0 | 0 | no |
| 32 | ch32-ai-native-data-companies.md | not started | 0 | 3500 | 0 | 0 | no |
| 33 | ch33-governance-catalog-security-companies.md | not started | 0 | 2500 | 0 | 0 | no |
| 34 | ch34-application-giants-data-platforms.md | QA pass | 3,419 | 2000 | 12 | 50 | no |
| 35 | ch35-business-models.md | not started | 0 | 2500 | 0 | 0 | no |
| 36 | ch36-unit-economics-kpis.md | not started | 0 | 2500 | 0 | 0 | no |
| 37 | ch37-public-comps-valuation.md | not started | 0 | 2500 | 0 | 0 | no |
| 38 | ch38-open-source-strategy.md | not started | 0 | 2000 | 0 | 0 | no |
| 39 | ch39-ma-history.md | not started | 0 | 3500 | 0 | 0 | no |
| 40 | ch40-gtm-partnerships.md | not started | 0 | 2000 | 0 | 0 | no |
| 41 | ch41-market-sizing.md | not started | 0 | 1000 | 0 | 0 | no |
| 42 | ch42-history-of-databases.md | not started | 0 | 3000 | 0 | 0 | no |
| 43 | ch43-modern-data-stack.md | not started | 0 | 2000 | 0 | 0 | no |
| 44 | ch44-future-trends.md | not started | 0 | 3000 | 0 | 0 | no |
| 45 | ch45-storage-moving-up-the-stack.md | not started | 0 | 2000 | 0 | 0 | no |
| 46 | ch46-talking-with-data-people.md | not started | 0 | 2200 | 0 | 0 | no |
| 47 | ch47-diligence-checklist.md | not started | 0 | 2000 | 0 | 0 | no |
| 48 | ch48-question-bank.md | not started | 0 | 2000 | 0 | 0 | no |
| 49 | ch49-explain-in-30-seconds.md | not started | 0 | 1500 | 0 | 0 | no |
| 50 | ch50-self-test-cheat-sheets.md | not started | 0 | 1300 | 0 | 0 | no |
