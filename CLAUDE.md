# CLAUDE.md — AI Data Atlas: standing rules and execution mode

This repository is the **AI Data Atlas**, a knowledge base of at least 100,000 words (target ~120,000) on databases, data pipelines, data platforms, the AI-data stack and the businesses behind them. It is written for a corporate-development / strategy professional (CFA, MBA, legal background, semiconductor and AI-infrastructure M&A experience) joining Strategy & Corporate Development at **Everpure** (formerly Pure Storage; renamed Feb 23, 2026; NYSE ticker changed from PSTG to **P** on Apr 17, 2026). A companion repo, the "Everpure Tech Atlas", already covers storage hardware, protocols and AI storage, so **do not re-teach storage**. Where storage matters, add a short "Storage bridge" box and move on.

**After any context compaction:** re-read this file and `PROGRESS.md`, then continue with the next unfinished item.

## Execution mode

- Build the entire atlas in one uninterrupted run, from empty repo to the Definition of Done (bottom of this file). Do not stop for review or ask questions.
- Ambiguity → make the most reasonable decision, log it in `meta/decisions.md`, keep going.
- Unverifiable fact → mark it `[VERIFY: …]` inline, log it in `meta/open-questions.md`, keep going.
- Keep `PROGRESS.md` current after every chapter (status, words, visuals, VERIFY count, next step).
- Stop only when the Definition of Done is met or a hard blocker makes progress impossible (write the blocker into `PROGRESS.md` first).

## Standing rules

1. **Accuracy over volume.** Never invent numbers, product names, deal values, valuations, revenue, customers, dates or quotes. Every quantitative or time-sensitive claim needs an inline footnote with source, publication date and retrieval date. Unverifiable items get `[VERIFY: …]`.
2. **Research live.** This industry moves monthly. Use web search and fetch for every current fact: products, pricing, funding, valuations, revenue/ARR, M&A, partnerships and leadership. Assume training data is stale for anything after mid-2025.
3. **Source priority:** (a) SEC filings (10-K, 10-Q, S-1, 8-K, proxy), earnings call transcripts, investor-day decks and company press releases; (b) official product docs, engineering blogs and open-source project docs (Apache, Linux Foundation); (c) academic and seminal industry papers (e.g., Snowflake SIGMOD 2016, Lakehouse CIDR 2021, Codd 1970, Dremel, Spanner); (d) top-tier business press (Reuters, Bloomberg, WSJ, FT, The Information, CNBC, TechCrunch) for private-company data; (e) respected analysts and practitioners (a16z data-stack essays, Benn Stancil, Tomasz Tunguz, public Gartner/IDC/Forrester summaries, Futurum, Constellation). Avoid SEO aggregators and AI-generated "data sites" unless they cite a primary source you can check.
4. **Financial rigor:** Label every figure as **GAAP / non-GAAP / company-stated run-rate / press-reported / estimate**. Label fiscal years explicitly (e.g., Snowflake's fiscal year ends Jan 31: "FY2026 = Feb 2025–Jan 2026"). Distinguish ARR, revenue run-rate, product revenue and total revenue. Show valuation multiples with their date and basis (EV/NTM revenue, etc.).
5. **Copyright:** Explain everything in your own words. Don't paste vendor or press text, and don't reproduce vendor diagrams; redraw concepts in original Mermaid or SVG. Keep any quote under 15 words, at most one quote per source.
6. **Public information only.** Frame strategy sections as *"options a strategy team might evaluate, based on public information."* Never speculate about non-public Everpure plans.
7. **Visual density:** at least **1 visual per ~700 words**; every chapter has at least 3 visuals (Mermaid, SVG, a generated chart from a CSV, or a structured comparison table). Prose-only chapters fail QA.
8. **Voice:** a sharp senior analyst briefing an executive: plain English, worked examples, real numbers, balanced. Steelman each company's bull and bear case; avoid hype.
9. **Templates are mandatory** (`meta/templates.md`).
10. **Consistency:** use `docs/glossary.md` terms and add every new one. Cross-link chapters with relative links.
11. **Commit continuously:** commit after each chapter (`docs(ch25): Databricks deep dive`), push after each batch, update `PROGRESS.md` after every chapter.
12. **Substance, not padding.** Meet word budgets with mechanisms, examples, numbers, history and implications.

## Depth labels

- **L1 – Vocabulary:** define it and use it in a sentence.
- **L2 – Mechanism:** whiteboard explanation, trade-offs, why one design/business model beats another. **← default depth.**
- **L3 – Implementation:** internals, code, query-engine source. **Only in short "Going deeper" boxes.**

**Bridges:** explain via analogies to semiconductors and memory hierarchies, datacenter infrastructure, storage (companion repo), and finance/valuation (CFA level).

## Where things live

- Chapters: `docs/<part>/chNN-<slug>.md` (file list in `meta/outline.md`). Glossary: `docs/glossary.md` (canonical; `glossary.md` at repo root is generated by `scripts/sync_root_files.py`).
- Data (single source of truth for numbers): `data/*.csv`; every row has `source` and `as_of`. Chapter drafters propose new rows in `data/staging/`; the integrator merges them.
- Charts: `scripts/make_charts.py` → `docs/assets/charts/*.png`. Diagrams (SVG): `docs/assets/diagrams/`.
- QA: `scripts/wordcount.py`, `scripts/lint_mermaid.sh`, `scripts/check_links.py`, `scripts/qa_report.py`.
- Meta: `meta/outline.md`, `meta/style-guide.md`, `meta/templates.md`, `meta/agent-brief.md`, `meta/sources.md`, `meta/decisions.md`, `meta/open-questions.md`.

## Definition of Done

- [ ] ≥100,000 words of substantive prose across 50 chapters plus Part 0
- [ ] Part 4 ≥28,000 words; Databricks and Snowflake chapters ≥4,000 words each
- [ ] ≥150 visuals; every chapter ≥3; all Mermaid renders cleanly; all charts regenerate from `data/`
- [ ] Every chapter follows its template, including the Conversation Playbook
- [ ] Every number is sourced, dated and labelled (GAAP/non-GAAP/run-rate/reported/estimate); fiscal years explicit
- [ ] `data/ma_deals.csv` ≥80 deals; `data/public_comps.csv` ≥20 companies; `data/private_funding.csv` ≥40 rounds
- [ ] Glossary ≥350 terms; question bank ≥150; flashcards ≥200
- [ ] Independent reviewer pass completed for all Parts
- [ ] Reads well on github.com and as a deployed MkDocs site
