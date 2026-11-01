# Research briefing: current state of the data / AI-data industry (as of 2026-11-01)

> **Integrator corrections (2026-11-01).** (1) **Ticker:** Everpure announced on 2026-04-07 that its NYSE ticker would change from PSTG to **P**, effective 2026-04-17 (Everpure press release, purestorage.com/company/newsroom/press-releases/everpure-to-change-ticker-symbol.html; Nasdaq, 2026-04-07). Use "NYSE: P (formerly PSTG)". (2) Confirmed: Snowflake Intelligence → **Snowflake CoWork** and Cortex Code → **CoCo**, announced at Snowflake Summit on 2026-06-02 (itdaily.com, itbrief.com.au). (3) Confirmed: Databricks closed a $5B round at a **$190B** valuation on 2026-08-13 and stated a **>$7B revenue run-rate** with >80% YoY growth in its Q2 (company-stated, unaudited); Lakebase >$100M run-rate; data-warehousing >$1.5B run-rate (thenextweb.com; virginiabusiness.com; Morningstar).


**Purpose.** Fact sheet for chapter writers. Each bullet gives the fact in our own words, followed by a footnote with publisher, URL and published date. All items were retrieved on 2026-11-01 unless noted.

**Method caveat (read first).** This sweep used live web search. Direct page fetches (WebFetch) were blocked by the session's network allowlist for most hosts, including everpuredata.com, blocksandfiles.com, storagenewsletter.com and clearygottlieb.com. Facts therefore come from search-engine summaries of the cited pages, not from full-page reads. Before a number is published in a chapter, re-open the primary source (SEC filing or company press release) where possible. Items marked `[VERIFY: …]` were either not confirmed live, came from a single or weak source, or rest on pre-2025 knowledge. The search budget ran out before every item could be checked. See "Open items" at the end.

**Fiscal-year conventions used below**
- Everpure (PSTG): the fiscal year ends on the Sunday nearest early February. "FY2026" ≈ Feb 2025–Jan/Feb 2026 (the 10-K period ended 2026-02-01). FY2027 Q2 ≈ May–Jul 2026.
- Snowflake (SNOW): the fiscal year ends Jan 31. FY2027 = Feb 2026–Jan 2027. Q2 FY2027 = May–Jul 2026.
- Databricks is private. Its figures are **company-stated revenue run-rates**, not GAAP revenue.

---

## A. Everpure (formerly Pure Storage)

### Rename
- Pure Storage announced on **23 Feb 2026** that it would rename itself **Everpure**. It announced the 1touch acquisition the same day. The stated logic is a move in emphasis from flash arrays toward data management for AI: the company no longer wants to be seen only as a storage vendor. The name carries forward the "Pure" and "Evergreen" brand equity.[^a1][^a2]
- Shares began trading as **Everpure on 5 Mar 2026**, keeping the **NYSE: PSTG** ticker. The corporate site is now everpuredata.com, and SEC filings are under "Everpure, Inc." (CIK 0001474432).[^a2][^a3]
- Brand-collision note: "Everpure" is also an existing water-filtration brand, acquired by Pentair in 2004. Expect name confusion in search results.[^a4][^a5]

### Leadership
- **Charles Giancarlo** is Chairman and CEO. **Tarek Robbiati** is CFO; both are quoted in the Q4 FY2026 earnings release.[^a6]

### Financial snapshot (FY2026, GAAP unless labelled)
- FY2026 revenue was **above $3.6B, up 16% YoY**. Q4 FY2026 revenue was about **$1.1B, up 20% YoY**. One summary rounds the full year to "~$3.7B"; use the press-release headline ">$3.6B" until it is checked against the 10-K.[^a6][^a7]
- **Subscription ARR** (company-defined KPI) was **$1.924B at FY2026 year-end, up 16%** from $1.658B. **RPO was $3.7B, up 40%**, and includes $228.5M of non-cancellable product orders. **Non-GAAP** operating margin was **17.3%**. Free cash flow (non-GAAP) was **$616M**.[^a6][^a3]
- FY2027 guidance was not captured in this sweep. `[VERIFY: FY2027 revenue guidance from the Q4 FY2026 release, 2026-03]`

### Enterprise Data Cloud and the intelligent control plane
- **Enterprise Data Cloud (EDC)** launched at **Pure//Accelerate on 19 Jun 2025** in Las Vegas. It is an architecture for managing storage across on-prem, public cloud and hybrid as one virtualised pool of data with unified control. **Pure Fusion** is the mechanism customers use to build their own EDC.[^a8][^a9]
- The **intelligent control plane** sits above the unified data plane and embeds AI-driven automation into operations. Announced items include Copilot workflow execution, enhanced cyber-anomaly detection, workload rebalance and mobility, and Fusion compliance reporting with "agentic triage". Coverage from Accelerate 2026 puts fully automated workload rebalancing in **Q4 2026**. Other roadmap dates come from a LinkedIn post. `[VERIFY: control-plane feature dates]`[^a10][^a11]

### Data-management / data-intelligence announcements, 2025–2026
- **Accelerate 2026 (Las Vegas, 16–18 Jun 2026):** Everpure framed its strategy as **"data primacy"** and launched **Universal Data Intelligence**, which has two parts.[^a11][^a12][^a13]
  - **Data Intelligence** is the productised 1touch technology. It discovers, classifies and adds context to structured and unstructured data across Everpure arrays, public clouds, SaaS apps, mainframes and **third-party storage**, without copying the data. Trade coverage lists connectors to NFS, SMB, object stores, Databricks, Snowflake, SQL Server, Oracle and major SaaS platforms. These are integrations, not announced partnerships.[^a12][^a14]
  - **Data Stream** was announced on **17 Jun 2026** and is reported as generally available. It vectorises relevant data and prepares it for AI pipelines, with stream-level access controls. It runs on **FlashBlade plus NVIDIA GPUs** and is built on the **NVIDIA AI Data Platform** reference design. Everpure also cited further work with NVIDIA ("STX").[^a13][^a14]
- Other Accelerate 2026 items: **Evergreen//One Overdrive**, a temporary burst of on-prem performance (Q3 2026); FlashBlade//EXA SPEC AI benchmark results; and GA of Azure-native VM support for Everpure Cloud.[^a11]
- Earlier in 2025: **FlashBlade//EXA** launched at **NVIDIA GTC on 11 Mar 2025**. It targets AI and HPC, with a vendor claim of >10 TB/s read in a single namespace, and scales metadata separately from data. It was described as GA by Accelerate 2025. At GTC 2025 Pure also said it was integrating the NVIDIA AI Data Platform into FlashBlade.[^a9][^a15]

### 1touch acquisition
- **Announced:** 23 Feb 2026 (intent to acquire). **Closed:** **7 May 2026** per the Everpure 10-Q. Counsel's closing announcement is dated 11 May 2026. 1touch is now a wholly owned subsidiary.[^a3][^a16]
- **Value:** cash consideration of **$125.0M** (GAAP, per 10-Q), subject to customary adjustments and escrow.[^a3]
- **What 1touch does:** It is a data-intelligence and orchestration company. Its software **discovers** data wherever it lives, **classifies** it (including sensitive data) and builds **semantic context** about what the data is and how it relates. Everpure's stated rationale is to move customers from controlling their data to understanding and contextualising it, so that data is "AI-ready". The CEO framed the deal this way.[^a1][^a3][^a12]
- **Status:** integrated and relaunched as Everpure **Data Intelligence** (June 2026).[^a12]

### FlashBlade, S3/object and lakehouse positioning; partnerships
- FlashBlade is Everpure's unified file-and-object (S3-compatible) platform. The company positions it as the on-prem object layer for AI pipelines (Data Stream) and for Iceberg lakehouses.[^a13][^a17]
- **Dremio:** there is a joint FlashBlade + Dremio solution for hybrid Iceberg lakehouses that queries data in place. **Dremio was acquired by SAP**: announced 4 May 2026, closed around July 2026, terms undisclosed. The partnership now runs through an SAP-owned company.[^a17][^a18]
- **Starburst:** Everpure's partner page shows a reference architecture, "Scalable Lakehouse Analytics", combining FlashBlade object storage, Iceberg tables and Starburst's MPP engine.[^a19]
- **NVIDIA:** this is the deepest partnership: AI Data Platform integration (2025), Data Stream on the NVIDIA reference design (2026), and FlashBlade//EXA launched at GTC.[^a13][^a15]
- **Databricks / Snowflake:** this sweep found **no formal partnership announcement** with either. In Everpure coverage they appear as connector targets for Data Intelligence and as contrasting "data platform" strategies. `[VERIFY: any Everpure–Databricks or –Snowflake joint announcement, e.g., Snowflake external-table / S3-compatible storage certification]`[^a14]

[^a1]: World Wide Technology (reposting Pure Storage release), https://www.wwt.com/news/pure-storage-rebrands-to-everpure-and-announces-intent-to-acquire-1touch, 2026-02-23.
[^a2]: ITdaily, "Pure Storage becomes Everpure and acquires 1touch", https://itdaily.com/news/business/pure-storage-everpure-1touch/, 2026-02.
[^a3]: Everpure, Inc., Form 10-Q (quarter ended 2026-05-03), SEC EDGAR, https://www.sec.gov/Archives/edgar/data/0001474432/000147443226000061/pstg-20260503.htm, 2026-06; and Form 10-K FY2026, https://www.sec.gov/Archives/edgar/data/1474432/000147443226000027/pstg-20260201.htm, 2026-03.
[^a4]: Pentair IR, "Acquisition of Everpure…", https://investors.pentair.com/investor-relations/news-releases/news-release-details/2003/Acquisition-of-Everpure-Makes-Pentair-a-Leading-Provider-of-Filtration-Systems-And-Products-for-Residential-and-Commercial-Markets/default.aspx, 2003.
[^a5]: Let's Data Science (summarising SDxCentral), https://letsdatascience.com/news/everpure-rebrands-targets-broader-data-management-147ec5d5, 2026-02 (weak source).
[^a6]: Everpure, Q4 FY2026 earnings press release (8-K Ex. 99.1), https://www.sec.gov/Archives/edgar/data/1474432/000147443226000015/pstg-ex991q4fy2026.htm, and https://s21.q4cdn.com/687136699/files/doc_financials/2026/q4/Everpure-Q4FY2026-Earnings-Press-Release.pdf, 2026-03.
[^a7]: Barchart (press-release syndication), https://www.barchart.com/story/news/424030/everpure-announces-fiscal-fourth-quarter-and-full-year-2026-financial-results, 2026-03.
[^a8]: Blocks & Files, "Pure Storage Enterprise Data Cloud", https://blocksandfiles.com/2025/06/18/pure-storage-enterprise-data-cloud/, 2025-06-18.
[^a9]: IT Brief UK, "Pure Storage unveils Enterprise Data Cloud…", https://itbrief.co.uk/story/pure-storage-unveils-enterprise-data-cloud-flash-upgrades, 2025-06; Pure Storage release text dated 2025-06-19.
[^a10]: Blocks & Files, "Everpure extends data and control planes for agentic AI", https://www.blocksandfiles.com/data-management/2026/06/17/everpure-extends-data-and-control-planes-for-agentic-ai/5257407, 2026-06-17.
[^a11]: TechTarget, "7 highlights from Pure Accelerate 2026", https://www.techtarget.com/it-infrastructure/opinion/7-highlights-from-Pure-Accelerate-2026, 2026-06.
[^a12]: Computer Weekly, "Everpure aims to bridge AI data gap with Universal Data Intelligence", https://www.computerweekly.com/news/366644438/Everpure-aims-to-bridge-AI-data-gap-with-Universal-Data-Intelligence, 2026-06.
[^a13]: Everpure via PR Newswire, "Everpure Unveils Data-Primacy Architecture for the AI Era", https://www.prnewswire.com/news-releases/everpure-unveils-data-primacy-architecture-for-the-ai-era-302803097.html, 2026-06-17; SiliconANGLE, https://siliconangle.com/2026/06/17/everpure-accelerates-ai-workloads-data-stream-unveils-data-primacy-architectural-vision/, 2026-06-17; Everpure newsroom, https://www.everpuredata.com/company/newsroom/press-releases/everpure-announces-data-stream.html, 2026-06-17.
[^a14]: Techzine, "Stop vectorizing garbage: inside Everpure's smart AI data pipeline", https://www.techzine.eu/blogs/infrastructure/144105/stop-vectorizing-garbage-inside-everpures-smart-ai-data-pipeline/, 2026-06.
[^a15]: Pure Storage via Seeking Alpha PR, "Pure Storage Integrates NVIDIA AI Data Platform into FlashBlade", https://seekingalpha.com/pr/20038454-pure-storage-integrates-nvidia-ai-data-platform-into-flashblade-to-fuel-enterprise-ai, 2025-03; TechRepublic, https://www.techrepublic.com/article/news-pure-storage-event-keynote-flashblade-exa/, 2025-03.
[^a16]: Cleary Gottlieb, "Everpure Completes Acquisition of 1touch", https://www.clearygottlieb.com/news-and-insights/news-listing/everpure-completes-acquisition-of-1touch, 2026-05-11.
[^a17]: Dremio partner page, https://www.dremio.com/partners/pure-storage/, and Pure/Dremio solution brief, https://dremio.com/wp-content/uploads/2024/10/Dremio-Pure-Storage-Solutions-Brief-1.pdf, 2024-10.
[^a18]: Dremio newsroom, "SAP to Acquire Dremio…", https://www.dremio.com/newsroom/sap-to-acquire-dremio-to-unify-sap-and-non-sap-data-to-power-agentic-ai/, 2026-05-04; CIO.com, https://www.cio.com/article/4166881/sap-to-acquire-data-lakehouse-vendor-dremio.html, 2026-05; SAP SE Form 6-K, https://www.sec.gov/Archives/edgar/data/0001000184/000110465926118617/tm2628113d1_ex99-1.htm, 2026.
[^a19]: Everpure partner page (Starburst), https://www.everpuredata.com/la/partners/technology-alliance-partners/starburst.html, n.d.

---

## B. Databricks

### Leadership, scale, valuation (private; company-stated)
- **CEO: Ali Ghodsi** (co-founder). `[VERIFY: still CEO as of 2026-11; no change surfaced in this sweep]`
- **Revenue run-rate (company-stated):** **>$7B** with **>80% YoY growth** in its Q2 (announced **13 Aug 2026**). Sub-lines: "Lakehouse" (data warehousing) above a **$1.5B** run-rate, and **Lakebase** above a **$100M** run-rate. The previous mark was **>$5.4B with >65% growth**, announced Feb 2026 for its Q4.[^b1][^b2]
- **Valuation:** a **$5B** "strategic funding" at a **$190B** valuation, led by Coatue with Blackstone, MGX, T. Rowe Price and new investor Sixth Street Growth (Aug 2026). Before that, the **Series L at $134B** (Dec 2025), plus a Feb 2026 package of about $5B equity at $134B and about $2B of debt capacity.[^b1][^b3]
- **IPO:** no date set. Press commentary still treats a listing as expected but unscheduled.[^b3]

### Current product names and status
- **Data Intelligence Platform** is still the umbrella brand (launched Dec 2023).[^b4]
- **Unity Catalog** is the governance layer. At DAIS 2026 Databricks added **Domains** (Public Preview) and **Unity AI Gateway**, which it positions as governance for all AI spend and agent traffic. **OpenSharing** (the Delta Sharing lineage) is now a **Linux Foundation** project. Unity Catalog OSS (github.com/unitycatalog) remains open source. `[VERIFY: LF AI & Data maturity stage of Unity Catalog OSS]`[^b5][^b6]
- **Lakebase** is serverless Postgres inside the platform, built on the Neon acquisition. It entered public preview at DAIS 2025 and was reported **GA** at DAIS 2026, with cross-region and cross-cloud failover and availability in Free Edition.[^b6][^b7]
- **Agent Bricks** launched at DAIS 2025 as a no-code way to build, evaluate and auto-optimise agents. In 2026 it expanded into a developer agent platform; Databricks claims 100k+ agents built. **Omnigent** is an open-source "meta-harness" for agents, announced at DAIS 2026.[^b6][^b8]
- **Genie:** AI/BI Genie evolved into **Genie One**, an "agentic coworker" with connectors to Drive, Jira, Slack and 50+ apps, reported GA. **Genie Ontology** is a live context layer for agents; sources disagree on whether it is Preview or GA. Databricks calls Genie its "AI coworker".[^b1][^b6][^b9]
- **Databricks One** (business-user front end) launched in private preview at DAIS 2025.[^b8]
- **Lakeflow** covers ingestion and pipelines; **Lakeflow Designer** (no-code ETL) was announced at DAIS 2025 in preview.[^b8]
- **New at DAIS 2026:** **Lakehouse//RT** on a real-time engine called "Reyden"; **LTAP**, which unifies Lakebase and the lakehouse on one copy of data and is described as "coming soon"; App Spaces and Genie App Builder alongside **Databricks Apps**; FedRAMP High on Azure.[^b6][^b9][^b10]
- **Delta Lake / UniForm, Photon, Mosaic AI:** these names were not re-verified in this sweep. They are believed current, with Mosaic AI branding increasingly folded under Agent Bricks. `[VERIFY: current status of the Mosaic AI brand and UniForm naming]`
- **DAIS 2025 (San Francisco, Jun 2025)** also introduced **Databricks Free Edition**.[^b8]
- **DAIS 2026** was held in San Francisco, 15–18 Jun 2026, themed around agents.[^b6]

### Databricks M&A (data-relevant)
- **Neon** (serverless Postgres): announced May 2025 at about **$1B** (press-reported). The technology now ships as Lakebase. `[VERIFY: formal close date]`[^b11]
- **Tecton** (feature store / real-time ML features): announced Aug 2025, terms undisclosed. One database lists the close as 22 Aug 2025. `[VERIFY]`[^b12]

[^b1]: Databricks press release, "Databricks Grows >80% YoY, Surpasses $7B Revenue Run-Rate…", https://www.databricks.com/company/newsroom/press-releases/databricks-grows-80-yoy-surpasses-7b-revenue-run-rate-scales, 2026-08-13.
[^b2]: Databricks via PR Newswire, "Databricks Grows >65% YoY, Surpasses $5.4 Billion Revenue Run-Rate…", https://www.prnewswire.com/news-releases/databricks-grows-65-yoy-surpasses-5-4-billion-revenue-run-rate-doubles-down-on-lakebase-and-genie-302682674.html, 2026-02.
[^b3]: Constellation Research, "Databricks hits $7 billion revenue run rate in Q2, $190 billion valuation", https://www.constellationr.com/insights/news/databricks-hits-7-billion-revenue-run-rate-q2-190-billion-valuation, 2026-08.
[^b4]: Databricks blog, "Welcome to the data intelligence era", https://www.databricks.com/blog/welcome-data-intelligence-era, 2023-12.
[^b5]: Databricks blog, "What's new with Unity Catalog at Data + AI Summit 2026", https://www.databricks.com/blog/whats-new-unity-catalog-data-ai-summit-2026, 2026-06.
[^b6]: Flexera, "Databricks Data + AI Summit 2026 recap", https://www.flexera.com/blog/perspectives/databricks-data-ai-summit-2026/, 2026-06; Qubika, https://qubika.com/blog/everything-databricks-announced-dais-data-ai-summit-2026/, 2026-06.
[^b7]: Polestar Analytics, DAIS 2026 highlights, https://www.polestaranalytics.com/blog/databricks-data-ai-summit-2026-highlights, 2026-06 (secondary).
[^b8]: Databricks, "Data + AI Summit 2025 announcements", https://www.databricks.com/kr/events/dataaisummit-2025-announcements, 2025-06; Capital One Software, https://www.capitalone.com/software/blog/databricks-top-features-announced-data-engineers-2025, 2025-06.
[^b9]: Addepto, "Databricks Data + AI Summit 2026 new features explained", https://addepto.com/blog/databricks-data-ai-summit-2026-new-features-explained/, 2026-06 (secondary).
[^b10]: Microsoft Tech Community, "Azure Databricks at Data + AI Summit 2026", https://techcommunity.microsoft.com/blog/azure-databricks/azure-databricks-at-databricks-data--ai-summit-2026-updates-and-new-announcement/4528388, 2026-06.
[^b11]: TechRepublic, "Databricks to Acquire Neon in $1 Billion Deal", https://www.techrepublic.com/article/news-databricks-neon-acquisition/, 2025-05.
[^b12]: Reuters via TradingView, "Databricks to buy Sequoia-backed Tecton in AI agent push", https://tr.tradingview.com/news/reuters.com,2025:newsml_L6N3UE0R1:0-databricks-to-buy-sequoia-backed-tecton-in-ai-agent-push, 2025-08.

---

## C. Snowflake

### Leadership
- **CEO: Sridhar Ramaswamy** since **Feb 2024**, succeeding Frank Slootman.[^c1]
- 2026 changes: Jonathan Beaulier was appointed **CRO** effective 31 Mar 2026, per a weak aggregator summary of an 8-K. Board member **Jeremy Burton** (CEO of Observe) resigned effective 30 Jan 2026 in connection with the Observe deal. Coverage also links **Christian Kleinerman** (EVP Product) stepping down to the Observe transaction, but the snippet was garbled. `[VERIFY: Kleinerman's status and role; CRO appointment, against Snowflake 8-Ks]`[^c2]

### Financials (GAAP total revenue; product revenue as reported)
- **Q2 FY2027** (quarter ended 31 Jul 2026, reported 2 Sep 2026): total revenue **$1.55B (+35% YoY)**, product revenue about **$1.49B (+37%)**, **NRR 126%**, **828** customers above $1M trailing-12-month product revenue (+27%). Non-GAAP product gross margin was **74.7%**, down from 76.4%.[^c3]
- **Guidance:** Q3 FY2027 product revenue **$1.588–1.593B** (+37–38%). **FY2027 product revenue $6.07B (+36%)**, raised from $5.84B. FY2027 non-GAAP operating margin **14.5%**.[^c3]

### Current product names (as of Nov 2026)
- **AI Data Cloud** is still the corporate positioning. `[VERIFY: still the tagline after the Summit 2026 rebrands]`
- **Rebrands at Summit 2026 (1–4 Jun 2026, San Francisco):** **Snowflake Intelligence → "Snowflake CoWork"**, positioned as a personal AI work assistant for knowledge workers and reported GA. **Cortex Code → "Snowflake CoCo"**, for developers. Functionality carried over and existing customers migrated automatically.[^c4][^c5]
- **Cortex AI:** At Summit 2026 Snowflake announced **Cortex AI Function Studio** (public preview), **Cortex Training** (managed GPU fine-tuning of open-weight models), **xAI Grok GA in Cortex** and **Cortex Sense** (grounding layer, private preview). **Cortex Agents** power CoWork. **Cortex AISQL** (generative AI inside SQL) launched in public preview at Summit 2025.[^c4][^c6]
- **Openflow** (ingestion, based on Apache NiFi lineage) was announced at Summit 2025, including a bring-your-own-compute VPC option. It became **GA on AWS, Azure and GCP** at Summit 2026, with a "headless" mode.[^c4][^c6]
- **Snowflake Postgres** is built on the **Crunchy Data** acquisition (announced Jun 2025, about **$250M press-reported, single source**). It reached **GA** at Summit 2026. **Postgres data mirroring** (CDC into Snowflake) was in preview at Summit and is reported GA on AWS and Azure in Oct 2026. `[VERIFY: mirroring GA date]`[^c4][^c6]
- **Compute:** **Adaptive Compute / Adaptive Warehouses** (auto-sizing per query) launched in private preview at Summit 2025. **Gen2 warehouses** came with a vendor claim of 2.1–4.4x faster.[^c6]
- **Iceberg:** Snowflake supports Apache Iceberg tables. **Iceberg v3 became GA on Snowflake on 7 May 2026**, per a secondary source. **Apache Polaris** (the open catalog Snowflake donated) **graduated to an ASF Top-Level Project**: Snowflake and Dremio blogs dated 19 Feb 2026, ASF announcement 5 Mar 2026. Polaris 1.4 shipped in 2026. **Horizon Catalog** remains Snowflake's governance and catalog layer, and secondary sources describe a "Horizon Context" semantic layer under CoWork. `[VERIFY: Horizon naming]`[^c7][^c8][^c5]
- **Snowpark** was not re-verified; it is believed current. **Observability:** Snowflake **acquired Observe, Inc.** (agreement 8 Jan 2026, **closed 2 Feb 2026** per 8-K), adding observability and telemetry. `[VERIFY: deal value]`[^c2]
- **Natoma** (agent / MCP governance): acquisition reported around 28 May 2026 by a weak aggregator. It is referenced in the Investor Day 2026 summary as connecting 100+ business systems with policy controls for agents. `[VERIFY: Snowflake press release]`[^c2][^c9]
- Snowflake's **Investor Day** was held alongside Summit on **2 Jun 2026**. See `data/market_sizes.csv` for TAM figures.[^c9]

[^c1]: BIIA (reposting), "Frank Slootman Steps Down as Snowflake CEO, AI Lead Sridhar Ramaswamy Steps Up", https://www.biia.com/?p=111893, 2024-02.
[^c2]: MarketScreener, "Snowflake Inc. signed a definitive agreement to acquire Observe, Inc.", https://uk.marketscreener.com/news/snowflake-inc-signed-a-definitive-agreement-to-acquire-observe-inc-ce7e59ddde80f021, 2026-01-08; StockTitan (Snowflake 8-K), https://www.stocktitan.net/sec-filings/SNOW/8-k-snowflake-inc-reports-material-event-a0896c05ace0.html, 2026; Autobound executive-changes tracker, https://www.autobound.ai/companies/snowflake/executive-changes, 2026 (weak).
[^c3]: Snowflake via Business Wire, "Snowflake Reports Financial Results for the Second Quarter of Fiscal 2027", https://secure.businesswire.com/news/home/20260902386235/en/Snowflake-Reports-Financial-Results-for-the-Second-Quarter-of-Fiscal-2027, 2026-09-02.
[^c4]: Flexera, "Snowflake Summit 2026 recap: rebrands, acquisition and 25+ announcements", https://www.flexera.com/blog/perspectives/snowflake-summit-2026/, 2026-06; SELECT, https://select.dev/posts/snowflake-summit-2026-product-announcement-recap, 2026-06.
[^c5]: IT Brief Australia, "Snowflake renames AI tools amid broader platform push", https://itbrief.com.au/story/snowflake-renames-ai-tools-amid-broader-platform-push, 2026-06; Atlan, https://atlan.com/know/snowflake/snowflake-cowork/, 2026.
[^c6]: Constellation Research, "Snowflake Summit 2025: Everything you need to know", https://www.constellationr.com/insights/news/snowflake-summit-2025-everything-you-need-know, 2025-06; BigDATAwire, https://www.bigdatawire.com/2025/06/03/snowflake-widens-analytics-and-ai-reach-at-summit-25, 2025-06-03.
[^c7]: Apache Polaris blog, "Apache Polaris graduates to top-level project", https://polaris.apache.org/blog/2026/02/19/apache-polaris-graduates-to-top-level-project/, 2026-02-19; ASF, https://news.apache.org/foundation/entry/the-apache-software-foundation-graduates-two-open-source-projects-from-incubator, 2026-03-05.
[^c8]: Atlan, "Apache Iceberg v3: What Snowflake Data Teams Need to Know", https://atlan.com/know/snowflake/apache-iceberg-v3/, 2026 (secondary).
[^c9]: Platform Aeronaut transcript summary, "Summit and welcome to Investor Day 2026-06-02 SNOW", https://transcripts.platformaeronaut.com/summaries/summit-and-welcome-to-investor-day-2026-06-02-SNOW, 2026-06-02 (AI-generated summary; weak).

---

## D. Hyperscalers and Oracle (current names)

### AWS
- **re:Invent 2025** (30 Nov–4 Dec 2025): **Amazon S3 Vectors went GA**, with up to 2B vectors per index, about 100 ms queries and an AWS claim of up to 90% lower cost than alternatives. **S3 Tables** (managed Iceberg tables) added an Intelligent-Tiering storage class and cross-Region / cross-account replication. Maximum S3 object size rose to **50 TB**. **Iceberg v3** support (incl. deletion vectors) arrived across EMR, Glue, SageMaker notebooks and S3 Tables. A new **Database Savings Plans** offering was also announced.[^d1][^d2][^d3]
- **Amazon SageMaker Unified Studio**: the "next generation of SageMaker" unifies analytics and AI. Onboarding was simplified so it can be reached from the SageMaker, Athena, Redshift and S3 Tables consoles. **SageMaker Catalog** can export asset metadata as Iceberg tables via S3 Tables.[^d3]
- **Redshift, Glue, Aurora DSQL, Bedrock Knowledge Bases**: these names are believed current. Aurora DSQL is distributed serverless SQL and reached GA in May 2025. `[VERIFY: Aurora DSQL GA date and Bedrock Knowledge Bases naming as of 2026]`

### Google Cloud
- **Agentspace was renamed Gemini Enterprise** (9 Oct 2025). The Agentspace name is retired.[^d4]
- **Dataplex Universal Catalog is now "Knowledge Catalog"**, per Google's own docs; a third party dates the rename to about 10 Apr 2026. APIs (`dataplex.googleapis.com`) and gcloud commands are unchanged.[^d5]
- **Next '26** (Las Vegas, Apr 2026; 260+ announcements): real-time replication from **Spanner, AlloyDB and Cloud SQL into BigQuery** is GA, with replication to Iceberg tables in preview. **Cross-Cloud Lakehouse** lets BigQuery run on data in AWS or Azure without migration. **BigQuery Graph** (preview). A **remote MCP server** and ADK toolset for BigQuery are GA, plus a Data Agent Kit (preview). Also announced: the "Gemini Enterprise Agent Platform" and 8th-gen TPUs. Some reports say Vertex AI was renamed to the Agent Platform. `[VERIFY: Vertex AI rename]`[^d6][^d7]
- **BigLake** is believed current as the Iceberg/lakehouse storage-engine brand. `[VERIFY]`

### Microsoft
- **Ignite 2025** (Nov 2025): **Fabric IQ**, a semantic intelligence layer, entered preview, alongside Work IQ and Foundry IQ. **Fabric Databases** (SQL database and Cosmos DB in Fabric) went **GA**. **OneLake** is positioned as the system of record, with shortcuts extended to Azure Blob Storage. **Azure HorizonDB** is a new scale-out PostgreSQL-compatible managed service in **preview**; Microsoft claims up to 3x throughput versus open-source Postgres.[^d8][^d9]
- Ignite 2026 is mid-November 2026, after this briefing date. Re-check then.

### Oracle
- **Oracle AI World** (Las Vegas, 14 Oct 2025): **Oracle AI Database 26ai** became the flagship, with AI built into the database. **Autonomous AI Lakehouse**, Exadata Database Service on Exascale and Base Database Service were declared GA.[^d10]
- **Multicloud:** **Oracle Database@Azure** was in 28 regions. **Oracle Database@Google Cloud** was in 8 regions with 9 more planned. **Oracle Database@AWS** has a reported expansion plan but no official region count was captured. Azure partners can resell via Microsoft Marketplace private offers.[^d10][^d11]

[^d1]: AWS News Blog, "Top announcements of AWS re:Invent 2025", https://aws.amazon.com/blogs/aws/top-announcements-of-aws-reinvent-2025, 2025-12.
[^d2]: Blocks & Files, "AWS piles on S3 upgrades from vector search to 50 TB objects", https://www.blocksandfiles.com/ai-ml/2025/12/03/aws-piles-on-s3-upgrades-from-vector-search-to-50-tb-objects/1704690, 2025-12-03; @IT (ITmedia), https://atmarkit.itmedia.co.jp/ait/articles/2512/17/news056.html, 2025-12-17.
[^d3]: AWS Big Data Blog, "AWS analytics at re:Invent 2025", https://aws.amazon.com/blogs/big-data/aws-analytics-at-reinvent-2025-unifying-data-ai-and-governance-at-scale, 2025-12.
[^d4]: Atlan, "Gemini Enterprise (Formerly Agentspace)", https://atlan.com/know/ai-agent/ai-agent-applications/google-agentspace/, 2026 (secondary).
[^d5]: Google Cloud docs, "Dataplex / Knowledge Catalog overview", https://docs.cloud.google.com/dataplex/docs/overview, accessed 2026-11-01; Atlan, https://atlan.com/know/ai-agent/gcp/google-knowledge-catalog/, 2026.
[^d6]: G-gen (Google Cloud partner), "Next '26 What's new in BigQuery", https://blog.g-gen.co.jp/entry/next-26-whats-new-in-bigquery, 2026-04 (Japanese).
[^d7]: VPSRanking, "Google Cloud Next '26 Recap: 260 Announcements…", https://vpsranking.com/news/cloud/cloud-2026-04-25-google-cloud-next-26-recap/, 2026-04-25 (weak).
[^d8]: Microsoft Azure blog, "Azure at Microsoft Ignite 2025: all the intelligent cloud news explained", https://azure.microsoft.com/en-us/blog/azure-at-microsoft-ignite-2025-all-the-intelligent-cloud-news-explained/, 2025-11.
[^d9]: Redmond Magazine, "Big Data Platform Changes Emerge at Ignite…", https://redmondmag.com/articles/2025/11/18/big-data-platform-changes-emerge-at-ignite-as-microsoft-broadens-its-azure-focus.aspx, 2025-11-18.
[^d10]: Oracle press release, "Oracle Database@Google Cloud adds new Oracle AI Database services…", https://www.oracle.com/news/announcement/ai-world-oracle-database-at-google-cloud-adds-new-oracle-ai-database-services-2025-10-14/, 2025-10-14.
[^d11]: Oracle press release, "Oracle Database@Azure powers cloud migrations…", https://www.oracle.com/news/announcement/ai-world-oracle-database-at-azure-powers-cloud-migrations-for-organizations-across-the-world-2025-10-14/, 2025-10-14.

---

## E. Key 2025–2026 industry events (one line each)

| Event | Status as of 2026-11-01 | Source |
|---|---|---|
| IBM–Confluent | **Closed 17 Mar 2026**; about **$11B**, $31/share cash. Announced 8 Dec 2025; Confluent delisted 16 Mar 2026 | [^e1] |
| Salesforce–Informatica | **Closed Nov 2025** (reported 18 Nov 2025); about **$8B** equity value, $25/share cash. Announced May 2025 | [^e2] |
| Fivetran–dbt Labs | All-stock merger announced Oct 2025, **closed 1 Jun 2026**. George Fraser CEO, Tristan Handy President. Combined ARR "approaching $600M" (company-stated). Final brand TBD | [^e3] |
| Databricks–Neon | Announced May 2025, about **$1B** (press-reported). Shipped as **Lakebase** (GA 2026; >$100M run-rate) | [^b11][^b1] |
| Snowflake–Crunchy Data | Announced Jun 2025, about **$250M** (press-reported, single source). Basis of **Snowflake Postgres** (GA Jun 2026) | [^c6][^c4] |
| Meta–Scale AI | Jun 2025: **$14.3B for 49%, non-voting**; values Scale at about $29B. Alexandr Wang joined Meta's superintelligence effort; Jason Droege became interim CEO | [^e4] |
| CoreWeave–Weights & Biases | **Closed 5 May 2025**. About **$1.7B** (press-reported via The Information; not company-disclosed) | [^e5] |
| Databricks–Tecton | Announced Aug 2025, terms undisclosed. Close reported 22 Aug 2025 `[VERIFY]` | [^b12] |
| SAP–Dremio (new) | Announced **4 May 2026** (with Prior Labs), closed about **Jul 2026**, terms undisclosed. Folded into SAP Business Data Cloud | [^a18] |
| Snowflake–Observe (new) | Agreement 8 Jan 2026, **closed 2 Feb 2026** | [^c2] |
| Supabase–Turso (new) | Announced with a $150M GIC-led raise on 2 Oct 2026 | [^e7] |
| Apache Iceberg v3 spec | v3 features: deletion vectors (Puffin / Roaring bitmaps), row lineage, variant, geo types, ns timestamps, default values. Iceberg **1.10.0 released 11 Sep 2025**; 1.11.0 May 2026. Engine support: AWS (Dec 2025), Snowflake GA (May 2026). V4 spec discussion has begun `[VERIFY: exact spec-ratification date]` | [^e8][^d3][^c8] |
| Apache Polaris | **Graduated to ASF TLP**: vote Feb 2026, ASF announcement 5 Mar 2026 | [^c7] |
| Unity Catalog OSS | Open-sourced Jun 2024 under LF AI & Data; still active. OpenSharing moved to the Linux Foundation (2026) `[VERIFY: LF maturity stage]` | [^b5] |
| DuckLake | **v1.0 released 13 Apr 2026** (production-ready). It stores lake metadata in a SQL database. Supported in DuckDB 1.5.2 | [^e9] |
| MCP adoption | Anthropic **donated MCP to the Agentic AI Foundation** (Linux Foundation directed fund) on **9 Dec 2025**, co-founded with Block and OpenAI and supported by Google, Microsoft, AWS and others. Data vendors ship MCP servers, e.g., a BigQuery remote MCP server (GA, Next '26) and Snowflake's Natoma deal for agent/MCP governance `[VERIFY: Snowflake/Databricks managed MCP server GA status]` | [^e10][^d6] |
| Lance format | Open lakehouse format (file + table + catalog spec) for multimodal AI data, from LanceDB. LanceDB's last confirmed round is a **$30M Series A (Jun 2025, Theory Ventures)**; no 2026 round found | [^e11] |
| OpenAI–Rockset | Acquisition announced **Jun 2024**; Rockset's tech went into OpenAI retrieval infrastructure and its public service was wound down. Not re-verified in this sweep `[VERIFY]` | — |
| Supabase valuation | **$500M Series F at $10.5B post-money** (Jun 2026, GIC-led; Salesforce Ventures new). Previously $5B (Series E, Oct 2025). A further **$150M (2 Oct 2026)** came with the Turso deal; the reported $10.65B valuation is unconfirmed | [^e7] |
| Neon valuation | Now part of Databricks (about $1B deal). No standalone valuation | [^b11] |
| Postgres-for-agents trend | Databricks Lakebase (>$100M run-rate), Snowflake Postgres (GA), Azure HorizonDB (preview), Supabase at $10.5B, Supabase–Turso. Agents spinning up ephemeral databases is the shared growth story `[VERIFY: any vendor-stated "% of DBs created by agents" figure before quoting]` | [^b1][^c4][^d8][^e7] |
| ClickHouse latest round | **$400M Series D at $15B** (Dragoneer-led), reported 16 Jan 2026 (Bloomberg). No later primary round found; secondary-market marks of $20B+ are estimates only | [^e6] |
| Pinecone CEO change | **8 Sep 2025**: **Ash Ashutosh** (ex-Google, ex-Actifio founder) became CEO; founder **Edo Liberty** moved to Chief Scientist | [^e12] |

[^e1]: ChannelWeb UK, "IBM completes $11bn Confluent acquisition", https://www.channelweb.co.uk/news-network/2026/ibm-completes-11bn-confluent-acquisition, 2026-03; StockTitan (IBM release), https://www.stocktitan.net/news/IBM/ibm-completes-acquisition-of-confluent-making-real-time-data-the-lbuwdbharsqe.html, 2026-03-17.
[^e2]: Seeking Alpha, "Salesforce completes acquisition of Informatica", https://seekingalpha.com/news/4523363-salesforce-completes-acquisition-of-informatica, 2025-11-18; Bloomberg Law, https://news.bloomberglaw.com/tech-and-telecom-law/salesforce-agrees-to-buy-informatica-in-deal-worth-8-billion, 2025-05.
[^e3]: Fivetran press release, "Fivetran & dbt Labs Complete Merger…", https://www.fivetran.com/press/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents, 2026-06-01; TechTarget, https://www.techtarget.com/data-technologies/news/366643590/Fivetran-DBT-Labs-complete-merger-to-form-data-layer-for-AI, 2026-06.
[^e4]: TechCrunch, "Scale AI confirms 'significant' investment from Meta, says CEO Alexandr Wang is leaving", https://techcrunch.com/2025/06/13/scale-ai-confirms-significant-investment-from-meta-says-ceo-alexandr-wang-is-leaving/, 2025-06-13; CNBC via NBC, https://www.nbcchicago.com/news/business/money-report/scale-ais-alexandr-wang-confirms-departure-for-meta-as-part-of-14-3-billion-deal/3767336/, 2025-06.
[^e5]: CoreWeave IR, "CoreWeave Completes Acquisition of Weights & Biases", https://investors.coreweave.com/news/news-details/2025/CoreWeave-Completes-Acquisition-of-Weights--Biases/default.aspx, 2025-05-05; Maginative, https://www.maginative.com/article/coreweave-acquires-weights-biases-in-a-1-7-billion-ai-cloud-play/, 2025-03.
[^e6]: Bloomberg, "ClickHouse Lands $15 Billion Valuation in AI Database Race", https://bloomberg.com/news/articles/2026-01-16/clickhouse-lands-15-billion-valuation-in-ai-database-race, 2026-01-16.
[^e7]: Orrick, "Supabase Raises $500 Million at $10.5 Billion Valuation…", https://www.orrick.com/en/News/2026/06/Supabase-Raises-500-Million-at-10-5-Billion-Valuation-to-Accelerate-Lead-in-Agentic-Infrastructure, 2026-06; IT Brief Australia, https://itbrief.com.au/story/supabase-raises-usd-500-million-in-series-f-round, 2026-06; NBR, https://www.nbr.co.nz/tech/supabase-raises-another-us150m/, 2026-10.
[^e8]: Apache Iceberg dev-list digest (A. Merced), https://amdatalakehouse.substack.com/p/apache-iceberg-dev-list-digest-sept, 2025-09; Databricks blog, "Iceberg v3: moving the ecosystem towards unification", https://www.databricks.com/en/blog/iceberg-v3-moving-ecosystem-towards-unification, 2025-06; AWS S3 docs, https://docs.aws.amazon.com/AmazonS3/latest/userguide/working-with-apache-iceberg-v3.md, n.d.
[^e9]: DuckDB blog, "DuckLake 1.0", https://duckdb.org/2026/04/13/ducklake-10.html, 2026-04-13.
[^e10]: Anthropic, "Donating the Model Context Protocol and establishing the Agentic AI Foundation", https://anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation, 2025-12-09.
[^e11]: LanceDB docs, "Lance", https://docs.lancedb.com/lance, n.d.; CB Insights, https://www.cbinsights.com/company/lancedb/financials, n.d. (aggregator).
[^e12]: Pinecone blog, "Moving Pinecone forward with Ash Ashutosh as CEO…", https://pinecone.io/blog/growing-ai-ambitions, 2025-09-08; VentureBeat, https://venturebeat.com/data-management/pinecone-founder-edo-liberty-steps-aside-as-ceo-and-appoints-googler-ash, 2025-09.

---

## F. Regulation

### EU AI Act
- **Baseline timeline** (pre-2025 knowledge, unchanged): entry into force 1 Aug 2024; prohibited practices and AI-literacy duties from 2 Feb 2025; **GPAI model obligations from 2 Aug 2025**, with the GPAI Code of Practice published Jul 2025. `[VERIFY: not re-checked live this sweep]`
- **Digital Omnibus on AI is now law.** Political agreement came **7 May 2026**; Parliament voted 16 Jun 2026 and the Council adopted on 29 Jun 2026. It was published in the OJ on **24 Jul 2026** as **Regulation (EU) 2026/1744** and entered into force on **27 Jul 2026**.[^f1][^f2][^f3]
  - **Standalone (Annex III) high-risk** obligations moved from 2 Aug 2026 to **2 Dec 2027**.
  - **Product-embedded (Annex I) high-risk** obligations moved from 2 Aug 2027 to **2 Aug 2028**.
  - **Watermarking / AI-generated-content** transparency was delayed to **2 Dec 2026**. The registration obligation was reinstated.[^f2][^f3]

### GDPR
- The **Digital Omnibus (data/GDPR/ePrivacy part)** was proposed on **19 Nov 2025** (procedure 2025/0360(COD)) and is **not enacted**. Proposed changes include a narrower test for what counts as personal data, AI-processing provisions, cookie-rule changes and a longer breach-notification window.[^f4][^f5]
  - The **EDPB–EDPS Joint Opinion 2/2026** was adopted on 10 Feb 2026.
  - Parliament committees (ITRE / LIBE / IMCO) are still working on it.
  - A Council compromise text was dated 2 Oct 2026, with a possible negotiating mandate around 11 Oct 2026. `[VERIFY: Council mandate outcome]`[^f4][^f5]

### CCPA / CPRA (California)
- The CPPA's regulations on **automated decision-making technology (ADMT), risk assessments and cybersecurity audits** were approved by OAL (announced **23 Sep 2025**) and took effect on **1 Jan 2026**.[^f6][^f7]
  - Risk assessments are required from 1 Jan 2026, with attestations and summaries due **1 Apr 2028**.
  - **ADMT compliance starts 1 Jan 2027.**
  - Cybersecurity audits phase in by revenue; the first submissions are due 1 Apr 2028 for businesses with more than $100M revenue.[^f6][^f7]

### EU Data Act
- Most obligations have applied since **12 Sep 2025**: B2B/B2C access to connected-product data, cloud-switching rights and limits on unfair data-sharing terms. Cloud **switching charges must reach zero by 12 Jan 2027**. `[VERIFY: not re-checked live this sweep; pre-2025 knowledge]`

### Data sovereignty trends (directional; cite specifics in chapters)
- Hyperscalers and database vendors keep pushing in-region / multicloud deployment. Examples: Oracle Database@Azure in 28 regions and Database@Google Cloud expanding to 17 planned. Sovereign-cloud offerings and the EU Data Act's switching rules lower lock-in. Everpure pitches its Data Stream controls as keeping data within enterprise boundaries.[^d11][^d10][^a13] `[VERIFY: AWS European Sovereign Cloud launch status; Microsoft/Google EU sovereign-cloud offerings, if cited]`

[^f1]: Council of the EU, "Artificial intelligence: Council and Parliament agree to simplify and streamline rules", https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/, 2026-05-07.
[^f2]: Future of Privacy Forum, "The AI Act implementation timeline: What changes under the AI Omnibus?", https://fpf.org/blog/the-ai-act-implementation-timeline-what-changes-under-the-ai-omnibus/, 2026.
[^f3]: White & Case, "EU agrees Digital Omnibus deal to simplify AI rules", https://www.whitecase.com/insight-alert/eu-agrees-digital-omnibus-deal-simplify-ai-rules, 2026-05; Usercentrics, https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/, 2026 (dates for OJ publication/entry into force).
[^f4]: MediaLaws, "Digital Omnibus legislative tracker", https://www.medialaws.eu/digital-omnibus-legislative-tracker/, 2026; Council document ST-10729-2026-INIT, https://data.consilium.europa.eu/doc/document/ST-10729-2026-INIT/en/pdf, 2026-10.
[^f5]: Clifford Chance, "EU Digital Omnibus" client briefing, https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2025/11/eu-digital-omnibus-clifford-chance-client-briefing-nov-2025.pdf, 2025-11.
[^f6]: California Privacy Protection Agency, "California Finalizes Regulations to Strengthen Consumers' Privacy", https://www.cppa.ca.gov/announcements/2025/20250923.html, 2025-09-23.
[^f7]: Skadden, "California Finalizes CPPA Regulations", https://www.skadden.com/insights/publications/2025/10/california-finalizes-cppa-regulations, 2025-10.

---

## Open items (to verify before publication)
1. Everpure FY2027 guidance; exact FY2026 revenue (">$3.6B" vs "~$3.7B"); whether any Databricks or Snowflake partnership exists.
2. Databricks CEO confirmation; Neon and Tecton close dates; Mosaic AI / UniForm naming.
3. Snowflake: Kleinerman and CRO changes; Observe and Natoma deal values and Natoma confirmation; Postgres mirroring GA date.
4. AWS Aurora DSQL GA date; Bedrock Knowledge Bases naming; Google Vertex AI rename and BigLake status.
5. Iceberg v3 spec-ratification date; Unity Catalog OSS LF stage; OpenAI–Rockset details.
6. EU Data Act and AI Act baseline dates (pre-2025 knowledge); Council GDPR-omnibus mandate outcome.
7. Market sizes for data integration, data management software, BI, data governance, data labeling and DSPM. No verified public figure was obtained this sweep (see `data/market_sizes.csv` notes).

> **Integrator note (from Ch 7 drafter, 2026-11-01):** Apache Polaris latest release 1.8.0 (2026-09-28); Apache Iceberg 1.12.0 released 2026-09-29; Iceberg spec: v1–v3 adopted, v4 not yet adopted; Iceberg Java library default table format version remains 2. Polaris graduation date: sources give 2026-02-15 (Incubator page), 2026-02-19 (blogs), 2026-03-05 (ASF announcement) — use "early 2026 (ASF announced 2026-03-05)".

> **Integrator notes from Part 2 / Ch 25 drafters (2026-11-01):** (1) **Everpure–Databricks:** Everpure was a launch partner of the *Databricks Storage Ecosystem* (announced 2026-06-10), with an OpenSharing connector in private preview — this supersedes "no formal partnership found" in section A. (2) Databricks renamed "Lakeflow Declarative Pipelines" (formerly Delta Live Tables) to **"Lakeflow Spark Declarative Pipelines"** in Nov 2025. (3) **Open Semantic Interchange (OSI):** Databricks joined in Jan 2026 — do not describe OSI as Snowflake-only. (4) **Fivetran–dbt:** closing release says combined ARR "approaching $600M". (5) New deals: Prefect–Dagster (announced 2026-07-13); FICO acquired GX Cloud (2026-05-06) and Fivetran took stewardship of GX Core (2026-05-13); Boomi–Elementary (2026-10-19, ~$40–45M press-reported).

> **Integrator note (Ch 16, 2026-11-01):** Google renamed **Vertex AI → "Gemini Enterprise Agent Platform"** in April 2026 (HPCwire 2026-04-23; Virtualization Review). FineWeb dataset card now states **>18.5T tokens** (not 15T). Meta–Scale AI 49% investment confirmed by TechCrunch 2025-06-13.

> **Integrator notes (Part 3, 2026-11-01):** (1) **AWS–DuckLabs:** Amazon signed a definitive agreement (~2026-08-25/26; aboutamazon.com/news/company-news/aws-ducklabs) to acquire DuckLabs (DuckDB Labs, Amsterdam); terms undisclosed; DuckDB/DuckLake remain MIT under the DuckDB Foundation. (2) ClickHouse stated >$250M ARR (company-stated, 2026-05-27). (3) Databricks docs now call Vector Search **"AI Search"** (rename date [VERIFY]). (4) Elastic acquired Jina AI ($43.4M per 10-Q). (5) A 2022 Pure Storage–Snowflake on-prem joint solution exists; no current FlashBlade certification found for Snowflake.

> **Integrator notes (Part 3 cont., 2026-11-01):** (1) **Lakebase GA:** Feb 2026 on AWS, Mar 2026 on Azure (Databricks blog; Azure Updates) — earlier than "GA at DAIS 2026". (2) Tecton's "$900M" figure is its 2022 valuation, not the Databricks deal price. (3) Neptune–OpenAI: "<$400M in stock" per The Information (press-reported). (4) Nscale–Anyscale deal staged. (5) SQL Server 2025: VECTOR type GA; DiskANN index still preview on-premises. (6) Milvus 2.6 coverage names Pure Storage as a tiered-storage partner (useful for Ch 32/45).

> **Integrator note (2026-11-01):** Salesforce renamed **Data Cloud → Data 360** at Dreamforce 2025 (effective ~2025-10-14) under the Agentforce 360 umbrella (Salesforce product page; salesforceben.com; Tableau help). **Search constraint:** the subagent web-search pool is exhausted as of Part 4; later drafters must rely on these research files and `data/*.csv`.
