# Independent review: Part 7, Part 0 and the cross-atlas consistency sweep

**Reviewer:** independent Phase 2 reviewer (principal data-platform engineer and buy-side software analyst lens) · **Date:** 2026-11-01
**Scope:** `docs/07-conversation-toolkit/` ch46–ch50; `docs/00-start-here/` ch00-1 and ch00-2; `docs/index.md`; the SVG `docs/assets/diagrams/ch00-market-map.svg`. All were read in full, including footnotes. A grep sweep of `docs/**/*.md` then checked nine named consistency items.
**Sources of truth used:** `meta/verified-facts.md` items 1–22; `data/public_comps.csv`, `data/company_financials.csv`, `data/ma_deals.csv`, `data/private_funding.csv`, `data/ch36_rule_of_40.csv` and `data/ch41_market_sizes_additions.csv`; integrator notes in `meta/research-briefing.md`; the reviewed Parts 1–6 chapters (Ch 25, 26, 27, 31, 33, 34, 37, 38, 39, 40, 45) as cross-checks. There was no web access.

## Summary

- **Chapters reviewed:** 8 files (ch00-1, ch00-2, index, ch46, ch47, ch48, ch49, ch50) plus 1 SVG.
- **Fixes:** about 44 edits in Part 7 and Part 0, plus 2 SVG label fixes. The sweep made 19 edits in 11 other files: ch25, ch26, ch27, ch30, ch31, ch34, ch39, ch40, ch43 and `docs/glossary.md`.
- **Post-edit QA:** `scripts/qa_report.py` OK on every edited chapter. `scripts/lint_mermaid.sh` found 0 failures. Three Mermaid timelines were edited (ch26, ch27 and ch34) and one timeline label in ch30. `scripts/check_links.py` found 4,581 internal links and 0 broken. The SVG still parses as XML.
- **Word counts after review:** ch00-1 1,760 (budget 1,200); ch00-2 2,053 (1,800); ch46 3,865 (2,200); ch47 3,671 (2,000); ch48 8,292 (2,000); ch49 4,676 (1,500); ch50 13,286 (1,300).
- **Flashcards (ch50):** all 253 were checked against the source chapters and CSVs. Most were correct. Eleven were fixed: Q16, Q171, Q178, Q190, Q197, Q204, Q233, Q240 and Q251, plus two deal-poster rows and the one-pager. The deck counts in the text (29/25/39/46/44/29/22/19 = 253) were not re-tallied card by card, but the Q-numbering runs from Q1 to Q253 without gaps.
- **Question bank (ch48):** a script re-tallied every tag. All 154 questions are tagged. The topic counts and the audience counts per topic (Engineer 69, PM 52, CFO/Finance 50, Customer 42, Founder/CEO 35, Partner manager 28) match Figure 48.3 exactly, and every tag sits in the matching `##` group. The H1 said "150 Questions" while the bank holds 154; the title is fixed.
- **KPI definitions (ch47):** NRR, GRR, magic number and CAC payback are correct. For CAC payback, 12 ÷ (magic number × GM) follows algebraically from the magic-number definition. Rule of 40 and RPO/cRPO were **missing** from the KPI table, so both rows were added with definitions, Snowflake reference points from the CSVs and the usual traps.
- **Learning paths (ch00-1):** every link resolves, and the 2-hour, 2-day and 2-week steps point to real chapters and anchors.
- **Market map (ch00-2 + SVG):** ownership matches the record. Neon → Databricks, Crunchy → Snowflake, Tabular → Databricks, Informatica → Salesforce, Confluent → IBM, Dremio → SAP, 1touch → Everpure and W&B → CoreWeave are closed. Varonis → Proofpoint is pending. Two SVG chips gained their status: **DuckLabs → AWS (agreed)** and **Dagster → Prefect (pending)**. To make room, Starburst moved to the second row of layer 5. New chip widths were sized with Liberation Sans metrics, and there is no overlap or overflow.

## Most serious issues

1. **Unlabelled Palantir 70x (sweep item 1).** Ch 31's TL;DR ("about **70x** on ~79% trailing growth") and its comparison table ("Public, 70x") gave no basis. Ch 34's TL;DR said "~70x trailing revenue" without EV. All three now read "~70x EV/TTM" with the ~53x EV/NTM (FY2026 guidance basis, `public_comps.csv`) alongside. Ch 49 entries 58 and 70 and Ch 50 Q171 now state the basis too.
2. **Fivetran–Census described as completed (sweep item 6).** These were fixed to "agreed to buy … closing not separately confirmed": Ch 30 (timeline, and "It bought Census" in the body), Ch 39 ("Fivetran bought … reverse ETL (Census)"), Ch 43 ("Census, inside Fivetran") and Ch 50 Q233 ("Fivetran bought Census"). The source is `ma_deals.csv` (status *announced*).
3. **Snowflake S3-compatible list not aligned with verified-facts #21 (sweep item 8).** Ch 27 still called Pure Storage's inclusion a "pre-2025 recollection", described vendors as "validated", and carried three broad `[VERIFY]`s. Ch 40 said Everpure "appears on" the list. Ch 50 Q240 deferred to "Ch 27 flags the list for re-checking". All three, plus Ch 46 and Ch 48 Q139, now say the same thing:
   - Snowflake's documentation lists PureStorage among other vendors.
   - Snowflake says it does not test or validate third-party products.
   - The current page requires a "Snowflake S3-compatible tested and compliant" service.
   - Pure and Snowflake announced a joint FlashBlade solution in May 2022.
   - FlashBlade's status under the newer wording is `[VERIFY]`.

   The broad `[VERIFY]`s were narrowed to that one open point, and a `[^pure-sf]` footnote was added to Ch 27 and Ch 50.
4. **Ch 50 Q204 contradicted Ch 38 and Ch 37.** It said growth "explains most of the gap" between open-source-origin and proprietary multiples. Ch 38 says growth explains only about one turn of the roughly 8-turn Snowflake–MongoDB spread, and MongoDB at 30% growth trades at 9.0x against Snowflake at 35% and 16.9x. The card was rewritten to match Ch 38.
5. **RPO decline mis-explained (Ch 49 entry 55; Ch 50 Q190).** Both attributed Snowflake's RPO fall from $9.77B to ~$9.0B solely to customers "burning commitments faster than they signed new ones". Most of that is fiscal-Q4 renewal seasonality. The seasonality is now stated, together with the ~54% current portion from `company_financials.csv`.
6. **Varonis value basis incomplete.** Ch 00-2 (three places), Ch 49 entry 33, Ch 50 Q178, Q197 and the deal poster, and the Ch 39 master table ("~$6.3B headline") lacked a basis. Each now gives the ~$6.3B transaction value, the ~$5.71B equity value and pending status. Multiples are labelled as on transaction value (~8.5x) or equity value (~7.7x).
7. **Status and basis slips in Part 0.**
   - "DuckLabs went to AWS" is only an agreement.
   - Teradata's "1.7x EV/NTM" is a TTM proxy.
   - Supabase "$10.65B" is a single-source press report; the confirmed Series F was $10.5B.
   - The "largest 2025–26 deals" row gave the window as Jun 2025–Oct 2026, but Moveworks was announced in Mar 2025.
   - "Agents, not people, now create most new databases" was stated as fact. It is now attributed to Neon's company-stated >80% figure.
   - Ch 00-1 said agents are "now the biggest new consumers" of context. That repeated the overclaim the Part 6 reviewer softened in Ch 44, and it is softened here too.
8. **Ch 47 overstated the 1touch outcome.** It called 1touch "the template … that avoided most of these traps" and counted it as evidence that metadata buys "did better". The deal closed in May 2026, so both statements now say it is too early to judge. The red-flag caption also left Row 1 (ARR reconciliation) off its list of gating rows, although Figure 47.6 gates on it. It now lists rows 1, 7, 16 and 17.

## Change log

| File | Issue | Fix | Source |
|---|---|---|---|
| ch00-1 | "every major data platform bought or built a Postgres service" | Named Databricks, Snowflake and the hyperscalers | ma_deals.csv |
| ch00-1 | "Agents are now the biggest new consumers" (unsupported) | "a fast-growing new consumer (no vendor yet discloses how large a share)" | Consistency with Part 6 fix in Ch 44 |
| ch00-1 | "143 curated deals" but the CSV now has 146 rows | 146 rows: 143 from 2010 (Ch 39's set) plus three 2007 BI deals | ma_deals.csv (recomputed: 143 rows ≥2010 reproduce Ch 39's 74 valued / 55 disclosed / $825M median) |
| ch00-2 TL;DR | "DuckLabs to AWS" implied a completed deal | "AWS signed an agreement to buy DuckLabs" | verified-facts #13 |
| ch00-2 table L3 | Varonis "~$6.3B (pending)" | ~$6.3B transaction value, ~$5.71B equity value, close expected 1H 2027 | verified-facts #14 |
| ch00-2 table L4 | Supabase $10.65B unqualified | Single source; $10.5B Jun 2026 Series F noted | private_funding.csv (row flagged [VERIFY]) |
| ch00-2 table L5 | Dremio and DuckLabs status | "(closed)" / "(agreement, not yet closed)" | ma_deals.csv |
| ch00-2 layer 3 text | Varonis basis | Transaction value / equity value / close timing | verified-facts #14 |
| ch00-2 layer 4 text | Supabase figure; agents-create-most-databases stated as fact | $10.5B with $10.65B caveat; thesis attributed to Neon's company-stated >80% | private_funding.csv; Ch 22 / Ch 50 |
| ch00-2 layer 5 text | Teradata "1.7x EV/NTM" | "EV/revenue (a trailing-revenue proxy)" | public_comps.csv (TTM proxy) |
| ch00-2 numbers table | Varonis basis; deal window "Jun 2025" | Basis added; window Mar 2025–Oct 2026 (Moveworks announced 2025-03-10) | ma_deals.csv |
| ch00-market-map.svg | DuckLabs and Dagster chips showed no deal status (Varonis did) | "→ AWS (agreed)", "→ Prefect (pending)"; widths recomputed; Starburst moved to row 2 of layer 5 | verified-facts #13; ma_deals.csv |
| ch46 | Snowflake S3 list wording | Aligned to verified-facts #21 | verified-facts #21 |
| ch46 | "Private offers now carry fees of 1.5–3%" (not tied to a marketplace) | Tied to AWS Marketplace, by contract size | AWS fee page (footnote) |
| ch47 TL;DR | 1touch called "the template that avoided most traps" | Recent example; too early to judge | 10-Q closing date 2026-05-07 |
| ch47 §8 | 1touch cited as evidence that metadata buys did better | "1touch … too recent to judge" | Same |
| ch47 KPI table | Rule of 40 and RPO/cRPO missing | Two rows added: definitions, Snowflake ~58 (35% + 23%) and RPO ~$9.0B / ~54% within 12 months, traps; new `[^r40]` footnote; key terms added | ch36_rule_of_40.csv; company_financials.csv |
| ch47 Fig 47.5 caption | Gating rows omitted Row 1 | Rows 1, 7, 16, 17 (matches Fig 47.6) | Internal consistency |
| ch48 H1 | "150 Questions" vs 154 in the bank | "154 Questions" | Tag tally script |
| ch48 Q139 | Snowflake list wording | Aligned to verified-facts #21 | verified-facts #21 |
| ch49 #2 | "NAND overwrite" (NAND cannot overwrite in place) | Update-in-place file system vs out-of-place FTL with GC | Settled storage knowledge |
| ch49 #33 | Varonis basis incomplete | Transaction + equity value, close 1H 2027 | verified-facts #14 |
| ch49 #46 | "every data vendor now ships one" (MCP) | "most major data vendors" | Oversimplification |
| ch49 #54 | NRR "net of expansion" (wrong: NRR includes expansion); cited the 158% FY2023 figure, not the 178% FY2022 peak | "including expansion, net of contraction and churn"; 178% peak added; footnote updated | company_financials.csv |
| ch49 #55 | RPO decline causal story | Seasonality stated; cRPO ~54% | company_financials.csv |
| ch49 #58, #70 | Palantir 53x basis | "FY2026 guidance basis; ~70x EV/TTM" | public_comps.csv |
| ch49 #65 | "most of that growth was AI compute, not BigQuery" stated as fact | "probably … BigQuery's share is not disclosed" | Ch 28 |
| ch49 #71 | Options said to be in Ch 24 and Ch 33 | Ch 45 (link added) | Ch 45 |
| ch50 Q16 | "Replication is harder" stated flatly | Consistency of replicas named as the hard part; cross-shard transactions noted | Settled distributed-systems knowledge |
| ch50 Q171 | "70x on trailing revenue" | "70x EV/TTM"; 53x tied to public_comps.csv | Sweep item 1 |
| ch50 Q178, Q197, deal poster | Varonis multiple basis | ~8.5x on transaction value, ~7.7x on equity value | Ch 37 / Ch 33 |
| ch50 Q190 | RPO decline causal story | Seasonality + cRPO | company_financials.csv |
| ch50 Q204 | "growth explains most of the gap" contradicts Ch 38 / Ch 37 | Rewritten to Ch 38's finding (~1 of ~8 turns) | Ch 38, Ch 37 |
| ch50 Q233 | "Fivetran bought Census" | "agreed to buy … closing not separately confirmed" | ma_deals.csv |
| ch50 Q240 + one-pager | Everpure–Snowflake relationship not aligned with #21 | Rewritten per #21; `[^pure-sf]` added; one [VERIFY] on FlashBlade's current status | verified-facts #21 |
| ch50 Q251 + deal poster | Portworx `[VERIFY]` / "flags for re-check" | Resolved: announced 2020-09-16, ~$370M disclosed | verified-facts #22 |
| ch50 market-map poster | "the eight layers the atlas uses" vs nine in Ch 0.2 | Said to compress the nine-layer map (catalogs with formats, operational DBs with engines) | Ch 0.2 |
| ch50 `[^ma]` / `[^sf-s3compat]` | Row count; #21 detail | 146 rows noted; #21 summary added | ma_deals.csv; verified-facts #21 |
| **Sweep:** ch31 TL;DR, comparison table | Unlabelled Palantir 70x | "~70x EV/TTM (~53x EV/NTM, FY2026 guide)" | Sweep item 1; public_comps.csv |
| **Sweep:** ch34 TL;DR | "70x trailing revenue" (no EV) | "70x EV/TTM revenue (~53x EV/NTM …)" | Same |
| **Sweep:** ch34 timeline | "later Data Cloud" (current name not given) | "later Data Cloud (now Data 360)" | verified-facts #11 |
| **Sweep:** glossary "Data Cloud" | "reportedly renamed Data 360" | Renamed at Dreamforce 2025 (Oct 2025); use Data 360 | verified-facts #11 |
| **Sweep:** ch26, ch27 timelines | "Snowflake Intelligence" without new name | "(now CoWork)" | verified-facts #15 |
| **Sweep:** ch25 bull case, ch27 bull case | "~50% at $4B … >80% at $7B" with no run-rate label | "at a $4B / $7B revenue run-rate (company-stated)" | Sweep item 9; verified-facts #8 |
| **Sweep:** ch30 timeline + body | "Fivetran buys Census"; "It bought Census" | "agrees to buy"; "agreed to buy … closing not separately confirmed" | Sweep item 6 |
| **Sweep:** ch39 consolidation para | "Fivetran bought … reverse ETL (Census)" | "agreed to buy … (closing not separately confirmed)" | Same |
| **Sweep:** ch43 Don't-say | "Census, inside Fivetran" | "Census, which Fivetran agreed to buy; closing not separately confirmed" | Same |
| **Sweep:** ch39 master table | Varonis "~$6.3B headline" | "~$6.3B transaction value; ~$5.71B equity value" | Sweep item 7 |
| **Sweep:** ch27 TL;DR, comparison row 17, "Where Everpure stands", `[^sf-s3compat]` | "Pre-2025 recollection", "validated", three broad [VERIFY]s | Aligned to #21; one narrowed [VERIFY]; `[^pure-sf]` added | Sweep item 8 |
| **Sweep:** ch40 TL;DR, rung 1–2 para, footnote | "Everpure appears on Snowflake's list"; no "tested and compliant" wording | Aligned to #21; [VERIFY] on FlashBlade's current status | Sweep item 8 |

## Sweep results by item

1. **Palantir multiple.** Fixed in Ch 31 (2 places), Ch 34 (TL;DR), Ch 49 (2) and Ch 50 (Q171). Ch 25, 26, 37 and 44 and the Ch 31 body were already labelled EV/TTM or FY2026-guide NTM. No "70x NTM" remains. Ch 31's Don't-say line explicitly corrects "70x forward revenue".
2. **MongoDB CEO.** Clean. Ch 29 and Ch 50 Q163 present Ittycheria as interim CEO since Sept 2026. No chapter presents Desai as current CEO.
3. **Everpure ticker.** Clean. Every PSTG mention is "formerly PSTG", "from PSTG to P" or an EDGAR filename.
4. **Snowflake renames.** Current-tense uses already say CoWork and CoCo. Two historical timeline entries (Ch 26, Ch 27) now carry "(now CoWork)".
5. **Data 360.** Current-tense uses are correct. One historical timeline (Ch 34) and the glossary entry are fixed. Remaining "Data Cloud" strings are source titles in footnotes or the historical FY2025 KPI name "Data Cloud and AI ARR", which is left as is.
6. **Fivetran–Census.** Four files fixed (Ch 30, 39, 43, 50). Ch 9, 10, 12, 43 (elsewhere) and 49 already said "agreed".
7. **Varonis.** Ch 00-2, 39, 49 and 50 fixed. Ch 15, 33, 37, 44 and 45 were already correct.
8. **S3-compatible list.** Ch 27, 40 and 50 aligned to #21, and Ch 46 and 48 too. Ch 45 already matched. Ch 24 ("self-certify") and Ch 26 (with its own [VERIFY]s on external-volume GA) are consistent and were left alone.
9. **Databricks figures.** $190B is always labelled a post-money valuation. ">$7B" always carries "run-rate", except two bull-case lines (Ch 25, Ch 27), now fixed. No chapter calls it revenue or ARR except in Don't-say corrections. The $188B figure appears only as the July 2026 term sheet in `private_funding.csv`. The "$188.6B" hits belong to Salesforce's market cap.

## Disagreements and items for the integrator

- **Everpure fiscal-year definition in `public_comps.csv`.** The row says "Sunday nearest Jan 31 (early Feb)". The chapters (Ch 00-1, Ch 50) say "Sunday nearest February 1". That matches the reported period ends (FY2026 ended 2026-02-01; FY2025 on 2025-02-02). A "Sunday nearest Jan 31" rule would put some year-ends in late January. I did not stage a correction because the field is descriptive; the integrator may want to align the CSV wording.
- **Snowflake ">$2B AWS Marketplace sales in calendar 2025" (Ch 40, Ch 47, Ch 50).** The source release is dated 2025-12-03, so it cannot cover the full calendar year. The phrasing is consistent across the atlas, so I left it. A safer wording would be "more than $2B in 2025 (to early December)".
- **SVG chip borders for "A → B" chips.** All arrow chips are solid, which the legend reads as "public company or product of one". Tabular → Databricks and Neon → Databricks are now products of a *private* company, and DuckLabs and Dagster are still private pending close. This is a minor legend inconsistency. I did not restyle the chips.
- **`ma_deals.csv` Informatica rationale** says "under Data Cloud/Agentforce". It is a CSV text field, not a chapter. Consider changing it to Data 360 at the next merge.
- **Ch 50 Q242** quotes Everpure Subscription ARR "+20%". `company_financials.csv` has the $2.1B level but no growth rate. It is left as is, since it comes from Ch 45.

## Remaining high-risk [VERIFY] items (in scope)

- FlashBlade's status under Snowflake's newer "tested and compliant" wording: Ch 27, Ch 40 and Ch 50 (Q240 and the one-pager). This is the most relevant open item for an Everpure reader.
- The Scale Venture Partners magic-number post date (Ch 47 `[^scale]`).
- Supabase $10.65B (single source, `private_funding.csv`). Where it is quoted, Ch 00-2 now gives the $10.5B confirmed round.
