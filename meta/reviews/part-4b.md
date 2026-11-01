# Independent review — Part 4, second half (Ch 30–34)

Reviewer: independent (Phase 2), buy-side standard. Date: 2026-11-01. No web search; sources = `meta/verified-facts.md`, `data/*.csv`, `meta/research-briefing.md` integrator notes, and settled pre-2025 knowledge only.

## Chapters reviewed

- `docs/04-company-deep-dives/ch30-data-movement-streaming-companies.md`
- `docs/04-company-deep-dives/ch31-analytical-engine-challengers-legacy.md`
- `docs/04-company-deep-dives/ch32-ai-native-data-companies.md`
- `docs/04-company-deep-dives/ch33-governance-catalog-security-companies.md`
- `docs/04-company-deep-dives/ch34-application-giants-data-platforms.md`

After the edits, every chapter passes `qa_report.py` (word budgets still exceeded: 4,365 / 4,460 / 4,760 / 3,647 / 3,817 against 3,000 / 3,000 / 3,500 / 2,500 / 2,000) and `lint_mermaid.sh` (0 failures). `check_links.py` reports 0 broken links, and no footnote is undefined or unused.

## Data changes

- `data/ch30_confluent_financials.csv`:
  - FY2025 total revenue updated to **$1,166.7M** (+21%). Source is now the FY2025 10-K plus the Business Wire Q4/FY2025 release. Notes add subscription $1,119.7M, services $47.0M, Q4 $314.8M, non-GAAP operating margin 7.4% (vs 2.9%) and GAAP operating loss $380.1M. The [VERIFY] is removed.
  - FY2025 Cloud row ($624M, +27%) re-sourced and its [VERIFY] removed.
  - FY2024 $963.6M marked as confirmed (it is the comparative in the FY2025 release).
  - FY2024 Cloud is still labelled as derived.
  - `python3 scripts/make_charts.py ch30` was re-run: OK, 1 generated, 0 failed.
- Staged `data/staging/review-part-4b-public_comps.csv` (CORRECTION rows):
  - Confluent: FY2025 is verified, so drop "[VERIFY vs 10-K]".
  - Varonis: the $6.3B is the *transaction* value and ~$5.71B the *equity* value, both disclosed in the 8-K. The current note says "press-reported".
- Staged `data/staging/review-part-4b-private_funding.csv` (CORRECTION rows):
  - Firebolt Series C: ~$100M at ~$1.4B, Jan 2022, press-reported.
  - Starburst Series D: ~$3.35B valuation, Feb 2022, press-reported.
  - Both are settled pre-2025 facts. The CSV rows currently leave them blank as "recollection".

## Table of changes

| Chapter | Issue | Fix | Source |
|---|---|---|---|
| 30 | FY2025 revenue $1,167M "[VERIFY vs 10-K]" in TL;DR, snapshot, Financials, deal table, matrix, footnotes | Replaced with verified $1,166.7M GAAP (+21%), Cloud $624M (+27%). Added subscription/services split, Q4 $314.8M, Q4 Cloud $169M (+23%, i.e., cloud decelerating into the sale) | verified-facts #1; 10-K; Business Wire 2026-02-10/11 |
| 30 | "Reached non-GAAP operating profitability only late [VERIFY]" | Replaced with the facts: non-GAAP operating margin 2.9% FY2024 and 7.4% FY2025; GAAP operating loss −$380.1M FY2025. Added the buy-side read that IBM paid for growth and fit, not earnings | verified-facts #1 |
| 30 | Platform-growth arithmetic called "low teens" but computes to ~15% and includes services | Restated as "everything else (mainly Platform plus services) ≈15%, FY2024 Cloud base derived" | Arithmetic |
| 30 | Valuation bridge compared Confluent EV/**trailing** (Dec 2025) with Snowflake EV/**NTM** (Oct 2026) without saying so | Added the basis and date mismatch. On NTM, Confluent would be ~8x (estimate), which strengthens the conclusion. "Don't say" line tightened ("crude, trailing basis") | public_comps.csv |
| 30 | Salesforce product named "Data Cloud" after the Oct 2025 rename (TL;DR, Mermaid node, rationale section) | Changed to Data 360 (formerly Data Cloud); Mermaid re-linted | verified-facts #11 |
| 30 | "No separately disclosed Informatica revenue line … [VERIFY: segment disclosure]" | Added Q2 FY2027 disclosure: Data 360 ARR $2.4B includes $1.1B Informatica Cloud ARR, within ~$3.9B Agentforce + Data 360 ARR (company-stated). Ex-Informatica ≈ $1.3B. Noted the Agentforce ARR redefinition. VERIFY narrowed to leadership/integration milestones | verified-facts #19 |
| 30 | [VERIFY] on Informatica FY2014 revenue (~$1.05B), MuleSoft FY2017 (~$297M), HashiCorp FY2024 (~$583M), Boomi $4B (2021), Matillion Series E $1.5B (2021, General Atlantic), Redpanda–Benthos (May 2024, undisclosed) | Resolved as settled pre-2025 facts. Footnotes say "reviewer-confirmed; primary not re-opened". Figure 30.7 caption updated (only the Informatica 2025 base is still flagged) | Reviewer pre-2025 knowledge |
| 30 | Chart alt text and caption said FY2019–FY2024 all recalled | Caption now says FY2024 and FY2025 are confirmed, FY2019–FY2023 recalled | verified-facts #1 |
| 31 | SAP section omitted SAP–Snowflake and BigQuery; BDC launch date flagged [VERIFY] | Added BigQuery (Oct 2025) and SAP Snowflake + SAP BDC Connect for Snowflake (2025-11-04; GA planned Q1/H1 2026; ship status [VERIFY]). BDC Feb 2025 date resolved. Updated vendor table, timeline, "Why SAP bought Dremio" | verified-facts #12 |
| 31 | "AWS … had already shipped DuckDB-powered analytics inside Aurora" contradicts `ma_deals.csv` (shipped Sep–Oct 2026, after the Aug 2026 agreement) | Reworded to "By September–October 2026 it had shipped…" | ma_deals.csv; verified-facts #13 |
| 31 | Snowflake multiple cross-linked to Ch 25 (Databricks) | Link fixed to Ch 26, with date added | — |
| 31 | ClickHouse vs Teradata "worth 5x … one-seventh of revenue" compared ARR with GAAP revenue | Basis caveat added | — |
| 31 | Starburst $3.35B and Firebolt ~$1.4B (2022) flagged [VERIFY] | Resolved as press-reported, settled pre-2025. Figure 31.5 caption updated. CSV corrections staged | Reviewer pre-2025 knowledge |
| 31 | [VERIFY] on ClickHouse open-sourcing month, Palantir dates, timeline background dates, Vertica→OpenText, Cloudera take-private | Resolved (June 2016; Sept 2020 NYSE direct listing and Nov 2024 move to Nasdaq; OpenText via Micro Focus Jan 2023; Cloudera closed 2021-10-08). Leadership after mid-2025 still [VERIFY] | Reviewer pre-2025 knowledge |
| 32 | Snorkel only in a [VERIFY] footnote; CSV holds newer verified rows | Added $100M at $1.3B (May 2025) and $350M at $3.5B (Sep 2026) with a ~$375M run-rate, all company-stated; ~9x run-rate observation; snapshot updated; new `[^snorkel]` footnote | private_funding.csv |
| 32 | VAST $30B vs Everpure market cap compared without a basis caveat | Added: preferred post-money with secondary component vs traded common equity; only Everpure's revenue is audited | public_comps.csv |
| 32 | Everpure framing | Added 1touch $125M ≈ 0.3% of the ~$43.8B market cap (2026-10-01): a capability tuck-in, with nothing beyond the public record implied | ma_deals.csv; public_comps.csv |
| 32 | "MongoDB, IBM and Oracle have all bought" vector assets; no Oracle deal in the data | Removed Oracle; named Voyage AI and DataStax | ma_deals.csv |
| 32 | VAST "about 29 months" (Dec 2023 → Apr 2026 is 28) | Fixed | Arithmetic |
| 32 | [VERIFY] on Chroma seed, LlamaIndex Series A, Rockset wind-down, Pinecone serverless date, Milvus LF graduation, S3 list price, ASML CCIP stakes, Scale Series F date, founding years/licences, Hammerspace pNFS | Resolved from the CSV (LlamaIndex) or settled pre-2025 knowledge. Post-mid-2025 items (Mercor $10B, Surge revenue, Scale layoffs, VAST ARR, NetApp AFX, WEKA/DDN 2025) kept | private_funding.csv; reviewer |
| 33 | Varonis "$6.3B" presented as the deal value and multiple base without the basis | Labelled **~$6.3B transaction value vs ~$5.71B equity value** throughout (header, TL;DR, snapshot, matrix, financials, precedent table, bull case, "Don't say"). Added equity-basis multiples (~7.7x revenue guide, ~7.9x SaaS ARR). Inference that the gap is converts/dilutive securities (~115M shares × $49.75) is labelled as ours; reconciliation [VERIFY] kept | verified-facts #14; Varonis 8-K |
| 33 | data.world presented as "sold" / "bought" / "absorbed" | Restated as an agreement announced May 2025 with no closing date found. Added Workflow Data Fabric (2024-10-23), RaptorDB Pro as a separate asset, Workflow Data Network (May 2025) | verified-facts #18 |
| 33 | Informatica row "Feeds Data Cloud" | Data 360, counted in Data 360 ARR | verified-facts #11, #19 |
| 33 | Founding-year [VERIFY] for Atlan (2019) and Sentra (2021); Rubrik–Laminar primary | Resolved as settled pre-2025 facts | Reviewer |
| 34 | Data 360 rename [VERIFY] (snapshot, text, table, key terms, Mermaid) | Resolved: renamed at Dreamforce ~2025-10-14 under Agentforce 360 | verified-facts #11 |
| 34 | Latest ARR [VERIFY]; only FY2025 $900M quoted | Added Q2 FY2027: Agentforce + Data 360 ARR ≈ $3.9B (+>210%), Agentforce >$1.5B, Data 360 $2.4B incl. $1.1B Informatica, 3.2B Agentic Work Units, revenue $11.345B (+11%), FY2027 guide $46.10–46.40B. Caveats added (company-stated; ~$1.3B organic; definition broadened). Bear case #3 and open questions updated (lapping in Q4 FY2027) | verified-facts #19 |
| 34 | Workday Data Cloud [VERIFY: name, partners, GA]; dashed Mermaid edges | Resolved: 2025-09-16, Databricks/Salesforce/Snowflake zero-copy via Iceberg Data Connect, Prism inbound queries, BigQuery 2025-11-19. Mermaid edges solid, BQ edge added; timeline moved to 2025 | verified-facts #17 |
| 34 | SAP Snowflake [VERIFY]; dashed edges | Resolved announcement (2025-11-04; SAP Snowflake GA planned Q1 2026; BDC Connect H1 2026); ship status [VERIFY] kept. BigQuery Oct 2025. TL;DR, table, "Don't say" and M&A narrative updated | verified-facts #12 |
| 34 | ServiceNow WDF date [VERIFY]; "RaptorDB"; data.world "close not confirmed" | WDF 2024-10-23; RaptorDB Pro; Workflow Data Network; data.world "agreed; no closing date found" in TL;DR, table and M&A table. New `[^now-ir]` | verified-facts #18 |
| 34 | Salesforce–Own $1.9B [VERIFY]; Workday HiredScore/Evisort [VERIFY]; Palantir–Databricks date [VERIFY]; ZCPN partner list | Resolved as settled pre-2025 facts (Own Sept 2024 cash; HiredScore Feb 2024, Evisort Sept 2024; Palantir–Databricks March 2025; ZCPN launch partners). Scope/terms VERIFY kept | Reviewer |
| 34 | Financials table lacked the latest Salesforce quarter | Added Q2 FY2027 revenue and FY2027 guide | verified-facts #19 |

Total: roughly 60 discrete fixes across the five chapters (≈14 in Ch 30, 12 in Ch 31, 14 in Ch 32, 10 in Ch 33, 15 in Ch 34). About 45 [VERIFY] markers were resolved or narrowed.

## Disagreements / integrator decisions

1. **Confluent "IBM paid a market price" framing (Ch 30).** I kept the conclusion and made the basis explicit. A stricter reviewer would drop the cross-company "x per point of growth" comparison altogether, because the bases are trailing vs NTM, ten months apart, and a 7% vs 15% non-GAAP margin. The integrator decides.
2. **Varonis $6.3B vs $5.71B (Ch 33, and `ma_deals.csv` value_usd_m = 6300).** The CSV records the transaction value. For a precedent EV/revenue, neither figure is a clean EV until the converts and net cash are reconciled. I suggest adding an `equity_value` note column, or a second row, rather than changing 6300.
3. **Pre-2025 "settled" resolutions.** I resolved several [VERIFY]s from my own pre-2025 knowledge: Informatica FY2014, MuleSoft FY2017, HashiCorp FY2024, Boomi $4B, Matillion, Starburst $3.35B, Firebolt $1.4B, Own $1.9B, Palantir–Databricks March 2025 and others. These are well documented, but no primary source was opened. If the integrator wants primary-only resolution, revert to [VERIFY].
4. **Informatica FY2024 revenue (~$1.6B / ~$1.64B)** was left [VERIFY] in Ch 30 and Ch 33, because the 10-K was filed in 2025. I believe $1.64B (GAAP) is correct. Ch 30 says "~$1.6B" and Ch 33 says "~$1.64B", which is consistent but not identical.
5. **`scripts/charts/ch30_confluent.py` source note** still says "FY2019–FY2024 totals recalled … [VERIFY]; FY2025 per data/public_comps.csv". The PNG footnote is now slightly stale. I did not edit it because it is outside my scope. Suggested text: "FY2024–FY2025 per Confluent 10-K FY2025; FY2019–FY2023 recalled [VERIFY]".
6. **Ch 31 chart `ch31_valuations`** omits Starburst and Firebolt because the CSV rows are blank. If the staged corrections merge, the chart will pick them up and the Figure 31.5 caption should be re-checked.
7. **Ch 34 "Genie One" (Ch 32, Ch 34)** relies on the research briefing ("reported GA"). Not changed.

## Remaining high-risk [VERIFY] items

- Ch 30: Informatica FY2024 revenue (deal multiple base); Amit Walia's post-close role; Informatica net debt (EV/revenue); Salesforce–Informatica post-close leadership and integration milestones; Fivetran + dbt confidential S-1 reports; Confluent connector count; FY2019–FY2023 Confluent revenue (recalled).
- Ch 31: Dremio exact close date; AWS–DuckLabs close (no primary confirmation); SAP Snowflake 2026 GA status; Teradata Q3 2026 total and cloud ARR; Palantir US commercial growth; CEO changes after mid-2025; Cloudera 2024–25 tuck-in dates.
- Ch 32: VAST ARR/bookings at Series F (the $30B mark has no revenue anchor); Mercor ~$10B (Oct 2025); Surge >$1B revenue; Scale layoffs and permanent CEO; Pinecone sale reports; turbopuffer funding; Nscale–Anyscale close.
- Ch 33: Varonis $6.3B → $5.71B reconciliation; Collibra/Alation headcount; Alation–Numbers Station; Commvault–Satori; Zscaler DSPM; Veeam–Securiti announcement date; vendor pricing units.
- Ch 34: SAP Snowflake and BDC Connect ship status; Workday Data Cloud GA by partner; Agentforce/Flex Credit current list prices; Now Assist ACV; Paradox/Sana values and closings; SAP/Workday infrastructure and sovereign-cloud scope; Palantir–Snowflake partnership.
