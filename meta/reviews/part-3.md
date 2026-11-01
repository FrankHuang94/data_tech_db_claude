# Independent review: Part 3, The AI Data Stack (Ch 16–24)

Reviewer pass, 2026-11-01. Sources used, in priority order: `meta/verified-facts.md`, `data/*.csv`, integrator notes at the bottom of `meta/research-briefing.md`, and settled pre-2025 knowledge (papers, launch dates). There was no web access. Claude list prices were also checked against Anthropic's model and pricing table cached 2026-10-06 (the `claude-api` reference available in this session), which matches the snapshot date the chapter cites.

## Chapters reviewed

| Ch | File | Prose words (budget) | Visuals | VERIFY after review | QA / Mermaid |
|---|---|---|---|---|---|
| 16 | ch16-ai-data-lifecycle.md | 3,660 (2,200) | 6 | 1 | OK / 0 failures |
| 17 | ch17-unstructured-data-processing.md | 3,160 (2,100) | 10 | 11 | OK / 0 failures |
| 18 | ch18-embeddings-and-vector-search.md | 4,467 (2,600) | 11 | 6 | OK / 0 failures |
| 19 | ch19-retrieval-architectures.md | 3,785 (2,200) | 11 | 6 | OK / 0 failures |
| 20 | ch20-training-data-supply-chain.md | 3,652 (2,200) | 8 | 20 | OK / 0 failures |
| 21 | ch21-ml-platforms-feature-stores-llmops.md | 3,436 (2,100) | 9 | 0 | OK / 0 failures |
| 22 | ch22-agents-and-data.md | 4,328 (2,400) | 10 | 4 | OK / 0 failures |
| 23 | ch23-real-time-analytics-htap.md | 3,366 (2,000) | 9 | 10 | OK / 0 failures |
| 24 | ch24-data-meets-compute-and-storage.md | 3,641 (2,200) | 11 | 3 | OK / 0 failures |

Every chapter is still well above its word budget, and all template headings, footnotes, captions and Mermaid blocks are intact. One Mermaid title was edited (Ch 22, Fig. 22.3) and re-linted.

## Overall assessment

Part 3 is in good shape. The arithmetic checks out: vector memory math, PQ 48x, the IVF probe fraction, RRF scores, long-context cost per query, KV-cache size, the S3 small-file and egress examples, the ClickHouse granule count, and the agent-loop and cost-per-query examples. Deal figures match `data/ma_deals.csv` and `data/private_funding.csv`:

- Meta–Scale: $14.3B for 49%, non-voting, about $29B implied, press-reported.
- ClickHouse: $15B, press-reported per the CSV; >$250M ARR, company-stated.
- OpenAI–Rockset: closed June 2024; customers off-boarded by 2024-09-30.
- AWS–DuckLabs: announced around 2026-08-26, terms undisclosed, DuckDB stays MIT.
- Crunchy Data: $164.5M per the 10-Q, versus about $250M press-reported.
- Elastic–Jina: $43.4M.
- 1touch: $125M.

Both the bull and bear cases are argued at their strongest in each chapter, and vendor claims are labelled. The Storage bridges stay short, do not re-teach storage, and use only public Everpure information (Data Stream, KVA, Data Intelligence/1touch, the Milvus 2.6 partner listing, the Databricks Storage Ecosystem, and the Dremio and Starburst architectures). Each uses the "options a strategy team might evaluate, based on public information" framing.

The most serious problem was in **Ch 22**. The chapter presented 91.2% on Spider 1.0, 73.0% on BIRD and 21.3% on Spider 2.0 as "the same model setup" scored three ways. In the Spider 2.0 paper, 91.2% and 73.0% are the leading leaderboard results of the time (they match MiniSeek on Spider and CHASE-SQL on BIRD). Only the 21.3% is the paper's o1-preview agent. I fixed this in the TL;DR, the body, Fig. 22.3 (title and caption), the Numbers table and "Don't say this".

## Table of changes

| Chapter | Issue | Fix | Source |
|---|---|---|---|
| 16 | IDC "90% (2022)" read as the publication year; Ch 17 dates the paper 2023 | Clarified that 2022 is the data year, the white paper was published in 2023, and it was Box-sponsored (body and Numbers table) | Ch 17 fn idc-box; footnote dates |
| 16 | Meta–Scale described as "bought 49%" | Added the $14.3B and "non-voting" | verified register / `private_funding.csv` |
| 16 | Checkpoint math used 16 bytes/param (in-memory state, including gradients). Ch 21 uses 14 bytes/param for checkpoints, so the two chapters disagreed | Now about 14 bytes/param, about 5.7 TB for 405B (about 6.5 TB with gradients), about 3 s at 2 TB/s. Numbers table updated | ZeRO accounting (Ch 21 fn zero) |
| 16 | "Discipline was renamed context engineering" overstated | Now "practitioners began describing the broader discipline as" | Anthropic post cited |
| 16 | "RAG attack only requires one document" overstated | Now "a handful of planted documents per targeted question" | Research literature on RAG poisoning, generalized |
| 16 | Databricks Vector Search naming | Added "(now 'AI Search' in its docs)" | research-briefing integrator note (Part 3) |
| 17 | VAST InsightEngine (Oct 2024) described as built on the NVIDIA AI Data Platform design, which was announced Mar 2025, so the dates don't work | InsightEngine now "built with NVIDIA NIM"; the AI Data Platform design is attributed only to NetApp AIDE and Everpure Data Stream. Who's-who row adjusted | Footnote dates; research-briefing §A (GTC 2025) |
| 17 | Editorial "weakest record of shipping software" | Softened to "shortest track record in shipping data-processing software" | Balance |
| 18 | Brute-force kNN at 1M×768 "milliseconds on one core": wrong, because the scan is memory-bandwidth-bound (about 3 GB per query) | Explained the bandwidth bound (about 15 ms at about 200 GB/s; quantization and batching help); threshold aligned with the table (1–5M) | Arithmetic |
| 18 | Cosine similarity "is the angle" | "the cosine of the angle" | Definition |
| 18 | Pre-filtering "exact but breaks the graph" mixed two cases together | Split into brute-force (exact, slow when the filter is broad) and in-graph (fast, can disconnect) | ANN literature |
| 18 | "Rack of large-memory servers" for 3.2 TB | "several large-memory servers" (consistent with the table) | Arithmetic |
| 18 | "25x cheaper", but the table gives $25,600 vs about $910 (about 28x) | TL;DR now "more than 25x"; caption now "roughly 28x" with the dollar figures | Arithmetic |
| 18 | DiskANN 3.3 TB omitted sector padding | Added that the on-disk footprint is about 4.1 TB at one record per 4 KB sector; the table uses payload | Arithmetic |
| 18 | S3 Vectors row priced at the S3 Standard rate without saying so | Labelled the S3 Standard proxy; noted that S3 Vectors bills its own rates, with a [VERIFY] | AWS pricing structure |
| 18 | Object storage "about 100 ms per access" | Now "tens of ms (up to about 100 ms)" | Typical S3 TTFB |
| 18 | efSearch 40→400 recall stated as universal | Added "typically … depends on dataset" | HNSW behaviour |
| 18 | Vespa [VERIFY: spin-out date and funding] | Resolved the spin-out (Oct 2023, pre-2025 knowledge); funding stays [VERIFY] | Pre-2025 knowledge |
| 18 | Databricks Vector Search naming | Added "AI Search" | Integrator note |
| 19 | Anthropic pricing footnote [VERIFY: long-context surcharge for Sonnet 5.5] | Resolved. Opus 5.5 $4/$20, Sonnet 5.5 $2/$10, cache read $0.20 and 1M context match Anthropic's table cached 2026-10-06, with no long-context surcharge listed for Opus or Sonnet 5.5. Added Haiku 5.5's >100K-token tier ($0.50/$2.50) | Anthropic pricing (2026-10-06 cache) |
| 19 | Google row named "Vertex AI" without the April 2026 rebrand | Added "(Vertex AI rebranded as Gemini Enterprise Agent Platform, Apr 2026)" | verified-facts #16 |
| 19 | "32K to 1M within two years" imprecise | "32K–100K tokens in 2023 to 1M+ within about two years" | Pre-2025 history |
| 20 | Scale CEO change (deSouza) not in the verified register; the brief asks for it to be marked uncertain | Added the Droege interim step, labelled "company-announced", and added a [VERIFY] flag | Brief; research-briefing (Droege interim only) |
| 20 | [VERIFY: AP / Shutterstock / Axel Springer 2023 dates] | Resolved (2023-07-13, 2023-07-11, 2023-12-13; terms undisclosed); new footnote `early-deals`; Fig. 20.3 caption updated | Pre-2025 knowledge |
| 20 | NeMo Curator "37 h → 3 h, 20x faster" is internally inconsistent (37 to 3 hours is about 12x) | Noted the inconsistency in the text and the Numbers table; added a [VERIFY] on the baseline | Arithmetic |
| 20 | Licensing range "$50–60M/yr" excluded the $70M Reddit–OpenAI estimate quoted in the same chapter | Now "$50M–$70M … press-reported or outside estimates" | Internal consistency |
| 20 | SemDeDup [VERIFY: ~50% LAION] | Resolved from the paper abstract (50% of LAION-440M, minimal loss) | Pre-2025 paper |
| 20 | "InstructGPT established the RLHF recipe" | "popularized … building on earlier preference-learning work" | Christiano 2017 / Stiennon 2020 |
| 21 | Fig. 21.5 says "five of seven categories" had a leading independent bought; the table supports four | Now "at least four of seven" with the categories named | Internal consistency |
| 22 | Spider 1.0 / BIRD / Spider 2.0 framed as one model scored three ways (see above) | Rewritten in the TL;DR, body, Fig. 22.3 title and caption, Numbers table and Don't-say | Spider 2.0 paper (leaderboard SOTA vs o1-preview agent) |
| 22 | MCP spec history: resource indicators and protected-resource metadata attributed to the Nov 2025 revision; they arrived in the 2025-06-18 revision | June 2025 now carries resource-server status, protected-resource metadata and resource indicators; Nov 2025 described generically (client registration) | MCP spec 2025-06-18 |
| 23 | Garbled sentence on DuckDB/AWS | Rewritten: "whose parent company, DuckLabs, AWS agreed to buy … (terms undisclosed)" | verified-facts #13 |
| 23 | Causal "That is why ClickHouse launched Claude agents" | Softened to "for example … in part for this reason" | Balance |
| 23 | [VERIFY: Oracle In-Memory GA 2014; HANA GA 2011] in the body and two timeline entries | Resolved (July 2014 with 12.1.0.2; June 2011) | Pre-2025 knowledge |
| 24 | S3 Express One Zone called "effectively a managed cache tier" | Clarified that it is a storage class, not an automatic cache, used as a hot tier | AWS docs (consistent with Fig. 24.4) |
| 24 | [VERIFY: RAPIDS launch Oct 2018] | Resolved (open-sourced at GTC Europe, Oct 2018) | Pre-2025 knowledge |
| 24 | EU Data Act dates [VERIFY] | Resolved against Reg. (EU) 2023/2854, Art. 50 and Art. 29 (12 Sep 2025; 12 Jan 2027) | Adopted regulation text |

That is 37 fixes in total. No CSV errors were found, so nothing was staged in `data/staging/`.

## Items checked and left unchanged (verified correct)

- HNSW: M, efConstruction, efSearch, and the layer-0 cap of 2M (128 B/vector at M=16). Vamana α>1 pruning; DiskANN NeurIPS 2019 headline (>5,000 QPS, <3 ms, 95%+ 1-recall@1, 64 GB RAM); PQ 64×12-dim with 256 codewords (64 B, 48x); IVF 65,536 lists, nprobe 64 (about 0.1%); S3 Vectors 2B/index, 20T/bucket; SQL Server 2025 VECTOR GA with DiskANN preview on-prem (integrator note).
- RRF k=60 and the worked scores; Anthropic contextual-retrieval figures (35/49/67%); LazyGraphRAG (0.1% of GraphRAG indexing, >700x lower global query cost); lost-in-the-middle (20 documents); Context Rot (18 models); Llama-3-70B KV-cache (about 0.33 MB/token, about 330 GB per 1M tokens).
- Long-context worked example: $1.61 / $0.17 / $0.03 per query on Sonnet 5.5; $4.02 / $0.42 / $0.07 on GPT-5.5 list prices.
- Feature-store point-in-time worked example and TTL logic; the ZeRO 16/14 bytes accounting; W&B 1.36x and Anyscale about 1.2x step-ups; Tecton "$900M" correctly treated as the 2022 valuation (integrator note).
- InstructGPT 13k/33k/31k; Llama 3 Tectonic (240 PB, 2/7 TB/s, 466 interruptions in 54 days); GPT-3 45 TB → 570 GB; FineWeb 15T/1.3T (about 9%), with the card now >18.5T; poisoning (250 documents, 0.00016%); Lee et al. (61-word sentence repeated >60k times); the MinHash-LSH S-curve formula.
- ClickHouse sparse index (8,192 rows; 1B rows → about 122k entries); the agent-loop and 167-QPS cost examples ($1.9M vs $12K, about 160x); Redset scope; S3 small-file ($5,000 PUT vs $92 storage) and egress chart arithmetic.

## Disagreements and calls for the integrator

1. **ClickHouse $15B basis.** The brief describes the $15B as company-stated. `data/private_funding.csv` labels it press-reported (Bloomberg), although Ch 23's footnote also cites a Business Wire release. I kept "press-reported" to match the CSV. If the integrator confirms the company's own release states $15B, both the CSV and Ch 23 should switch to company-stated.
2. **Spider 2.0 baseline reading (Ch 22).** I am confident that 91.2% and 73.0% are leaderboard SOTA figures the paper cites, because they match MiniSeek and CHASE-SQL exactly. A spot check of the paper's Figure 1 / Table 1 is still worth doing before publication.
3. **Resolutions from pre-2025 knowledge.** Several [VERIFY] markers were resolved from settled pre-2025 knowledge: Oracle In-Memory and HANA GA, the RAPIDS date, the AP/Shutterstock/Axel Springer dates, the Vespa spin-out, the SemDeDup 50% figure and the EU Data Act articles. The brief allows this for settled facts. If the integrator wants only sources 1–3 to resolve markers, these are easy to revert; each is labelled "pre-2025 knowledge" in its footnote.
4. **Claude pricing cross-check (Ch 19).** I used Anthropic's model and pricing table cached 2026-10-06 to clear the surcharge [VERIFY]. That is a first-party snapshot, not a live page fetch. The integrator may want to note it in `meta/sources.md`.
5. **Scale AI CEO (Ch 20).** The deSouza appointment is cited to a scale.com post dated 2026-07-30 but is not in the verified register. I flagged it [VERIFY] rather than removing it.

## Remaining high-risk [VERIFY] items

- **Ch 20:** Scale AI 2026 round at about $20B; the deSouza appointment; Mercor $20B talks and the >$2B run-rate (a CEO post on X); Surge/Scale 2024 revenue (Ben's Bites secondary); Handshake and Labelbox valuations; Wiley's $49M AI licensing figure against its 10-Q; Toloka's Nebius status; the NeMo Curator 20x baseline.
- **Ch 22:** the Snowflake–Natoma deal (weak aggregator only); contents of the 2026-07 MCP spec revision; Entra Agent ID GA date; the n.v. cells in the Postgres-for-agents table.
- **Ch 19:** Glean $300M ARR (secondary only, also flagged in the CSV); GPT-5.5's >272K-token surcharge; Cohere Rerank pricing (reseller-reported, with a possible Oct 2026 move to Rerank 5); the date of the Vector Search → AI Search rename; Everpure KVA–Dynamo GA date.
- **Ch 23:** the ClickHouse–LibreChat and –RunReveal deals (aggregator only); PingCAP funding; SingleStore close date; pg_duckdb 1.0 date.
- **Ch 24:** the NVIDIA–HEAVY.AI deal (no primary announcement found); Voltron Data's 2026 status.
- **Ch 18:** S3 Vectors list prices; turbopuffer round size and lead.
- **Ch 17:** official Gemini 3 Flash, LlamaParse credit and Azure DI USD list prices (the Figure 17.4 chart depends on them).
- **Ch 16:** status of the Mosaic AI brand. This underpins the interpretive claim that MosaicML's folding into Agent Bricks "suggests the market chose RAG and agents".
