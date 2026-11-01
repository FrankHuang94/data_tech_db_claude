# Independent review — Part 2 (Pipelines, Movement and Governance)

**Reviewer:** independent Phase 2 reviewer (principal data-platform engineer + buy-side software analyst lens) · **Date:** 2026-11-01
**Scope:** `docs/02-pipelines-and-governance/` ch09–ch15 (all seven chapters read in full, including footnotes).
**Sources of truth used:** `meta/verified-facts.md` (items 1, 11, 14), `data/ma_deals.csv`, `data/private_funding.csv`, `data/public_comps.csv`, integrator notes in `meta/research-briefing.md` (sections E, F and the Part 2 note), and the reviewer's own knowledge for settled pre-2025 facts only. No web access.

## Summary

- **Chapters reviewed:** 7 (ch09, ch10, ch11, ch12, ch13, ch14, ch15).
- **Fixes made:** 49 text edits addressing the 38 issues in the change log, plus 2 staged CSV correction rows.
- **Post-edit QA:** `scripts/qa_report.py` OK on all seven; `scripts/lint_mermaid.sh` 0 failures (29 blocks). No Mermaid was edited. Word counts all rose slightly and stay well above budget (ch09 3,503 / 2,000; ch10 2,758 / 1,900; ch11 3,681 / 2,200; ch12 3,319 / 1,900; ch13 3,448 / 1,800; ch14 2,900 / 2,000; ch15 4,434 / 2,200).
- **Overall:** Part 2 is in good shape. The worked arithmetic I re-checked line by line is all correct: Fivetran MAR tiers including the 1B-MAR figure of ~$5,619/month, the Airbyte self-host cost, the 1 GB/s cross-AZ bill ($172,800 / $138,240 / $34,560), the S3 request math (~$579) and the IBM–Confluent ~9.4x EV/FY2025 revenue. Deal statuses mostly match the CSVs. The main problems were: wording on deal status and ARR that ran ahead of the sources (Census, Prefect–Dagster, "~$600M"), some stale product names (Data Cloud, Delta Live Tables), multiples with no basis label (Varonis), and a few Kafka-semantics points that were oversimplified.

## Most serious issues

1. **Varonis multiple and value basis (ch15).** The chapter used $6.3B as the deal value without saying it is the *transaction* value, it never gave the ~$5.71B equity value, and in places it did not say the deal is still pending. It also called Cyera's ~80x a price that "buyers" pay, when that figure comes from a private funding round and Cyera disputes it. **Fixed:** both bases now shown (~8.5x on transaction value, ~7.7x on equity value, both against the CY2026 guide midpoint), "pending, close expected 1H 2027" added throughout, and the caption rewritten.
2. **Deal status overstated.** Ch09, ch10 and ch12 said Fivetran "bought", "added" or "absorbed" Census, but `ma_deals.csv` marks the deal *announced* with closing not verified. Ch12 also listed Prefect–Dagster among completed mergers, although it is only announced. **Fixed** to "agreed to buy" or "pending".
3. **Fivetran–dbt ARR.** The text said "~$600M" in ch09 (twice), "about $0.6B" in the ch10 caption, and called the transformation layer "a roughly half-billion-dollar ARR franchise" in the ch12 caption. That last claim is wrong: the combined figure includes Fivetran ingestion, while dbt alone was >$100M ARR in early 2025. **Fixed** to "approaching $600M" (company-stated, at close), with dbt's share stated separately.
4. **Largest-deal claim (ch09).** The chapter named IBM–Confluent and Fivetran–dbt as "the two largest recent deals" in the layer and left out Salesforce–Informatica (~$8B equity value, closed 2025-11-18). That deal is larger than Fivetran–dbt, whose terms were undisclosed. **Fixed.**
5. **Kafka semantics oversimplified (ch11).** Three gaps: `acks=all` without the `min.insync.replicas` caveat; the idempotent producer described without its per-session scope or `transactional.id` epoch fencing (and without the fact that idempotence is on by default since Kafka 3.0); and an object-storage cost sketch that left out compaction and metadata request traffic. **Fixed**, one clause each. Also fixed the Figure 11.4 caption: removing replication alone still leaves about $69K a month, so only removing *all* cross-AZ copying changes the order of magnitude.
6. **Cross-chapter inconsistency on Spark real-time mode latency.** Ch09 said p99 ~40–300 ms; ch11 said single-digit ms. Both are vendor claims for different workloads. **Reconciled** in both tables, with cross-links.
7. **AI Act timeline precision (ch15 TL;DR).** The TL;DR said high-risk duties start in "December 2027" without saying which category. **Fixed:** Annex III (standalone) from 2 Dec 2027 and Annex I (product-embedded) from 2 Aug 2028, citing Regulation (EU) 2026/1744. This now matches the body text, the timeline and research-briefing section F.

## Change log

| Chapter | Issue | Fix | Source |
|---|---|---|---|
| ch09 | "Two largest recent deals" left out Salesforce–Informatica (~$8B) | Added Informatica; Fivetran–dbt marked "terms undisclosed"; "All three were bets…" | `ma_deals.csv` (2025-05-27 row); research-briefing §E |
| ch09 | "~$600M combined ARR" (TL;DR-adjacent para + Numbers table) | "Approaching $600M", company-stated at close | research-briefing integrator note (4); §E |
| ch09 | Latency table listed "Delta Live Tables" as a current tool | "Lakeflow Spark Declarative Pipelines (formerly Delta Live Tables)" | research-briefing integrator note (2) |
| ch09 | Debezium exactly-once had no context | Added Kafka Connect exactly-once source framework (KIP-618, Kafka 3.3, 2022) | Reviewer knowledge (settled pre-2025) |
| ch09 | "Salesforce Data Cloud" (zero-ETL list, Who's who table) | Data 360 (renamed Oct 2025); footnote note added | verified-facts #11 |
| ch09 | Fig 9.6 caption "roughly 100x" understates the 4–28 h → 1–5 min change | "two to three orders of magnitude" | Arithmetic from the chapter's own table |
| ch09 | "Fivetran (Census)" and "Fivetran absorbed … Census" | "Census, agreed 2025"; "agreed to buy Census"; Salesforce–Informatica added to the consolidation sentence | `ma_deals.csv` (Census status = announced) |
| ch09 | Spark RTM latency inconsistent with ch11 | Both claims shown, labelled workload-dependent, cross-linked | ch09/ch11 footnotes (vendor) |
| ch09 | `[^ma-csv]` footnote missing Informatica row and Census status | Added | `ma_deals.csv` |
| ch10 | Airbyte ELv2 called open source ("Yes (ELv2)", "Free software") | "Source-available (ELv2; some connectors MIT), not OSI open source" | Chapter's own `[^ab-license]`; ELv2 is not OSI-approved |
| ch10 | `Talend Open Studio retired [VERIFY]` | Resolved: retired 2024-01-31; footnote note added | Reviewer knowledge (settled pre-2025) |
| ch10 | "Fivetran added Census…" / timeline "Fivetran buys Census" | "Agreed to buy Census … buys Tobiko" | `ma_deals.csv` |
| ch10 | Fig 10.8 caption "about $0.6B of ARR" | "Approaching $0.6B (company-stated, June 2026)" | research-briefing §E |
| ch11 | `acks=all` durability overstated | Added `min.insync.replicas ≥ 2` caveat | Kafka design docs (settled) |
| ch11 | Idempotent producer scope | Added: default since 3.0; per-session only; `transactional.id` epoch fencing | KIP-98 / KIP-679 (settled) |
| ch11 | Tiered storage "under development from 3.6" | "Early access in Kafka 3.6 (Oct 2023)" | KIP-405 history (settled) |
| ch11 | Fig 11.4 caption implied removing replication alone changes the order of magnitude | Reworded: all cross-AZ copying | Chapter's own table |
| ch11 | S3 request sketch omitted compaction/metadata requests | Added to caveat 2 | Engineering judgment |
| ch11 | Spark RTM numbers row | Reconciled with ch09 | Vendor footnotes |
| ch11 | `[^cflt-10k]` said "via secondary summary; re-check" | Marked confirmed; Business Wire FY2025 release added | verified-facts #1 |
| ch12 | "dbt's 2025 license change" (dbt Core's licence did not change) | "Decision to ship Fusion under ELv2 and proprietary terms" | Chapter's own `[^fusion-lic]` |
| ch12 | SQLMesh "owner also owns dbt" (SQLMesh is now a Linux Foundation project) | "Main sponsor (Fivetran) also owns dbt" | Chapter's own `[^sqlmesh-lf]` |
| ch12 | Census in Fivetran portfolio stated as owned | "Agreed May 2025; closing not separately announced" | `ma_deals.csv` |
| ch12 | Prefect–Dagster listed as completed merger; "Both 2021-vintage valuations" (dbt's was 2022); one-sided conclusion that marks "were rich" | Pending status; 2021/2022 marks; bull and bear readings both given | `ma_deals.csv`; `private_funding.csv` |
| ch12 | Fig 12.7 "transformation layer is a ~half-billion ARR franchise" | Combined vendor approaching $0.6B ARR; dbt >$100M (early 2025) | research-briefing §E; `[^dbt-100m]` |
| ch13 | Observe "$596.2M" given as the price with no basis | "Preliminary consideration per FY2026 10-K vs ~$1B press-reported" | `ma_deals.csv` (2026-01-08 row) |
| ch13 | "Monte Carlo remains the largest independent" (unsupported) | "Best-funded independent", $1.6B May 2022, company-stated | `[^mc-d]` |
| ch13 | "2021-vintage valuations"; "$1.6B mark predates the downturn" (May 2022 does not) | "2021–22-vintage"; "set in May 2022, at the tail of the boom" | `[^mc-d]` |
| ch13 | `[VERIFY: GX project start year]` | Resolved (repository 2017; Feb 2018 "Down with Pipeline Debt" essay) | Reviewer knowledge (settled pre-2025) |
| ch14 | OSI framed as Snowflake-convened, Databricks' role absent from the "Why this matters" section | Databricks joined Jan 2026 (with Qlik, AtScale) added; counter-case paragraph balanced | research-briefing integrator note (3); `[^osi-v1]` |
| ch14 | "Tableau Semantics (on Salesforce Data Cloud)" | Data 360, formerly Data Cloud; footnote note | verified-facts #11 |
| ch14 | Snowflake semantic views "querying then in preview": status stale as of 2026-11 | Added `[VERIFY: query GA status in 2026]` | — |
| ch15 | Varonis value basis / pending status / multiple basis (TL;DR, Who's who, Positioning, Numbers, footnote) | Transaction value $6.3B vs equity ~$5.71B; 8.5x / 7.7x; pending, 1H 2027 | verified-facts #14; `public_comps.csv` |
| ch15 | Proofpoint "bought" Normalyze (completion unverified) | "Agreed to buy" | `ma_deals.csv` outcome note |
| ch15 | TL;DR AI Act: "December 2027" without category | Annex III 2027-12-02 / Annex I 2028-08-02, Reg. (EU) 2026/1744 | research-briefing §F |
| ch15 | Macie 1 PB ≈ $1M treated as the estimate; tiers unknown | Kept $1M flat-rate figure; added pre-2025 tiered estimate (~$0.4M) with `[VERIFY]` retained | Reviewer knowledge of pre-2025 Macie list (flagged) |
| ch15 | Natoma price lacked consideration type and status | "Mostly in stock; announced May 2026; closing not verified" | `ma_deals.csv` (2026-05-24 row) |
| ch15 | Fig 15.8 caption "buyers paying 8–80x revenue" mixed an M&A mark with a disputed private-round mark | Rewritten to separate the two bases | `[^cyera-g]`; verified-facts #14 |

**Staged CSV corrections** (marked CORRECTION):
- `data/staging/review-part-2-ma_deals.csv`: Fivetran–dbt Labs rationale "~$600M" → "approaching $600M".
- `data/staging/review-part-2-private_funding.csv`: dbt Labs Series D note, same wording fix.

## Checked and found correct (no change)

These items were checked against the sources of truth or settled facts and needed no change:

- Kafka 0.11/KIP-98 (2017); KRaft and the Kafka 4.0 ZooKeeper removal (Mar 2025; 3.9 bridge); KIP-405 production-ready in 3.9; KIP-392 follower fetching; share groups (KIP-932) in 4.2.
- AWS pricing: cross-AZ $0.01/GB each way; S3 PUT $0.005 and GET $0.0004 per 1,000; MSK not billing inter-broker replication.
- Tableflow GA (2025-03-18); Redpanda Iceberg Topics GA (25.1); WarpStream $135.1M + $76.2M holdbacks; Immerok $54.9M.
- IBM–Confluent: $31/share, closed 2026-03-17, ~$11B. Confluent FY2025 revenue $1,166.7M and Cloud revenue $624M (verified-facts #1).
- Salesforce–Informatica: $25/share, closed 2025-11-18. FICO–GX Cloud (2026-05-06) and Fivetran–GX Core (2026-05-13). Datadog–Metaplane (2025-04-23). Boomi–Elementary (~$40–45M, press-reported). Veeam–Securiti ($1.725B, closed 2025-12-11). Everpure–1touch ($125.0M, closed 2026-05-07).
- Prefect–Dagster announced 2026-07-13; Temporal $5B → $12.55B; Hightouch, Sigma, Omni and Cyera rounds all match `private_funding.csv`.
- Fivetran tier table and every derived dollar figure; Power BI and Tableau list prices.
- data.world 16.7% → 54.2% benchmark result; Looker deal ($2.6B, 6 June 2019) and Tableau deal ($15.7B, four days later).
- GDPR: Art. 12 deadline, Art. 21 absolute right to object to direct marketing, Art. 83 caps, pseudonymised data still personal data.
- Regulatory dates: CCPA/CPRA; CPPA ADMT rules (1 Jan 2027); Schrems II; Latombe (2025-09-03); PIPL; DORA; Data Act (2025-09-12); AI Act entry into force and the 2025 GPAI dates.
- NIST SP 800-162 (2014); MTE 16-byte granules.

## Disagreements and calls for the integrator

1. **Census closing.** All three chapters now say "agreed / closing not separately announced". If the integrator has evidence that the deal closed, update `ma_deals.csv` status and the three chapters (ch09, ch10, ch12) together.
2. **Debezium 3.3 "exactly-once for core connectors" (ch09, ch11).** This is plausible and footnoted to the 3.3.0.Final release post, but I could not re-open it. I kept the claim. The KIP-618 context I added is settled.
3. **Macie tiers (ch15).** The $0.50/$0.25 tiers come from my pre-2025 knowledge and are flagged `[VERIFY]`. If current pricing is flat $1/GB, delete the tiered clause.
4. **"Kafka 4.2 share groups production-ready" (ch11).** This rests on the Kafka 4.2 announcement footnote (2026-02-17). I left it as is. "Queue semantics … were added only in Kafka 4.2" is fair if one reads "added" as "production-ready". Earlier preview releases existed (4.0 early access, 4.1 preview).
5. **Snowflake–Observe $596.2M.** The CSV and chapter attribute this to the FY2026 10-K (FY ended 2026-01-31), but the deal closed on 2026-02-02, after fiscal year-end. A subsequent-event disclosure in the 10-K is plausible. Even so, the integrator may want to confirm whether the figure comes from the 10-K or from the Q1 FY2027 10-Q.
6. **Talend Open Studio and GX start date.** I resolved both from settled pre-2025 knowledge, and both are noted as reviewer knowledge in the text or footnote. Revert if the integrator prefers only fetched sources.

## Remaining high-risk `[VERIFY]` items (not resolvable from sources 1–3)

- ch12: dbt Core v2 launch date and maturity, and the list of Fusion GA adapters. This is high-risk because it drives the licensing narrative.
- ch12 / ma_deals: Prefect–Dagster closing date.
- ch14: Databricks metric views GA date; Snowflake semantic-view query GA; the full 2026 Gartner ABI MQ Leaders list; Looker Conversational Analytics GA date; Sigma tiering.
- ch15: exact GA date for Unity Catalog ABAC (one docs page still showed Public Preview); Macie tiers; independent DSPM market size; IAPP state count; Veeam–Securiti announcement date; Rubrik–Laminar primary release.
- ch11: Redpanda Cloud Topics GA date; WarpStream Tableflow and AutoMQ table-topic status; Google Managed Kafka GA date.
- ch10: Matillion credit ratio; Informatica IPU blog dates; Azure Data Factory rates; Estuary $17M vs $14M; dlt seed date; EC2 m6i rate.
- ch13: original Gartner $12.9M wording; Monte Carlo five-pillars original date; Unity Catalog lineage gaps (sourced only to community posts); Sifflet round label.
