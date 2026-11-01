# Templates (mandatory)

Every chapter uses one of the templates below. `scripts/qa_report.py` checks for the `##` headings verbatim (case-insensitive), so keep the heading text exactly as written. You may add `###` sub-headings freely, and you may add extra `##` sections where they help (e.g., `## Worked example`).

## Concept chapter template (Parts 1, 2, 3, 5, 6 and the concept-style Part 0/7 chapters)

```markdown
# <#>. <Title>
> **Depth:** L2 · **Reading time:** ~X min · **Last verified:** YYYY-MM-DD · **Prerequisites:** [links]

## TL;DR                              (5 bullets)
## Why this matters                   (business + Everpure lens)
## How it works                       (L2 explanation, analogies, worked examples, visuals interleaved)
## Design choices and trade-offs      (comparison table; steelman alternatives)
## Who's who                          (vendors/projects in this layer, with positioning)
## History and trajectory             (dated, sourced)
## Numbers that matter                (table: metric | value | basis | source/date)
## Storage bridge                     (only when relevant: 2–4 sentences + link to the companion repo)
## Conversation playbook              (3 PM questions, 3 engineer questions, what good answers sound like, "Don't say this")
## Going deeper                       (L3 pointers, short)
## Key terms
## Sources                            (numbered footnotes: URL, publisher, published, retrieved)
```

Notes:
- The heading "Why this matters" may carry a suffix, e.g. `## Why this matters (business + Everpure lens)`.
- "Storage bridge" is optional; QA does not require it.
- Part 7 toolkit chapters (46–50) are reference material: they must still have `## TL;DR`, `## Why this matters`, `## Conversation playbook` (or `## How to use this chapter` for 48–50), `## Key terms` and `## Sources`, but the body sections can be organized by topic.

## Company deep-dive template (Part 4)

```markdown
# <#>. <Company>
> **Status:** public/private · **HQ:** … · **Founded:** … · **Latest valuation/market cap:** … (basis, date) · **Last verified:** YYYY-MM-DD

## TL;DR
## Snapshot table                     (founders, CEO, employees, revenue/ARR, growth, funding, key investors — all sourced/labelled)
## Origin story and strategic arc     (timeline diagram)
## Product and technology             (architecture diagram + L2 explanation of how it works)
## How it makes money                 (pricing units, consumption dynamics, gross margin drivers)
## Financials                         (charts from data/company_financials.csv; GAAP vs non-GAAP labelled)
## Customers and go-to-market
## M&A and investments                (deal table + rationale + integration outcome)
## Competitive position               (vs. 3–5 named rivals; matrix)
## Why it's winning / bull case
## Risks / bear case and open questions
## Relevance to Everpure              (compete / partner / other options, public info only)
## Conversation playbook
## Sources
```

Group chapters in Part 4 (28–34) cover several companies: use the same `##` headings, and inside each section use `###` per company (or a grouped table). The status line can summarize the group (e.g., "**Status:** mixed public/private").

## Footnotes format

Use GitHub/MkDocs-compatible footnotes. Each chapter's footnotes are local to the chapter.

```markdown
Snowflake reported product revenue of $X billion in FY2026 (Feb 2025–Jan 2026), GAAP.[^sf-10k]

[^sf-10k]: Snowflake Inc., "Form 10-K for fiscal year ended January 31, 2026," https://…, published 2026-03-xx; retrieved 2026-11-01.
```

Put all footnote definitions under `## Sources` at the end of the chapter.

## Callout boxes

Use blockquote callouts so they render on both GitHub and MkDocs:

```markdown
> **Storage bridge.** …two to four sentences… See the companion *Everpure Tech Atlas* for protocol detail.

> **Going deeper (L3).** …

> **Bridge: semiconductors.** A B-tree's fan-out is like …
```
