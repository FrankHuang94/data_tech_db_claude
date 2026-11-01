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
