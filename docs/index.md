# AI Data Atlas

**Databases, data pipelines, data platforms and the AI-data stack: how the technology works, how the businesses make money, and where it all meets storage.**

The AI Data Atlas is a knowledge base of 50 chapters plus a two-chapter orientation (Part 0). It explains the data industry from the bytes up: how databases, table formats, catalogs, pipelines, vector search and AI agents work; who sells them; how those companies make money and are valued; and where the industry is heading. Figures are current as of **2026-11-01**.

## Who it is for

It is written for a corporate-development and strategy professional (CFA, MBA, legal background, semiconductor and AI-infrastructure M&A experience) joining **Everpure** (formerly Pure Storage; NYSE: P, formerly PSTG) as the company moves up the stack from storage into data management and data intelligence. It assumes fluency in finance and storage, and builds fluency in everything above storage. A companion *Everpure Tech Atlas* covers storage hardware and protocols, so this atlas does not re-teach them; short **Storage bridge** boxes link the two. Product managers, engineers and investors who want the business and technology of data in one place will find it useful too.

## The map

![Layered market map of the data and AI-data stack, from infrastructure and object storage at the bottom through file and table formats, catalogs and governance, operational databases, analytical platforms, pipelines and streaming, semantic layer and BI, and AI data, up to agents and applications, with representative companies in each layer and Everpure highlighted](assets/diagrams/ch00-market-map.svg)

*The one-page market map from [0.2](00-start-here/ch00-2-market-map.md). Value is migrating up the stack, from storage and compute toward catalogs, semantic context and agents.*

## How to navigate

Start with Part 0, then follow a learning path or jump to a Part.

- **Part 0 · Start Here** — [0.1 How to Use This Atlas](00-start-here/ch00-1-how-to-use.md) and [0.2 The One-Page Market Map](00-start-here/ch00-2-market-map.md).
- **Part 1 · Data Systems Foundations** — begins with [1. The Data Stack Map](01-data-systems-foundations/ch01-data-stack-map.md): data models, database internals, engines, file and table formats, catalogs.
- **Part 2 · Pipelines, Movement and Governance** — begins with [9. Pipeline Patterns](02-pipelines-and-governance/ch09-pipeline-patterns.md): ingestion, streaming, transformation, quality, semantic layers, governance.
- **Part 3 · The AI Data Stack** — begins with [16. The AI Data Lifecycle](03-ai-data-stack/ch16-ai-data-lifecycle.md): unstructured data, vectors, retrieval, training data, agents, real-time.
- **Part 4 · Company Deep Dives** — begins with [25. Databricks](04-company-deep-dives/ch25-databricks.md): Snowflake, hyperscalers, database, streaming, AI-native, governance and application vendors.
- **Part 5 · Business and Economics** — begins with [35. Business Models](05-business-and-economics/ch35-business-models.md): unit economics, comps, open source, M&A, go-to-market, market sizing.
- **Part 6 · History and Future** — begins with [42. A History of Databases](06-history-and-future/ch42-history-of-databases.md) and ends with what it all means for a storage company moving up the stack.
- **Part 7 · Conversation Toolkit** — begins with [46. Talking with Data People](07-conversation-toolkit/ch46-talking-with-data-people.md): diligence checklist, question bank, one-liners and flashcards.

Terms are defined in the [glossary](glossary.md).

## Three learning paths

| If you have… | Read | Goal |
|---|---|---|
| **2 hours** | 0.1 and 0.2, then Ch 1, 7, 8, the TL;DRs of 25 and 26, Ch 27, 45 and 49 | Hold your own in a first meeting |
| **2 days** | Parts 1–4, then Ch 35–37 and 45 | Whiteboard any layer and read a data company's P&L |
| **2 weeks** | Everything, plus the drills in Ch 48–50 | Lead partnership, diligence and founder conversations |

The full path table, with a goal for every step, is in [0.1](00-start-here/ch00-1-how-to-use.md#learning-paths). Chapters are written at **L2** (mechanism) by default; **L1** is vocabulary and **L3** implementation detail appears only in "Going deeper" boxes.

## Data, charts and limitations

Every number in the atlas has a footnote with its source and date, and a label: GAAP, non-GAAP, company-stated run-rate, press-reported or estimate. Shared figures live in the repository's `data/*.csv` files (public comps, private funding rounds, M&A deals, financials and market sizes), each row with a `source` and an `as_of` date. Charts are regenerated from those files by `scripts/make_charts.py`, never drawn by hand.

Research for this edition used web search only, without direct page fetches, so some facts rest on search summaries of the cited pages. Claims we could not confirm are flagged with bracketed VERIFY markers. Market data is a snapshot as of 2026-11-01. Everpure strategy content is framed as options a strategy team might evaluate, based on public information only; nothing here is investment advice.
