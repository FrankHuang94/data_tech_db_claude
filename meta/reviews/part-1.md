# Independent review — Part 1 (Data systems foundations)

**Reviewer:** independent Phase 2 reviewer (principal data-platform engineer / buy-side analyst lens) · **Date:** 2026-11-01
**Chapters reviewed (full read):** ch01-data-stack-map, ch02-data-models, ch03-database-internals, ch04-distributed-databases, ch05-analytical-engines, ch06-file-formats, ch07-open-table-formats, ch08-catalogs-and-metastores.
**Sources of truth checked against:** `meta/verified-facts.md` (items 10, 13 used directly), `data/ma_deals.csv`, `data/private_funding.csv`, `meta/research-briefing.md` integrator notes (Polaris 1.8.0 / graduation wording, Iceberg 1.12.0 and spec status, AWS–DuckLabs, SAP–Dremio, LanceDB).
**Post-edit QA:** `scripts/qa_report.py` OK for all eight files (all above word budget; visuals unchanged); `scripts/lint_mermaid.sh` 0 failures on all eight; every footnote reference defined and every definition used.

Overall verdict: Part 1 is technically strong. The L2 explanations are mostly correct and well hedged, and I found no stale financials (Part 1 carries few). The fixes are mostly precision fixes to isolation, concurrency and consensus claims, plus bringing product/status lines (Polaris, Iceberg, DuckDB Labs, Dremio) into line with the integrator register. No Lakeflow, Vertex, Data Cloud, Snowflake Intelligence/Cortex or MongoDB-CEO references appear in Part 1, so those renames needed no changes here. The Everpure name and ticker usage (NYSE: P, formerly PSTG) is consistent.

## Changes made

| Chapter | Issue | Fix | Source |
|---|---|---|---|
| ch01 | Postgres usage given as "58.2% of respondents". Ch 2 and Ch 4 use 55.6% of all respondents; 58.2% is the professional-developer cut | Text and Numbers table now give both figures and their bases | Ch 2 footnote `so25` (Vonng secondary); internal consistency |
| ch02 | "DynamoDB traces back to the Dynamo paper" implies a leaderless Dynamo design; DynamoDB actually uses a Multi-Paxos leader per partition | Clarified that DynamoDB borrows ideas but not the leaderless design; added footnote | Elhemali et al., USENIX ATC 2022 |
| ch02 | GQL described as "largely based on Cypher" (oversimplified) | Now: draws heavily on Cypher MATCH, with input from PGQL and G-CORE | ISO/IEC 39075 background (settled) |
| ch02 | `[VERIFY: DataStax–IBM close date]` | Resolved: closed 2025-05-28; footnote added | `data/ma_deals.csv` (DBTA) |
| ch03 | Isolation table implied that InnoDB repeatable read ≈ snapshot isolation. InnoDB RR lets `UPDATE`/locking reads see the latest row and can lose updates, so it is weaker than SI. Also not flagged as MySQL's default | Row rewritten | MySQL InnoDB consistent-read semantics (settled; Hermitage-style results) |
| ch03 | "Only true serializability catches write skew" | Added explicit locking (`SELECT … FOR UPDATE`) as the practical alternative | Berenson et al. 1995; PG docs |
| ch03 | WAL recovery "rolls back" losers, stated as if every engine does undo | Clause added: PostgreSQL has no undo pass (aborted xids stay invisible via the commit log) | PG docs (settled) |
| ch03 | Implied that PostgreSQL group commit depends on `commit_delay` | Corrected: group commit happens automatically; `commit_delay`/`commit_siblings` only enlarge groups | PG runtime-config docs |
| ch03 | "Point lookup ≈ one storage read" ignores the heap fetch | Added "+1 heap read in heap-organized tables (PostgreSQL)" | Mechanism (chapter's own clustered vs heap section) |
| ch03 | **Wrong generalization:** "Distributed databases lean optimistic" | Replaced with the real split: Spanner pessimistic (wound-wait); CockroachDB write intents + timestamp ordering + retries; TiDB default switched optimistic→pessimistic (2020); DSQL fully optimistic | Spanner OSDI 2012; TiDB docs (settled) |
| ch03 | InnoDB change buffer cited as a live hybrid feature | Noted that MySQL 8.4 disabled it by default | MySQL 8.4 release notes (2024) |
| ch04 | "Two regions plus a witness" did not say where the witness sits | The witness must be in a third location | Quorum math |
| ch04 | "3f+1 is why blockchains are more expensive" (oversimplified) | Reworded: BFT costs, plus open membership for public chains | Mechanism |
| ch04 | CockroachDB 500 ms max-offset default cited only to v20.1 docs | Kept the value; added `[VERIFY: current default in 25.x/26.x]` | Cited doc is version-old |
| ch04 | Aurora quorum sentence garbled the write/read availability split (AZ vs AZ+1) | Rewritten: writes survive the loss of an AZ; reads and repair survive AZ+1 | Verbitski et al., SIGMOD 2017 |
| ch04 | "Spanner is the only one with hardware-backed global time", which contradicts the chapter's own DSQL/Time Sync section | Reworded: Spanner was the original; AWS Time Sync (used by DSQL) is a second | Internal consistency; AWS DSQL blog |
| ch04 | **Missing key fact:** Aurora DSQL offers *snapshot* isolation, not serializable, so write skew is possible | Added to the DSQL positioning bullet, with footnote | AWS DSQL architecture blog (`dsql-arch`) |
| ch05 | TL;DR said BigQuery "took the same path" as Snowflake, contradicting the chapter's own "Don't say" (Dremel disaggregated storage earlier) | Reworded: BigQuery's Dremel lineage disaggregated earlier; the three converged | Dremel decade paper (VLDB 2020) |
| ch05 | Arithmetic: 0.13 GB at 10 GB/s ≈ 0.013 s, not "a few hundredths" | Now "roughly a hundredth of a second" | Arithmetic |
| ch05 | DuckDB/MotherDuck and Dremio listed with no 2026 corporate status | Added the AWS–DuckLabs definitive agreement (Aug 2026, terms undisclosed; DuckDB stays MIT under the DuckDB Foundation) and Dremio's acquisition by SAP; engine table now says "MIT; DuckDB Foundation" | verified-facts #13; `ma_deals.csv` (SAP–Dremio) |
| ch06 | `[VERIFY: Arrow Flight introduction date]` | Resolved: Flight introduced Oct 2019; Flight SQL in Arrow 7.0 (Feb 2022) | Arrow project blog (settled) |
| ch06 | `[VERIFY: Avro origin / Doug Cutting]` and `[VERIFY: Parquet TLP date]` | Resolved: Avro started by Cutting as a Hadoop subproject (2009), TLP 2010; Parquet incubator 2014, TLP April 2015 | ASF announcements (settled) |
| ch06 | `[VERIFY: S3 5,500 GET/HEAD per prefix]` | Resolved and cited (5,500 GET/HEAD; 3,500 PUT/COPY/POST/DELETE), matching Ch 5 and Ch 7 | AWS S3 performance guide |
| ch06 | LanceDB footnote said "lead unconfirmed" while the briefing names Theory Ventures | Footnote now records both | research-briefing (Lance row); `private_funding.csv` |
| ch07 | TL;DR: "Microsoft now writes Iceberg". OneLake is Delta-native and exposes Iceberg by metadata translation | Reworded; Figure 7.7 caption changed to "reads Iceberg; most write it natively" | Ch 8 OneLake row; Microsoft docs cited there |
| ch07 | Polaris status: graduation date and current release missing | "Graduated early 2026 (ASF announced 2026-03-05)"; release 1.8.0 by 2026-09-28; footnote now cites the ASF announcement | Integrator note (Ch 7), research-briefing |
| ch07 | Iceberg "current version" cell omitted that the Java default `format-version` is still 2 | Now: spec v1–v3 adopted, v4 not yet adopted; Java 1.12.0 default `format-version` 2 | Integrator note (Ch 7) |
| ch07 | DuckDB Labs row had no AWS deal; Dremio row had no close | Added AWS–DuckLabs (definitive agreement ~2026-08-25, MIT/DuckDB Foundation); SAP–Dremio announced 2026-05-04, closed ~Jul 2026, terms undisclosed | verified-facts #13; research-briefing §A; `ma_deals.csv` |
| ch07 | Vendor framing: "Databricks pushed Delta's features into Iceberg v3", based only on a Databricks blog | Labelled "by Databricks' own account" and noted Snowflake and other contributors | Balance; `dbx-v3` is a vendor source |
| ch07 | Timeline/text omitted Iceberg's May 2020 graduation | Added (timeline and Phase 1 text) with footnote | ASF announcement 2020-05-19 (settled) |
| ch07 | `[VERIFY: URL not re-fetched]` on the Polaris press release | Resolved with the Business Wire syndication already cited in Ch 8 | Ch 8 `polaris-pr` |
| ch08 | Polaris described only up to 1.4; graduation phrasing incomplete | Added the Feb 19 blogs and release 1.8.0 (2026-09-28), with a new footnote | Integrator note (Ch 7) |

**Count:** 32 fixes (ch01 1, ch02 3, ch03 7, ch04 6, ch05 3, ch06 4, ch07 7, ch08 1). Seven `[VERIFY]` markers resolved; one added (ch04 CockroachDB max offset).

## Checked and left unchanged (spot list)

- Ch 3 worked-example cost arithmetic (Plans A/B1/B2, the bad-estimate case, the illustrative EXPLAIN costs) recomputes exactly from PostgreSQL cost constants.
- Ch 4 worked-example RTT sums, the async-loss figure (200 ms × 5,000/s = 1,000) and the Abadi PACELC classifications all match the 2012 paper.
- Ch 6 sandbox ratios (7.5×, 11.9×, ~37% zstd saving, 17–18× speed-up) are internally consistent.
- Ch 7 small-file arithmetic (11,520 files and 1,440 snapshots per day; 2,000 LIST calls ≈ 1 minute ≈ $0.01) is correct. Iceberg defaults (512 MB, 8 MB manifests, 5-day expiry, 4 retries, COW default) and Delta defaults (checkpoint every 10 commits, 30/7-day retention) are correct.
- TrueTime ε (1–7 ms, ~4 ms), Aurora 4/6 write and 3/6 read quorums, the S3 LIST page size, S3 strong consistency (Dec 2020) and S3 conditional writes (Aug 2024) are all correct.
- The IBM–Confluent (~$11B EV, closed 2026-03-17), Fivetran–dbt ("approaching $600M" ARR), Everpure–1touch ($125.0M; closed 2026-05-07), Databricks–Tabular (~$2B press-reported), Neon (~$1B press-reported), ClickHouse ($400M at $15B) and Cockroach Labs ($278M at $5B) figures all match the CSVs and keep their basis labels.

## Disagreements and items for the integrator

1. **LanceDB Series A lead.** `research-briefing.md` says Theory Ventures; `data/private_funding.csv` says lead unconfirmed `[VERIFY]`. CSV outranks the briefing, so I did not stage a correction. The integrator should decide and align the CSV.
2. **Ch 1 "Snowflake's Postgres mirroring"** (HTAP bullet) is unsourced in-chapter, and its GA date is an open item in research-briefing §"open questions" (item 3). I left it because the brief does not let me change post-mid-2025 facts from memory. Consider adding a footnote or rewording to "Snowflake's Postgres-to-Snowflake replication (status [VERIFY])".
3. **Ch 7 "Delta 4.4.x", "Hudi 1.2.x", "Paimon 2.1", "DuckLake 1.1"** version cells come from the drafter's GitHub reads and are not in sources 1–3. They are plausible, but I could not verify them.
4. **Ch 7 "draft v4 spec forbids writing new equality deletes"** and the v4 "root manifest" description are draft-spec details that may change. They are labelled "draft", which is acceptable.
5. **Broken links in ch01** to `../00-start-here/ch00-2-market-map.md`, `../07-conversation-toolkit/ch46-…` and `ch48-…`. The target files do not exist yet (Parts 0 and 7 are not written). These are not chapter errors; they will resolve when those Parts land.

## Remaining high-risk `[VERIFY]` items

- **ch04 CockroachDB default `--max-offset`** (500 ms, cited to v20.1 docs). I believe newer versions may have lowered it. This matters if a reader quotes it.
- **ch01/ch02/ch04 Stack Overflow 2025 PostgreSQL percentages** (55.6% all / 58.2% professional). Every source is secondary, and they disagree on which cohort is which. This is a high-visibility figure.
- **ch08 Delta-support cells** for Glue, Polaris generic tables, Horizon, BigLake, Gravitino and Nessie, plus the Unity Catalog OSS LF AI & Data stage. The chapter itself says these are the least-verified cells.
- **ch04 Aurora DSQL replication protocol / flagship reference**, and the **Spanner PG-dialect coverage**.
- **ch05 Vertica's current owner** (OpenText, via Micro Focus, as of 2023; any post-2025 change is unverified) and **Redshift's current compilation model**.
- **ch06 Nimble release/licence status** and **Wes McKinney's current affiliation**.
- Lower risk: ch03 RocksDB "20–30×" wording; ch02 DiskANN reads per query; ch07 S3 LIST price; ch01 citation-metadata VERIFYs (DOI, a16z update date, Confluent benchmark date).
