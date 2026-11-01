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
| ch20 | ch20: Scale AI 2026 fundraising talks at ~$20B valuation (single aggregator source) — confirm with Bloomberg/Reuters/The Information. | open |
| ch20 | ch20: AP–OpenAI (Jul 2023), Shutterstock–OpenAI (Jul 2023), Axel Springer–OpenAI (Dec 2023) dates and terms — not re-verified (search budget exhausted); timeline Figure 20.3 depends on them. | open |
| ch20 | ch20: Handshake AI latest valuation (Sacra lists $3.5B 2025; TechCrunch says $3.3B in 2022) — confirm. | open |
| ch20 | ch20: Labelbox customers, last round and valuation (recollection: $110M Series D Jan 2022, SoftBank) and expert-network (Alignerr) status — confirm. | open |
| ch20 | ch20: Toloka customers, valuation, day of $72M Bezos Expeditions round, and Nebius retained stake — confirm with primary release. | open |
| ch20 | ch20: Turing and Invisible gross margins — no public data found. | open |
| ch20 | ch20: Snorkel AI gross margin / revenue mix — no public data found. | open |
| ch20 | ch20: Sacra "Scale: the $290M/year Mechanical Turk" publication date (gross-margin estimates for Scale/Appen/TELUS). | open |
| ch20 | ch20: Original outlet and date of report that Surge told staff $1B 2024 revenue vs Scale $870M (cited via Ben's Bites). | open |
| ch20 | ch20: Mercor $20B talks — month (Jul 2026?) and whether closed; Crypto Briefing article date. | open |
| ch20 | ch20: Search Engine Land "OpenAI may pay Reddit $70M" publication date. | open |
| ch20 | ch20: Wiley FY2026 AI licensing revenue ($49M) — verify against Wiley 10-K (FY ends Apr 30, 2026). | open |
| ch20 | ch20: Thomson Reuters v. Ross Third Circuit (No. 25-02153) — outcome after June 2026 argument. | open |
| ch20 | ch20: NVIDIA NeMo Data Curator blog publication date (20x/5x dedup claim). | open |
| ch20 | ch20: SemDeDup ~50% LAION removal with minimal loss — confirm figure against arXiv:2303.09540. | open |
| ch20 | ch20: Snorkel AI Series D exact day (late May 2025) for staging row. | open |
| ch27 | ch27: Snowflake list prices per credit by edition ($2/$3/$4 Standard/Enterprise/Business Critical, AWS US East on-demand) and warehouse credits/hour (XS 1, S 2, M 4, L 8) are pre-2025 knowledge; confirm against snowflake.com/en/pricing-options and the Service Consumption Table (Nov 2026). Used in Fig 27.5/27.6 and worked example. | open |
| ch27 | ch27: Databricks Serverless SQL warehouse DBU/hour by size (2X-Small 4, Small 12) are pre-2025 knowledge; confirm against Databricks docs/pricing. Used in Fig 27.6 and worked example B. | open |
| ch27 | ch27: Customer overlap — find a primary analyst/survey figure (ETR, Gartner, Battery, company commentary) for the share of large enterprises running both Databricks and Snowflake. | open |
| ch27 | ch27: Snowflake S3-compatible storage — current documented vendor list; whether Pure Storage/Everpure is listed; whether Iceberg tables on S3-compatible external volumes are GA; whether Snowflake has any named storage-partner program comparable to the Databricks Storage Ecosystem. | open |
| ch27 | ch27: Horizon Catalog Iceberg REST interoperability (read/write by external engines; catalog-linked databases) — current status as of Nov 2026. | open |
| ch27 | ch27: Databricks serverless share of DBUs / revenue (undisclosed) — needed to size the infrastructure-inclusion effect on reported growth. | open |
| ch27 | ch27: TPC-DS dispute (Nov 2021) blog URLs (Databricks 2021-11-02; Snowflake "Industry Benchmarks and Competing with Integrity") taken from pre-2025 knowledge; re-open to confirm. | open |
| ch27 | ch27: Snowflake SIGMOD 2016 DOI URL and Bozeman, MT principal office per SEC filings — pre-2025 knowledge; confirm. | open |
| ch30 | ch30: Confluent GAAP revenue FY2019–FY2024 ($149.8M, $236.6M, $388.0M, $585.9M, $777.0M, $963.6M) recalled from S-1/10-K filings; re-check against EDGAR (data/ch30_confluent_financials.csv). | open |
| ch30 | ch30: Confluent FY2025 revenue $1,167M and Confluent Cloud $624M (+27%) still rest on a secondary summary; verify vs FY2025 10-K. FY2024 Cloud revenue ($491M) is derived, replace with reported figure. | open |
| ch30 | ch30: Confluent IPO details (June 2021, Nasdaq CFLT, pricing) — re-open 424B4. | open |
| ch30 | ch30: Confluent first non-GAAP operating-profitable quarter. | open |
| ch30 | ch30: Confluent pre-built connector count (120+?) and Confluent Cloud pricing-unit names (eCKU, CFU) and Platform licensing basis. | open |
| ch30 | ch30: Informatica FY2024 GAAP revenue (~$1.6B), net debt at deal (EV vs $8B equity), Oct 2021 re-IPO details, CEO post-close role. | open |
| ch30 | ch30: Informatica FY2014 revenue (~$1.05B) for 2015 take-private multiple. | open |
| ch30 | ch30: Salesforce–Informatica April 2024 talks (WSJ/Reuters) — primary URLs. | open |
| ch30 | ch30: Salesforce post-close disclosure of Informatica (segment, leadership, integration milestones, IDMC neutrality). | open |
| ch30 | ch30: MuleSoft FY2017 revenue (~$297M) for 2018 multiple. | open |
| ch30 | ch30: IBM–HashiCorp ~$6.4B (announced 2024-04, closed 2025-02) and HashiCorp FY2024 revenue (~$583M). | open |
| ch30 | ch30: Boomi sale by Dell to Francisco Partners/TPG (~$4B, 2021) — primary source. | open |
| ch30 | ch30: Matillion Series E ($150M at ~$1.5B, 2021), current CEO, Maia launch date. | open |
| ch30 | ch30: Redpanda–Benthos acquisition (2024) date and terms. | open |
| ch30 | ch30: Estuary Series A $17M vs $14M; founding year, HQ and CEO. | open |
| ch30 | ch30: Airbyte current agent-facing product names (2025–26). | open |
| ch30 | ch30: dbt platform 2026 pricing (seats plus models-built meter). | open |
| ch30 | ch30: Qlik Open Lakehouse product status. | open |
| ch30 | ch30: Any Fivetran + dbt Labs IPO filing/timetable reports. | open |
| ch30 | ch30: Post-close attrition/integration reports for Confluent (IBM) and Informatica (Salesforce). | open |
| ch30 | ch30: S3-compatible on-prem support for WarpStream BYOC, Redpanda Cloud Topics, AutoMQ, Bufstream; Fivetran hybrid deployment S3-compatible destinations. | open |
| ch32 | ch32: Search budget exhausted during drafting; all items below rest on datasets or training knowledge (pre-mid-2025) and need live re-checking. | open |
| ch32 | ch32: Pinecone reported 2025 sale exploration — publisher, date and current status (any transaction in 2025–2026?). | open |
| ch32 | ch32: Pinecone serverless launch date (Jan 2024) and pricing units (read/write units, GB-month). | open |
| ch32 | ch32: Weaviate Series B day/lead (Apr 2023, Index Ventures) — only aggregator source (Clay). | open |
| ch32 | ch32: Milvus LF AI & Data graduation date; Zilliz total funding and any post-2022 round. | open |
| ch32 | ch32: Chroma seed (~$18M, 2023) and Chroma Cloud launch. | open |
| ch32 | ch32: turbopuffer funding rounds and customer list (company-stated). | open |
| ch32 | ch32: LlamaIndex Series A (~$19M, 2025) details; Vectara and Contextual AI Series A sizes. | open |
| ch32 | ch32: Scale AI Series F day; Scale permanent CEO after Jason Droege's interim appointment; July 2025 layoff (~14%) primary source; post-Meta customer exits. | open |
| ch32 | ch32: Surge AI 2024 revenue (>$1B, press-reported) and whether the 2025 round at up to $25B closed. | open |
| ch32 | ch32: Mercor valuations ($2B Feb 2025; ~$10B Oct 2025). | open |
| ch32 | ch32: Snorkel AI Series D (~$100M at ~$1.3B, May 2025) and Turing Series E (~$111M at ~$2.2B, Mar 2025). | open |
| ch32 | ch32: VAST Data product timeline (DataBase 2023, InsightEngine Oct 2024, AI Operating System 2025); VAST company-stated ARR/bookings at Series E and Series F; Series E/F leads; OEM partner list; CoreWeave agreement (~$1.17B, late 2025). | open |
| ch32 | ch32: Hammerspace founding year and pNFS v4.2 technical claims. | open |
| ch32 | ch32: WEKA Series E and NeuralMesh rebrand; DDN–Blackstone investment (Jan 2025, ~$300M at ~$5B). | open |
| ch32 | ch32: NetApp AFX and AI Data Engine announcement (INSIGHT, Oct 2025) and GA status. | open |
| ch32 | ch32: S3 Standard list price (~$0.023/GB-month) used in the worked example. | open |
| ch32 | ch32: OpenAI–Rockset details; Nscale–Anyscale (~$1.65B) close status and primary source. | open |
| ch32 | ch32: Glean ~$300M ARR (May 2026) — find the primary company release (dataset cites Wikipedia). | open |
| ch32 | ch32: ASML Customer Co-Investment Program (2012) stakes — primary source. | open |
| ch32 | ch32: Gross margins of labeling vendors (no audited figures disclosed). | open |
| ch33 | ch33: CEO changes since mid-2025 at Collibra, Alation, Atlan, BigID, Cyera, Varonis (snapshot table uses pre-2025 public record; web search budget exhausted). | open |
| ch33 | ch33: Atlan founding year (2019 assumed), Sentra founding year (c. 2021), 1touch founding year and HQ. | open |
| ch33 | ch33: Alation–Numbers Station acquisition (2025) — date and terms. | open |
| ch33 | ch33: Reports of headcount reductions at Collibra and Alation, 2023–2026; any Collibra priced round or secondary mark since 2021. | open |
| ch33 | ch33: Vendor pricing units for Collibra, Alation, Atlan, Cyera, BigID (business-model table uses author's summary). | open |
| ch33 | ch33: Reconciliation of Proofpoint–Varonis $6.3B headline value to ~$5.71B equity value (convertible notes / dilutive securities?). | open |
| ch33 | ch33: Informatica CY2024 GAAP revenue (~$1.64B, pre-2025 knowledge) used for ~4.9x Salesforce–Informatica multiple. | open |
| ch33 | ch33: Zscaler DSPM acquisitions (none in data/ma_deals.csv). | open |
| ch33 | ch33: Commvault–Satori Cyber acquisition (believed 2025) — date and terms. | open |
| ch33 | ch33: Rubrik–Laminar primary release (Aug 2023); Palo Alto–Dig announcement day; Veeam–Securiti announcement date (Oct 2025); Cyera Series D/E leads and days. | open |
| ch33 | ch33: ServiceNow–data.world closing confirmation. | open |
| ch34 | (ch34) Session web-search budget was exhausted before research began; all items below rest on Atlas datasets or pre-mid-2025 training knowledge. | open |
| ch34 | (ch34) Salesforce Data Cloud renamed "Data 360" (and "Agentforce 360") at Dreamforce Oct 2025 — confirm name and date. | open |
| ch34 | (ch34) Latest Salesforce Data Cloud/Data 360 and AI ARR and any Agentforce ARR (FY2026/FY2027 disclosures); confirm FY2025 ~$900M, ~120% figure and Q4 FY2025 release URL. | open |
| ch34 | (ch34) Agentforce pricing: $2/conversation (2024) and Flex Credits $0.10/action, $500 per 100k credits (May 2025) — confirm URLs and current list prices. | open |
| ch34 | (ch34) Salesforce Zero Copy Partner Network current partner list (Snowflake, Databricks, BigQuery, Redshift; Fabric?) and Snowflake bidirectional GA blog date. | open |
| ch34 | (ch34) Salesforce Genie/Data Cloud Dreamforce 2022 launch URL; Agentforce GA announcement URL. | open |
| ch34 | (ch34) Salesforce–Own ($1.9B, 2024-09) value and closing — CSV row is training knowledge. | open |
| ch34 | (ch34) ServiceNow Workflow Data Fabric announcement date, RaptorDB origin, zero-copy connector list (Databricks, Snowflake, BigQuery). | open |
| ch34 | (ch34) ServiceNow AI Control Tower status; Now Assist Pro Plus/Enterprise Plus packaging and pricing; latest Now Assist ACV. | open |
| ch34 | (ch34) ServiceNow–data.world closing confirmation. | open |
| ch34 | (ch34) SAP Business Data Cloud announcement URL (2025-02-13); "SAP Snowflake" announcement and status; BigQuery BDC Connect; BDC pricing units (capacity units, AI units). | open |
| ch34 | (ch34) SAP–Dremio closing date (~Jul 2026) and SAP plans for Dremio OSS and partner channel. | open |
| ch34 | (ch34) SAP sovereign-cloud scope in 2026 (Delos Cloud, EU sovereign offerings). | open |
| ch34 | (ch34) Workday Agent System of Record (Feb 2025), Paradox (Aug 2025) and Sana (~$1.1B, Sep 2025) deals — dates, values, closings; HiredScore and Evisort (2024). | open |
| ch34 | (ch34) "Workday Data Cloud" name, zero-copy partners (Databricks, Snowflake, Salesforce) and GA status; Workday agent pricing/Flex Credits. | open |
| ch34 | (ch34) Workday and SAP BDC hosting infrastructure (which hyperscalers). | open |
| ch34 | (ch34) Palantir–Databricks partnership (2025) date/scope; Palantir–Snowflake partnership; AIP page. | open |
| ch34 | (ch34) Microsoft Copilot Studio agent pricing meters; Oracle Fusion Data Intelligence, AI Agent Studio names and pricing, Oracle semantic models. | open |
| ch34 | (ch34) ServiceNow self-hosted deployment options and own data centres (Everpure section). | open |
| ch29 | ch29: Web-search budget was exhausted before any ch29 search ran; all items below rest on repo data files, other chapters' sources or pre-mid-2025 knowledge. | open |
| ch29 | ch29: MongoDB Q2 FY2027 — confirm Atlas share of revenue (~73%), non-GAAP operating margin (~24%) and customer count (>69,300) against the 2026-09-01 release; also confirm YoY growth (CSV says 30%; $771.8M / $591.4M computes 30.5%). | open |
| ch29 | ch29: MongoDB CEO transition Dev Ittycheria -> Chirantan "CJ" Desai (Nov 2025) — confirm release, date, effective date and Ittycheria's continuing role. | open |
| ch29 | ch29: MongoDB quarterly revenue Q1 FY2024–Q3 FY2026 in data/ch29_mongodb_quarterly.csv — verify each against the 8-K releases (they reconcile to 10-K annual totals); add Q1 FY2027 (Feb–Apr 2026). | open |
| ch29 | ch29: MongoDB quarterly Atlas growth FY2025–FY2026 and size of the FY2025 multi-year EA licence headwind. | open |
| ch29 | ch29: MongoDB FY2026 Annual Report (ARS) publication date. | open |
| ch29 | ch29: Oracle FY2025 cloud services and license support ($44.0B) and total revenue ($57.4B) — confirm against Oracle Q4 FY2025 release (2025-06). | open |
| ch29 | ch29: Oracle co-CEOs Clay Magouyrk and Mike Sicilia — confirm appointment and date. | open |
| ch29 | ch29: Oracle support at ~22% of net licence fee — find an Oracle primary source. | open |
| ch29 | ch29: Redis Inc. CEO (Rowan Trollope) and Series G ($110M at >$2B, Apr 2021) primary source; Valkey vector-search status. | open |
| ch29 | ch29: Couchbase last public fiscal-year revenue (~$200M), licence (BSL), Capella AI services, and Haveli announcement date (2025-06-20). | open |
| ch29 | ch29: SingleStore–Vector Capital completion; DataStax and SingleStore 2021–22 valuation marks. | open |
| ch29 | ch29: PlanetScale last disclosed round; EDB ownership by Bain Capital (2019) and EDB Postgres AI product. | open |
| ch29 | ch29: YugabyteDB $1.3B (Oct 2021) valuation; Aerospike Series E ($109M, Apr 2024); TiDB, ScyllaDB, CockroachDB, YugabyteDB and Aerospike vector-search features. | open |
| ch29 | ch29: ScyllaDB source-available licence change (blog 2024-12-18) URL and date. | open |
| ch29 | ch29: Neon ">80% of databases created by AI agents" — exact wording in Databricks' 2025-05 press release. | open |
| ch29 | ch29: Supabase as default backend for Lovable/Bolt — find company or press statement. | open |
| ch29 | ch29: Stack Overflow 2025 PostgreSQL usage (55.6%) and DB-Engines July 2026 positions — confirm on primary pages (shared with ch02). | open |
| ch29 | ch29: Gartner cloud DBMS share (~61%) is derived and indicative. | open |
