# Independent review — Part 4, first half (Ch 25–29)

Reviewer: Phase 2 independent reviewer (data-platform engineer + buy-side software analyst lens). Date: 2026-11-01.
No web access; checks were made against `meta/verified-facts.md`, `data/*.csv` and `meta/research-briefing.md` integrator notes.

## Chapters reviewed

- `docs/04-company-deep-dives/ch25-databricks.md` (5,3xx words, budget 4,500; QA OK; Mermaid 5/5 OK)
- `docs/04-company-deep-dives/ch26-snowflake.md` (6,4xx words, budget 4,500; QA OK; Mermaid 4/4 OK)
- `docs/04-company-deep-dives/ch27-databricks-vs-snowflake.md` (3,9xx words, budget 2,500; QA OK; Mermaid 3/3 OK)
- `docs/04-company-deep-dives/ch28-hyperscaler-data-platforms.md` (5,3xx words, budget 3,500; QA OK; Mermaid 3/3 OK)
- `docs/04-company-deep-dives/ch29-operational-database-vendors.md` (4,5xx words, budget 3,000; QA OK; Mermaid 3/3 OK)

Also touched (per caller instruction for Ch 28): `data/ch28_cloud_segments.csv`, `scripts/charts/ch28_cloud_growth.py` (y-axis limit, gap logic and source note, which still said "AWS latest quarter not compiled"), regenerated `docs/assets/charts/ch28_cloud_growth.png`. Staged: `data/staging/review-part-4a-company_financials.csv`.

Spot-checked arithmetic that held up (no change needed): Snowflake 16.9x = 106.31/6.30; RPO 1.4 years of NTM; EV/FCF ~73x; IPO returns (2.55x ≈ 17%/yr; 1.25x ≈ 4%/yr); product revenue 8x FY2021→FY2026 and ~18x FY2020→FY2026; Q4 FY2027 implied ~$1.66B (+35%); Databricks growth-implied prior-year base; Ch 27 valuation table ($168B / $120B / $269B); M&A sums ($4.4B / $1.86B); MongoDB quarterly growth (13% Q2 FY25, 19% Q3 FY26, 27% Q4 FY26, 30% Q2 FY27); Oracle RPO prior year $455B; Databricks debt ($2.75B term loan + $2.5B revolver).

## Changes

| Chapter | Issue | Fix | Source |
|---|---|---|---|
| 25 | TL;DR set Databricks' 27x beside Snowflake's 16.9x with no caveat | Added explicit non-comparability: post-money equity / unaudited run-rate vs public EV / guidance-derived GAAP revenue | public_comps.csv; Ch 27 bridge |
| 25 | Snapshot and text called FCF "positive"; company language is "adjusted FCF positive" | Relabelled as adjusted, non-GAAP, reaffirmed Aug 2026 | verified-facts #8 |
| 25 | $1M-customer comparison (>800 vs 828) treated as like-for-like | Explained run-rate vs trailing-12-month threshold; Databricks count flattered | db-54; Snowflake Q2 FY27 |
| 25 | Palantir multiple shown as "~70x EV/revenue" in two places without basis | Labelled 70.3x **EV/TTM** (not NTM), 2026-10-30 | public_comps.csv (Palantir row) |
| 25 | Bull case #6 called Databricks' ratio "EV/run-rate" | Changed to post-money value / run-rate; flagged different numerators and denominators | private_funding.csv |
| 25 | Competitive matrix "latest scale marker" row mixed run-rate, GAAP quarter, TTM and a private valuation | Added a comparability-note row | — |
| 25 | Old product name "declarative pipelines (formerly Delta Live Tables)" | Lakeflow Spark Declarative Pipelines (renamed Nov 2025) | research-briefing integrator note |
| 26 | **Bull case #5 was wrong:** said Snowflake trades *below* Databricks on a growth-adjusted basis; the chapter's own figures show 0.48x vs 0.34x (Snowflake dearer) | Rewritten: cheaper on headline (17x vs 27x), not on growth-adjusted; Palantir labelled EV/TTM | public_comps.csv; Ch 25/27 arithmetic |
| 26 | Valuation bridge compared growth-adjusted ratios without basis caveat; NTM proxy not flagged | Added equity-vs-EV and run-rate-vs-GAAP caveat; noted FY-guide proxy understates NTM | public_comps.csv notes |
| 26 | $1M-customer comparison cited the Aug 2026 release for a Jan 2026 Databricks figure | Re-cited to db-54 (Feb 2026) and added definitional caveat; added `[^db-54]`, `[^comps-pltr]` footnotes | db-54 |
| 26 | Competitive matrix scale row mixed bases | Added comparability-note row (Snowflake ×4 ≈ $6.2B; Databricks run-rate not comparable) | — |
| 26 | SAP × Snowflake partnership (Nov 2025) missing | Added to partner-ecosystem paragraph with ship-status `[VERIFY]` and `[^sap-sf]` footnote | verified-facts #12 |
| 27 | TL;DR "Databricks is cheaper" growth-adjusted, stated without basis | Added: only on its own unaudited run-rate; numerators and denominators differ | — |
| 27 | Snapshot FCF label | "Adjusted FCF positive (company-stated, non-GAAP)" | verified-facts #8 |
| 27 | M&A spend row mixed press-reported (Databricks) and filed (Snowflake) values without saying so | Stated bases; added Snowflake press-basis total (~$2.35B) | ma_deals.csv |
| 27 | Crunchy "$164.5M disclosed" / "Databricks paid ~6x more"; Observe "$596.2M disclosed" | Crunchy: 10-Q purchase accounting vs ~$250M press; ~6x on filed, ~4x on press. Observe: preliminary consideration per 10-K vs ~$1B press | ma_deals.csv |
| 27 | Openflow "(GA 2026)" contradicted Ch 26 (GA May 2025; gen-2 runtimes GA Sep 2026) | Aligned with Ch 26 | Snowflake release notes (Ch 26 `[^openflow-ga]`) |
| 27 | Lakeflow pipeline name | Spark Declarative Pipelines | research-briefing |
| 27 | Snowflake bull #4 and "Don't say" valuation line | Clarified headline vs growth-adjusted, and the adjustments needed | — |
| 28 | **AWS Q3 2026 missing** (chapter said "could not be checked"; used Q3 2025 $33.0B as latest, including in TL;DR, snapshot, Fig 28.5/28.6, matrix) | Updated throughout: $46.0B, +39% (GAAP segment), +37% in Q2 2026, $184B annualised run-rate (company-stated = quarter × 4), Amazon net sales $201.9B (+12%); new `[^amzn-q3]` footnote | verified-facts #2 (Amazon 8-K) |
| 28 | Text said Azure (~$33.2B) was "roughly level with AWS" | Corrected: ~$13B a quarter behind AWS's $46.0B; segment definitions differ | verified-facts #2, #3 |
| 28 | Microsoft backlog and capex not shown | Added commercial RPO $677B (+73%) and capex $39.4B, labelled press-reported summary of company release | verified-facts #3 |
| 28 | Microsoft footnote basis | Relabelled "press-reported summary of company release", FY note, Azure $ figure still `[VERIFY]` | verified-facts #3 |
| 28 | Absolute-dollar context missing | Added: AWS +~$13.0B YoY vs Google Cloud +~$15.5B (author arithmetic) | ch28_cloud_segments.csv |
| 28 | Bull #5 / risk #1 incomplete | Added AWS 39% and Microsoft $39.4B capex | verified-facts #2, #3 |
| 28 (data) | `ch28_cloud_segments.csv` lacked AWS 2026 rows; 2026 rows' basis notes did not reference live verification | Added AWS Q2 2026 (growth 37%) and Q3 2026 ($46.0B, 39%) rows with source/as_of; updated basis on Google Q3 2026, Azure Q1 FY2027, OCI Q1 FY2027 rows | verified-facts #2–5 |
| 28 (chart) | Chart could not show AWS 2026; bar axis capped at $38B | Plot all post-gap points with dotted bridge; y-limit 52; source note updated; regenerated `ch28_cloud_growth.png` | — |
| 29 | **MongoDB CEO stale:** said CJ Desai is CEO (with `[VERIFY]`) in snapshot, leadership section, open questions, timeline | Snapshot: Ittycheria interim President & CEO since Sep 2026; Desai CEO 2025-11-10 → Sep 2026 (left for Meta); permanent search under way. Leadership paragraph rewritten (incl. governance/execution-risk read); timeline both events; open question replaced; new "Don't say" bullet; `[^mdb-ceo]` footnote rebuilt with primary release + StorageNewsletter | verified-facts #9 |
| 29 | TL;DR said MongoDB re-accelerated "from about 19% a year earlier"; Q2 FY2026 growth was ~24% (591.4/478.1) | Fixed to ~24% a year earlier with a 19% trough in Q3 FY2026 | ch29_mongodb_quarterly.csv |
| 29 | `[VERIFY]` on Q2 FY2027 Atlas share and non-GAAP operating margin | Resolved: ~73% (~$565.9M, third-party split) and 24% vs 15%; added GAAP net income $40.9M, EA/other +36%, Q3 guide $756–761M with note that the sequential dip reflects upfront EA licence recognition | verified-facts #7 |
| 29 | Atlas customer ">69,300" presented as total customers | Relabelled as Atlas customers per search summary, kept `[VERIFY]` (it exceeds the FY2026 total-customer count of 65,200, so needs checking) | verified-facts #7 |
| 29 | Crunchy value in TL;DR and snapshot showed only 10-Q figure | Added ~$250M press-reported alongside $164.5M purchase consideration | ma_deals.csv |
| 29 | MongoDB vs Snowflake multiple compared without dates/basis | Dated both (2026-10-20 vs 2026-10-30), same FY-guide proxy; bear-side added CEO uncertainty and FY27 guide implying ~22% growth | public_comps.csv |

Total: 34 discrete fixes (25: 7; 26: 6; 27: 8; 28: 9 incl. CSV/chart; 29: 8 counting the CEO change once per location group). (Several rows above bundle multiple edits.)

## Disagreements / items for the integrator

1. **Chart script edit.** The brief limits edits to chapters, log and staging, but the caller explicitly asked for the Ch 28 CSV update and chart regeneration; the chart script's hard-coded source note ("AWS latest quarter not compiled [VERIFY]") and y-limit made a script edit unavoidable. Please confirm.
2. **`data/ch28_cloud_segments.csv` edited in place** (not staged) on the caller's instruction. `data/company_financials.csv` still carries an Amazon Q3 2025 row whose note says "Q3 2026 figure still needed"; corrections/additions staged in `data/staging/review-part-4a-company_financials.csv`. `data/public_comps.csv` Amazon row note still says "AWS segment growth [VERIFY]" — integrator should update to 39% (Q3 2026).
3. **Azure ~$33.2B dollar figure** appears only in secondary coverage, not in `meta/verified-facts.md` (which verifies +48%). Kept, labelled press-reported with `[VERIFY]`. If Microsoft did not actually disclose Azure dollars, remove it from Ch 28 text, chart bar and CSV.
4. **Growth-adjusted valuation framing (Ch 25/26/27).** The chapters lean on "~0.34x vs ~0.48x per point of growth". I kept it with caveats, but a buy-side reader may object that it divides an equity/run-rate multiple by a run-rate growth floor and an EV/NTM-proxy multiple by trailing GAAP growth. Integrator may prefer to demote it to a footnote.
5. **MongoDB Atlas customers >69,300** vs FY2026 total customers >65,200: one of these is likely mislabelled in the search summary (verified-facts item 7 itself carries a "?"). Needs the release.
6. Microsoft's prior-quarter Azure growth ("42%?") in verified-facts is uncertain; not added to the CSV.

## Remaining high-risk `[VERIFY]` items

- Ch 25: Databricks employee count; Azure share of Databricks revenue; Mosaic AI brand status; Everpure OpenSharing connector GA status (most relevant to the reader); Ghodsi IPO quote (secondary source).
- Ch 26: CFO transition (Robins/Scarpelli) date; Q2 FY2027 cRPO; current credit list prices; buyback/convert terms; S3-compatible external-volume GA and vendor list (incl. Pure Storage 2022 certification); Investor Day TAM ($225B/$460B from an AI-generated transcript summary — weak); SAP Snowflake ship status; FY2020–24 values not re-read.
- Ch 27: DBU-per-hour by SQL warehouse size and Snowflake credit prices (drive the worked example); TPC-DS 2021 blog URLs; customer-overlap data.
- Ch 28: Azure dollar figure; AWS Q3 2026 segment operating income; 2024–25 segment rows drafter-compiled; Oracle HQ (Austin vs Nashville); Gartner vendor ranking; Fabric customer count; OpenAI–Oracle $300B (WSJ, press-reported).
- Ch 29: Oracle co-CEOs (Magouyrk/Sicilia); Oracle FY2025 support line $44.0B; MongoDB Atlas customer count; quarterly MongoDB 8-K values before Q4 FY2026; Redis/Couchbase/Yugabyte/PlanetScale/Aerospike valuation and licence details; SingleStore close.
