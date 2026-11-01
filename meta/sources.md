# Sources register

Retrieval date for all entries is 2026-11-01 unless stated. **Verification note:** direct page fetching was blocked by this session's network allowlist. Seminal-paper URLs below are canonical DOI, publisher or author-hosted links. Entries marked "(search-confirmed)" appeared in live search results on 2026-11-01. Entries marked "(canonical, not live-fetched)" are the standard citations and are stable, but should be click-checked by `scripts/check_links.py`. Exact paths marked `[VERIFY]` should be confirmed first.

## Seminal papers and docs

### Relational foundations
- **Codd (1970)**, "A Relational Model of Data for Large Shared Data Banks", *Communications of the ACM* 13(6). https://doi.org/10.1145/362384.362685 (canonical, not live-fetched)
- **System R**
  - Astrahan et al. (1976), "System R: Relational Approach to Database Management", *ACM TODS* 1(2). https://doi.org/10.1145/320455.320457 (canonical, not live-fetched)
  - Retrospective: Chamberlin et al. (1981), "A History and Evaluation of System R", *CACM* 24(10). https://doi.org/10.1145/358769.358784 (canonical, not live-fetched)

### Cloud warehouse and lakehouse
- **Snowflake (SIGMOD 2016)**: Dageville et al., "The Snowflake Elastic Data Warehouse". https://doi.org/10.1145/2882903.2903741 (canonical, not live-fetched)
- **Lakehouse (CIDR 2021)**: Armbrust, Ghodsi, Xin, Zaharia, "Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics". https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf (canonical, not live-fetched)
- **Delta Lake (VLDB 2020)**: Armbrust et al., "Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores", PVLDB 13(12). https://www.vldb.org/pvldb/vol13/p3411-armbrust.pdf (canonical, not live-fetched)

### Google and Amazon distributed-systems papers
- **Dremel (VLDB 2010)**: Melnik et al., "Dremel: Interactive Analysis of Web-Scale Datasets". https://research.google/pubs/dremel-interactive-analysis-of-web-scale-datasets-2/ ; PDF: https://www.vldb.org/pvldb/vldb2010/papers/R29.pdf (canonical, not live-fetched)
- **Spanner (OSDI 2012)**: Corbett et al., "Spanner: Google's Globally-Distributed Database". https://www.usenix.org/conference/osdi12/technical-sessions/presentation/corbett (canonical, not live-fetched)
- **Bigtable (OSDI 2006)**: Chang et al., "Bigtable: A Distributed Storage System for Structured Data". https://www.usenix.org/legacy/event/osdi06/tech/chang/chang.pdf (canonical, not live-fetched)
- **Dynamo (SOSP 2007)**: DeCandia et al., "Dynamo: Amazon's Highly Available Key-value Store". https://doi.org/10.1145/1294261.1294281 ; author copy: https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf (canonical, not live-fetched)
- **MapReduce (OSDI 2004)**: Dean & Ghemawat, "MapReduce: Simplified Data Processing on Large Clusters". https://www.usenix.org/legacy/event/osdi04/tech/full_papers/dean/dean.pdf (canonical, not live-fetched)
- **GFS (SOSP 2003)**: Ghemawat, Gobioff, Leung, "The Google File System". https://doi.org/10.1145/945445.945450 (canonical, not live-fetched)

### Streaming and consensus
- **Kafka (NetDB 2011)**: Kreps, Narkhede, Rao, "Kafka: a Distributed Messaging System for Log Processing". https://www.microsoft.com/en-us/research/wp-content/uploads/2017/09/Kafka.pdf (canonical, not live-fetched) `[VERIFY path]`
- **Raft (USENIX ATC 2014)**: Ongaro & Ousterhout, "In Search of an Understandable Consensus Algorithm". https://www.usenix.org/conference/atc14/technical-sessions/presentation/ongaro ; extended version: https://raft.github.io/raft.pdf (canonical, not live-fetched)
- **Paxos Made Simple (2001)**: Lamport. https://lamport.azurewebsites.net/pubs/paxos-simple.pdf (canonical, not live-fetched)

### Columnar and vectorised execution
- **C-Store (VLDB 2005)**: Stonebraker et al., "C-Store: A Column-oriented DBMS". https://dl.acm.org/doi/10.5555/1083592.1083658 (canonical, not live-fetched) `[VERIFY DOI]`
- **MonetDB/X100 (CIDR 2005)**: Boncz, Zukowski, Nes, "MonetDB/X100: Hyper-Pipelining Query Execution". https://www.cidrdb.org/cidr2005/papers/P19.pdf (canonical, not live-fetched)

### Vector search and retrieval
- **HNSW**: Malkov & Yashunin, "Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs", arXiv 2016 / IEEE TPAMI 2020. https://arxiv.org/abs/1603.09320 ; https://doi.org/10.1109/TPAMI.2018.2889473 (canonical, not live-fetched)
- **DiskANN (NeurIPS 2019)**: Subramanya et al., "DiskANN: Fast Accurate Billion-point Nearest Neighbor Search on a Single Node". https://proceedings.neurips.cc/paper/2019 (proceedings index; search the title) `[VERIFY paper-specific URL]`
- **RAG (NeurIPS 2020)**: Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks". https://arxiv.org/abs/2005.11401 (canonical, not live-fetched)

### Table formats, file formats and catalogs (official docs)
- **Apache Iceberg table spec**: https://iceberg.apache.org/spec/ (canonical). v3 context: https://www.databricks.com/en/blog/iceberg-v3-moving-ecosystem-towards-unification (search-confirmed)
- **Delta Lake protocol**: https://github.com/delta-io/delta/blob/master/PROTOCOL.md (canonical, not live-fetched)
- **Apache Hudi docs**: https://hudi.apache.org/docs/overview (canonical, not live-fetched)
- **Apache Parquet docs**: https://parquet.apache.org/docs/ (canonical, not live-fetched)
- **Apache Arrow docs**: https://arrow.apache.org/docs/ ; columnar format spec: https://arrow.apache.org/docs/format/Columnar.html (canonical, not live-fetched)
- **Lance format docs**: https://docs.lancedb.com/lance (search-confirmed); repo: https://github.com/lancedb/lance (canonical)
- **DuckLake**: https://ducklake.select/ ; v1.0 announcement: https://duckdb.org/2026/04/13/ducklake-10.html (search-confirmed)
- **Unity Catalog OSS**: https://github.com/unitycatalog/unitycatalog ; https://www.unitycatalog.io/ (canonical, not live-fetched)
- **Apache Polaris**: https://polaris.apache.org/ ; graduation post: https://polaris.apache.org/blog/2026/02/19/apache-polaris-graduates-to-top-level-project/ (search-confirmed)

### Agent protocol
- **Model Context Protocol spec**: https://modelcontextprotocol.io/specification (canonical, not live-fetched). Governance: https://anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation (search-confirmed, 2025-12-09)

## Current-state sources

All search-confirmed on 2026-11-01. Full footnotes with dates are in `meta/research-briefing.md`.

### Everpure (formerly Pure Storage)
- SEC EDGAR, Everpure 10-Q (Q1 FY2027, period ended 2026-05-03): https://www.sec.gov/Archives/edgar/data/0001474432/000147443226000061/pstg-20260503.htm
- SEC EDGAR, Everpure 10-K FY2026: https://www.sec.gov/Archives/edgar/data/1474432/000147443226000027/pstg-20260201.htm
- SEC EDGAR, Everpure 8-K Ex. 99.1 (Q4 FY2026 release): https://www.sec.gov/Archives/edgar/data/1474432/000147443226000015/pstg-ex991q4fy2026.htm
- Everpure IR, Q4 FY2026 release PDF: https://s21.q4cdn.com/687136699/files/doc_financials/2026/q4/Everpure-Q4FY2026-Earnings-Press-Release.pdf
- Everpure IR, prepared remarks: https://s21.q4cdn.com/687136699/files/doc_financials/2026/q4/Q4FY26-Everpure-Prepared-Remarks.pdf
- Everpure DEF 14A (2026): https://www.sec.gov/Archives/edgar/data/0001474432/000147443226000041/pstg-20260430.htm
- Barchart (release syndication): https://www.barchart.com/story/news/424030/everpure-announces-fiscal-fourth-quarter-and-full-year-2026-financial-results
- WWT (rename + 1touch release): https://www.wwt.com/news/pure-storage-rebrands-to-everpure-and-announces-intent-to-acquire-1touch
- ITdaily: https://itdaily.com/news/business/pure-storage-everpure-1touch/
- ChannelWeb UK (CEO interview): https://www.channelweb.co.uk/news-network/2026/pure-storage-ceo-on-everpure
- Cleary Gottlieb (closing): https://www.clearygottlieb.com/news-and-insights/news-listing/everpure-completes-acquisition-of-1touch
- Let's Data Science / SDxCentral (brand collision; weak): https://letsdatascience.com/news/everpure-rebrands-targets-broader-data-management-147ec5d5
- Pentair IR (2003 Everpure water-filtration acquisition): https://investors.pentair.com/investor-relations/news-releases/news-release-details/2003/Acquisition-of-Everpure-Makes-Pentair-a-Leading-Provider-of-Filtration-Systems-And-Products-for-Residential-and-Commercial-Markets/default.aspx
- PR Newswire (Data-Primacy Architecture): https://www.prnewswire.com/news-releases/everpure-unveils-data-primacy-architecture-for-the-ai-era-302803097.html
- Everpure newsroom (Data Stream): https://www.everpuredata.com/company/newsroom/press-releases/everpure-announces-data-stream.html
- Everpure newsroom (data-centric architecture): https://www.everpuredata.com/company/newsroom/press-releases/everpure-unveils-data-centric-architecture.html
- SiliconANGLE (Accelerate 2026): https://siliconangle.com/2026/06/17/everpure-accelerates-ai-workloads-data-stream-unveils-data-primacy-architectural-vision/
- Computer Weekly (Universal Data Intelligence): https://www.computerweekly.com/news/366644438/Everpure-aims-to-bridge-AI-data-gap-with-Universal-Data-Intelligence
- TechTarget (Accelerate 2026 highlights): https://www.techtarget.com/it-infrastructure/opinion/7-highlights-from-Pure-Accelerate-2026
- Techzine (Data Stream pipeline): https://www.techzine.eu/blogs/infrastructure/144105/stop-vectorizing-garbage-inside-everpures-smart-ai-data-pipeline/
- Blocks & Files (control plane, 2026): https://www.blocksandfiles.com/data-management/2026/06/17/everpure-extends-data-and-control-planes-for-agentic-ai/5257407
- Blocks & Files (EDC, 2025): https://blocksandfiles.com/2025/06/18/pure-storage-enterprise-data-cloud/
- IT Brief UK (EDC launch): https://itbrief.co.uk/story/pure-storage-unveils-enterprise-data-cloud-flash-upgrades
- Futurum (data primacy analysis): https://futurumgroup.com/?p=91636
- Seeking Alpha PR (NVIDIA AI Data Platform in FlashBlade, 2025): https://seekingalpha.com/pr/20038454-pure-storage-integrates-nvidia-ai-data-platform-into-flashblade-to-fuel-enterprise-ai
- TechRepublic (FlashBlade//EXA): https://www.techrepublic.com/article/news-pure-storage-event-keynote-flashblade-exa/
- Dremio partner page (Pure): https://www.dremio.com/partners/pure-storage/
- Dremio/Pure solution brief: https://dremio.com/wp-content/uploads/2024/10/Dremio-Pure-Storage-Solutions-Brief-1.pdf
- Everpure partner page (Starburst): https://www.everpuredata.com/la/partners/technology-alliance-partners/starburst.html
- Everpure blog (AWS re:Invent 2025 S3 view): https://blog.everpuredata.com/news-events/aws-reinvent-2025-future-of-enterprise-ai-storage/

### Databricks
- Press release, >$7B run-rate, $190B (2026-08-13): https://www.databricks.com/company/newsroom/press-releases/databricks-grows-80-yoy-surpasses-7b-revenue-run-rate-scales
- PR Newswire, >$5.4B run-rate (2026-02): https://www.prnewswire.com/news-releases/databricks-grows-65-yoy-surpasses-5-4-billion-revenue-run-rate-doubles-down-on-lakebase-and-genie-302682674.html
- Constellation Research: https://www.constellationr.com/insights/news/databricks-hits-7-billion-revenue-run-rate-q2-190-billion-valuation
- Blog, Unity Catalog at DAIS 2026: https://www.databricks.com/blog/whats-new-unity-catalog-data-ai-summit-2026
- Blog, security at DAIS 2026: https://www.databricks.com/blog/whats-new-databricks-platform-security-and-compliance-data-ai-summit-2026
- Blog, Data Intelligence era: https://www.databricks.com/blog/welcome-data-intelligence-era
- DAIS 2025 announcements page: https://www.databricks.com/kr/events/dataaisummit-2025-announcements
- Flexera (DAIS 2026 recap): https://www.flexera.com/blog/perspectives/databricks-data-ai-summit-2026/
- Qubika (DAIS 2026 recap): https://qubika.com/blog/everything-databricks-announced-dais-data-ai-summit-2026/
- Addepto (DAIS 2026 recap): https://addepto.com/blog/databricks-data-ai-summit-2026-new-features-explained/
- Microsoft Tech Community (Azure Databricks at DAIS 2026): https://techcommunity.microsoft.com/blog/azure-databricks/azure-databricks-at-databricks-data--ai-summit-2026-updates-and-new-announcement/4528388
- theCUBE Research (DAIS 2026 wrap-up): https://thecuberesearch.com/databricks-data-ai-summit-2026-wrap-up-the-lakehouse-becomes-the-operating-layer-for-agentic-ai/
- Futurum (DAIS, LTAP): https://futurumgroup.com/insights/databricks-data-ai-summit-looking-beyond-the-database-through-unified-transactions-analytics-and-agentic-ai/
- Capital One Software (DAIS 2025): https://www.capitalone.com/software/blog/databricks-top-features-announced-data-engineers-2025
- Forrester (DAIS 2025, Databricks One): https://www.forrester.com/blogs/beyond-the-lakehouse-databricks-bold-play-for-the-business-persona
- TechRepublic (Neon, ~$1B): https://www.techrepublic.com/article/news-databricks-neon-acquisition/
- Reuters via TradingView (Tecton): https://tr.tradingview.com/news/reuters.com,2025:newsml_L6N3UE0R1:0-databricks-to-buy-sequoia-backed-tecton-in-ai-agent-push

### Snowflake
- Business Wire, Q2 FY2027 results (2026-09-02): https://secure.businesswire.com/news/home/20260902386235/en/Snowflake-Reports-Financial-Results-for-the-Second-Quarter-of-Fiscal-2027
- Flexera (Summit 2026 recap): https://www.flexera.com/blog/perspectives/snowflake-summit-2026/
- SELECT (Summit 2026 recap): https://select.dev/posts/snowflake-summit-2026-product-announcement-recap
- Atlan (Summit 2026): https://atlan.com/know/snowflake/summit-2026-announcements/
- IT Brief Australia (CoWork/CoCo rename): https://itbrief.com.au/story/snowflake-renames-ai-tools-amid-broader-platform-push
- Futurum (Summit 2026): https://futurumgroup.com/insights/at-snowflake-summit-the-snowmentum-was-palpable/
- Atlan (CoWork): https://atlan.com/know/snowflake/snowflake-cowork/
- Atlan (Iceberg v3 on Snowflake): https://atlan.com/know/snowflake/apache-iceberg-v3/
- Constellation (Summit 2025): https://www.constellationr.com/insights/news/snowflake-summit-2025-everything-you-need-know
- BigDATAwire (Summit 2025): https://www.bigdatawire.com/2025/06/03/snowflake-widens-analytics-and-ai-reach-at-summit-25
- Snowflake blog (Polaris TLP): https://www.snowflake.com/en/blog/apache-polaris-top-level-project/
- MarketScreener (Observe agreement): https://uk.marketscreener.com/news/snowflake-inc-signed-a-definitive-agreement-to-acquire-observe-inc-ce7e59ddde80f021
- StockTitan (Snowflake 8-K): https://www.stocktitan.net/sec-filings/SNOW/8-k-snowflake-inc-reports-material-event-a0896c05ace0.html
- Autobound (exec changes; weak): https://www.autobound.ai/companies/snowflake/executive-changes
- Investor Day 2026 transcript summary (weak): https://transcripts.platformaeronaut.com/summaries/summit-and-welcome-to-investor-day-2026-06-02-SNOW
- BIIA (2024 CEO change): https://www.biia.com/?p=111893

### Hyperscalers and Oracle
- AWS News Blog (re:Invent 2025 top announcements): https://aws.amazon.com/blogs/aws/top-announcements-of-aws-reinvent-2025
- AWS Big Data Blog (analytics at re:Invent 2025): https://aws.amazon.com/blogs/big-data/aws-analytics-at-reinvent-2025-unifying-data-ai-and-governance-at-scale
- AWS S3 docs (Iceberg v3): https://docs.aws.amazon.com/AmazonS3/latest/userguide/working-with-apache-iceberg-v3.md
- Blocks & Files (S3 upgrades): https://www.blocksandfiles.com/ai-ml/2025/12/03/aws-piles-on-s3-upgrades-from-vector-search-to-50-tb-objects/1704690
- @IT / ITmedia (re:Invent 2025 database/storage): https://atmarkit.itmedia.co.jp/ait/articles/2512/17/news056.html
- Google Cloud docs (Knowledge Catalog / Dataplex): https://docs.cloud.google.com/dataplex/docs/overview
- Atlan (Gemini Enterprise, formerly Agentspace): https://atlan.com/know/ai-agent/ai-agent-applications/google-agentspace/
- Atlan (Google Knowledge Catalog): https://atlan.com/know/ai-agent/gcp/google-knowledge-catalog/
- G-gen (Next '26 BigQuery): https://blog.g-gen.co.jp/entry/next-26-whats-new-in-bigquery
- BigQuery release notes: https://docs.cloud.google.com/bigquery/docs/release-notes
- VPSRanking (Next '26 recap; weak): https://vpsranking.com/news/cloud/cloud-2026-04-25-google-cloud-next-26-recap/
- Azure blog (Ignite 2025): https://azure.microsoft.com/en-us/blog/azure-at-microsoft-ignite-2025-all-the-intelligent-cloud-news-explained/
- Redmond Magazine (Ignite 2025 data): https://redmondmag.com/articles/2025/11/18/big-data-platform-changes-emerge-at-ignite-as-microsoft-broadens-its-azure-focus.aspx
- Oracle (Database@Google Cloud, AI World): https://www.oracle.com/news/announcement/ai-world-oracle-database-at-google-cloud-adds-new-oracle-ai-database-services-2025-10-14/
- Oracle (Database@Azure, AI World): https://www.oracle.com/news/announcement/ai-world-oracle-database-at-azure-powers-cloud-migrations-for-organizations-across-the-world-2025-10-14/

### Industry events
- IBM–Confluent close: https://www.channelweb.co.uk/news-network/2026/ibm-completes-11bn-confluent-acquisition ; https://www.stocktitan.net/news/IBM/ibm-completes-acquisition-of-confluent-making-real-time-data-the-lbuwdbharsqe.html
- Salesforce–Informatica close: https://seekingalpha.com/news/4523363-salesforce-completes-acquisition-of-informatica ; terms: https://news.bloomberglaw.com/tech-and-telecom-law/salesforce-agrees-to-buy-informatica-in-deal-worth-8-billion
- Fivetran–dbt Labs close: https://www.fivetran.com/press/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents ; https://www.techtarget.com/data-technologies/news/366643590/Fivetran-DBT-Labs-complete-merger-to-form-data-layer-for-AI
- SAP–Dremio: https://www.dremio.com/newsroom/sap-to-acquire-dremio-to-unify-sap-and-non-sap-data-to-power-agentic-ai/ ; https://www.cio.com/article/4166881/sap-to-acquire-data-lakehouse-vendor-dremio.html ; https://www.forrester.com/blogs/sap-is-targeting-the-ai-data-control-plane/ ; https://starburst.io/blog/dremio-acquired-by-sap/ ; SAP 6-K: https://www.sec.gov/Archives/edgar/data/0001000184/000110465926118617/tm2628113d1_ex99-1.htm
- Meta–Scale AI: https://techcrunch.com/2025/06/13/scale-ai-confirms-significant-investment-from-meta-says-ceo-alexandr-wang-is-leaving/ ; https://www.nbcchicago.com/news/business/money-report/scale-ais-alexandr-wang-confirms-departure-for-meta-as-part-of-14-3-billion-deal/3767336/
- CoreWeave–W&B: https://investors.coreweave.com/news/news-details/2025/CoreWeave-Completes-Acquisition-of-Weights--Biases/default.aspx ; https://www.maginative.com/article/coreweave-acquires-weights-biases-in-a-1-7-billion-ai-cloud-play/
- ClickHouse $15B: https://bloomberg.com/news/articles/2026-01-16/clickhouse-lands-15-billion-valuation-in-ai-database-race
- Supabase $10.5B: https://www.orrick.com/en/News/2026/06/Supabase-Raises-500-Million-at-10-5-Billion-Valuation-to-Accelerate-Lead-in-Agentic-Infrastructure ; https://itbrief.com.au/story/supabase-raises-usd-500-million-in-series-f-round ; Oct 2026 raise: https://www.nbr.co.nz/tech/supabase-raises-another-us150m/
- Pinecone CEO: https://pinecone.io/blog/growing-ai-ambitions ; https://venturebeat.com/data-management/pinecone-founder-edo-liberty-steps-aside-as-ceo-and-appoints-googler-ash
- Iceberg 1.10 release digest: https://amdatalakehouse.substack.com/p/apache-iceberg-dev-list-digest-sept
- ASF Polaris graduation: https://news.apache.org/foundation/entry/the-apache-software-foundation-graduates-two-open-source-projects-from-incubator
- DuckLake 1.0: https://duckdb.org/2026/04/13/ducklake-10.html
- MCP / Agentic AI Foundation: https://anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
- LanceDB funding (aggregator): https://www.cbinsights.com/company/lancedb/financials

### Regulation
- Council of the EU (AI omnibus deal, 2026-05-07): https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/
- FPF (AI Act timeline under omnibus): https://fpf.org/blog/the-ai-act-implementation-timeline-what-changes-under-the-ai-omnibus/
- White & Case: https://www.whitecase.com/insight-alert/eu-agrees-digital-omnibus-deal-simplify-ai-rules
- Usercentrics (OJ publication / in force): https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/
- MediaLaws (omnibus tracker): https://www.medialaws.eu/digital-omnibus-legislative-tracker/
- Council doc ST-10729-2026: https://data.consilium.europa.eu/doc/document/ST-10729-2026-INIT/en/pdf
- Clifford Chance (omnibus proposal brief): https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2025/11/eu-digital-omnibus-clifford-chance-client-briefing-nov-2025.pdf
- CPPA (final regs, 2025-09-23): https://www.cppa.ca.gov/announcements/2025/20250923.html
- Skadden (CPPA regs): https://www.skadden.com/insights/publications/2025/10/california-finalizes-cppa-regulations

### Market sizing (see `data/market_sizes.csv`)
- Gartner DBMS market-share abstracts: https://www.gartner.com/en/documents/6494271 ; https://www.gartner.com/en/documents/6588602 ; https://www.gartner.com/en/documents/5441963
- TechRepublic (Gartner cloud DBMS 2021): https://www.techrepublic.com/article/new-gartner-report-shows-massive-growth-database-market-fueled-cloud/
- The Register (Gartner DBMS chart, 2026): https://www.theregister.com/2026/04/21/gartner_bamboozling_dbms_chart_shows/
- Benzinga (Snowflake TAM $170B to $355B): https://www.benzinga.com/analyst-stock-ratings/analyst-color/25/08/47337689/snowflake-analyst-remains-bullish-ahead-of-q2-earnings-release
- Morningstar (Snowflake $342B TAM): https://www.morningstar.com/stocks/after-earnings-is-snowflake-stock-buy-sell-or-fairly-valued-7
