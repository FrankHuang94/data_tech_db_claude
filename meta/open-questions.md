# Open questions ([VERIFY] register)

Every `[VERIFY: …]` left in the text is listed here with its chapter. Resolve by finding a primary source, then remove the marker and the line.

| Chapter | Item | Notes |
|---|---|---|
| ch02 | ch02: Stack Overflow 2025 survey — confirm PostgreSQL 55.6% (all respondents) vs 58.2% (professional) directly on survey.stackoverflow.co/2025 (only secondary blog sources seen). | open |
| ch02 | ch02: DB-Engines July 2026 ranking positions (Oracle, MySQL, SQL Server, PostgreSQL, MongoDB, Snowflake, Databricks) come from a secondary report (HelloGitHub); confirm on db-engines.com and update to Nov 2026 edition. | open |
| ch02 | ch02: DataStax acquisition by IBM — confirm close date before stating "now part of IBM". | open |
| ch02 | ch02: Timescale's 2025 rename to TigerData — confirm name and date. | open |
| ch02 | ch02: Typical DiskANN random 4 KB reads per query ("a few dozen") — confirm against DiskANN paper/Microsoft docs. | open |
| ch07 | ch07 / Confirm Amazon S3 Standard LIST request price is still $0.005 per 1,000 (us-east-1) / footnote [^s3-pricing]; used only for an order-of-magnitude worked example. | open |
| ch07 | ch07 / Re-fetch Snowflake Polaris press release URL (2024-06-03) / footnote [^sf-polaris]; URL from memory, page could not be fetched (WebFetch blocked, WebSearch budget exhausted). | open |
| ch08 | ch08: Glue Data Catalog Delta Lake support — which engines read Delta tables registered in Glue (Athena, EMR, Redshift) as of 2026-11. | open |
| ch08 | ch08: Apache Polaris Delta support via "generic tables" — confirm release (believed Polaris 1.0, 2025) and maturity. | open |
| ch08 | ch08: Snowflake Horizon Catalog Delta support (Delta-sourced Iceberg tables) — confirm current status. | open |
| ch08 | ch08: Google BigLake / BigQuery Delta Lake table support — confirm current status and naming. | open |
| ch08 | ch08: Microsoft OneLake catalog — confirm launch (believed Ignite Nov 2024) and governance features (Purview integration). | open |
| ch08 | ch08: Apache Gravitino Delta Lake support — confirm. | open |
| ch08 | ch08: Project Nessie Delta Lake support — confirm (historically experimental). | open |
| ch08 | ch08: Unity Catalog OSS maturity stage at LF AI & Data (sandbox vs incubation vs graduated) as of 2026-11; one wiki says sandbox, latest release v0.4.0 (2026-02) unconfirmed. | open |
| ch01 | ch01: Confirm DOI https://doi.org/10.1109/ICDE.2005.1 resolves to Stonebraker & Çetintemel, "One Size Fits All" (ICDE 2005); search confirmed citation (pp. 2–11) but not the DOI. | open |
| ch01 | ch01: Exact publication date of a16z's updated "Emerging Architectures for Modern Data Infrastructure" (believed 2022; page metadata inconsistent). | open |
| ch01 | ch01: Exact publication date of Confluent blog "Benchmarking Apache Kafka, Apache Pulsar, and RabbitMQ" (2020; Kafka 2.6 era). | open |
| ch01 | ch01: Verify Stack Overflow Developer Survey 2025 PostgreSQL usage of 58.2% (all respondents) against survey.stackoverflow.co/2025; currently from a secondary summary (enstacked.com). | open |
| ch05 | ch05: Confirm Amazon Redshift's current query-compilation model (code-generated query segments) for the engine table. (ch05) | open |
| ch05 | ch05: Confirm Vertica's current owner (OpenText, via its 2023 Micro Focus acquisition). (ch05) | open |
| ch06 | ch06 / Arrow Flight introduction date (believed Oct 2019 Apache Arrow blog "Introducing Apache Arrow Flight") / search budget exhausted | open |
| ch06 | ch06 / Nimble (Meta) release status and license as of 2026-11 (github.com/facebookincubator/nimble) / only third-party status table found | open |
| ch06 | ch06 / S3 request-rate guidance: 5,500 GET/HEAD requests per second per partitioned prefix (AWS S3 performance docs) / from prior knowledge, not re-verified | open |
| ch06 | ch06 / Wes McKinney's current affiliation (Voltron Data / Posit) / from prior knowledge | open |
| ch06 | ch06 / Avro origin date (~2009, Hadoop subproject, Doug Cutting) / not re-verified | open |
| ch06 | ch06 / Parquet Apache top-level project date (believed April 2015) / not re-verified | open |
| ch03 | ch03: [VERIFY: confirm 20–30x wording in RocksDB blog 2022-10-31] — "leveled compaction write amplification typically 20–30x user data" was surfaced via a search summary attributed to rocksdb.org/blog/2022/10/31/align-compaction-output-file.html; page could not be fetched. Also used in "Numbers that matter". | open |
| ch04 | ch04 / Spanner PostgreSQL-dialect interface: confirm current feature coverage/GA status (Who's who table). / Search budget exhausted. | open |
| ch04 | ch04 / Aurora DSQL: confirm the AWS-documented replication protocol of the journal (third-party sources say Paxos-based). / Only third-party descriptions found. | open |
| ch04 | ch04 / Aurora DSQL: find a named public production reference customer. / None surfaced. | open |
| ch04 | ch04 / Stack Overflow 2025 survey PostgreSQL usage (~55.6%): check against survey.stackoverflow.co; secondary sources disagree whether figure is all respondents or professionals (other figure 58.2%). / Secondary sources only. | open |
| ch09 | ch09: Fivetran–Census closing date (announced 2025-05-01; no closing announcement found; ma_deals.csv status still "announced"). | open |
| ch09 | ch09: Exact publication date of Snowflake blog "Bidirectional Data Sharing Between Snowflake and Salesforce Data Cloud Is Now Generally Available" (believed 2024). | open |
| ch09 | ch09: BigQuery "Introduction to federated queries" doc page not re-opened this session (search budget exhausted); confirm URL and supported sources (Cloud SQL, Spanner, AlloyDB). | open |
| ch10 | ch10: Talend Open Studio retirement status/date (vendor table, Qlik Talend row). | open |
| ch10 | ch10: Publication dates of Informatica's IPU consumption-pricing and Flex IPU blog posts. | open |
| ch10 | ch10: Launch date of Airbyte capacity-based (Data Workers) pricing (BigDATAwire item; possibly Feb 2025). | open |
| ch10 | ch10: Matillion credits-per-task-hour ratio by edition (pricing page vs Credit Consumption Terms conflict). | open |
| ch10 | ch10: Azure Data Factory USD rates ($1 per 1,000 orchestration runs; $0.25/DIU-hour) against the Azure pricing calculator. | open |
| ch10 | ch10: Publication date of Databricks "Announcing General Availability of Lakeflow Connect" blog (Salesforce, Workday). | open |
| ch10 | ch10: Estuary Series A amount ($17M company release vs $14M SiliconANGLE headline). | open |
| ch10 | ch10: dltHub $8M seed announcement date (Aug vs Nov 2025). | open |
| ch10 | ch10: AWS EC2 m6i.xlarge on-demand price ($0.192/hour, US East) used as worked-example assumption. | open |
| ch11 | ch11: WarpStream Tableflow (Iceberg output from WarpStream BYOC) — confirm product name and GA status. | open |
| ch11 | ch11: AutoMQ "table topic" Iceberg feature — confirm GA status. | open |
| ch11 | ch11: Redpanda Cloud Topics — confirm GA date (targeted March 2026 per Streamfest 2025 blog). | open |
| ch11 | ch11: Google Cloud Managed Service for Apache Kafka — confirm service GA date (release notes show feature GAs but not core GA). | open |
| ch11 | ch11: Databricks "Introducing Apache Spark 4.1" blog — confirm exact publication date (2025-12?). | open |
| ch12 | ch12: dbt Core v2 launch date (weekly digest suggests July 2026) and current maturity (docs say both alpha and beta); current list of Fusion GA adapters beyond Snowflake. | open |
| ch12 | ch12: Earliest documented use of the job title "analytics engineer" (commonly credited to dbt Labs' community, c. 2018–2019). | open |
| ch12 | ch12: Closing date of Prefect's acquisition of Dagster Labs (announced 2026-07-13; some sources say closed same day, others say close expected August 2026). | open |
| ch12 | ch12 (footnote only): Snowflake Dynamic Tables GA date — third parties say April 2024; not confirmed from a Snowflake release note. | open |
| ch13 | ch13: Confirm Gartner $12.9M wording ("average" vs "at least") and original document (2020 MQ for Data Quality Solutions reference survey; repeated in Gartner July 2024 "12 Actions…"). | open |
| ch13 | ch13: Original publication date of Monte Carlo blog "Introducing the 5 Pillars of Data Observability" (believed 2020). | open |
| ch13 | ch13: Exact GX (Great Expectations) 1.0 / GX Core release date (believed Aug 2024). | open |
| ch13 | ch13: Confirm Unity Catalog column-lineage behaviour (automatic capture; gaps for path-based access, some UDFs, hive_metastore) against official Databricks lineage docs; current sources are community posts. | open |
| ch13 | ch13: Sifflet 2025 round label (Series A vs B) and exact date (CB Insights: 2025-06-19, $18.32M). | open |
| ch13 | ch13: Great Expectations open-source project start year (2017, from general knowledge; used in timeline). | open |
| ch13 | ch13 (staging CSV only): Anomalo ~$10M Series B extension reported Nov 2024; confirm amount/date. | open |
| ch14 | ch14: Databricks Unity Catalog metric views GA date (Public Preview 2025-05-29; 2026 status of "Unity Catalog Metrics/Business Semantics" rests on secondary sources). | open |
| ch14 | ch14: Sigma current pricing tiers (per-user; whether viewers are free on current plans). | open |
| ch14 | ch14: Complete list of Leaders in the 2026 Gartner ABI Magic Quadrant (dated 2026-06-29); only Salesforce/Tableau, Google/Looker, Qlik confirmed from vendor pages. | open |
| ch14 | ch14: Exact GA date of Looker Conversational Analytics (Google blog undated in search; aggregator says Apr 2026). | open |
| ch25 | ch25: Databricks company-stated employee headcount (only aggregator/Wikipedia estimates ~10k-12k found). | open |
| ch25 | ch25: Full participant lists for Databricks Series G and later rounds (snapshot "notable investors" row) per data/private_funding.csv notes. | open |
| ch25 | ch25: Current status of the Mosaic AI brand vs. Agent Bricks (believed folding in; not confirmed). | open |
| ch25 | ch25: Share of Databricks revenue transacted through Azure Databricks (no public figure found). | open |
| ch25 | ch25: Everpure OpenSharing connector GA status (private preview from 2026-06-09 per Everpure blog; Databricks lists Everpure as launch partner). | open |
| ch25 | ch25: Primary source (Bloomberg TV, June 2026) for Ghodsi's "terrible year to go public" comment; currently from a secondary summary. | open |
