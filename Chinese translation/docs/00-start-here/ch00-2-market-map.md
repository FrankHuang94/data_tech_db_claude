# 0.2 一页纸市场地图
> **深度：** L1 · **阅读时间：** 约 9 分钟 · **最后核实：** 2026-11-01 · **前置阅读：** [0.1 如何使用本图谱](ch00-1-how-to-use.md)

## 要点速览（TL;DR）

- 数据与 AI 数据行业可以画成 **九个层级**，底层是对象存储（object storage），顶层是智能体（agent）与应用。本图谱中的每家公司都位于其中一层或多层，而最大的那些公司正试图占据全部九层。
- 两家具备规模的独立厂商合计价值约 **$300B**（3,000 亿美元）：Databricks 的 **投后估值为 $190B**，对应 **公司披露的年化运行率 >$7B**（2026 年 8 月）；Snowflake 的 **市值为 $107.88B**（2026-10-30）。[^db-aug26][^comps] 超大规模云厂商（hyperscaler）位于两者之下和身旁，其云业务在 2026 年 9 月季度增长了 39–103%。[^amzn-q3][^msft-q1][^goog-q3]
- **价值正沿着技术栈向上迁移。** 存储容量和通用计算正在商品化。开放格式（Iceberg、Delta、Parquet）使数据变得可移植，因此控制权转移到了位于其上的目录（catalog）、语义层（semantic layer）和智能体接口。
- 技术栈的中间层在 2025–26 年被纷纷出售。Informatica 归入 Salesforce（约 $8B），Confluent 归入 IBM（约 $11B），Dremio 归入 SAP，Neon 归入 Databricks，AWS 也签署了收购 DuckLabs 的协议。私人资本则集中流向少数赢家：VAST Data（$30B）、Scale AI（隐含约 $29B）、ClickHouse（$15B）和 Cyera（$12B）。[^ma][^funding]
- Everpure 的公开举措位于第 1 层（存储），自 **$125.0M** 收购 1touch 以来，已延伸至第 3 层（数据发现、数据分类与语义上下文）。[^ep-1touch] [第 45 章](../06-history-and-future/ch45-storage-moving-up-the-stack.md)阐述了相关可选方案。

## 地图

下面这张地图就是一页纸上的整本图谱。请自下而上阅读：每一层都依赖于其下一层，而每往上一层，就离提出问题的人或智能体更近一步。

![数据与 AI 数据栈的分层市场地图，共九条水平带。自下而上依次为：基础设施与对象存储（AWS S3、Azure Blob、Google Cloud Storage、Everpure、NetApp、Dell、VAST Data、MinIO）；文件与表格式（Parquet、Arrow、Lance、Iceberg、被 Databricks 收购的 Tabular、Delta Lake、Hudi）；目录与数据治理（Unity Catalog、Polaris 与 Horizon、Glue、Dataplex、Purview、Collibra、Atlan、Alation、BigID、Cyera、被 Everpure 收购的 1touch、待出售给 Proofpoint 的 Varonis）；运营型数据库（Oracle、MongoDB、PostgreSQL、归入 Databricks 的 Neon、归入 Snowflake 的 Crunchy Data、Supabase、Redis、CockroachDB、DynamoDB、Spanner、Aurora）；分析平台与引擎（Databricks、Snowflake、BigQuery、Redshift、Fabric、ClickHouse、DuckDB、归入 AWS 的 DuckLabs、Trino、Starburst、归入 SAP 的 Dremio、Teradata）；数据管道与流处理（Fivetran 与 dbt Labs、Airbyte、归入 Salesforce 的 Informatica、归入 IBM 的 Confluent、Redpanda、Flink、Airflow、Astronomer、归入 Prefect 的 Dagster）；语义层与 BI（Power BI、Tableau、Looker、Sigma、ThoughtSpot、Cube、AtScale）；AI 数据（Pinecone、Weaviate、Qdrant、Milvus 与 Zilliz、Unstructured、LlamaIndex、Scale AI、Snorkel AI、MLflow、归入 CoreWeave 的 Weights and Biases）；以及智能体与应用（Model Context Protocol、Salesforce Agentforce 与 Data 360、ServiceNow、SAP Business Data Cloud、Palantir AIP、Workday Data Cloud）。右侧一个高箭头表示价值向上迁移。Everpure 和 1touch 以朱红色轮廓标出](../assets/diagrams/ch00-market-map.svg)

*图 0.2.1 — SV-1，一页纸市场地图。九个层级，约 80 家具名公司和项目，以及一个发展方向：价值正从字节转向位于其上的元数据、语义和智能体。标签边框表示上市（实线）、私有（虚线）和开源（灰色）状态；"A → B"表示 2024–26 年的一笔收购。*

三条阅读规则会有所帮助。第一，**层级不等于市场**。一家公司出现在其主要产品所在的位置，但 Databricks 和 Snowflake 如今在九层中的大多数层都有产品，而每家超大规模云厂商几乎在所有层都有产品。第二，**颜色表示层级的角色**。紫色标记两个"语义"层（目录与语义），本图谱认为控制权正在这里积聚。第三，**箭头讲述整合的故事**。大多数"→"标签是在截至 2026 年 10 月的 18 个月内添加的，而且大多从一家独立的专业厂商指向一个平台。

下表补充了每一层的状态和最新估值，数据取自本图谱的数据集。

| 层级 | 代表性公司（状态） | 最新估值或市值（口径，日期） | 深度研究 |
|---|---|---|---|
| 1. 基础设施与对象存储 | Amazon/AWS、Microsoft/Azure、Alphabet/Google Cloud、Everpure、NetApp、Dell（上市）；VAST Data、MinIO（私有） | Amazon $2,600B、Microsoft $3,880B、Alphabet $3,440B 市值（2026-10-30）；Everpure $43.79B、NetApp $42.24B（2026-10-01）；VAST $30B 投后估值（2026 年 4 月，公司披露）[^comps][^funding] | [28](../04-company-deep-dives/ch28-hyperscaler-data-platforms.md)、[32](../04-company-deep-dives/ch32-ai-native-data-companies.md)、[45](../06-history-and-future/ch45-storage-moving-up-the-stack.md) |
| 2. 文件与表格式 | Parquet、Arrow、Iceberg、Hudi（Apache 项目）；Delta Lake（Linux Foundation）；Lance（LanceDB，私有） | 项目本身没有估值；Tabular → Databricks 约 $2B（2024 年 6 月，媒体报道）[^ma] | [6](../01-data-systems-foundations/ch06-file-formats.md)、[7](../01-data-systems-foundations/ch07-open-table-formats.md) |
| 3. 目录与数据治理 | Unity Catalog（Databricks）、Horizon/Polaris（Snowflake/Apache）、Glue、Dataplex、Purview；Collibra、Atlan、Alation、BigID、Cyera（私有）；Varonis（上市） | Cyera $12B（2026 年 6 月，媒体报道）；Collibra $5.25B（2021 年 11 月，媒体报道）；Alation $1.7B（2022 年 11 月，媒体报道）；BigID $1B（2024 年 3 月，公司披露）；Atlan $750M（2024 年 5 月，公司披露）；1touch → Everpure $125.0M（GAAP）；Varonis → Proofpoint 交易价值约 $6.3B、股权价值约 $5.71B（待完成，预计 1H 2027 交割）[^funding][^ma][^ep-1touch] | [33](../04-company-deep-dives/ch33-governance-catalog-security-companies.md) |
| 4. 运营型数据库 | Oracle、MongoDB（上市）；Supabase、Redis、Cockroach Labs（私有）；DynamoDB、Aurora、Spanner（超大规模云厂商服务） | Oracle $382.45B（2026-10-23）；MongoDB $29.5B（2026-10-20）；Supabase $10.65B（2026 年 10 月，媒体报道，单一来源；2026 年 6 月 F 轮时为 $10.5B，媒体报道）；Cockroach Labs $5B（2021 年 12 月，媒体报道）；Neon → Databricks 约 $1B（媒体报道）；Crunchy Data → Snowflake $164.5M（依据 10-Q）[^comps][^funding][^ma] | [29](../04-company-deep-dives/ch29-operational-database-vendors.md) |
| 5. 分析平台与引擎 | Databricks、ClickHouse、Starburst（私有）；Snowflake、Teradata（上市）；BigQuery、Redshift、Fabric（超大规模云厂商） | Databricks $190B 投后估值（2026-08-13，公司披露）；Snowflake $107.88B，16.9x EV/未来 12 个月收入（2026-10-30，估算）；ClickHouse $15B（2026 年 1 月，媒体报道）；Starburst $3.35B（2022 年 2 月，媒体报道）；Teradata $3.19B（2026-10-28）；Dremio → SAP（已完成）和 DuckLabs → AWS（已签协议，尚未完成）金额未披露[^db-aug26][^comps][^funding][^ma] | [25](../04-company-deep-dives/ch25-databricks.md)、[26](../04-company-deep-dives/ch26-snowflake.md)、[27](../04-company-deep-dives/ch27-databricks-vs-snowflake.md)、[31](../04-company-deep-dives/ch31-analytical-engine-challengers-legacy.md) |
| 6. 数据管道与流处理 | Fivetran + dbt Labs、Airbyte、Redpanda、Astronomer（私有）；Flink、Airflow（Apache 项目） | Confluent → IBM 约 $11B EV（2026 年 3 月完成）；Informatica → Salesforce 约 $8B 股权价值（2025 年 11 月完成）；最后一次独立估值为 Fivetran $5.6B（2021）和 dbt Labs $4.2B（2022），公司披露；Airbyte $1.5B（2021）；Redpanda $1B（2025 年 4 月）；Astronomer $775M（2025 年 5 月，媒体报道）[^ma][^funding] | [30](../04-company-deep-dives/ch30-data-movement-streaming-companies.md) |
| 7. 语义层与 BI | Power BI（Microsoft）、Tableau（Salesforce）、Looker（Google）；Sigma、Omni、ThoughtSpot、Cube、AtScale（私有） | Sigma $3B（2026 年 5 月，媒体报道）；Omni $1.5B（2026 年 4 月，公司披露）；ThoughtSpot、Cube 和 AtScale 的估值未收录于数据集[^funding] | [14](../02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)、[34](../04-company-deep-dives/ch34-application-giants-data-platforms.md) |
| 8. AI 数据 | Pinecone、Weaviate、Qdrant、Zilliz、Unstructured、LlamaIndex、Snorkel AI、Scale AI（私有）；MLflow（开源） | Scale AI 隐含约 $29B（Meta 以 $14.3B 收购 49%，2025 年 6 月，媒体报道）；Snorkel AI $3.5B（2026 年 9 月，公司披露）；Pinecone $750M（2023 年 4 月，媒体报道）；W&B → CoreWeave 约 $1.7B（媒体报道）[^funding][^ma] | [32](../04-company-deep-dives/ch32-ai-native-data-companies.md) |
| 9. 智能体与应用 | Palantir、SAP、Salesforce、ServiceNow、Workday（上市）；Model Context Protocol（开放标准） | Palantir $442.43B、SAP $273.8B、Salesforce $188.61B（2026-10-30）；ServiceNow $142.4B（2026-10-01）；Workday $45.99B（2026-10-16）[^comps] | [22](../03-ai-data-stack/ch22-agents-and-data.md)、[34](../04-company-deep-dives/ch34-application-giants-data-platforms.md) |

*图 0.2.2 — 按层级列示公司。最大的价值集中在底部（超大规模云厂商）和顶部（应用与智能体平台）；中间层则是 2025–26 年交易发生的地方。2021–22 年的私募估值尚未重新定价，应视为过时数据。*
