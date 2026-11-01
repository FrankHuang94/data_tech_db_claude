# Research notes: data-infrastructure and AI-data M&A, 2020–2026

Companion to `data/staging/ma_2020_2026.csv` (72 deals, as_of 2026-11-01). All sources retrieved 2026-11-01 through web search. Direct page fetches were blocked in this session (sec.gov, techcrunch.com and others did not resolve), so figures come from search-result extracts of the pages listed below. Rows whose `source` says "training knowledge … [VERIFY]" were **not** re-verified live because the web-search budget ran out. Re-check them before merging into `data/ma_deals.csv`.

## Source list

| Publisher | Title | URL | Published | Retrieved |
|---|---|---|---|---|
| SEC EDGAR / Snowflake | Form 10-K FY2026 (Observe purchase accounting) | https://www.sec.gov/Archives/edgar/data/1640147/000164014726000008/snow-20260131.htm | 2026-03 | 2026-11-01 |
| SEC EDGAR / Snowflake | Form 10-Q, quarter ended 2025-10-31 (Crunchy Data $164.5M) | https://www.sec.gov/Archives/edgar/data/1640147/000164014725000211/snow-20251031.htm | 2025-12 | 2026-11-01 |
| SEC EDGAR / Snowflake | Form 10-Q, quarter ended 2026-04-30 (Natoma Labs ~$110M) | https://www.sec.gov/Archives/edgar/data/0001640147/000164014726000030/snow-20260430.htm | 2026-05/06 | 2026-11-01 |
| SEC EDGAR / Snowflake | Form 10-Q, quarter ended 2023-07-31 (Neeva $185.4M) | https://www.sec.gov/Archives/edgar/data/1640147/000164014723000199/snow-20230731.htm | 2023-08/09 | 2026-11-01 |
| SEC EDGAR / Everpure | Form 10-Q, quarter ended 2026-05-03 (1touch $125.0M) | https://www.sec.gov/Archives/edgar/data/0001474432/000147443226000061/pstg-20260503.htm | 2026-06 | 2026-11-01 |
| Cleary Gottlieb | Everpure (f/k/a Pure Storage) to Acquire 1touch / Completes Acquisition | https://www.clearygottlieb.com/news-and-insights/news-listing/everpure-completes-acquisition-of-1touch | 2026-02 / 2026-05 | 2026-11-01 |
| SEC EDGAR / Confluent | Form 10-Q Q3 2024 (WarpStream $135.1M; Immerok $54.9M in earlier 10-Q) | https://www.sec.gov/Archives/edgar/data/1699838/000095017024119042/cflt-20240930.htm | 2024-11 | 2026-11-01 |
| SEC EDGAR / CrowdStrike | Form 10-Q FY2026 (Onum consideration) | https://www.sec.gov/Archives/edgar/data/0001535527/000153552726000031/crwd-20260731.htm | 2026-08/09 | 2026-11-01 |
| Stock Titan (IBM release) / ChannelWeb | IBM completes acquisition of Confluent | https://www.stocktitan.net/news/IBM/ibm-completes-acquisition-of-confluent-making-real-time-data-the-lbuwdbharsqe.html | 2026-03-17 | 2026-11-01 |
| Business Wire via FinancialContent | Salesforce Completes Acquisition of Informatica | https://markets.financialcontent.com/clarkebroadcasting.mymotherlode/article/bizwire-2025-11-18-salesforce-completes-acquisition-of-informatica | 2025-11-18 | 2026-11-01 |
| Bloomberg Law | Salesforce Reaches an $8 Billion Deal to Buy Informatica | https://news.bloomberglaw.com/tech-and-telecom-law/salesforce-agrees-to-buy-informatica-in-deal-worth-8-billion | 2025-05 | 2026-11-01 |
| Fivetran | Fivetran & dbt Labs complete merger | https://www.fivetran.com/press/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents | 2026-06 | 2026-11-01 |
| dbt Labs | dbt Labs and Fivetran sign definitive agreement to merge | https://www.getdbt.com/blog/dbt-labs-and-fivetran-sign-definitive-agreement-to-merge | 2025-10-13 | 2026-11-01 |
| Fivetran | Fivetran Acquires Tobiko Data | https://www.fivetran.com/press/fivetran-acquires-tobiko-data-to-power-the-next-generation-of-advanced-ai-ready-data-transformation | 2025-09-03 | 2026-11-01 |
| Fivetran | Fivetran to Acquire HVR; $565M Series D | https://www.fivetran.com/press/fivetran-to-acquire-hvr-announces-565-million-in-series-d-funding | 2021-09-20 | 2026-11-01 |
| Business Wire | Fivetran signs agreement to acquire Census | https://www.businesswire.com/news/home/20250501266140/en | 2025-05-01 | 2026-11-01 |
| Databricks | Databricks Completes Acquisition of MosaicML | https://www.databricks.com/company/newsroom/press-releases/databricks-completes-acquisition-mosaicml | 2023-07-19 | 2026-11-01 |
| TechCrunch | Databricks acquires Arcion for $100M | https://techcrunch.com/2023/10/23/after-43b-valuation-databricks-acquires-data-replication-startup-arcion-for-100m | 2023-10-23 | 2026-11-01 |
| TechCrunch | Databricks reportedly paid $2 billion in Tabular acquisition | https://techcrunch.com/2024/08/14/databricks-reportedly-paid-2-billion-in-tabular-acquisition | 2024-08-14 | 2026-11-01 |
| TechRepublic | Databricks to Acquire Neon in $1 Billion Deal | https://www.techrepublic.com/article/news-databricks-neon-acquisition/ | 2025-05-15 | 2026-11-01 |
| Databricks | Mooncake Labs joins Databricks | https://www.databricks.com/blog/mooncake-labs-joins-databricks-accelerate-vision-lakebase | 2025-10-01 | 2026-11-01 |
| Fenwick | Fenwick Represents Databricks in Acquisition of the Assets of Tecton | https://www.fenwick.com/insights/experience/fenwick-represents-databricks-in-acquisition-of-the-assets-of-tecton | 2025-08/09 | 2026-11-01 |
| SiliconANGLE | Databricks buys feature engineering startup Fennel | https://siliconangle.com/2025/04/17/databricks-buys-feature-engineering-startup-fennel-enhance-ai-model-development/ | 2025-04-17 | 2026-11-01 |
| Databricks | Databricks Acquires BladeBridge Technology and Talent | https://www.databricks.com/company/newsroom/press-releases/databricks-acquires-bladebridge-technology-and-talent | 2025-02 | 2026-11-01 |
| SiliconANGLE | Databricks introduces Lakewatch SIEM, acquires two cybersecurity startups | https://siliconangle.com/2026/03/24/databricks-introduces-lakewatch-siem-acquires-two-cybersecurity-startups/ | 2026-03-24 | 2026-11-01 |
| Databricks | Databricks Agrees to Acquire Panther | https://www.databricks.com/company/newsroom/press-releases/databricks-agrees-acquire-panther-further-establishing-security | 2026-06-16 | 2026-11-01 |
| InfoWorld | Databricks acquires Electric | https://www.infoworld.com/article/4209184/databricks-acquires-electric-to-bring-local-postgres-databases-to-agentic-apps.html | 2026-08-11 | 2026-11-01 |
| TechCrunch | Databricks buys Row Zero and is scouting for more startups | https://techcrunch.com/2026/09/24/databricks-buys-row-zero-and-is-scouting-for-more-startups-to-acquire/ | 2026-09-24 | 2026-11-01 |
| TechCrunch | Snowflake announces intent to buy Observe | https://techcrunch.com/2026/01/08/snowflake-announces-its-intent-to-buy-observability-platform-observe | 2026-01-08 | 2026-11-01 |
| TechCrunch | Snowflake to acquire database startup Crunchy Data | https://www.techcrunch.com/2025/06/02/snowflake-to-acquire-database-startup-crunchy-data/ | 2025-06-02 | 2026-11-01 |
| Snowflake | Snowflake to Acquire Select Star | https://www.snowflake.com/en/blog/snowflake-acquire-select-star/ | 2025-11-24 | 2026-11-01 |
| Snowflake | Snowflake Agrees to Acquire Datavolo | https://www.snowflake.com/news/snowflake-agrees-to-acquire-open-data-integration-platform-datavolo/ | 2024-11-20 | 2026-11-01 |
| TechCrunch | Snowflake goes all in on data clean rooms with Samooha | https://techcrunch.com/2023/12/18/snowflake-goes-all-in-on-data-clean-rooms-with-samooha-acquisition | 2023-12-18 | 2026-11-01 |
| TechCrunch | Snowflake acquires Streamlit for $800M | https://techcrunch.com/2022/03/02/snowflake-acquires-streamlit-for-800m-to-help-customers-build-data-based-apps/ | 2022-03-02 | 2026-11-01 |
| Snowflake | Snowflake to Acquire Applica | https://www.snowflake.com/en/blog/snowflake-to-acquire-applica/ | 2022-08-24 | 2026-11-01 |
| Intelligence Community News | Snowflake acquires Night Shift Development | https://intelligencecommunitynews.com/snowflake-acquires-night-shift-development/ | 2024-09 | 2026-11-01 |
| IBM Newsroom | IBM Completes Acquisition of StreamSets and webMethods | https://newsroom.ibm.com/2024-07-01-IBM-Completes-Acquisition-of-StreamSets-and-webMethods,-Bolstering-its-Automation,-Data-and-AI-Portfolios | 2024-07-01 | 2026-11-01 |
| DBTA | IBM Officially Closes Acquisition of DataStax | https://www.dbta.com/Editorial/News-Flashes/IBM-Officially-Closes-Acquisition-of-DataStax-169711.aspx | 2025-05/06 | 2026-11-01 |
| Business Wire | ServiceNow completes acquisition of Moveworks | https://www.businesswire.com/news/home/20251215128980/en/ServiceNow-completes-acquisition-of-Moveworks | 2025-12-15 | 2026-11-01 |
| TechCrunch | ServiceNow acquires data.world | https://techcrunch.com/2025/05/07/servicenow-acquires-data-world-two-months-after-acquiring-moveworks | 2025-05-07 | 2026-11-01 |
| Bloomberg | OpenAI to Buy Product Testing Startup Statsig for $1.1 Billion | https://www.bloomberg.com/news/articles/2025-09-02/openai-to-buy-product-testing-startup-statsig-for-1-1-billion | 2025-09-02 | 2026-11-01 |
| Olhar Digital | OpenAI adquire Neptune | https://olhardigital.com.br/2025/12/03/pro/openai-adquire-neptune-para-reforcar-controle-sobre-treinamento-de-ia/ | 2025-12-03 | 2026-11-01 |
| Couchbase | Haveli Investments Completes Acquisition of Couchbase | https://www.couchbase.com/press-releases/haveli-investments-completes-acquisition-of-couchbase/ | 2025-09-24 | 2026-11-01 |
| New Relic | Francisco Partners and TPG Complete Acquisition of New Relic | https://newrelic.com/press-release/20231108 | 2023-11-08 | 2026-11-01 |
| Clearlake | Clearlake and Insight Complete Acquisition of Alteryx | https://clearlake.com/clearlake-capital-group-and-insight-partners-complete-acquisition-of-alteryx/ | 2024-03-19 | 2026-11-01 |
| SecurityWeek | Palo Alto Networks to Acquire Chronosphere in $3.35 Billion Deal | https://securityweek.com/palo-alto-networks-to-acquire-observability-platform-chronosphere-in-3-35-billion-deal/ | 2025-11-19 | 2026-11-01 |
| Palo Alto Networks IR | Palo Alto Networks Completes Chronosphere Acquisition | https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-completes-chronosphere-acquisition-unifying | 2026-01-29 | 2026-11-01 |
| Palo Alto Networks | A Decade of Strategic Acquisitions (Dig Security $400M) | https://www.paloaltonetworks.com/cyberpedia/palo-alto-networks-strategic-acquisitions | n/d | 2026-11-01 |
| CrowdStrike IR | CrowdStrike Agrees to Acquire Onum | https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-agrees-acquire-onum-supercharge-falcon-next-gen-siem | 2025-08-27 | 2026-11-01 |
| Cyera | Cyera Acquires Trail Security for $162M | https://www.cyera.com/press-releases/cyera-acquires-trail-security-for-162m-redefining-ai-powered-data-security-with-comprehensive-data-loss-prevention | 2024-10-17 | 2026-11-01 |
| Cohesity | Cohesity completes combination with Veritas | https://www.cohesity.com/press/cohesity-becomes-worlds-largest-data-protection-provider-after-completing-combination-with-veritas-enterprise-data-protection-business/ | 2024-12-10 | 2026-11-01 |
| CoreWeave IR | CoreWeave Completes Acquisition of Weights & Biases | https://investors.coreweave.com/news/news-details/2025/CoreWeave-Completes-Acquisition-of-Weights--Biases/default.aspx | 2025-05-05 | 2026-11-01 |
| TechCrunch | Nvidia completes acquisition of Run:ai | https://techcrunch.com/2024/12/30/nvidia-completes-acquisition-of-ai-infrastructure-startup-runai/ | 2024-12-30 | 2026-11-01 |
| TechCrunch | Nvidia reportedly acquires Gretel | https://techcrunch.com/2025/03/19/nvidia-reportedly-acquires-synthetic-data-startup-gretel | 2025-03-19 | 2026-11-01 |
| Seeking Alpha | MongoDB acquires Voyage AI for $220M | https://seekingalpha.com/news/4412466-mongodb-acquires-voyage-ai-for-220m-to-boost-ai-search | 2025-02-24 | 2026-11-01 |
| Datadog | Datadog acquires Metaplane | https://www.datadoghq.com/about/latest-news/press-releases/datadog-metaplane-acquisition/ | 2025-04 | 2026-11-01 |
| Seeking Alpha | Datadog buying startup Eppo for $220M – report | https://seekingalpha.com/news/4439188-datadog-buying-startup-eppo-for-220m-report | 2025-05 | 2026-11-01 |
| ClickHouse | ClickHouse acquires HyperDX / welcomes Langfuse | https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability | 2025-03-13 / 2026-01-16 | 2026-11-01 |
| TechCrunch | ClickHouse acquires PeerDB | https://techcrunch.com/2024/07/30/real-time-database-startup-clickhouse-acquires-peerdb-to-expand-its-postgres-support | 2024-07-30 | 2026-11-01 |
| NetApp | NetApp Acquires DataPelago | https://www.netapp.com/en/newsroom/press-releases/news-rel-20260716-210092/ | 2026-07-16 | 2026-11-01 |
| SiliconANGLE | Supabase raises $150M, acquires Turso | https://siliconangle.com/2026/10/02/database-startup-supabase-raises-150m-acquires-turso/ | 2026-10-02 | 2026-11-01 |
| BigDATAwire | What Boomi's Acquisition of Elementary Means for Data Teams | https://www.hpcwire.com/bigdatawire/2026/10/26/what-boomis-acquisition-of-elementary-means-for-data-teams/ | 2026-10-26 | 2026-11-01 |
| Startups Acquired | Top startup acquisitions of 2026 (tracker; low confidence) | https://www.startupsacquired.com/top-startup-acquisitions/2026 | rolling | 2026-11-01 |

## Pattern observations

- **Table-format and catalog control came first.** Databricks bought Tabular in June 2024. The WSJ put the price at $1–2B for a company that had raised $37M, so Databricks was paying to take the Iceberg-vs-Delta format fight off the board. After that, catalogs became the contested layer. Snowflake bought Select Star for Horizon (2025) and Natoma for agent/MCP governance (2026), ServiceNow bought data.world, and Salesforce bought Informatica's catalog and MDM.
- **The Postgres land grab was the defining 2025–26 theme.** The moves were Databricks–Neon (~$1B press-reported), Snowflake–Crunchy Data ($164.5M per 10-Q against ~$250M press-reported), Databricks–Mooncake (Postgres-to-columnar), Databricks–Electric/PGlite (agent-local Postgres) and Supabase–Turso (SQLite for agents). The shared argument is that AI agents provision databases on their own, so whoever owns the OLTP database owns the new workloads.
- **Press-reported prices for private targets tend to run high.** Crunchy: ~$250M reported vs $164.5M in the 10-Q. Observe: ~$1B reported vs $596.2M preliminary consideration in the 10-K. Neeva: ~$150M first disclosed, then $185.4M final. Treat outlet figures as upper-bound signals until a filing appears.
- **AI acquihires span from $100M to $14B.** MosaicML ($1.3B), Neeva, Einblick, Lilac, SiftD, Run:ai (~$700M press-reported) and Statsig ($1.1B all-stock) all bought teams. Meta's ~$14.3B 49% Scale AI stake is the extreme case: a non-control investment built to bring in a CEO and steer the data supply, while avoiding a merger review.
- **The modern data stack consolidated into one ingestion-to-activation vendor.** Fivetran bought HVR (CDC, 2021), Census (reverse ETL, 2025) and Tobiko/SQLMesh (2025), then merged with dbt Labs (all-stock, closed 2026-06-01, ~$600M combined ARR). dbt itself had bought Transform for its semantic layer. The standalone point tools of 2020 have mostly been absorbed.
- **Streaming became a strategic asset again.** IBM–Confluent (~$11B EV, closed 2026-03-17) was the largest pure data-infrastructure deal of the period after Cisco–Splunk. Smaller streaming buys support the same view: Confluent–WarpStream ($135.1M, object-storage-native Kafka), Confluent–Immerok (Flink) and CrowdStrike–Onum (telemetry pipeline).
- **Observability turned into a data-platform feature.** Snowflake–Observe, Palo Alto–Chronosphere ($3.35B, ~21x ARR per Calcalist), Datadog–Metaplane, ClickHouse–HyperDX and Langfuse, Databricks–Panther (security lakehouse) and Boomi–Elementary all follow one premise: telemetry is just more data, so it should live on the lakehouse or warehouse.
- **Application vendors bought their way down into the data layer.** Salesforce bought Own ($1.9B) and Informatica (~$8B). ServiceNow bought Moveworks ($2.85B) and data.world. IBM bought StreamSets/webMethods, DataStax and Confluent. Each wants governed, real-time enterprise data feeding its own agents, rather than depending on Snowflake or Databricks.
- **PE take-privates targeted mature, slower-growth data vendors.** Examples: Cloudera ($5.3B, KKR/CD&R), New Relic ($6.5B), Alteryx (~$4.4B incl. debt), Couchbase ($1.5B, Haveli) and Qlik–Talend (Thoma Bravo platform). Haveli also led the funding for Cohesity–Veritas. The model is to buy durable maintenance-style revenue at low multiples and roll it up.
- **Storage vendors are moving up into data services.** Pure–Portworx (2020), NetApp–Instaclustr (2022), Cohesity–Veritas (2024), Everpure–1touch ($125M, 2026, data discovery/classification) and NetApp–DataPelago (2026, GPU data processing at the storage layer) show storage firms buying the metadata and processing layer just above the array. This is the most relevant pattern for an Everpure corp-dev reader.
- **Databricks is the most active serial acquirer.** It made 16 deals in this file, 5 of them in 2026 alone. Nearly all were undisclosed tuck-ins that each fill one platform gap: migration (BladeBridge), features (Fennel, Tecton), OLTP (Neon, Mooncake, Electric), security (Antimatter, Panther) and UI (Row Zero). That pattern points to a buy-not-build approach funded by private capital.
- **Embedding models and retrieval are being folded into databases.** MongoDB–Voyage AI ($220M), IBM–DataStax, OpenAI–Rockset and Nvidia–Gretel show model vendors and database vendors converging on retrieval and synthetic data.

## Gaps / to verify

- Search budget ran out before re-verifying these from live sources: Salesforce–Own, Meta–Scale AI, Cisco–Splunk, Cloudera, Qlik–Talend, OpenAI–Rockset, Pure–Portworx, NetApp–Instaclustr, Snowflake–TruEra year, Couchbase announcement date, Cohesity–Veritas announcement date, and the Alteryx value.
- Exact announcement days still to confirm: Immerok, Dig Security, Lilac, Tecton, Boomi–Elementary.
- Closings not confirmed: Fivetran–Census, ServiceNow–data.world, OpenAI–Statsig, OpenAI–Neptune, Snowflake–Natoma, Databricks–Electric.
- Not researched: Qlik–Upsolver, Qlik–Kyvos, Alation–Numbers Station, Collibra/Atlan deals, Varonis–Cyral, SentinelOne–Observo AI, Redpanda–Benthos, Supabase–OrioleDB, Snowflake–Datometry (tech asset), and Microsoft/AWS/Google/Workday/HPE/Teradata/Nutanix/Matillion deals.
- Apple–Kuzu comes only from a tracker and should be treated as low confidence.
