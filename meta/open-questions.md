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
