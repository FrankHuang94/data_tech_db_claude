# Independent review: Part 6 (History and Future)

**Reviewer:** independent Phase 2 reviewer (principal data-platform engineer and buy-side software analyst lens) · **Date:** 2026-11-01
**Scope:** `docs/06-history-and-future/` ch42–ch45, all read in full including footnotes, plus the SVG `docs/assets/diagrams/ch45-storage-data-ai-stack.svg`.
**Sources of truth used:** `meta/verified-facts.md` (items 10, 14, 20), `data/company_financials.csv`, `data/public_comps.csv`, `data/ma_deals.csv`, integrator notes in `meta/research-briefing.md` (section A plus the bottom-of-file notes), Ch 40 footnotes, and the reviewer's own knowledge for settled pre-2025 history only. No web access.

## Summary

- **Chapters reviewed:** 4 (ch42, ch43, ch44, ch45) and 1 SVG.
- **Fixes:** 47 issues fixed through about 55 text edits. Of these, 24 `[VERIFY]` markers were resolved from settled pre-2025 knowledge: 21 in ch42, 1 in ch44 and 2 in ch45. One trivial SVG text edit. 3 new M&A rows staged in `data/staging/review-part-6-ma_deals.csv`.
- **Post-edit QA:** `scripts/qa_report.py` OK on all four chapters. `scripts/lint_mermaid.sh` found 0 failures across 12 blocks; one Mermaid timeline in ch42 was edited. `scripts/check_links.py` found no broken links in Part 6. Word counts after review: ch42 4,723 (budget 3,000), ch43 2,296 (2,000), ch44 4,325 (3,000), ch45 2,765 (2,000).
- **SVG:** parses as well-formed XML. It has `<title>` and `<desc>` and a 1000×700 viewBox. A text-width check with Arial-metric fonts (Liberation Sans) found no text overflowing its box. Its labels match the chapter: layers 1/2/3/6 solid and 4/5/7 dashed; 1touch at $125.0M, closed May 2026; OpenSharing connector in private preview (Jun 2026); Databricks Storage Ecosystem launch partner; Portworx 2020; Snowflake CoWork and Gemini Enterprise named correctly.

## Most serious issues

1. **Spark/AMPLab dating (ch42).** The chapter said Spark "began in 2009 at UC Berkeley's AMPLab", and the timeline said "open-sourced from AMPLab" (2010). AMPLab opened in 2011. Spark began in 2009 in its predecessor, the RAD Lab. **Fixed** in the text and in the Mermaid timeline.
2. **Internal inconsistency in a forecast (ch44, T8).** The call said a Databricks IPO by end-2028 was "Medium" likelihood. The chapter's own scenario table puts ~25% on Bull and ~50% on Base, and both list by 2028. That is ≥75%, which is "High" on the chapter's own scale (≥70%). **Fixed:** the call and the Who's-who row now state ~75% (High, low end). I did not change the author's scenario probabilities. Also added the missing *Signposts* line to T8, and a falsifier to the one contrarian call that lacked one (cloud-warehouse repatriation).
3. **Unsupported claim (ch44 TL;DR).** "Agents are already the biggest new writers of SQL" had no evidence; the only evidence is Neon's agent-created databases share. **Softened** to "becoming a major new writer of SQL (estimate; no vendor yet discloses the share)."
4. **Deal status overstated (ch43).** Ch43 said in five places (TL;DR, Act 4, timeline, Who's who and Don't-say) that Fivetran "bought" Census. `ma_deals.csv` marks the deal *announced*, closing not verified. This is the same issue the Part 2 reviewer fixed elsewhere. **Fixed** to "agreed to buy".
5. **Arithmetic in captions (ch43).** Fig 43.2 said the 2021 funding peak fell "almost exactly halfway" between 2012 and the 2025–26 merger wave; it falls about two-thirds of the way. Fig 43.6 said platforms are "one to two orders of magnitude" larger than Fivetran–dbt. The ratio is about 8x (Snowflake FY2026 GAAP revenue) to 12x (Databricks run-rate), i.e. about one order of magnitude. **Fixed**, and the mixed bases are now flagged.
6. **Deal-value basis (ch44, ch45).** Varonis was shown as "$6.3B" with no basis. **Fixed** to "~$6.3B transaction value; ~$5.71B equity value; pending (close expected 1H 2027)" per verified-facts #14. Cyera is now labelled as a private-round mark and Securiti as disclosed.
7. **Everpure partner record incomplete (ch45).** Ch45 said nothing about the Snowflake side. Ch40 and the integrator note record that Pure Storage is on Snowflake's *self-reported* S3-compatibility list (Snowflake does not certify), that the two announced a joint on-prem solution in May 2022, and that no current certification was found. **Added** one sentence with two footnotes copied from Ch 40, so the chapters agree.

## Change log

| Chapter | Issue | Fix | Source |
|---|---|---|---|
| ch42 | Spark "began at AMPLab" (2009); timeline "open-sourced from AMPLab" | Began in RAD Lab 2009; AMPLab opened 2011; timeline "open-sourced at UC Berkeley" | Settled history (Zaharia et al. NSDI 2012 footnote; AMPLab founding 2011) |
| ch42 | `[VERIFY: IDMS commercial release year]`; CODASYL "around 1969–71" | DBTG reports 1969 and 1971; IDMS built at B.F. Goodrich, sold by Cullinane from 1973 | Settled history |
| ch42 | IMS "IBM shipped the first release in 1968" (imprecise) | Built from 1966 with Rockwell (and Caterpillar); live at Rockwell 1968; product IMS/360 in 1969; footnote VERIFY narrowed to URL only | Settled history; `[^ims]` |
| ch42 | `[VERIFY: IMS pricing history after unbundling]` ("monthly license") | Reworded to June 1969 unbundling, separately priced "program product" license | Settled history |
| ch42 | `[VERIFY: Sybase–Microsoft license and split]` | 1988 license (with Ashton-Tate) for OS/2; SQL Server 1.0 1989; split 1993–94; SQL Server 6.0 (1995) first Microsoft-only release | Settled history |
| ch42 | `[VERIFY: DBC/1012 first shipment]` (text + footnote) | Released 1984 after 1983 Wells Fargo beta | Settled company history; `[^teradata-10k]` |
| ch42 | `[VERIFY: OLAP paper sponsorship and title]` | Title stated; Arbor commissioned it; sponsorship criticism noted; URL VERIFY kept | Settled history; `[^olap]` |
| ch42 | `[VERIFY: individual deal values]` 2007 BI deals | Oracle–Hyperion ~$3.3B, SAP–Business Objects ~€4.8B (~$6.8B), IBM–Cognos ~$5B; new footnote `[^bi-2007]`; rows staged | Company announcements (settled public record) |
| ch42 | `[VERIFY: Redis first public release, 2009]` | Resolved (2009, Sanfilippo) | Settled project history |
| ch42 | Redis licensing incomplete | Added Redis 8 (2025) AGPL option | Settled (May 2025, pre-cutoff) |
| ch42 | `[VERIFY: Aslett 451 Group coinage]` | Resolved; new footnote `[^newsql]` (Pavlo & Aslett, SIGMOD Record 2016) | Canonical paper |
| ch42 | `[VERIFY]` Intel–Cloudera amount/stake; `[VERIFY: IPO dates]` | Mar 2014, ~$740M for ~18% (press-reported); Hortonworks Dec 2014, Cloudera Apr 2017; new footnote `[^hadoop-capital]` | Settled public record |
| ch42 | BigQuery "GA around 2011–12" (vague) | Limited preview May 2010; opened to all 2011–12, with the Nov 2011 vs May 2012 ambiguity stated | Settled history (see disagreements) |
| ch42 | Redshift GA missing | Added GA February 2013 | Settled history |
| ch42 | Snowflake founding/GA | Founded 2012; out of stealth Oct 2014; GA June 2015 | Settled; SIGMOD 2016 footnote |
| ch42 | "The format war ended in 2024" (overstated) | "Largely de-escalated"; Delta and Hudi still in production | Reviewer judgment |
| ch42 | `[VERIFY: SQL standard part and year]` | Resolved: SQL:1999 structured types; SQL:2003 Part 14 SQL/XML; SQL:2016 JSON; SQL:2023 Part 16 SQL/PGQ; GQL 2024 | Settled standards history; `[^gql]` |
| ch42 | Numbers table: Cloudera take-private `[VERIFY]`; Snowflake IPO `[VERIFY]` | Announced 2021-06-01, closed Oct 2021; priced 2020-09-15, traded 2020-09-16 | Settled public record |
| ch42 | Footnote VERIFYs: Cassandra month, Hadoop dates, ma-cloudera, sf-ipo, Neon wording, pgvector 2021, Fivetran–dbt close date | Resolved (July 2008; 2006/Jan 2008; terms; $120/28M shares; "over 80%"; April 2021; 2026-06-01 per Ch 43 footnote) | Settled history; Ch 43 `[^merger-close]` |
| ch43 | "Fivetran bought Census" (×5) | "Agreed to buy … closing not separately confirmed" | `ma_deals.csv` (status = announced) |
| ch43 | Fig 43.2 "funding peak almost exactly halfway" | ~13 years, peak about two-thirds through | Arithmetic |
| ch43 | Fig 43.6 "one to two orders of magnitude" | ~8–12x, about one order; bases flagged | `company_financials.csv`; verified-facts #8 |
| ch44 | TL;DR "agents already the biggest new writers of SQL" | Softened, labelled estimate | No supporting disclosure |
| ch44 | TL;DR OpenSharing connector status missing | "(private preview)" | Integrator note; `[^everpure-os]` |
| ch44 | "In five years the infrastructure layer has gained…" (reads as forecast) | "Over the past five years" | Clarity |
| ch44 | `[VERIFY: Data Act dates against EUR-Lex]` | Resolved: switching charges zero from 2027-01-12; applies from 2025-09-12; footnote now cites Reg. (EU) 2023/2854 Arts 29, 50 | Settled law (2023) |
| ch44 | Varonis / Cyera / Securiti / 1touch values unlabelled | Basis labels added (transaction vs equity, private round, disclosed, GAAP) | verified-facts #14; `ma_deals.csv` |
| ch44 | "Models are commodities" (overstated) | "For this task, frontier models are increasingly interchangeable" | Balance |
| ch44 | T8 IPO likelihood "Medium" contradicts Fig 44.4 (≥75%) | Call and Who's-who row aligned to ~75% (High, low end) | Chapter's own scenario table |
| ch44 | T8 call lacked Signposts | Added (S-1, strategic bids, antitrust review) | Template consistency |
| ch44 | T9 Palantir "near 70x" without basis | "EV/TTM revenue" | `public_comps.csv` note |
| ch44 | "Assembly outlived the people who wrote it by hand" (inaccurate) | Machine-code/compiler analogy | Accuracy |
| ch44 | Repatriation contrarian call had no falsifier | Falsifier added | Forecast discipline |
| ch45 | "chose its name to signal the move" (motive attribution) | "presented its new name as a signal" | Public-information framing |
| ch45 | Snowflake relationship missing; inconsistent with Ch 40 | Added the self-reported S3-compatibility listing, the May 2022 joint solution and "no current certification found"; `[^sf-s3compat]`, `[^pure-sf]` | Ch 40 footnotes; integrator note (Part 3 cont.) |
| ch45 | Rubrik–Laminar date vague | "August 2023, terms undisclosed" (primary-release VERIFY kept) | `ma_deals.csv` |
| ch45 | Portworx `[VERIFY]` (table + `[^ma-csv]`) | Resolved: ~$370M cash, announced 2020-09-16 | Settled pre-2025 public record |
| ch45 | Varonis "$6.3B" (two tables) and DSPM price range | Transaction vs equity value; pending; "disclosed deal values" | verified-facts #14 |
| ch45 | DiskANN author "F. Devvrit" | "Devvrit" (single name) | NeurIPS 2019 paper |
| ch45 SVG | Hammerspace listed in layer 1 (media/arrays), contradicting chapter (software over others' storage, layer 3) | Removed from layer-1 line; remains in layer 3 | Chapter text, Who's-who table |

**Checked and found correct (no change):** Codd 1970; System R 1974–79 and Selinger 1979; Ingres from 1973; Oracle (SDL 1977, Oracle V2 1979); SQL/DS 1981, DB2 1983; ANSI 1986 / ISO 1987; Teradata 1979; Inmon 1992 / Kimball 1996; GFS 2003, MapReduce 2004, Bigtable 2006, Dynamo 2007; Hadoop 2006, Apache TLP 2008; Cloudera 2008 / MapR 2009 / Hortonworks 2011; Cloudera–Hortonworks $5.2B (Oct 2018 / Jan 2019); Spark ASF 2013 / TLP Feb 2014; Databricks 2013; Redshift Nov 2012 and ParAccel; RA3 Dec 2019; Snowflake IPO $120 / ~$3.4B; Iceberg (Netflix, Apache 2018); Delta open-sourced 2019; Lakehouse CIDR 2021; Tabular 2024; Postgres JSONB 9.4 (2014); Spanner 2012; MongoDB 4.0 transactions; S3 consistency (Dec 2020), conditional writes (Aug/Nov 2024), Express One Zone (Nov 2023), S3 Tables (Dec 2024); KV-cache arithmetic (2×80×8×128×2 B ≈ 0.33 MB/token); DiskANN figures. Everpure facts all match the registers: rename 2026-02-23; ticker P effective 2026-04-17; 1touch $125.0M cash, closed 2026-05-07; Databricks Storage Ecosystem launch partner 2026-06-10; Q2 FY2027 ~$1.19B (+38%), product $687M, subscription services $499M, GAAP GM 68.4% / non-GAAP 69.9%; FY2027 guide $5.03–5.07B; market data from `public_comps.csv`.

## Forecast discipline (ch44): assessment

Each of T1–T10 has a thesis, dated evidence, mechanism, likelihood (on a defined scale: High ≥70%, Medium 40–70%, Low <40%), timing window (near/mid/long), winners, losers, signposts (T8's are now added), a falsifier and an Everpure implication. All placements and probabilities are labelled author estimates. Vendor benchmarks (NVIDIA, dbt, data.world, Cloudera survey) are labelled vendor-run or vendor-commissioned. All four contrarian calls now carry falsifiers. The one internal contradiction (T8) is fixed. The tone is balanced: every trend has a steelmanned counter-thesis in Fig 44.6.

## Public-information framing (ch45): assessment

The chapter states the framing in the "Why this matters" section, before the options matrix and in captions ("options a strategy team might evaluate, based on public information … does not describe Everpure plans"). No speculation about non-public Everpure plans was found. One motive attribution was reworded. The options matrix uses option language ("OpenSharing connector to GA" and "Small catalog team only if integration stalls" are options, not reported plans). Questions in the playbook are written for internal colleagues, which is acceptable for a new joiner.

## Disagreements and items for the integrator

1. **Stale bullet in `meta/research-briefing.md` section A.** It still says shares trade "keeping the NYSE: PSTG ticker". The integrator correction at the top supersedes it, and Part 6 correctly uses P. Recommend deleting the stale bullet so it does not reintroduce PSTG.
2. **verified-facts #20 basis.** It gives "total gross margin 69.9%" with no basis. `company_financials.csv` labels 69.9% non-GAAP and 68.4% GAAP, and ch45 follows the CSV. Recommend adding the label in verified-facts.
3. **BigQuery GA date.** Accounts differ: the Nov 2011 wider opening and the May 2012 "available to all developers" milestone are both cited. I left "2011–12" and stated the ambiguity rather than pick one from memory. The integrator may standardise atlas-wide (check Ch 5 and Ch 28).
4. **T8 likelihood.** I aligned the label to the scenario table. If the author's real view is "Medium", the alternative fix is to move ~10–15 points from Base to Bear in Fig 44.4. That is the integrator's call.
5. **SVG edit.** It is outside chapter prose, but it is the ch45 figure under review. One line was changed (Hammerspace removed from layer 1). The file is still well-formed.
6. **CSV.** Staged three 2007 BI deals (Hyperion, Business Objects, Cognos) as NEW rows, since ch42 cites them and `ma_deals.csv` lacks them. The Portworx and Cloudera take-private rows cite "training knowledge [VERIFY]" in their source column. Their values are correct, so no correction row was staged, but the integrator may want to replace those sources with the company releases.

## Remaining high-risk `[VERIFY]` items

- **ch45:** "Modern Data Software" TAM $22B by FY2030 (second-hand NAND Research summary of the 2026-09-23 analyst meeting; confirm on the deck). OpenSharing connector GA status. KVA–Dynamo GA date. Rubrik–Laminar primary release. Peer product details resting on training knowledge (VAST, WEKA, DDN, Hammerspace, Cohesity/Rubrik AI features). Semiconductor-bridge primary announcements (low risk).
- **ch44:** Managed MCP server GA at Snowflake and Databricks. Genie Ontology status (Preview vs GA). Agentforce current list prices (the 2024–25 historic prices are settled). Ghodsi IPO remark (secondary source only). SAP–Dremio closing date. MotherDuck and Reducto post dates.
- **ch43:** Census closing; Prefect–Dagster closing; date of the a16z 2022 update; Stancil essay URL; named MDS layoffs.
- **ch42 (low risk, URL or date only):** IBM Heritage, Oracle history, Inmon publisher, OLAP paper and Gartner/ASF URL paths; WGACA author-copy URL; MongoDB ARS date; Pinecone sale-report date.
