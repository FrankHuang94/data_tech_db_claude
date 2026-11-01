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
| ch15 | ch15: Amazon Macie per-GB inspection tier schedule above 50 TB (third-party sources cite $0.50 and $0.25 tiers; not confirmed on AWS page). | open |
| ch15 | ch15: IAPP count of US states with comprehensive privacy laws as of 2026-11 (secondary summaries say ~20; one cites 23 enacted as of 2026-04-13). | open |
| ch15 | ch15: Independent DSPM market-size figure (only vendor-cited ~$415M for 2024 via Palo Alto Networks Cyberpedia). | open |
| ch15 | ch15: Veeam–Securiti AI announcement date (believed Oct 2025; completion 2025-12-11 confirmed). | open |
| ch15 | ch15: Rubrik–Laminar primary press release (announced 2023-08, terms undisclosed). | open |
| ch15 | ch15: Exact GA date of Unity Catalog ABAC row-filter/column-mask policies (governed tags GA 2026-04-02; one GCP docs page still showed Public Preview). | open |
| ch15 | ch15: US Census Bureau differential-privacy page URL not re-fetched. | open |
| ch15 | ch15: EDPB Meta €1.2B fine press-release URL not re-fetched. | open |
| ch15 | ch15: Stanford DigiChina PIPL translation URL not re-fetched. | open |
| ch16 | ch16: [VERIFY: current status of the Mosaic AI brand] — whether Databricks still markets "Mosaic AI" or has folded it fully into Agent Bricks (footnote mosaic). | open |
| ch16 | ch16: Llama 4 ">30T tokens" is company-stated in Meta's 2025-04-05 blog but was confirmed only via secondary summaries this sweep (WebFetch blocked). | open |
| ch16 | ch16: Menlo Ventures 2024 RAG 51% / fine-tuning 9% figures came via secondary summaries; menlovc.com URL and exact publication date (Nov 2024) not opened directly. | open |
| ch16 | ch16: Bartz v. Anthropic final-approval exact day (July 2026) and covered-work count (~465k vs ~500k) differ across reports. | open |
| ch16 | ch16: Snowflake Cortex Training (Summit 2026) status and supported models rest on secondary sources (Flexera, Atlan); confirm against Snowflake docs/newsroom. | open |
| ch23 | ch23: Oracle Database In-Memory GA date (believed July 2014, 12.1.0.2) and SAP HANA GA date (believed 2011) — not verified (search budget exhausted); also in timeline. | open |
| ch23 | ch23: ClickHouse acquisitions of LibreChat (Nov 2025) and RunReveal (Sep 2026) — single aggregator sources only. | open |
| ch23 | ch23: PingCAP/TiDB latest funding round and valuation — aggregator claims of a 2024 $300M round at ~$3B unconfirmed. | open |
| ch23 | ch23: Apache Pinot top-level-project month (August vs December 2021). | open |
| ch23 | ch23: Exact publication date of MotherDuck "Redshift Files: The Hunt for Big Data" (2024); figures (0.03% >10 TB; ~6% of execution time) taken from search summaries, page not fetched. | open |
| ch23 | ch23: ClickHouse blog "SharedMergeTree and lightweight updates" exact date (2023). | open |
| ch23 | ch23: Google Cloud AlloyDB columnar engine blog exact date (2022). | open |
| ch23 | ch23: pg_duckdb 1.0 release date (reported ~Sep 2025). | open |
| ch23 | ch23: AWS News Blog date for Aurora PostgreSQL Iceberg/Parquet (DuckDB-powered) querying (Sep–Oct 2026). | open |
| ch23 | ch23: AWS–DuckLabs closing status (agreement signed 2026-08-26; later Amazon/InfoQ items say "acquired"). | open |
| ch23 | ch23: SingleStore–Vector Capital close date (secondary sources say Oct 2025) and ~$500M (Bloomberg, press-reported). | open |
| ch17 | ch17: Embedding list price assumption ($0.02 per million tokens) used in the worked example — confirm against a current embedding-model price list. | open |
| ch17 | ch17: CMSWire (J. Mancini) "Deconstructing a content management urban legend" — publication date. | open |
| ch17 | ch17: Databricks "From PDFs to Production" document-intelligence blog — exact publication day (Nov 2025); also whether ai_parse_document has left Beta/Public Preview. | open |
| ch17 | ch17: Glean post-2025 ARR ($200M Dec 2025; ~$300M May 2026) — primary source; data/private_funding.csv note labels $300M "company-stated" but search found it only in Sacra (estimate). | open |
| ch17 | ch17: Azure AI Document Intelligence current USD list rates (Read $1.50, Layout $10 per 1,000 pages) on the official pricing page. | open |
| ch17 | ch17: Mistral OCR 3 announcement — exact day (Dec 2025). | open |
| ch17 | ch17: LlamaParse credit price ($1.25 per 1,000 credits, from usagepricing tracker) on the official pricing page. | open |
| ch17 | ch17: Reducto r-1 blog — exact publication day (Sept 2026) and confirmation of ~1 cent/page "all in". | open |
| ch17 | ch17: Docling's donation to the Linux Foundation (which foundation; date). | open |
| ch17 | ch17: NVIDIA "Finding the Best Chunking Strategy" blog — publication date. | open |
| ch17 | ch17: Official Gemini 3 Flash list price ($0.50 / $3.00 per 1M input/output tokens per aggregator). | open |
| ch18 | ch18: Cohere Embed v4 release date (secondary sources say April 2025; confirm against Cohere release notes). | open |
| ch18 | ch18: S3 Standard list storage price still $0.023/GB-month (US East, first 50 TB) as of 2026-11-01. | open |
| ch18 | ch18: turbopuffer Dec 2025 round — amount and lead (aggregators cite Thrive Capital and Lachy Groom; one lists $10M seed, unconfirmed). | open |
| ch18 | ch18: Publication date of The Information / Calcalist report that Pinecone explored a sale (believed 2025). | open |
| ch18 | ch18: Vespa.ai spin-out from Yahoo (believed 2023) and its funding round (believed $31M led by Blossom Capital) — not re-verified. | open |
| ch19 | ch19: Confirm whether Anthropic applies a long-context surcharge to Claude Sonnet 5.5 prompts above 200K tokens (illustrative cost example assumes flat $2/$10 pricing). | open |
| ch19 | ch19: Verify the press-reported GPT-5.5 surcharge ($10/$45 per M tokens for prompts above 272K tokens) against OpenAI's pricing page. | open |
| ch19 | ch19: Verify Cohere Rerank 4 Fast/Pro rates ($2.00/$2.50 per 1,000 searches) on Cohere's own pricing page; check the reported Oct 2026 per-token Rerank 5 pricing. | open |
| ch19 | ch19: Find Glean's primary press release for $300M ARR (May 2026); currently seen only via secondary sources and data/private_funding.csv notes. | open |
| ch19 | ch19: Exact publication date of Snowflake blog "Cortex Search: State-of-the-Art Hybrid Search for RAG Applications" (2024). | open |
| ch19 | ch19: Date on which Databricks renamed Vector Search to "Databricks AI Search". | open |
| ch19 | ch19: GA date of Everpure KVA integration with NVIDIA Dynamo (reported as planned for Feb–Apr 2026). | open |
| ch21 | ch21: no [VERIFY] markers left in text. Open items for later: confirm Cisco–Galileo (2026-05-22) and PANW–Portkey (2026-05-29) close dates from primary sources; Check Point–Lakera close date; Portkey Series A day. | open |
| ch22 | ch22: Contents and status of the reported 2026-07-28 MCP specification revision (only 2025-06-18 and 2025-11-25 confirmed via search). | open |
| ch22 | ch22: Postgres-for-agents table (Figure 22.7) cells marked "n.v." — branching, scale-to-zero and pricing units for Snowflake Postgres, Supabase, AlloyDB, Azure HorizonDB, PlanetScale Postgres, Xata, Prisma Postgres and Turso; Lakebase pricing unit. | open |
| ch22 | ch22: Microsoft Entra Agent ID GA date (sources conflict: announced Build May 2025; GA reported variously as 2025 or April 2026). | open |
| ch22 | ch22: Snowflake–Natoma acquisition — confirm with a Snowflake press release (currently weak aggregator, ~2026-05-28). | open |
| ch24 | ch24: Voltron Data operating status in 2026 (last public news found: Accenture investment 2025-02-20, Carahsoft partnership 2025-04); confirm whether Theseus is still sold. | open |
| ch24 | ch24: NVIDIA–HEAVY.AI acquisition — date, terms and primary announcement (only PitchBook/NEA/dbdb.io and NVIDIA-hosted docs found). | open |
| ch24 | ch24: RAPIDS launch date (believed GTC Europe, October 2018) used in the History timeline. | open |
| ch24 | ch24: S3 request list prices ($0.005 per 1,000 PUT/LIST; $0.0004 per 1,000 GET) not re-confirmed on the live AWS pricing page. | open |
| ch24 | ch24: EU Data Act dates (application 2025-09-12; switching charges to zero by 2027-01-12) not re-checked against EUR-Lex. | open |
