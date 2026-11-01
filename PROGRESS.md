# PROGRESS

> Memory file for the autonomous build. After any context compaction: re-read `CLAUDE.md` and this file, then continue with the next unfinished item.

## Current status

- **Phase:** 1–2 overlap — Parts 1–4 drafted; Part 5 (35–41) and Part 6 (42–45) drafting; Phase 2 reviewers running for Parts 1, 2, 3, 4a, 4b (see meta/reviewer-brief.md, logs in meta/reviews/). Subagent web search exhausted; integrator verifies key facts live into meta/verified-facts.md.
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

**Totals:** 49/52 chapters drafted · 190,625 prose words · 456 visuals · 450 [VERIFY] markers.

| Ch | File | Status | Words | Budget | Visuals | VERIFY | Reviewed |
|---|---|---|---|---|---|---|---|
| 0.1 | ch00-1-how-to-use.md | not started | 0 | 1200 | 0 | 0 | no |
| 0.2 | ch00-2-market-map.md | not started | 0 | 1800 | 0 | 0 | no |
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
| 25 | ch25-databricks.md | reviewed | 5,339 | 4500 | 13 | 6 | yes |
| 26 | ch26-snowflake.md | reviewed | 6,449 | 4500 | 16 | 29 | yes |
| 27 | ch27-databricks-vs-snowflake.md | reviewed | 3,918 | 2500 | 11 | 17 | yes |
| 28 | ch28-hyperscaler-data-platforms.md | reviewed | 5,371 | 3500 | 10 | 26 | yes |
| 29 | ch29-operational-database-vendors.md | reviewed | 4,557 | 3000 | 11 | 40 | yes |
| 30 | ch30-data-movement-streaming-companies.md | reviewed | 4,365 | 3000 | 10 | 25 | yes |
| 31 | ch31-analytical-engine-challengers-legacy.md | reviewed | 4,460 | 3000 | 8 | 21 | yes |
| 32 | ch32-ai-native-data-companies.md | reviewed | 4,760 | 3500 | 11 | 24 | yes |
| 33 | ch33-governance-catalog-security-companies.md | reviewed | 3,647 | 2500 | 9 | 15 | yes |
| 34 | ch34-application-giants-data-platforms.md | reviewed | 3,817 | 2000 | 12 | 38 | yes |
| 35 | ch35-business-models.md | QA pass | 3,881 | 2500 | 9 | 1 | no |
| 36 | ch36-unit-economics-kpis.md | QA pass | 4,083 | 2500 | 11 | 10 | no |
| 37 | ch37-public-comps-valuation.md | QA pass | 3,199 | 2500 | 15 | 6 | no |
| 38 | ch38-open-source-strategy.md | QA pass | 3,283 | 2000 | 8 | 6 | no |
| 39 | ch39-ma-history.md | QA pass | 4,745 | 3500 | 11 | 2 | no |
| 40 | ch40-gtm-partnerships.md | QA pass | 2,915 | 2000 | 9 | 6 | no |
| 41 | ch41-market-sizing.md | QA pass | 1,762 | 1000 | 7 | 6 | no |
| 42 | ch42-history-of-databases.md | QA pass | 4,723 | 3000 | 7 | 10 | no |
| 43 | ch43-modern-data-stack.md | QA pass | 2,284 | 2000 | 6 | 5 | no |
| 44 | ch44-future-trends.md | QA pass | 4,204 | 3000 | 9 | 12 | no |
| 45 | ch45-storage-moving-up-the-stack.md | QA pass | 2,707 | 2000 | 8 | 17 | no |
| 46 | ch46-talking-with-data-people.md | QA pass | 3,846 | 2200 | 7 | 0 | no |
| 47 | ch47-diligence-checklist.md | QA pass | 3,616 | 2000 | 6 | 1 | no |
| 48 | ch48-question-bank.md | QA pass | 8,274 | 2000 | 15 | 0 | no |
| 49 | ch49-explain-in-30-seconds.md | QA pass | 4,606 | 1500 | 7 | 0 | no |
| 50 | ch50-self-test-cheat-sheets.md | not started | 0 | 1300 | 0 | 0 | no |
