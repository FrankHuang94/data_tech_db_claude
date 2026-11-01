# Translation brief: AI Data Atlas → Simplified Chinese (简体中文)

You are a senior bilingual (English ↔ Simplified Chinese) technical and financial translator, fluent in database and data-platform engineering and in buy-side equity research. You are translating part of the **AI Data Atlas** (repo: `/home/user/data_tech_db_claude`) into Simplified Chinese. The Chinese edition lives in the folder **`/home/user/data_tech_db_claude/Chinese translation/`**, which mirrors the English structure (`README.md`, `glossary.md`, `docs/index.md`, `docs/glossary.md`, `docs/<part>/chNN-….md`) with **identical file names**.

The Chinese edition is a **reference translation**: be generally precise and complete. Translate the *entire* content, and do not summarize, shorten, skip sections or add commentary. No separate accuracy QA bar is required, but meaning, numbers and structure must match the English.

## What to translate and what to keep

| Element | Rule |
|---|---|
| Prose, headings, list items, table cells, callouts, captions, TL;DR, playbooks, flashcards, questions | **Translate** into natural, professional Simplified Chinese (the register of a Chinese sell-side research note or a top-tier tech publication). |
| Numbers, currencies, percentages, dates, fiscal-year labels | **Keep exactly** (e.g., `$190B` → `1,900 亿美元` is NOT wanted; keep `$190B` / `US$190B` as written, optionally add a Chinese gloss in parentheses only if it aids reading, e.g., `$190B（1900 亿美元）` — use this sparingly, at most for headline figures). Keep `FY2027`, `Q2 FY2027`, `CY2025`, ISO dates. |
| Company, product, project and person names | **Keep in English** (Databricks, Snowflake, Apache Iceberg, Unity Catalog, Everpure, MongoDB, …). On first use in a chapter you may add a common Chinese name in parentheses if one is standard (e.g., 甲骨文 for Oracle is optional — prefer English). |
| Technical terms | Use the **terminology table below**. On first use in each chapter write `中文（English）`, e.g., `湖仓一体（lakehouse）`, then the Chinese alone. Acronyms (OLTP, OLAP, ACID, MVCC, CDC, ETL, RAG, MCP, NRR, RPO, ARR, GAAP, DSPM…) stay as acronyms. |
| Financial labels | `GAAP` → `GAAP`; `non-GAAP` → `非 GAAP`; `company-stated run-rate` → `公司披露的年化运行率`; `press-reported` → `媒体报道`; `estimate` → `估算`; `company-stated` → `公司披露`. |
| `[VERIFY: …]` markers | Keep the literal `[VERIFY: …]` tag; translate the text inside it. |
| Markdown structure | Keep **identical**: same heading levels and order, same number of headings, same tables (same rows/columns), same lists, blockquote callouts (`> **Bridge: …**` → `> **类比：…**`, `> **Storage bridge.**` → `> **存储桥接。**`, `> **Going deeper (L3).**` → `> **深入（L3）。**`). |
| Chapter metadata line | Translate labels: `**Depth:**` → `**深度：**`, `**Reading time:**` → `**阅读时间：**` (`~X min` → `约 X 分钟`), `**Last verified:**` → `**最后核实：**`, `**Prerequisites:**` → `**前置阅读：**`, `**Status:**` → `**状态：**`, `**HQ:**` → `**总部：**`, `**Founded:**` → `**成立：**`, `**Latest valuation/market cap:**` → `**最新估值/市值：**`. |
| Footnote markers `[^id]` | Keep the **same ids** and positions. |
| Footnote definitions (in `## Sources`) | Keep publisher names, document titles and URLs in their **original language**; translate only connective words: `published` → `发布`, `retrieved` → `检索`, `not re-fetched` → `未重新抓取`, and any explanatory note. |
| Links `[text](target)` | Translate the link **text**; keep the **target exactly as in the English file** (the integrator's script fixes paths afterwards). This includes `../glossary.md#slug` anchors and image paths. |
| Images `![alt](path)` | Translate the alt text; keep the path unchanged. |
| Mermaid blocks | Translate the **labels and text** (node labels, edge labels, titles, axis labels, timeline items, mindmap text, quadrant labels) but keep **node IDs, keywords, arrows and syntax unchanged**. Keep every label that contains punctuation or spaces in double quotes, e.g., `A["对象存储（S3）"]`. In `xychart-beta`, keep numeric data; translated category labels must stay inside `"…"`. In `quadrantChart`, quadrant/axis text must not contain colons. In `timeline`, keep the `period : event` separator ` : ` and avoid colons inside event text (use `，` instead). Do not use the `；` character inside unquoted labels. |
| Code blocks (non-Mermaid), file paths, CLI commands, SQL | Keep unchanged (you may translate comments inside them). |
| HTML (`<details>`, `<summary>`, `<a id>`, `<br/>`) | Keep tags; translate the text inside. |

## Terminology table (use consistently)

| English | 简体中文 |
|---|---|
| database | 数据库 |
| data warehouse | 数据仓库 |
| data lake | 数据湖 |
| lakehouse | 湖仓一体 / 湖仓 |
| open table format | 开放表格式 |
| catalog / metastore | 目录 / 元数据存储 |
| data catalog (business) | 数据目录 |
| control point | 控制点 |
| query optimizer | 查询优化器 |
| storage engine | 存储引擎 |
| B-tree / LSM-tree | B 树 / LSM 树 |
| write-ahead log (WAL) | 预写日志（WAL） |
| transaction | 事务 |
| isolation level | 隔离级别 |
| sharding / replication / consensus | 分片 / 复制 / 共识 |
| columnar storage | 列式存储 |
| vectorized execution | 向量化执行 |
| separation of storage and compute | 存算分离 |
| object storage | 对象存储 |
| file format | 文件格式 |
| time travel | 时间旅行（历史版本查询） |
| schema evolution | 模式演进 |
| snapshot | 快照 |
| pipeline | 数据管道 |
| ingestion | 数据摄取 |
| change data capture (CDC) | 变更数据捕获（CDC） |
| reverse ETL | 反向 ETL |
| zero-ETL / zero-copy | 零 ETL / 零拷贝 |
| streaming / event streaming | 流处理 / 事件流 |
| orchestration | 编排 |
| transformation | 数据转换 |
| data contract | 数据契约 |
| data quality / observability / lineage | 数据质量 / 可观测性 / 数据血缘 |
| semantic layer / metrics layer | 语义层 / 指标层 |
| business intelligence (BI) | 商业智能（BI） |
| governance | 数据治理 |
| access control (RBAC/ABAC) | 访问控制（RBAC/ABAC） |
| data classification / discovery | 数据分类 / 数据发现 |
| masking / tokenization | 脱敏 / 令牌化 |
| data security posture management (DSPM) | 数据安全态势管理（DSPM） |
| data sovereignty | 数据主权 |
| embedding | 嵌入（向量） |
| vector database / vector search | 向量数据库 / 向量检索 |
| approximate nearest neighbor (ANN) | 近似最近邻（ANN） |
| retrieval-augmented generation (RAG) | 检索增强生成（RAG） |
| reranking / hybrid search | 重排序 / 混合检索 |
| knowledge graph | 知识图谱 |
| context engineering | 上下文工程 |
| agent / agentic | 智能体 / 智能体式 |
| text-to-SQL | 文本转 SQL |
| feature store | 特征存储 |
| fine-tuning / pretraining | 微调 / 预训练 |
| labeling / RLHF | 数据标注 / 人类反馈强化学习（RLHF） |
| synthetic data | 合成数据 |
| real-time analytics / HTAP | 实时分析 / 混合事务分析处理（HTAP） |
| data gravity | 数据引力 |
| egress fees | 出口流量费 |
| consumption pricing / usage-based | 按用量计费 |
| subscription | 订阅 |
| open core | 开放核心（open core） |
| managed service | 托管服务 |
| run-rate | 年化运行率 |
| annual recurring revenue (ARR) | 年度经常性收入（ARR） |
| net revenue retention (NRR) | 净收入留存率（NRR） |
| remaining performance obligations (RPO) | 剩余履约义务（RPO） |
| gross margin | 毛利率 |
| stock-based compensation (SBC) | 股权激励费用（SBC） |
| free cash flow (FCF) | 自由现金流（FCF） |
| Rule of 40 | 40 法则 |
| enterprise value (EV) / EV/NTM revenue | 企业价值（EV） / EV/未来 12 个月收入 |
| valuation / post-money | 估值 / 投后估值 |
| take-private | 私有化 |
| acquihire | 人才收购（acquihire） |
| go-to-market (GTM) | 市场进入（GTM） |
| co-sell / marketplace | 联合销售 / 云市场 |
| committed spend | 承诺消费额度 |
| total addressable market (TAM) | 总可服务市场（TAM） |
| bull case / bear case | 看多逻辑 / 看空逻辑 |
| steelman | 最强版本论证 |
| due diligence | 尽职调查 |
| Conversation playbook | 对话手册 |
| TL;DR | 要点速览（TL;DR） |
| Key terms | 关键术语 |
| Sources | 资料来源 |
| Numbers that matter | 关键数字 |
| Who's who | 主要参与者 |
| Design choices and trade-offs | 设计选择与权衡 |
| History and trajectory | 历史与发展轨迹 |
| How it works | 工作原理 |
| Why this matters | 为何重要 |
| Going deeper | 深入阅读 |
| Storage bridge | 存储桥接 |
| Relevance to Everpure | 与 Everpure 的相关性 |
| Snapshot table | 概览表 |
| Origin story and strategic arc | 起源与战略演进 |
| Product and technology | 产品与技术 |
| How it makes money | 盈利模式 |
| Financials | 财务数据 |
| Customers and go-to-market | 客户与市场进入 |
| M&A and investments | 并购与投资 |
| Competitive position | 竞争地位 |
| Why it's winning / bull case | 制胜原因 / 看多逻辑 |
| Risks / bear case and open questions | 风险 / 看空逻辑与待解问题 |
| Figure N.k — | 图 N.k — |

Glossary entries in the Chinese glossary use the heading pattern `### 中文术语（English Term）` preceded by an anchor line `<a id="english-slug"></a>` (the integrator adds missing anchors automatically, but keep any that exist).

## How to work (important, to avoid output-size limits)

1. Read the English source file fully first (`Read` in chunks if long).
2. Translate **section by section**. Write the first chunk with the `Write` tool, then **append** each later chunk with Bash using a quoted heredoc so nothing is interpolated:
   ```bash
   cat >> "/home/user/data_tech_db_claude/Chinese translation/docs/<part>/<file>.md" <<'__ZH_EOF__'
   …translated markdown…
   __ZH_EOF__
   ```
   Keep each chunk to roughly ≤ 250 lines / ≤ 8,000 Chinese characters.
3. After finishing a file, verify:
   - Heading count matches: `grep -c '^#' <english>` vs `grep -c '^#' <chinese>`, and table-row count roughly matches (`grep -c '^|'`).
   - Footnote definitions all present: compare `grep -c '^\[\^' ` counts.
   - Mermaid renders: `cd /home/user/data_tech_db_claude && scripts/lint_mermaid.sh "Chinese translation/docs/<part>/<file>.md"` → 0 failures (fix labels if any fail; simplify punctuation inside labels).
4. Do not edit any English file, do not run git, do not touch other translators' files.
5. Reply in ≤ 80 words: files written, heading/footnote/Mermaid checks passed, anything left untranslated.
