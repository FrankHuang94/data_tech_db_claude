# Independent review — Part 5 (Ch 35–41, business and economics)

Reviewer: Phase 2 independent reviewer (data-platform engineer + buy-side software analyst / CFA lens). Date: 2026-11-01.
No web access. Checks were made against `meta/verified-facts.md`, `data/*.csv` (re-computed with pandas), `meta/research-briefing.md` integrator notes, and the chart scripts that render the Part 5 figures.

## Chapters reviewed

| Chapter | Words (budget) | Visuals | VERIFY left | QA | Mermaid |
|---|---|---|---|---|---|
| `docs/05-business-and-economics/ch35-business-models.md` | 3,9xx (2,500) | 9 | 1 | OK | 3/3 OK |
| `docs/05-business-and-economics/ch36-unit-economics-kpis.md` | 4,1xx (2,500) | 11 | 8 | OK | 2/2 OK |
| `docs/05-business-and-economics/ch37-public-comps-valuation.md` | 3,4xx (2,500) | 15 | 6 | OK | 2/2 OK |
| `docs/05-business-and-economics/ch38-open-source-strategy.md` | 3,3xx (2,000) | 8 | 6 | OK | 3/3 OK (xychart edited, re-linted) |
| `docs/05-business-and-economics/ch39-ma-history.md` | 4,8xx (3,500) | 11 | 1 | OK | 2/2 OK |
| `docs/05-business-and-economics/ch40-gtm-partnerships.md` | 2,9xx (2,000) | 9 | 6 | OK | 4/4 OK |
| `docs/05-business-and-economics/ch41-market-sizing.md` | 1,8xx (1,000) | 7 | 6 | OK | 2/2 OK |

Staged: `data/staging/review-part-5-public_comps.csv` (ServiceNow growth refresh, proposed; Palantir notes clean-up).

## Recomputations that held up (no change needed)

- **Ch 39 vs `data/ma_deals.csv` (pandas):** 143 rows; 74 valued (51.7% → "52%"); 55 disclosed (38.5%), 19 press-reported (13%), 69 undisclosed (48%); median valued $825M, median disclosed $1,050M; 54 deals in 2025–26 (Jan 2025–Oct 2026 = 22 months), 42.6% valued ("43%"); 8 deals in 2020–22; per-year counts 3 (2010) / 32 (2025) / 22 (2026); value sums $46.6B (2018), $43.4B (2023), $48.4B (2025); Databricks 16 deals (5 in 2026), Snowflake 12, IBM 7; Salesforce data-layer spend $32.9B ("more than $32B"). Veeam–Securiti is now dated 2025-10-21 and Palo Alto–Protect AI 2025-04-28 in the CSV (announcement dates).
- **Ch 37 regression (pandas, mirrors `scripts/charts/core_comps.py`):** ex-Palantir (>40x) and ex-Confluent (acquired), Domo included, n = 24: EV/NTM = 4.13 + 0.189 × growth, R² 0.384. Ex-C3.ai, n = 23: 1.07 + 0.327 × growth, R² 0.567. Everpure residual −2.81 → gap 2.81 × $5.05B ≈ $14.2B. Group medians (10.6x / 9.0x / 7.6x / 7.1x / 6.4x / 6.0x / 5.7x) unchanged whether Palantir is 53.1x or 70.3x. Every EV/NTM in the CSV re-derives from EV ÷ NTM revenue within rounding.
- Other arithmetic: Snowflake product growth 106% / 70% / 38% (FY2022–24 from CSV); Confluent Cloud 53% of FY2025 revenue; Everpure product 58% of Q2 FY2027 revenue, FY2027 guide/FY2026 = 1.38; Everpure GAAP op margin 5.3%, gap ~14 pts; MongoDB GAAP op margin 3.7%, gap ~20 pts; Snowflake SBC-burdened Rule of 40 ≈ 20; magic number 1.06 raw / 0.72 day-adjusted; cRPO ≈ $4.86B; private-mark multiples (VAST 60x, ClickHouse 60x, Temporal 50x, Supabase 62x, Snorkel 9x); Confluent ~9.43x; Varonis 8.55x on $6.3B; Qualcomm QTL EBT margin 72%; Ch 41 TAM ratios (Snowflake 2.0%, Confluent 1.2%, 100/5.9 ≈ 17x, 100/34.8 ≈ 2.9x).
- Verified-facts consistency: Everpure Q2 FY2027 (revenue ~$1.19B +38%, product $687M +54%, subscription services $499M +20%, FCF −$238M) and FY2027 guide $5.03–5.07B (midpoint $5.05B used as NTM); Confluent FY2025 $1,166.7M; Databricks $190B / >$7B run-rate; Proofpoint–Varonis 2026-10-15; MongoDB Q2 FY2027 figures; Snowflake Q2 FY2027 figures — all consistent across Ch 35–41.

## Changes

| Chapter | Issue | Fix | Source |
|---|---|---|---|
| 37 | **Palantir basis inconsistent with the CSV and the chart.** Table, TL;DR and growth-adjusted table used 70.3x EV/TTM and 79% TTM growth, while `public_comps.csv` (and the SV-14 scatter, which reads it) shows 53.1x on the FY2026 guide and 93% latest-quarter growth; alt text described a point at "70x and 79%" that is not on the chart | Table row now 53.1x (G), 93% (Q), Rule of 40 156, with 70.3x explicitly labelled EV/TTM ($6.16B TTM). TL;DR, alt text, "Why Palantir is an outlier", Numbers table and "Don't say this" rewritten on both bases | public_comps.csv; company_financials.csv (TTM $6.16B); Palantir Q2 2026 8-K |
| 37 | **Analytical claim reversed by the basis fix:** "Palantir is an outlier even after growth-adjusting" (0.89 turns/pt) mixed a TTM multiple with TTM growth; like-for-like with the rest of the table it is 53.1/93 = 0.57, about Datadog's 0.60 | Reframed: outlier on level of growth and assumed duration, not on price per point; 0.89 retained as the TTM/TTM figure | Our arithmetic on public_comps.csv |
| 37 | Regression sample misdescribed ("24 comps, Palantir excluded"); it actually includes Domo (asset-sale case) and excludes Confluent; table caption said "25 companies" but lists 24 | Sample described precisely in TL;DR and Figure 37.2 caption; table count corrected to 24 | core_comps.py; pandas re-fit |
| 37 | Residual list omitted C3.ai (+6.9x, second-largest positive) and Domo (−3.3x); MSFT/AMZN residuals rest on TTM denominators | Added C3.ai and Domo context and TTM caveats | pandas re-fit |
| 37 | "T"-basis rows (8 companies) were EV/TTM inside an "EV/NTM" column without a caption flag; ServiceNow growth is Q2 2026 although Q3 2026 (20.5%) is used in Ch 36 | Caption lists the EV/TTM rows; ServiceNow quarter flagged; CSV refresh staged | public_comps.csv; ch36_rule_of_40.csv |
| 37 | Rule of 40 values differ from Ch 36 (Snowflake 61 vs 58; Everpure ~55 vs 52) without explanation | Caption notes Ch 36 uses FY2027 FCF guides | ch36_rule_of_40.csv |
| 37 | **NRR comparability:** "Snowflake's 126% and MongoDB's 122%" treated as the same metric; 122% is press-reported (Zacks) and is MongoDB's ARR-based net ARR expansion rate (10-K: ~121% at FY2026 year-end) | Text and growth-adjusted table now name both definitions, label the source, and warn the gap is not meaningful | Ch 36 definitions; public_comps.csv notes |
| 37 | **Databricks re-rating decomposition wrong:** Figure 37.8 said run-rate rose "from about $4B" over the 20 months since the $62B round; the run-rate at that round was ~$3B (company projection for the quarter to Jan 2025). "Half from revenue, half from multiple" therefore wrong | Corrected to ~$3B → >$7B; multiple ~21x → ~27x; ~three-quarters of re-rating from revenue (log decomposition) | ch25_databricks_runrate.csv; private_funding.csv |
| 37 | Databricks ~27x labelled only "run-rate" in the growth-adjusted table | Labelled post-money equity ÷ company-stated run-rate; not EV/NTM | private_funding.csv |
| 37 | ClickHouse ~60x mixes a Jan 2026 mark with a May 2026 revenue figure | Flagged; multiple at pricing was higher | private_funding.csv |
| 37 | **Precedent table:** Veeam–Securiti dated by completion (2025-12-11) in an "Announced" column; Everpure–1touch and Domo rows out of order | Announcement date 2025-10-21 (completion noted); rows re-ordered chronologically | ma_deals.csv; verified-facts |
| 37 | Varonis multiple quoted as "~8.5x FY-guide" without saying the $6.3B is transaction value, not equity value, or that FY2026 = calendar 2026 (current-year, not NTM) | ~8.5x on $6.3B transaction value / ~7.7x on ~$5.71B equity value, CY2026 guide midpoint $737M; footnote updated | verified-facts #14; public_comps.csv |
| 37 | Confluent precedent basis "trailing" at an announcement date when FY2025 was not yet reported; Informatica basis not labelled equity value | Confluent: ~$11B EV ÷ FY2025 GAAP revenue $1,166.7M (announced 2025-12-08, closed 2026-03-17); Informatica labelled equity value (EV adds net debt) | verified-facts #1; Confluent 10-K |
| 37 | Palantir and Varonis footnotes lacked the arithmetic and bases | Footnotes now give both Palantir denominators and the Varonis equity/transaction distinction | — |
| 36 | TL;DR Rule-of-40 range "~18 to ~58" unexplained (18 never derived in the text) | Spelled out the four variants (GAAP op margin 18; SBC-burdened 20; quarterly adj. FCF 41; FY guide 58) | Figure 36.5 arithmetic |
| 36 | cRPO "covers ~80% of FY2027 guide" bridge overstated NTM coverage (half of FY2027 was already recognized) | Added clause that true NTM coverage is lower | Snowflake 10-Q |
| 36 | MongoDB expansion rate ~121% (10-K, Jan 2026) vs 122% used in Ch 37 | Both shown with dates and bases; comps footnote extended | public_comps.csv |
| 36 | Palantir release date [VERIFY day] | Resolved to 2026-08-03 (same 8-K as Ch 37 citation) | Ch 37 [^pltr] |
| 35 | Figure 35.9 claimed consumption leaders' premium is "because NRR above 120% compounds"; MongoDB (~121–122%, ARR-based) at 9.0x contradicts it | Softened to "partly", with the MongoDB counter-example and non-comparability note | public_comps.csv |
| 35 | EV/NTM row in Numbers table lacked dates and basis | Basis (current-FY guidance proxy) and per-company dates added | public_comps.csv |
| 38 | **Overclaim:** "growth explains most of the gap" between open-source-origin (4.6–9.0x) and proprietary names (16.9–21.5x). On the Ch 37 regression, growth explains ~1 turn of the ~8-turn Snowflake–MongoDB spread | TL;DR and Figure 38.7 caption rewritten (retention, visibility, AI exposure explain more; licence not a factor) | Ch 37 regression |
| 38 | Figure 38.7 put Confluent's control-deal multiple (EV/trailing) in an "EV/NTM" bar chart dated "March 2026" | Bar labelled "(trailing)"; caption gives ~$11B EV ÷ $1,166.7M, announced 2025-12-08, closed 2026-03-17; Mermaid re-linted | verified-facts #1 |
| 38 | Licence table labelled MySQL Community as GPLv3 | Row now "GPL (v2 and v3)", MySQL Community (GPLv2) | Settled pre-2025 fact |
| 38 | IBM–HashiCorp and IBM–Confluent dated only by closing | Announcement and closing dates both given | ma_deals.csv |
| 39 | Veeam–Securiti caption still said "per staged correction" (now merged); source note pointed to staging file | Caption and [^ma-csv] updated; reviewer's pandas statistics recorded in footnote | ma_deals.csv |
| 39 | Varonis "~8.4x LTM revenue, press-reported" conflicted with Ch 37's 8.5x and has an unstated basis (LTM revenue at Oct 2026 should be below the $737M CY2026 guide, so 8.4x on $6.3B looks inconsistent) | Replaced with Ch 37's labelled multiples; press figure retained only as "unstated basis" | Varonis 8-K; public_comps.csv |
| 39 | Old product name "Data Cloud" in MuleSoft row | "Data 360 (formerly Data Cloud) and Agentforce" | verified-facts #11 |
| 39 | Informatica outcome lacked post-deal evidence | Added $1.1B Informatica Cloud ARR inside $2.4B Data 360 ARR (Q2 FY2027, company-stated) with new footnote [^crm-q2] | verified-facts #19 |
| 39 | IBM–Confluent labelled "~$11B" without EV basis or multiple; Numbers table dated by completion only | ~$11B EV, ~9.4x FY2025 GAAP revenue; announced 2025-12-08 | verified-facts #1 |
| 39 | Informatica IPO price [VERIFY] | Resolved: priced at $28, below the $29–32 range (30M shares ≈ $840M, consistent with the ~$841M cited) | 424B4; settled pre-2025 fact |
| 39 | Figure 39.1 read a curated file as a market census ("collapsed", "exploded") | Caption now says "curated file… pattern, not a census"; softened verbs | — |
| 41 | Everpure revenue/TAM "~3.3%" on ">$3.6B" | $3.66B (FY2026 GAAP) ÷ $108B ≈ 3.4% | 10-K FY2026 |
| 41 | Storage bridge compared a FY2030 company TAM ($22B) with a 2023 Gartner market ($11.1B) without adjusting for years | Added: even at 8.1% growth Gartner's figure would be ~$19B by 2030 (our arithmetic) | market_sizes additions |

Total: 34 logged fixes (Ch 35: 2; Ch 36: 4; Ch 37: 14; Ch 38: 4; Ch 39: 8; Ch 41: 2; Ch 40: 0), comprising about 55 individual text edits. Some table rows bundle closely related edits.

**Ch 41 market-size labels:** every syndicated, derived or second-hand figure (2023/2025 DBMS derivations, cloud DBMS, Apps Run the World BI, Grand View metadata, FMI/Securiti DSPM, MarketsandMarkets vector, GMI training data, Snowflake 2026 TAM, Everpure FAM TAMs) is flagged **Weak** or *Derived* in the text and table. No unlabelled weak source found.

**Ch 40:** no factual fixes. Fee schedules, programme names and dates are consistent with the cited sources; Snowflake's >$2B / >$7B are correctly labelled marketplace sales (not revenue).

## Disagreements / for the integrator

1. **Palantir house basis.** Ch 25, 26, 34 and 44 cite **70.3x EV/TTM** (correctly labelled); Ch 49 and now Ch 37 lead with **~53x EV/NTM (FY2026 guide)**, which is what `public_comps.csv` and the SV-14 chart use. Both are correct when labelled. Recommend one house default (NTM proxy, to match every other comps row) and that Ch 25/26 add the 53x figure when next touched. The Palantir CSV note ("ch37 kept original values for consistency with SV-14") is now stale; a notes-only correction is staged.
2. **ServiceNow growth** in `public_comps.csv` is Q2 2026 (24%, may include Moveworks) while Q3 2026 (20.5%) has been reported and is used in Ch 36. Staged as a proposed correction; the regression is unchanged (slope 0.189, R² 0.38).
3. **MongoDB "NRR"** in `public_comps.csv` (`nrr_pct` = 122) is a press-reported net ARR expansion rate, not an NRR, and the row's notes also say "NRR not quantitatively disclosed [VERIFY]". Suggest renaming the column semantics in the notes or blanking it, to stop other chapters comparing it with Snowflake's 126%.
4. **Domo in the regression.** The SV-14 fit includes Domo (0.9x, asset sale pending) although Ch 37's table excludes it. Excluding Domo gives 4.47 + 0.178 × growth, R² 0.35. I disclosed rather than changed it, because the chart script defines the canonical fit; integrator may prefer to filter Domo in `core_comps.py`.
5. **Varonis transaction value vs EV.** The $6.3B is the 8-K's transaction value, which is above the $5.71B equity value, so it likely includes debt (convertible notes) without netting cash; it is not a clean EV. Ch 37/39 now say "transaction value". Net cash per CSV (~$0.38B, older snapshot) is [VERIFY].
6. **Splunk growth at deal ("low teens [VERIFY]").** My recollection is ~14% (Q2 FY2024, quarter to Jul 2023), but I left the marker because I could not check the 10-Q.

## Remaining high-risk [VERIFY] items

- Ch 37: Splunk LTM revenue (~$3.9B) and growth at deal; Couchbase FY2025 revenue (~$209M via aggregator); BVP index multiple date/basis; Supabase $10.65B extension (single source).
- Ch 36: Snowflake Q1 FY2027 S&M (~$590M, derived) feeds the magic number; non-GAAP add-back split; Everpure segment gross margins (press-reported).
- Ch 39: AWS–DuckLabs closing not confirmed by a primary source (and the Aurora PostgreSQL DuckDB claim rests on it).
- Ch 41: Snowflake June 2026 TAM (~$225B / >$460B, AI-generated transcript summary); Everpure FAM TAMs ($108B/$207B/$22B, second-hand); sovereign cloud ~$80B total.
- Ch 38: dbt Fusion licence split; Iceberg committers by employer.
- Ch 40: whether Everpure's cloud listings are MACC/EDP-eligible; NVIDIA AI Data Platform partner list.
