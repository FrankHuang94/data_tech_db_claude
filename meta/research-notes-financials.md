# Research notes: financials

## Public comps & financials sources

Sweep date 2026-11-01. **Method caveat:** in this session, WebFetch could not reach primary hosts (businesswire.com, nasdaq.com, snowflake.com, investors.snowflake.com, sec.gov all failed DNS or proxy checks), and the shared web-search budget ran out partway through. So the figures below come from search-result excerpts of the sources listed, not from full-document reads. Before publishing, re-check every number against the filing. Rows in `data/company_financials.csv` whose source is an EDGAR company-index URL with as_of 2026-11-01 (Snowflake FY2020–FY2024, MongoDB FY2021–FY2025 revenue, Everpure FY2024–FY2025 revenue) are historical 10-K figures carried from analyst records. They were **not** re-read this sweep. [VERIFY]

All sources retrieved 2026-11-01.

| Publisher | Title | URL | Published |
|---|---|---|---|
| Snowflake (via Nasdaq/Business Wire) | Snowflake Reports Financial Results for the Second Quarter of Fiscal 2027 | https://www.nasdaq.com/press-release/snowflake-reports-financial-results-second-quarter-fiscal-2027-2026-09-02 | 2026-09-02 |
| Snowflake (Business Wire) | Snowflake Reports Financial Results for the First Quarter of Fiscal 2027 | https://www.businesswire.com/news/home/20260527027931/en/Snowflake-Reports-Financial-Results-for-the-First-Quarter-of-Fiscal-2027 | 2026-05-27 |
| Snowflake / SEC | Form 8-K Ex. 99.1, Q4 and FY2026 results | https://www.sec.gov/Archives/edgar/data/1640147/000162828026011631/fy2026q4earnings.htm | 2026-02-25 |
| Snowflake / SEC | Form 10-K, FY2026 (fiscal year ended 2026-01-31) | https://www.sec.gov/Archives/edgar/data/1640147/000164014726000008/snow-20260131.htm | 2026 [VERIFY filing date] |
| Snowflake / SEC | Form 8-K Ex. 99.1, Q4 and FY2025 results | https://www.sec.gov/Archives/edgar/data/1640147/000164014725000016/fy2025q4earnings.htm | 2025-02-26 |
| Snowflake / SEC | Form 10-K, FY2025 | https://www.sec.gov/Archives/edgar/data/1640147/000164014725000052/snow-20250131.htm | 2025 [VERIFY filing date] |
| Pulse 2.0 | Snowflake: Q2 Fiscal 2027 Revenue Rises 35% To $1.55 Billion As Product Revenue Guidance Is Raised | https://pulse2.com/snowflake-q2-fiscal-2027-revenue-rises-35-to-1-55-billion-as-product-revenue-guidance-is-raised/ | 2026-09 |
| MongoDB IR | MongoDB, Inc. Announces Second Quarter Fiscal 2027 Financial Results | https://investors.mongodb.com/news-releases/news-release-details/mongodb-inc-announces-second-quarter-fiscal-2027-financial | 2026-09-01 |
| MongoDB / SEC | Form 8-K Ex. 99.1, Q4 FY2026 results | https://www.sec.gov/Archives/edgar/data/1441816/000162828026013199/mdb-13126xex991xrelease.htm | 2026-03-02 |
| MongoDB / SEC | Annual Report to Shareholders (ARS), FY2026 | https://www.sec.gov/Archives/edgar/data/0001441816/000162828026036431/ars.htm | 2026 [VERIFY] |
| The Motley Fool | MongoDB (MDB) Q4 2026 Earnings Call Transcript | https://www.fool.com/earnings/call-transcripts/2026/03/02/mongodb-mdb-q4-2026-earnings-call-transcript/ | 2026-03-02 |
| Everpure IR | Everpure Announces Second Quarter Fiscal 2027 Financial Results | https://investor.everpuredata.com/news-and-events/press-releases/press-release-details/2026/Everpure-Announces-Second-Quarter-Fiscal-2027-Financial-Results/default.aspx | 2026-08-26 |
| Everpure / SEC | Form 8-K Ex. 99.1, Q4 and FY2026 results | https://www.sec.gov/Archives/edgar/data/1474432/000147443226000015/pstg-ex991q4fy2026.htm | 2026-02-25 |
| StockAnalysis.com | Statistics / market-cap / ratios / revenue pages for SNOW, MDB, DDOG, ESTC, ORCL, PLTR, CRM, NOW, TDC, MSFT, AMZN, GOOGL, P | https://stockanalysis.com/stocks/{ticker}/statistics/ (and /market-cap/, /financials/ratios/, /revenue/) | snapshots 2026-10-01 to 2026-10-30 |
| CompaniesMarketCap | Snowflake (SNOW) market capitalization | https://companiesmarketcap.com/snowflake/marketcap/ | 2026-10-28 snapshot |

### Notable findings

- **Snowflake is speeding up.** Q2 FY2027 (May–Jul 2026) product revenue grew 37% YoY to about $1.49B, up from 34% in Q1, 30% in Q4 FY2026 and 29% for full-year FY2026. FY2027 product guidance was raised twice: $5.66B (Feb 2026), then $5.84B (May), then $6.07B (Sep). NRR is steady at 126%. Customers with >$1M TTM product revenue: 828 (+27%). The non-GAAP product gross-margin guide was cut to 74% on lower-margin AI workload mix. Q2 RPO was about $9.0B, below Q1's $9.21B. The prior quarter-end RPO peak ($9.77B) included the largest deal in company history, and Q1 coverage cited a $6B AWS commitment [VERIFY]. Press said shares rose about 22% after the print.
- **Snowflake valuation.** About $108B market cap on 2026-10-30 per stockanalysis. companiesmarketcap showed about $120B on 2026-10-28, so the two sources disagree. EV / FY2027 guidance-derived revenue is about 17x.
- **MongoDB.** Q2 FY2027 revenue was $771.8M (+30%), with Atlas +29%. FY2027 revenue guidance was raised to $2.99–3.03B. Atlas was 73% of FY2026 revenue (70% in FY2025). Customers were 65,200+ at FY2026 year-end.
- **Pure Storage renamed Everpure** (February 2026). StockAnalysis and press releases show it trading as **NYSE: P** [VERIFY ticker-change date]. Q2 FY2027 revenue was about $1.19B (+38%), with product revenue +54%. FY2027 revenue guidance jumped to $5.03–5.07B from $4.41–4.51B. Subscription ARR is $2.1B (+20%) and RPO is $4.1B (+44%). Q2 free cash flow was −$238M.
- **Oracle.** Market cap is about $382–398B at roughly $131/share, against EV of about $515–530B. TTM free cash flow is about −$28.7B because capex (about $75.7B) exceeds operating cash flow. The balance sheet is now an AI-infrastructure leverage story.
- **De-rating of application software.** Salesforce market cap fell about 21% YoY to about $189B. ServiceNow is about $142B. Alphabet fell more than 12% after its 2026-10-28 report (press-reported).
- **Confluent.** IBM agreed to acquire it (announced Dec 2025, about $31/share cash). Closing and delisting status was not verified this sweep. [VERIFY]

### Gaps (not retrieved; search budget exhausted)

- Market and fundamental data for SAP, Workday, IBM, Varonis, Domo, NetApp, Nutanix, Dynatrace, Rubrik, Commvault, GitLab, C3.ai and Confluent. The rows exist but are blank and marked [VERIFY].
- Consensus NTM revenue for all names. Rows use FY-guidance-derived figures or TTM proxies.
- Databricks run-rate disclosures, Confluent annual 2021–2025, Oracle OCI revenue and RPO, Elastic, Datadog annual revenue, Teradata total and cloud ARR, Palantir US commercial growth.
- Snowflake quarterly GAAP total gross margin, quarterly SBC, and Q3 FY2026 KPIs. MongoDB NRR and Q1 FY2027 detail.

## Comps gap-fill (2026-11-01)

Method: WebSearch excerpts only (WebFetch/HTTP blocked). Market cap/EV from stockanalysis.com snapshots (dates in `as_of`; undated snapshots use the retrieval date and are flagged in notes). Revenue, growth and guidance from company releases as quoted in search excerpts. Re-check against filings before publication. [VERIFY] All sources retrieved 2026-11-01.

| Publisher | Title | URL | Published |
|---|---|---|---|
| SAP / SEC | Form 6-K Ex. 99.1, Q3 2026 quarterly statement | https://www.sec.gov/Archives/edgar/data/0001000184/000110465926118617/tm2628113d1_ex99-1.htm | 2026-10-21 |
| Workday IR | Workday Announces Fiscal 2027 Second Quarter Financial Results | https://investor.workday.com/news-and-events/press-releases/news-details/2026/Workday-Announces-Fiscal-2027-Second-Quarter-Financial-Results/default.aspx | 2026-08-27 |
| IBM / SEC | Form 8-K Ex. 99.1, Q3 2026 results | https://www.sec.gov/Archives/edgar/data/0000051143/000005114326000093/ibm-20261021xex991.htm | 2026-10-21 |
| IBM / SEC | Form 10-Q, Q1 2026 (Confluent close 2026-03-17) | https://www.sec.gov/Archives/edgar/data/0000051143/000005114326000038/ibm-20260331.htm | 2026 |
| Confluent / SEC | Form 10-K, FY2025 | https://www.sec.gov/Archives/edgar/data/1699838/000169983826000006/cflt-20251231.htm | 2026 |
| Varonis IR | Varonis Announces Second Quarter 2026 Financial Results | https://s203.q4cdn.com/582009126/files/doc_news/Varonis-Announces-Second-Quarter-2026-Financial-Results-2026.pdf | 2026-07-28 |
| SiliconANGLE | Proofpoint agrees to buy data security company Varonis for $6.3B in cash | https://siliconangle.com/2026/10/15/proofpoint-agrees-to-buy-data-security-company-varonis-for-6-3b-in-cash/ | 2026-10-15 |
| Constellation Research | Progress Software buys Domo's AI and data platform business for $400 million | https://www.constellationr.com/insights/news/progress-software-buys-domos-ai-and-data-platform-business-400-million | 2026-07 |
| Domo (Business Wire) | Domo Announces Timing for Second Quarter Fiscal 2027 Financial Results and Provides Transaction Timing Update | https://secure.businesswire.com/news/home/20260831807380/en/Domo-Announces-Timing-for-Second-Quarter-Fiscal-2027-Financial-Results-and-Provides-Transaction-Timing-Update | 2026-08-31 |
| Benzinga | Domo earnings forecasts (FY2027 guidance summary) | https://www.benzinga.com/quote/DOMO/earnings-forecasts | 2026 |
| NetApp | NetApp Reports First Quarter of Fiscal Year 2027 Results | https://netapp.com/newsroom/press-releases/news-rel-20260902-results-607632 | 2026-09-02 |
| Nutanix / SEC | Form 8-K Ex. 99.1, Q4 and FY2026 results | https://www.sec.gov/Archives/edgar/data/0001618732/000117184326005752/exh_991.htm | 2026-08-26 |
| Dynatrace IR | Q1 FY2027 earnings release (Ex. 99) | https://ir.dynatrace.com/sec-filings/all-sec-filings/content/0001773383-26-000049/q1fy27-earningsreleaseex99.htm | 2026-08-05 |
| Rubrik | Rubrik Reports Second Quarter Fiscal Year 2027 Financial Results | https://www.rubrik.com/company/newsroom/press-releases/26/rubrik-reports-second-quarter-fiscal-year-2027-financial-results | 2026-08 |
| Commvault (via Finviz/PR Newswire) | Commvault Announces Second Quarter Fiscal 2027 Financial Results | https://finviz.com/news/408629/commvault-announces-second-quarter-fiscal-2027-financial-results | 2026-10-27 |
| StorageNewsletter | Commvault fiscal 2Q27 results (total revenue ~$312M) | https://www.storagenewsletter.com/?p=306407 | 2026-10 |
| GitLab (Business Wire) | GitLab Reports Second Quarter Fiscal Year 2027 Financial Results | https://secure.businesswire.com/news/home/20260901768402/en/GitLab-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results | 2026-09-01 |
| C3.ai | C3 AI Announces Fiscal First Quarter 2027 Results | https://c3.ai/news/c3-ai-announces-fiscal-first-quarter-2027-results | 2026-09-02 |
| Datadog / SEC | Form 8-K Ex. 99.1, Q2 2026 results | https://www.sec.gov/Archives/edgar/data/0001561550/000162828026053829/ex-991x20260630x8k.htm | 2026-08-06 |
| Elastic (via 01net) | Elastic Reports First Quarter Fiscal 2027 Financial Results | https://www.01net.it/elastic-reports-first-quarter-fiscal-2027-financial-results/ | 2026-08-27 |
| StorageNewsletter | Oracle fiscal 1Q27 financial results | https://storagenewsletter.com/2026/09/23/oracle-fiscal-1q27-financial-results | 2026-09-23 |
| Runtime Wire | Microsoft revenue hits $92.3 billion as Azure growth accelerates to 48% | https://runtimewire.com/article/microsoft-revenue-hits-92-3-billion-as-azure-growth-accelerates-to-48 | 2026-10 |
| Alphabet / SEC | Form 8-K Ex. 99.1, Q3 2026 results | https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000080/googexhibit991q32026.htm | 2026-10-28 |
| StockAnalysis.com | Statistics / market-cap / ratios / revenue pages for SAP, WDAY, IBM, VRNS, DOMO, NTAP, NTNX, DT, RBRK, CVLT, GTLB, AI, MSFT, GOOGL | https://stockanalysis.com/stocks/{ticker}/ | snapshots 2026-06-05 to 2026-10-30 |

### Notable findings

- **Two new take-privates or asset sales in the comp set.** Proofpoint (backed by Thoma Bravo) agreed on 2026-10-15 to buy Varonis for $49.75/sh in cash, about $6.3B and roughly 8.5x FY2026 revenue guidance. Progress agreed in July 2026 to buy Domo's operating assets for $400M, about 1.3x revenue. Domo carries a going-concern warning.
- **Confluent precedent.** IBM paid about $11B EV, or about 9.4x FY2025 revenue of $1,167M (+21%). The deal closed 2026-03-17. IBM's 10-Q reports a purchase price of $11.6B.
- **Hyperscaler cloud is accelerating.** Google Cloud grew 103% to $30.7B in Q3 2026. Azure grew 48% in Q1 FY2027. Oracle's OCI grew 121% in Q1 FY2027, and its RPO is $664B.
- **Infrastructure with AI exposure.** NetApp grew 30% in Q1 FY2027, but its non-GAAP gross margin guidance is down to 67–68% on component costs. Rubrik grew 38% and trades at about 16x EV/FY-guide revenue, the highest multiple in the security and data-protection group.
- **Gaps that remain:** gross margin for SAP, Workday, IBM, Nutanix, Dynatrace, Rubrik, Commvault, C3.ai, Datadog, Elastic and Oracle; the C3.ai market-cap snapshot is stale (2026-06-05); the Domo, Varonis and NetApp market-data snapshots are undated or older; Commvault total-revenue guidance; Amazon AWS growth. [VERIFY]
