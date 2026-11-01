# Outline: files, word budgets and planned visuals

Word budgets are **prose words** as counted by `scripts/wordcount.py` (excludes code/Mermaid blocks, tables, footnote definitions, headings, HTML tags). Target total ≈ 120,000; floor 100,000. "SV-n" = signature visual n from the brief (listed at the bottom).

## Part 0 — Start Here (~3,000) · `docs/00-start-here/`

| Ch | File | Budget | Planned visuals |
|---|---|---|---|
| 0.1 | `ch00-1-how-to-use.md` | 1,200 | learning-path flowchart; 2h/2d/2w path table; depth-label table |
| 0.2 | `ch00-2-market-map.md` | 1,800 | **SV-1 market map SVG**; "data industry in 10 diagrams" gallery (links); layer×company table |

## Part 1 — Data Systems Foundations (~16,000) · `docs/01-data-systems-foundations/`

| Ch | File | Budget | Planned visuals |
|---|---|---|---|
| 1 | `ch01-data-stack-map.md` | 2,200 | **SV-2 byte's journey**; OLTP/OLAP/streaming/AI workload table; quadrant of latency vs. data volume |
| 2 | `ch02-data-models.md` | 1,900 | data-model mindmap; same entity modelled 4 ways; model-fit table |
| 3 | `ch03-database-internals.md` | 2,300 | **SV-3 B-tree vs LSM**; **SV-3 query lifecycle**; WAL/MVCC sequence diagram; isolation-level table |
| 4 | `ch04-distributed-databases.md` | 2,000 | sharding/replication diagram; Raft sequence; CAP/PACELC table; NewSQL comparison |
| 5 | `ch05-analytical-engines.md` | 2,200 | **SV-4 row vs columnar**; **SV-4 vectorized execution**; MPP vs separated storage/compute diagram |
| 6 | `ch06-file-formats.md` | 1,800 | Parquet file anatomy; format comparison table; Arrow zero-copy flow |
| 7 | `ch07-open-table-formats.md` | 2,000 | **SV-6 Iceberg metadata tree + Delta log**; commit sequence; format comparison; format-war timeline |
| 8 | `ch08-catalogs-and-metastores.md` | 1,600 | **SV-7 catalog control point**; catalog evolution timeline; catalog comparison table |

## Part 2 — Pipelines, Movement and Governance (~14,000) · `docs/02-pipelines-and-governance/`

| Ch | File | Budget | Planned visuals |
|---|---|---|---|
| 9 | `ch09-pipeline-patterns.md` | 2,000 | ETL vs ELT flow; CDC sequence; batch/micro-batch/stream latency table; zero-ETL diagram |
| 10 | `ch10-ingestion-and-integration.md` | 1,900 | connector-economics chart/table; vendor positioning quadrant; integration architecture |
| 11 | `ch11-streaming-and-event-platforms.md` | 2,200 | **SV-8 Kafka log/partition/consumer group**; Kafka-on-object-storage diagram; streaming engine table |
| 12 | `ch12-transformation-and-orchestration.md` | 1,900 | DAG diagram; dbt project flow; orchestrator comparison |
| 13 | `ch13-data-quality-observability-lineage.md` | 1,800 | lineage graph; five pillars of observability; vendor table |
| 14 | `ch14-semantic-layers-and-bi.md` | 2,000 | semantic layer → LLM bridge diagram; BI landscape quadrant; semantic-layer comparison |
| 15 | `ch15-governance-security-privacy.md` | 2,200 | discovery/classification engine pipeline; RBAC vs ABAC; regulation timeline; DSPM vendor table |

## Part 3 — The AI Data Stack (~20,000) · `docs/03-ai-data-stack/`

| Ch | File | Budget | Planned visuals |
|---|---|---|---|
| 16 | `ch16-ai-data-lifecycle.md` | 2,200 | **SV-9 AI data lifecycle master diagram**; tools-by-stage table; feedback-loop diagram |
| 17 | `ch17-unstructured-data-processing.md` | 2,100 | parsing/chunking pipeline; chunking strategy table; vendor map |
| 18 | `ch18-embeddings-and-vector-search.md` | 2,600 | **SV-10 HNSW intuition**; IVF-PQ diagram; DiskANN/flash diagram; vector DB comparison |
| 19 | `ch19-retrieval-architectures.md` | 2,200 | **SV-10 RAG pipeline**; hybrid search + rerank flow; long-context vs RAG table; GraphRAG diagram |
| 20 | `ch20-training-data-supply-chain.md` | 2,200 | supply-chain flow; labeling vendor table; licensing-deals timeline; dedup pipeline |
| 21 | `ch21-ml-platforms-feature-stores-llmops.md` | 2,100 | ML lifecycle; feature store online/offline diagram; LLMOps tool table |
| 22 | `ch22-agents-and-data.md` | 2,400 | **SV-11 agent → MCP → semantic layer → catalog → data**; text-to-SQL sequence; Postgres-for-agents table |
| 23 | `ch23-real-time-analytics-htap.md` | 2,000 | HTAP architecture; engine comparison table; latency/concurrency quadrant |
| 24 | `ch24-data-meets-compute-and-storage.md` | 2,200 | GPU data-processing flow; lakehouse-on-object-storage stack; egress/data-gravity diagram; storage requirements table |

## Part 4 — Company Deep Dives (~32,000) · `docs/04-company-deep-dives/`

| Ch | File | Budget | Planned visuals |
|---|---|---|---|
| 25 | `ch25-databricks.md` | 4,500 | **SV-5 lakehouse architecture**; **SV-12 funding/valuation timeline, revenue chart, M&A timeline**; snapshot table; competitive matrix |
| 26 | `ch26-snowflake.md` | 4,500 | **SV-5 storage/compute separation**; **SV-12 revenue chart, M&A timeline**; NRR/RPO charts; competitive matrix |
| 27 | `ch27-databricks-vs-snowflake.md` | 2,500 | **SV-13 multi-dimension comparison**; pricing-unit table; workload-winner quadrant; growth chart |
| 28 | `ch28-hyperscaler-data-platforms.md` | 3,500 | four-cloud stack comparison; coopetition diagram; product mapping table |
| 29 | `ch29-operational-database-vendors.md` | 3,000 | vendor matrix; Postgres ecosystem map; MongoDB financials chart |
| 30 | `ch30-data-movement-streaming-companies.md` | 3,000 | consolidation timeline; Confluent financials chart; vendor matrix |
| 31 | `ch31-analytical-engine-challengers-legacy.md` | 3,000 | positioning quadrant; vendor table; Palantir ontology diagram |
| 32 | `ch32-ai-native-data-companies.md` | 3,500 | vector-DB funding chart; comparison table; AI-data-infra map |
| 33 | `ch33-governance-catalog-security-companies.md` | 2,500 | vendor matrix; consolidation map; business-model table |
| 34 | `ch34-application-giants-data-platforms.md` | 2,000 | app-vendor data-layer diagram; comparison table; deal timeline |

## Part 5 — Business and Economics (~16,000) · `docs/05-business-and-economics/`

| Ch | File | Budget | Planned visuals |
|---|---|---|---|
| 35 | `ch35-business-models.md` | 2,500 | pricing-unit table; consumption vs subscription revenue-volatility chart; model decision tree |
| 36 | `ch36-unit-economics-kpis.md` | 2,500 | KPI tree; worked 10-Q example table; Snowflake NRR chart; Rule of 40 chart |
| 37 | `ch37-public-comps-valuation.md` | 2,500 | **SV-14 comps scatter (EV/NTM vs growth)**; comps table; private marks chart |
| 38 | `ch38-open-source-strategy.md` | 2,000 | relicensing timeline; open-core flywheel; license comparison table |
| 39 | `ch39-ma-history.md` | 3,500 | **SV-15 M&A timeline + deal-value chart**; category chart; pattern table |
| 40 | `ch40-gtm-partnerships.md` | 2,000 | marketplace co-sell flow; partner-program table; storage-partner certification diagram |
| 41 | `ch41-market-sizing.md` | 1,000 | market-size chart; TAM table; drivers/headwinds diagram |

## Part 6 — History and Future (~10,000) · `docs/06-history-and-future/`

| Ch | File | Budget | Planned visuals |
|---|---|---|---|
| 42 | `ch42-history-of-databases.md` | 3,000 | **SV-16 history timeline**; lessons-by-era table; Inmon vs Kimball diagram |
| 43 | `ch43-modern-data-stack.md` | 2,000 | MDS unbundling/rebundling diagram; consolidation timeline; survivor table |
| 44 | `ch44-future-trends.md` | 3,000 | **SV-17 future-trends radar (quadrant)**; trend likelihood/timing table; convergence diagram |
| 45 | `ch45-storage-moving-up-the-stack.md` | 2,000 | **SV-18 storage → data → AI stack map with Everpure's position (SVG)**; options matrix; partner/compete/acquire map |

## Part 7 — Conversation Toolkit (~9,000) · `docs/07-conversation-toolkit/`

| Ch | File | Budget | Planned visuals |
|---|---|---|---|
| 46 | `ch46-talking-with-data-people.md` | 2,200 | persona mindmap; question-set table; conversation-flow diagram |
| 47 | `ch47-diligence-checklist.md` | 2,000 | diligence flow; red-flag table; scoring matrix |
| 48 | `ch48-question-bank.md` | 2,000 | topic×audience matrix; question-count chart; 150 tagged questions |
| 49 | `ch49-explain-in-30-seconds.md` | 1,500 | concept mindmap; category table; 60 one-liners |
| 50 | `ch50-self-test-cheat-sheets.md` | 1,300 | acronym sheet; market-map poster; deal-table poster; Databricks vs Snowflake one-pager; 200 flashcards |

## Other files

- `docs/index.md` (MkDocs home, mirrors README), `docs/glossary.md` (≥350 terms).

## Signature visuals (minimum)

1. Full data/AI-data market map (layers × companies) — Ch 0.2 (SVG)
2. A byte's journey: app → OLTP → CDC/stream → lakehouse → BI/semantic layer → RAG/agent — Ch 1
3. B-tree vs. LSM-tree; query lifecycle (parse → optimize → execute) — Ch 3
4. Row vs. columnar layout; vectorized execution — Ch 5
5. Snowflake storage/compute separation; Databricks lakehouse architecture — Ch 26, Ch 25
6. Iceberg metadata tree and Delta log equivalent — Ch 7
7. Catalog control-point diagram — Ch 8
8. Kafka log/partition/consumer-group — Ch 11
9. AI data lifecycle master diagram — Ch 16
10. RAG pipeline (Ch 19) and HNSW intuition (Ch 18)
11. Agent-data access path — Ch 22
12. Databricks & Snowflake funding/valuation timeline, revenue growth, M&A timeline — Ch 25, 26
13. Databricks vs. Snowflake multi-dimension comparison — Ch 27
14. Public comps scatter (EV/NTM revenue vs. growth) — Ch 37
15. Data-industry M&A timeline and deal-value chart 2010–2026 — Ch 39
16. History of databases timeline — Ch 42
17. Future-trends radar — Ch 44
18. Layered storage → data → AI stack map with Everpure's position — Ch 45
