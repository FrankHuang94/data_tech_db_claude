# 49. 30 秒讲清楚
> **深度：** L1–L2 · **阅读时间：** 约 20 分钟 · **最后核实：** 2026-11-01 · **前置阅读：** 无；每条一句话解释都链接到详细讲解它的章节（[第 1 章 — 数据栈全景图](../01-data-systems-foundations/ch01-data-stack-map.md)是最好的单一起点）

## 要点速览（TL;DR）

- 本章收录 **71 条一句话解释**，编号并分为七类：基础、湖仓一体、数据管道、数据治理、AI 数据、商业以及公司。每一条都说明这个东西是什么、为什么重要，并给出一个类比。每一条都链接到深入讲解它的章节。
- 每条大约需要 30 秒说完。这大致就是一位高管在判断你究竟是理解这个话题还是在背诵之前愿意听的时长。
- 类比取材于读者熟悉的领域：半导体与存储层次结构、存储、数据中心以及金融。如果某个类比在追问之下站不住，就放弃它，直接讲机制。链接的章节里有机制。
- 这里的数字是一小组带日期的数据，取自本知识库的数据集（`data/*.csv`）和已核实事实登记表。每个数字都带有标签（GAAP、公司披露的年化运行率、媒体报道或估算）和脚注。复述时不要向上取整。
- 两张图展示了概念之间如何关联，以及哪些概念对最常被混淆。数据话题对话中的许多信誉损失，来自混淆相邻术语：ARR 与年化运行率、数据湖与湖仓一体、向量索引与向量数据库。

## 为何重要

一位加入 Everpure（原 Pure Storage）的企业发展专业人士，会在一周之内、在非常不同的场合中听到这些术语：一次关于 Data Intelligence 的产品评审、一位投行人士关于某家数据目录初创公司的推介、一场 Snowflake 的财报电话会、一次与湖仓厂商的合作伙伴会议。这些场合里没有人会停下来给 Iceberg 或 NRR 下定义。能够干净利落地定义一个术语、把它放到技术栈中的正确位置并说出其商业后果的人，才会被托付下一个问题。

这些一句话解释也是对理解程度的检验。如果你说不出一个东西做什么、买方为什么为它付费、以及它在你已经熟悉的世界里像什么，那么你对它的了解还不足以评估一笔建立在它之上的交易。会前把这些条目当作速览摘要使用；当会议讨论超过 30 秒的深度时，再去看链接的章节。

此外还有一个具体的 Everpure 视角。公司在 2026 年通过收购 1touch 并发布 Data Intelligence，从"存储数据"转向"理解数据"，这使它与下文的若干类别相邻：数据分类、DSPM、数据目录、语义上下文、向量数据管道。能够准确解释这些相邻领域，正是战略团队得以基于公开信息讨论选项、合作伙伴和竞争对手的前提。

## 如何使用本章

1. **会议之前**，浏览相关的类别。与湖仓合作伙伴的电话需要第 10–19 条和第 62–63 条。对一家 AI 初创公司的尽职调查电话需要第 38–50 条和第 57–59 条。
2. **说完第一句就停下。** 每条的第一句是定义，应当能够独立成立。如果对方点头，再补上第二句（为什么重要）。只有在对方看起来不太确定时才使用类比。
3. **绝不即兴编造数字。** 如果需要数字，就使用条目中的数字，并附上其标签和日期（"公司披露的年化运行率，2026 年 8 月"）。一个被自信地说出口的错误数字，比说"我会再确认"造成的损害更大。
4. **把文末的易混淆概念对照表**当作"不要这样说"清单使用。
5. **当有人问"这到底是怎么运作的？"时，去看链接的章节。** 那是一个 L2 问题，而本章大部分是 L1。

```mermaid
flowchart LR
  Q["现场提出的问题"] --> D["第 1 句<br/>它是什么"]
  D --> W["第 2 句<br/>买方为什么为它付费"]
  W --> A{"听者不确定？"}
  A -->|"是"| AN["类比<br/>芯片、内存、存储或金融"]
  A -->|"否"| N["一个带标签的数字（如有）"]
  AN --> N
  N --> L["推荐对应章节<br/>以了解机制"]
```

*图 49.1 — 一个 30 秒回答的结构。先给出定义，赢得说第二句的机会，只在听者需要时才使用类比。数字是可选的，但如果给出，就要给出其标签和日期。*

```mermaid
mindmap
  root((71 个概念))
    基础
      OLTP 与 OLAP
      B 树与 LSM 树
      MVCC
      列式存储
      向量化执行
      存算分离
      Parquet
      Arrow
      预写日志
    湖仓一体
      数据湖与湖仓一体
      开放表格式
      Iceberg
      Delta Lake
      Hudi
      目录
      Unity Catalog
      Polaris
      时间旅行
      压缩合并
    数据管道
      ETL 与 ELT
      CDC
      Kafka
      Flink
      dbt
      编排
      反向 ETL
      零 ETL
      数据契约
      可观测性
      数据血缘
      语义层
    数据治理
      RBAC 与 ABAC
      DSPM
      数据分类
      脱敏与令牌化
      EU AI Act
      权限感知检索
    AI 数据
      嵌入
      向量数据库与向量索引
      HNSW
      DiskANN
      RAG
      重排序
      GraphRAG
      上下文工程
      MCP
      文本转 SQL
      特征存储
      RLHF 数据
      混合检索
    商业
      DBU
      Snowflake credit
      按用量计费模式
      NRR
      RPO
      云 COGS
      40 法则
      EV 与未来 12 个月收入之比
      年化运行率与 ARR
      开放核心
      SSPL 与 BSL
    公司
      Databricks
      Snowflake
      Microsoft Fabric
      BigQuery
      ClickHouse
      DuckDB
      Confluent
      Fivetran 加 dbt
      Palantir
      Everpure 与 1touch
```

*图 49.2 — 71 个概念分为七类。基础和湖仓一体解释数据存放在哪里，数据管道和数据治理解释数据如何流动以及谁可以接触它，AI 数据解释模型如何使用数据，商业和公司则解释谁在赚钱。*

| 类别 | 条目 | 数量 | 主要章节 |
|---|---|---|---|
| 基础 | 1–9 | 9 | [第 1 章](../01-data-systems-foundations/ch01-data-stack-map.md)、[第 3 章](../01-data-systems-foundations/ch03-database-internals.md)、[第 5 章](../01-data-systems-foundations/ch05-analytical-engines.md)、[第 6 章](../01-data-systems-foundations/ch06-file-formats.md) |
| 湖仓一体 | 10–19 | 10 | [第 7 章](../01-data-systems-foundations/ch07-open-table-formats.md)、[第 8 章](../01-data-systems-foundations/ch08-catalogs-and-metastores.md)、[第 27 章](../04-company-deep-dives/ch27-databricks-vs-snowflake.md) |
| 数据管道 | 20–31 | 12 | [第 9 章](../02-pipelines-and-governance/ch09-pipeline-patterns.md)至[第 14 章](../02-pipelines-and-governance/ch14-semantic-layers-and-bi.md) |
| 数据治理 | 32–37 | 6 | [第 15 章](../02-pipelines-and-governance/ch15-governance-security-privacy.md)、[第 33 章](../04-company-deep-dives/ch33-governance-catalog-security-companies.md) |
| AI 数据 | 38–50 | 13 | [第 16 章](../03-ai-data-stack/ch16-ai-data-lifecycle.md)至[第 22 章](../03-ai-data-stack/ch22-agents-and-data.md) |
| 商业 | 51–61 | 11 | [第 35 章](../05-business-and-economics/ch35-business-models.md)至[第 38 章](../05-business-and-economics/ch38-open-source-strategy.md) |
| 公司 | 62–71 | 10 | [第 25 章](../04-company-deep-dives/ch25-databricks.md)至[第 34 章](../04-company-deep-dives/ch34-application-giants-data-platforms.md) |
| **合计** | 1–71 | **71** | |

*图 49.3 — 类别汇总。AI 数据和数据管道两组条目最多，因为高管们最常在这两个领域听到陌生的行话。商业术语较少，但在这里答错最损信誉。*

```mermaid
pie title "按类别划分的一句话解释（共 71 条）"
  "基础" : 9
  "湖仓一体" : 10
  "数据管道" : 12
  "数据治理" : 6
  "AI 数据" : 13
  "商业" : 11
  "公司" : 10
```

*图 49.4 — 各类别条目占比。本章大约三分之一的内容（第 38–61 条）涉及 AI 数据和商业术语，这两个领域是战略对话推进最快、定义也最常被引申的地方。*

## 基础

**1. OLTP vs OLAP（联机事务处理与联机分析处理）.** 联机事务处理（OLTP）一次记录一笔小交易，记录的是业务本身；联机分析处理（OLAP）扫描数以百万计的此类记录，以回答关于业务的问题。两者的调优方向相反，因此大多数公司同时运行两者，并为在它们之间搬运数据付费，就像收银机旁边放着总账。（[第 1 章](../01-data-systems-foundations/ch01-data-stack-map.md)、[第 2 章](../01-data-systems-foundations/ch02-data-models.md)）

**2. B-tree vs LSM-tree（B 树与 LSM 树）.** B 树原地更新有序页面，读取速度快；日志结构合并树（LSM 树）追加写入、之后再合并有序文件，因此写入速度快。选择哪一种，决定了由读还是由写来付出代价，这与原地更新的文件系统和异地写入、事后垃圾回收的闪存转换层（FTL）之间的权衡相同。（[第 3 章](../01-data-systems-foundations/ch03-database-internals.md)）

**3. MVCC（多版本并发控制）.** 多版本并发控制为每一行保留多个版本，因此读者看到的是一致的快照，而写入者可以继续工作。这就是为什么一份长时间运行的报表不会冻结结账页面，正如会计在冻结的试算平衡表上结账，而应付账款部门仍在继续过账。（[第 3 章](../01-data-systems-foundations/ch03-database-internals.md)）

**4. Columnar storage（列式存储）.** 把每一列的值存放在一起，而不是把每一行的值存放在一起，这样一个只涉及 200 列中 3 列的查询只需读取那 3 列，而且压缩效果好。这是分析型数据库速度快的主要原因，就像 DRAM 突发传输读取连续字节而不是零散字节。（[第 5 章](../01-data-systems-foundations/ch05-analytical-engines.md)）

**5. Vectorized execution（向量化执行）.** 引擎每次操作处理约一千个值的批次，而不是一次处理一行，从而让 CPU 缓存和 SIMD 单元保持忙碌。所有现代引擎（DuckDB、Photon、Velox）都这样工作；它是从标量指令转向 SIMD 指令在软件层面的翻版。（[第 5 章](../01-data-systems-foundations/ch05-analytical-engines.md)）

**6. Separation of storage and compute（存算分离）.** 持久化数据存放在共享的对象存储中，计算集群启动后查询这些数据，空闲时停止。它把数据仓库从一次性的容量采购变成了按量计费的公用事业，并由 Snowflake 实现了商业化，就像无晶圆厂公司租用代工产能而不是自建晶圆厂。（[第 5 章](../01-data-systems-foundations/ch05-analytical-engines.md)、[第 26 章](../04-company-deep-dives/ch26-snowflake.md)）

**7. Apache Parquet.** 默认的开放列式文件格式：行组按列存储并压缩，附带最小/最大值统计，使引擎可以跳过不需要的数据块。从物理上看，几乎每一张湖仓表都是一堆 Parquet 文件，就像任何板卡厂商都能贴装的标准封装。（[第 6 章](../01-data-systems-foundations/ch06-file-formats.md)）

**8. Apache Arrow.** 一种标准的内存列式布局，使系统之间传递数据时无需逐行转换。Parquet 是数据在磁盘上静止时的形态，Arrow 是数据在内存中和网络上流动时的形态，就像 PCIe 这样的通用总线协议。（[第 6 章](../01-data-systems-foundations/ch06-file-formats.md)）

**9. Write-ahead log（预写日志，WAL）.** 数据库在改动数据文件之前，先把每一项变更追加到一个持久化的顺序日志中，这样崩溃之后可以重放。同一个日志之后还会为变更数据捕获（第 21 条）提供数据；先记日记账，后过总账。（[第 3 章](../01-data-systems-foundations/ch03-database-internals.md)）

## 湖仓一体

**10. Data lake vs lakehouse（数据湖与湖仓一体）.** 数据湖是存放在对象存储中的廉价文件，没有事务；湖仓一体在此基础上增加了表格式和目录，使同样的文件表现得像数据仓库的表。区别在于元数据层，而不在于存储，就像库存管理系统上线前后的同一片托盘仓库。（[第 7 章](../01-data-systems-foundations/ch07-open-table-formats.md)）

**11. Open table format（开放表格式）.** 一个元数据层加一套提交协议，把一个装满不可变 Parquet 文件的文件夹变成一张支持原子提交、快照和模式演进的表。每次提交只替换一个小指针，很像更新页表，因此多个引擎可以安全地共享同一份数据。（[第 7 章](../01-data-systems-foundations/ch07-open-table-formats.md)）

**12. Apache Iceberg.** 诞生于 Netflix 的开放表格式，它把一张表跟踪为一棵元数据文件树，并依赖目录来完成原子提交。它已成为中立的行业标准，相当于表格领域的 JEDEC；2024 年 6 月，Databricks 以媒体报道的约 $2B 收购了其创建者的公司 Tabular。[^tabular]（[第 7 章](../01-data-systems-foundations/ch07-open-table-formats.md)）

**13. Delta Lake.** Databricks 的开放表格式：Parquet 文件加上一个有序的 JSON 提交日志，并定期生成检查点，就像带定期试算平衡的日记账。它在 Databricks 环境中占主导地位，而 UniForm 让 Delta 表也能发布 Iceberg 元数据，供其他引擎使用。（[第 7 章](../01-data-systems-foundations/ch07-open-table-formats.md)、[第 25 章](../04-company-deep-dives/ch25-databricks.md)）

**14. Apache Hudi.** 来自 Uber 的表格式，围绕操作时间线构建，并针对更新插入（upsert）和流式数据摄取进行了调优。它擅长处理频繁的行级变更，但在三者中商业生态最小，就像一个客户寥寥的专用工艺节点。（[第 7 章](../01-data-systems-foundations/ch07-open-table-formats.md)）

**15. Catalog（目录）.** 记录有哪些表、其当前元数据存放在哪里以及谁可以读取它们的服务；对于 Iceberg，它还负责执行提交。每个引擎都要先问它，因此它是湖仓一体的控制点，就像股份登记机构，其登记簿决定了所有权。（[第 8 章](../01-data-systems-foundations/ch08-catalogs-and-metastores.md)）

**16. Unity Catalog.** Databricks 面向表、文件、模型和函数的治理目录，负责权限、数据血缘、审计和短期存储凭证，并有一个开源版本。即使数据以开放格式存放，Databricks 也正是借此保持对策略的控制，就像握有钥匙的房东控制着一栋开放式布局的大楼。（[第 8 章](../01-data-systems-foundations/ch08-catalogs-and-metastores.md)、[第 25 章](../04-company-deep-dives/ch25-databricks.md)）

**17. Apache Polaris.** 由 Snowflake 于 2024 年捐赠的开源 Iceberg REST 目录，此后已晋升为 Apache 顶级项目。这是 Snowflake 以中立姿态争取成为其他引擎注册表的地方的尝试，而其更丰富的治理能力仍保留在专有的 Horizon 中，就像由一家厂商发起的标准组织。（[第 8 章](../01-data-systems-foundations/ch08-catalogs-and-metastores.md)、[第 27 章](../04-company-deep-dives/ch27-databricks-vs-snowflake.md)）

**18. Time travel（时间旅行，历史版本查询）.** 按照表在某个较早快照时的状态进行查询；之所以可行，是因为旧文件在快照过期之前一直保留。它服务于审计、可复现的机器学习训练集以及撤销错误的加载，而且成本低廉，原因与阵列快照相同：只有发生变化的数据才是新的。（[第 7 章](../01-data-systems-foundations/ch07-open-table-formats.md)）

**19. Compaction（压缩合并）.** 在后台把大量小文件重写为少量大文件，并执行快照过期和孤立文件清理。流式写入者不断产生小文件，因此这种类似 SSD 的垃圾回收，如今是湖仓一体运营成本和厂商差异化的主要所在。（[第 7 章](../01-data-systems-foundations/ch07-open-table-formats.md)）

## 数据管道

**20. ETL vs ELT.** 抽取-转换-加载（ETL）在数据落地之前对其进行重塑；抽取-加载-转换（ELT）先让原始数据落地，再在数据仓库内用 SQL 进行转换。廉价的云计算使 ELT 成为默认做法，并造就了 Fivetran 和 dbt 的市场，就像把原矿运到大型冶炼厂，而不是在矿山就地精炼。（[第 9 章](../02-pipelines-and-governance/ch09-pipeline-patterns.md)）

**21. Change data capture（变更数据捕获，CDC）.** 变更数据捕获（CDC）读取数据库的事务日志，并把每一次已提交的插入、更新和删除作为事件发出。它让分析只比生产系统落后几分钟，而又不给源系统增加负载，就像读取银行的实时流水，而不是每晚重新打印一次对账单。（[第 10 章](../02-pipelines-and-governance/ch10-ingestion-and-integration.md)）

**22. Apache Kafka.** 一个开源的分布式日志：生产者把事件追加到主题（topic）中，众多消费者各自独立读取，就像各个交易台读取同一条交易所行情带。它是默认的事件流骨干，而 IBM 已于 2026 年 3 月完成对 Kafka 主要厂商 Confluent 约 $11B 的收购。[^ibm-close]（[第 11 章](../02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)）

**23. Apache Flink.** 一个流处理引擎，在事件到达时对其持续运行关联、聚合和时间窗口计算，并提供托管状态和精确一次（exactly-once）保证。Kafka 负责搬运事件，Flink 负责对事件进行计算：一个是传送带，一个是传送带上的检测工位。（[第 11 章](../02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)）

**24. dbt.** 一个开源框架，分析师在其中编写 SQL SELECT"模型"，dbt 将其编译为依赖图，并在数据仓库内进行测试和运行。它把数据转换变成了有版本控制的工程工作（分析工程），就像每次改动都要跑回归测试的芯片设计流程。（[第 12 章](../02-pipelines-and-governance/ch12-transformation-and-orchestration.md)）

**25. Orchestration（编排）.** 编排器（Airflow、Dagster、Prefect）以有向无环图的形式，按依赖顺序调度、运行、重试并记录数据管道任务。它是数据领域的晶圆厂制造执行系统（MES）：很少光鲜亮丽，但早上 6 点的仪表盘一迟到，挨骂的总是它。（[第 12 章](../02-pipelines-and-governance/ch12-transformation-and-orchestration.md)）

**26. Reverse ETL（反向 ETL）.** 把数据仓库中建模好的数据同步回 CRM 或广告平台等运营工具，让一线团队据此采取行动。它让数据仓库既是数据的汇集地，也是数据的来源，就像一座同时经营配送车队的炼油厂；Fivetran 于 2025 年同意为此收购 Census。（[第 9 章](../02-pipelines-and-governance/ch09-pipeline-patterns.md)、[第 30 章](../04-company-deep-dives/ch30-data-movement-streaming-companies.md)）

**27. Zero-ETL（零 ETL）.** 由厂商管理的、从运营数据库到分析服务的复制（Aurora 到 Redshift、Fabric 镜像），客户无需自建任何数据管道。"零"指的是你不需要建管道，而不是零副本，就像银行的自动资金归集：钱仍然在移动。（[第 9 章](../02-pipelines-and-governance/ch09-pipeline-patterns.md)）

**28. Data contract（数据契约）.** 一份由数据生产方负责并强制执行的协议，约定数据集的模式、含义和质量，并在变更发布之前自动检查。它把质量责任前移给那些可能破坏数据的工程师，就像芯片模块之间的接口规范：改动一个引脚，集成测试就会失败。（[第 12 章](../02-pipelines-and-governance/ch12-transformation-and-orchestration.md)、[第 13 章](../02-pipelines-and-governance/ch13-data-quality-observability-lineage.md)）

**29. Data observability（数据可观测性）.** 对每张表的新鲜度、数据量、模式、值分布和数据血缘进行自动化监控，以便在用户发现之前捕捉到损坏的数据。其商业理由是"数据停机时间"，其工作方式就像晶圆厂的在线量测，在最终测试之前就捕捉到漂移。（[第 13 章](../02-pipelines-and-governance/ch13-data-quality-observability-lineage.md)）

**30. Data lineage（数据血缘）.** 描述数据如何从源头经过各种转换流向仪表盘和模型的图，越来越多地细化到列级。它回答"如果我改了这个，什么会坏？"和"这个数字是从哪里来的？"，相当于从一个报告数字追溯回其会计分录的审计轨迹。（[第 13 章](../02-pipelines-and-governance/ch13-data-quality-observability-lineage.md)）

**31. Semantic layer（语义层）.** 一套受治理的业务定义，例如"收入"或"活跃客户"，所有 BI 工具和 AI 智能体都查询它，而不是各自重新推导。在 AI 时代它更加重要，因为直接编写原始 SQL 的模型只能猜测定义；语义层就是会计科目表。（[第 14 章](../02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)）

## 数据治理

**32. RBAC vs ABAC（基于角色与基于属性的访问控制）.** 基于角色的访问控制（RBAC）把权限授予角色；基于属性的访问控制（ABAC）则根据敏感度标签、区域和用途等属性对每个请求作出决定。规模一大，RBAC 就会膨胀出成千上万个角色，而 ABAC 通过标签实现扩展，就像办公室钥匙与检查安全级别的门禁读卡器之间的区别。（[第 15 章](../02-pipelines-and-governance/ch15-governance-security-privacy.md)）

**33. DSPM（数据安全态势管理）.** 数据安全态势管理（DSPM）持续发现敏感数据存放在哪里、谁能够接触它以及其暴露程度，覆盖各个云、SaaS 和本地存储。它相当于审计前的存货盘点；Proofpoint 待完成的 Varonis 交易于 2026 年 10 月宣布，交易价值约 $6.3B（股权价值约 $5.71B；预计 2027 年上半年完成交割），为该类别定了价。[^varonis]（[第 15 章](../02-pipelines-and-governance/ch15-governance-security-privacy.md)、[第 33 章](../04-company-deep-dives/ch33-governance-catalog-security-companies.md)）

**34. Data classification（数据分类）.** 按类型和敏感度（电子邮件地址、卡号、健康记录）给数据贴标签，使策略附着在标签上，而不是附着在每一张表上。分类器结合模式匹配、校验和以及机器学习模型，而规则随标签而行，就像集装箱上的危险品标识。（[第 15 章](../02-pipelines-and-governance/ch15-governance-security-privacy.md)）

**35. Masking vs tokenization（脱敏与令牌化）.** 动态脱敏根据查询者的身份在查询时改写敏感值（`****1234`）；令牌化则用一个替代值取代存储的原值，只有经授权的保险库才能将其还原。脱敏是视图上的磨砂玻璃；令牌化是保护每一份下游副本的保险箱。（[第 15 章](../02-pipelines-and-governance/ch15-governance-security-privacy.md)）

**36. EU AI Act（欧盟《人工智能法案》）.** Regulation (EU) 2024/1689 为 AI 系统规定了按风险分级的义务，其中包括高风险系统的训练数据治理（第 10 条）。在 2026 年 AI Omnibus 之后，这些义务自 2027 年 12 月 2 日（独立系统）和 2028 年 8 月 2 日（嵌入产品的系统）起生效，使数据血缘和质量记录成为合规证据，正如 SOX 对内部控制所起的作用。[^aiact][^omnibus]（[第 15 章](../02-pipelines-and-governance/ch15-governance-security-privacy.md)）

**37. Permission-aware retrieval（权限感知检索）.** 在查询时强制执行源系统的访问权限，使 AI 助手只检索提问用户本来就能直接打开的段落。没有它，检索就成了泄露人力资源文件夹的快捷方式；它就像一座逐本书核验借书证、而不只是在门口查验的图书馆。（[第 17 章](../03-ai-data-stack/ch17-unstructured-data-processing.md)、[第 19 章](../03-ai-data-stack/ch19-retrieval-architectures.md)）

## AI 数据

**38. Embedding（嵌入向量）.** 由模型生成的一串数字，长度从几百到几千不等，使相似的条目彼此靠近。嵌入让软件能够按含义而不是按精确字词进行搜索：它是含义的 GPS 坐标，"invoice"（发票）和"bill"（账单）只隔一个街区。（[第 18 章](../03-ai-data-stack/ch18-embeddings-and-vector-search.md)）

**39. Vector database vs vector index（向量数据库与向量索引）.** 向量索引（HNSW、IVF、DiskANN）是快速查找最近邻的数据结构；向量数据库则在索引之外包裹了存储、过滤、更新、访问控制和扩展能力。如今大多数主流数据库都自带索引，这挤压了独立向量数据库的空间，正如集成内存控制器挤压了独立北桥芯片。（[第 18 章](../03-ai-data-stack/ch18-embeddings-and-vector-search.md)）

**40. HNSW（分层可导航小世界图）.** Hierarchical Navigable Small World，一种分层图索引：搜索先在稀疏的上层跳跃，再在稠密的下层精细查找——先走高速公路，再走主干道，最后走本地街道。它是内存向量检索的默认选择，快速而准确，但很耗内存。（[第 18 章](../03-ai-data-stack/ch18-embeddings-and-vector-search.md)）

**41. DiskANN.** Microsoft 的图向量索引，把图和完整向量放在 SSD 上，只把压缩后的向量放在 RAM 中，从而在单台机器上实现十亿级向量检索。它把向量检索的成本从 DRAM 转移到 NAND，是存储层次结构的实际应用，这一点对存储厂商有直接意义。（[第 18 章](../03-ai-data-stack/ch18-embeddings-and-vector-search.md)、[第 24 章](../03-ai-data-stack/ch24-data-meets-compute-and-storage.md)）

**42. RAG（检索增强生成）.** 检索增强生成（RAG）在提问时取回相关段落并加入提示词中，使大语言模型（LLM）依据你的数据而不是凭记忆作答。它就像开卷考试，是获得最新、私有且可引用答案的最便宜途径，而质量更多取决于检索，而不是模型。（[第 19 章](../03-ai-data-stack/ch19-retrieval-architectures.md)）

**43. Reranking（重排序）.** 一个第二阶段模型（通常是交叉编码器）把查询与排名靠前的几十个候选逐一对照阅读，并按真实相关性重新排序。快速的第一轮换取召回率，较慢的第二轮换取精确率，就像先做晶圆探针测试，再做最终测试。（[第 19 章](../03-ai-data-stack/ch19-retrieval-architectures.md)）

**44. GraphRAG.** Microsoft Research 于 2024 年提出的方法：由 LLM 把实体和关系抽取到知识图谱中，对聚类进行摘要，再基于该结构进行检索。它有助于回答需要跨大量文档"串联线索"的问题，但索引成本高得多，就像分析师手中的交易关系图与一摞申报文件之间的区别。（[第 19 章](../03-ai-data-stack/ch19-retrieval-architectures.md)）

**45. Context engineering（上下文工程）.** 在每一次模型调用时决定哪些指令、检索到的数据、工具结果和记忆进入有限的上下文窗口，以及以什么顺序进入。它已经取代提示词措辞，成为提升智能体质量的主要杠杆，因为冗长嘈杂的上下文会降低模型表现；它就是对模型最快一级存储的缓存管理。（[第 16 章](../03-ai-data-stack/ch16-ai-data-lifecycle.md)、[第 22 章](../03-ai-data-stack/ch22-agents-and-data.md)）

**46. MCP（模型上下文协议）.** 模型上下文协议（MCP）是一项通过"MCP 服务器"把 AI 应用连接到工具和数据的开放标准，由 Anthropic 于 2024 年 11 月推出，并于 2025 年 12 月捐赠给 Linux Foundation 旗下的 Agentic AI Foundation。[^mcp] 它是智能体的 USB-C：做好一个连接器，任何兼容的智能体都能使用，这也是为什么大多数主要数据厂商如今都提供 MCP 服务器。（[第 22 章](../03-ai-data-stack/ch22-agents-and-data.md)）

**47. Text-to-SQL（文本转 SQL）.** 由 LLM 把一个用自然英语提出的问题翻译成 SQL 查询。演示很容易，生产很难，因为在真实的企业模式上准确率会下降，除非模型以语义层为依据，就像一位精通 SQL 却不了解你们会计科目表的新分析师。（[第 14 章](../02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)、[第 22 章](../03-ai-data-stack/ch22-agents-and-data.md)）

**48. Feature store（特征存储）.** 一个对每个机器学习特征（例如"过去七天的交易笔数"）只定义一次，并向训练（离线）和实时预测（在线）提供完全相同取值的系统。它防止训练与服务之间的偏差，充当测试和生产共同校准的黄金基准；作为一个独立类别，它已经在很大程度上被平台吸收。（[第 21 章](../03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)）

**49. RLHF data（RLHF 数据）.** 人类反馈强化学习（RLHF）以一个奖励模型为目标来调优模型，而该奖励模型是用人类对"哪个回答更好"的判断训练出来的。稀缺的投入是偏好数据和专家数据，这就是数据标注公司和专家网络公司能获得高估值的原因；它相当于良率学习，工程师的判断变成了训练信号。（[第 20 章](../03-ai-data-stack/ch20-training-data-supply-chain.md)）

**50. Hybrid search（混合检索）.** 把关键词检索（BM25）与向量检索结合起来，并合并两份排序列表，通常采用倒数排名融合（reciprocal rank fusion）。关键词能抓住嵌入会模糊掉的精确零件号和名称，向量能抓住同义改写，就像一只基金把量化筛选与分析师判断相结合。（[第 18 章](../03-ai-data-stack/ch18-embeddings-and-vector-search.md)）

## 商业

**51. DBU（Databricks 单位）.** Databricks Unit（DBU）是一种按小时计的标准化处理量单位，定价从传统作业计算（classic jobs compute）的约 $0.15 到无服务器 SQL 的约 $0.70 不等（第三方整理的美国标价）。[^dbx-pricing] 可以把它想象成千瓦时：一块电表，不同工作负载适用不同的电价。（[第 25 章](../04-company-deep-dives/ch25-databricks.md)、[第 35 章](../05-business-and-economics/ch35-business-models.md)）

**52. Snowflake credit（Snowflake 积分）.** Snowflake 的计算单位：正在运行的虚拟仓库按秒消耗积分，规格每升一档，每小时费率翻一倍，而每个积分的价格取决于版本和区域。客户通常预先承诺购买积分，Snowflake 只在积分被消耗时才确认收入，就像预付费的手机通话分钟数。（[第 26 章](../04-company-deep-dives/ch26-snowflake.md)、[第 35 章](../05-business-and-economics/ch35-business-models.md)）

**53. Consumption model（按用量计费模式）.** 客户按实际使用量付费，而不是按席位或许可证付费，因此收入跟随工作负载变化。它把价格与价值挂钩，并让小额交易得以成长，但也使收入更难预测，并把客户的优化行为转化为增长放缓：这是收费公路，而不是租约。（[第 35 章](../05-business-and-economics/ch35-business-models.md)）

**54. NRR（净收入留存率）.** 净收入留存率（NRR）是去年那批客户今年带来的收入，除以同一批客户一年前带来的收入，包含扩张并扣除缩减和流失：相当于软件行业的同店销售额。Snowflake 披露 Q2 FY2027（2026 年 5–7 月，公司 KPI）的 NRR 为 126%，低于 FY2022 的 178% 峰值和 FY2023 的 158%。[^sf-q2][^sf-hist]（[第 36 章](../05-business-and-economics/ch36-unit-economics-kpis.md)）

**55. RPO（剩余履约义务）.** 剩余履约义务（RPO）是已签约但尚未确认的收入：即在手订单。Snowflake 在 Q2 FY2027 的 RPO 约为 $9.0B（GAAP；其中约 54% 预计在 12 个月内确认，即当期部分 cRPO），低于 FY2026 年末的 $9.77B。这一下降部分是季节性的：许多续约在财年 Q4 签订，随后在 Q1–Q2 被消耗的速度快于新承诺到来的速度。[^sf-q2]（[第 36 章](../05-business-and-economics/ch36-unit-economics-kpis.md)）

**56. Cloud COGS（云销货成本）.** 对于云数据平台而言，销货成本（COGS）主要是支付给超大规模云厂商的账单，用于运行客户查询所需的计算、存储和网络。毛利率是在一项厂商无法控制的成本之上获得的溢价，相当于无晶圆厂公司的晶圆成本，而承诺消费额度协议就是它的长期晶圆协议。（[第 36 章](../05-business-and-economics/ch36-unit-economics-kpis.md)）

**57. Rule of 40（40 法则）.** 收入增速加上自由现金流利润率应至少达到 40%，这是检验增长是否靠花钱买来的快速测试。Snowflake 得分约 58（Q2 FY2027 GAAP 收入增速 35%，加上 23% 的全年调整后 FCF 利润率指引），Palantir 披露的得分为 155%（公司披露，Q2 2026）。[^r40][^pltr]（[第 36 章](../05-business-and-economics/ch36-unit-economics-kpis.md)）

**58. EV/NTM revenue（EV/未来 12 个月收入）.** 企业价值除以预期未来十二个月收入，相当于尚无可观 EBITDA 的公司的 EV/EBITDA。2026 年 10 月 30 日，Snowflake 的交易倍数接近 16.9x，Palantir 接近 53x（以 FY2026 指引为基础；按过去 12 个月收入计约为 70x），两者都基于由指引推导出的未来 12 个月估算值。[^comps]（[第 37 章](../05-business-and-economics/ch37-public-comps-valuation.md)）

**59. Run-rate vs ARR（年化运行率与 ARR）.** 收入年化运行率把最近一个季度或月份的全部收入（包括用量收入）年化；年度经常性收入（ARR）则把已签约的订阅价值年化。Databricks 的">$7B 收入年化运行率"（公司披露，2026 年 8 月）既不是 ARR，也不是经审计的 GAAP 收入，正如晶圆厂某一个月的强劲产出并不等于一份已签署的长期协议。[^db-7b]（[第 25 章](../04-company-deep-dives/ch25-databricks.md)、[第 36 章](../05-business-and-economics/ch36-unit-economics-kpis.md)）

**60. Open core（开放核心）.** 免费开放开源核心，围绕它销售专有功能、托管服务或支持，Databricks（Spark）、Confluent（Kafka）和 MongoDB 都是这么做的。它能以低成本推动采用，就像用免费的参考设计来卖芯片，但超大规模云厂商同样可以托管这个免费核心。（[第 38 章](../05-business-and-economics/ch38-open-source-strategy.md)）

**61. SSPL and BSL（SSPL 与 BSL 许可）.** 两种源码可见许可，用于阻止竞争对手（主要是超大规模云厂商）将软件作为服务出售：MongoDB 的 Server Side Public License（2018）要求公开整个服务栈，而 Business Source License 在某个变更日期之前限制生产用途。两者都不是 OSI 认可的开源许可；可以把它们看作带有使用领域限制条款的专利许可。（[第 38 章](../05-business-and-economics/ch38-open-source-strategy.md)）

## 公司

**62. Databricks.** 湖仓一体公司，由 Apache Spark 的创建者创立，基于开放格式销售数据工程、数据仓库、数据治理（Unity Catalog）、Postgres（Lakebase）和 AI 工具。2026 年 8 月，公司披露其收入年化运行率超过 $7B，增速超过 80%，并以 $190B 估值融资 $5B（公司披露）。[^db-7b]（[第 25 章](../04-company-deep-dives/ch25-databricks.md)）

**63. Snowflake.** 将存算分离商业化的云数据仓库，目前正扩展到 Iceberg、Postgres 和 AI 智能体（Snowflake CoWork）。Q2 FY2027（2026 年 5–7 月）产品收入约为 $1.49B，增长 37%（GAAP），FY2027 产品收入指引上调至 $6.07B（公司披露）。[^sf-q2]（[第 26 章](../04-company-deep-dives/ch26-snowflake.md)、[第 27 章](../04-company-deep-dives/ch27-databricks-vs-snowflake.md)）

**64. Microsoft Fabric.** Microsoft 的 SaaS 分析套件（数据管道、Spark、数据仓库、实时分析、Power BI），构建在 OneLake 之上——一个以 Delta 和 Parquet 格式存储、覆盖整个租户的数据湖。它的优势在于能够以一张容量账单分发到现有的 Power BI 和 Microsoft 365 环境中，就像一家把整块板卡打包销售的垂直整合器件制造商（IDM）。（[第 28 章](../04-company-deep-dives/ch28-hyperscaler-data-platforms.md)）

**65. BigQuery.** Google Cloud 的无服务器数据仓库，源自 Google 的 Dremel，按扫描的 TB 数或按槽位小时（slot-hour）计价。它所在的云业务分部在 Q3 2026 增长 103% 至 $30.7B（GAAP 分部收入），不过这一增长大部分可能来自 AI 算力和 TPU 销售；BigQuery 的份额未披露。[^goog-q3]（[第 28 章](../04-company-deep-dives/ch28-hyperscaler-data-platforms.md)）

**66. ClickHouse.** 一个源自 Yandex 的开源列式数据库，为极速实时分析而构建：相当于市场中的高主频芯片。其公司于 2026 年 1 月获得媒体报道的 $15B 估值，并于 2026 年 5 月披露 ARR 超过 $250M。[^ch-seriesd][^ch-arr]（[第 23 章](../03-ai-data-stack/ch23-real-time-analytics-htap.md)、[第 31 章](../04-company-deep-dives/ch31-analytical-engine-challengers-legacy.md)）

**67. DuckDB.** 一个进程内分析型数据库（"分析领域的 SQLite"），无需服务器即可在笔记本电脑、notebook 或应用程序内部运行，是数据世界里的边缘芯片。AWS 于 2026 年 8 月同意收购其背后的公司 DuckLabs，条款未披露；DuckDB 仍在 DuckDB Foundation 之下保持 MIT 许可。[^aws-duck]（[第 31 章](../04-company-deep-dives/ch31-analytical-engine-challengers-legacy.md)）

**68. Confluent.** 由 Kafka 创建者创立的公司，销售托管的 Kafka 和 Flink。FY2025（日历年）收入为 $1,166.7M，增长 21%（GAAP），其中 Confluent Cloud 贡献 $624M；IBM 于 2026 年 3 月 17 日完成了约 $11B 的收购。[^cflt][^ibm-close]（[第 30 章](../04-company-deep-dives/ch30-data-movement-streaming-companies.md)）

**69. Fivetran + dbt Labs.** Fivetran 的托管抽取与加载连接器与 dbt Labs 的数据转换框架进行了合并，这是一笔全股票交易，于 2025 年 10 月宣布、2026 年 6 月 1 日完成，合并后 ARR "接近 $600M"（公司披露）。[^ft-dbt-close] 这是现代数据栈的整合，正如当年单点工具型 EDA 厂商被并入套件。（[第 30 章](../04-company-deep-dives/ch30-data-movement-streaming-companies.md)、[第 43 章](../06-history-and-future/ch43-modern-data-stack.md)）

**70. Palantir.** 一种构建"本体（ontology）"的软件——本体是对客户业务对象及其允许操作的受治理模型——使操作人员和 AI 智能体通过它采取行动（Foundry、AIP）；在这里，语义层本身就是产品。Q2 2026 收入增长 93%（GAAP），股票交易倍数接近 53x EV/未来 12 个月收入（以 FY2026 指引为基础，估算；EV/过去 12 个月收入约为 70x）。[^pltr][^comps]（[第 34 章](../04-company-deep-dives/ch34-application-giants-data-platforms.md)）

**71. Everpure and 1touch（Everpure 与 1touch）.** Everpure（原 Pure Storage；NYSE: P）以 $125.0M 的披露现金对价收购了一家数据发现、数据分类和语义上下文公司 1touch；交易于 2026 年 5 月 7 日完成交割，并于 2026 年 6 月以 Everpure Data Intelligence 的名义重新发布。[^ep-10q][^ep-di] 这是一家存储厂商从"存储数据"走向"理解数据"；战略团队基于公开信息可能评估的选项见第 45 章。（[第 24 章](../03-ai-data-stack/ch24-data-meets-compute-and-storage.md)、[第 33 章](../04-company-deep-dives/ch33-governance-catalog-security-companies.md)、[第 45 章](../06-history-and-future/ch45-storage-moving-up-the-stack.md)）

## 概念之间如何关联

把这些一句话解释当作一条链条来记，比当作一张清单来记更容易。下面的流程图沿着一条路径，从存储上的字节一直走到智能体给出的答案。每个节点都是上文的一个条目，每个箭头都是一种依赖关系：右边的层只有在左边的层运作良好时才能运作良好。

```mermaid
flowchart LR
  subgraph Store["数据存放在哪里"]
    OBJ["对象存储"] --> PQ["Parquet 文件"]
    PQ --> ICE["Iceberg 或 Delta 表"]
    ICE --> CAT["目录<br/>Unity 或 Polaris"]
  end
  subgraph Move["数据如何流动"]
    WAL["预写日志"] --> CDC["CDC"]
    CDC --> KAF["Kafka 与 Flink"]
    KAF --> ICE
    DBT["dbt 模型"] --> ICE
  end
  subgraph Govern["谁可以使用数据"]
    CLS["数据分类与 DSPM"] --> POL["RBAC 与 ABAC 策略"]
  end
  subgraph Serve["AI 如何使用数据"]
    SEM["语义层"] --> MCP["MCP 服务器"]
    EMB["嵌入与向量索引"] --> RAG["RAG 与重排序"]
    RAG --> CTX["上下文工程"]
    MCP --> CTX
    CTX --> AGT["AI 智能体的回答"]
  end
  CAT --> SEM
  CAT --> POL
  POL --> MCP
  POL --> RAG
  PQ --> EMB
```

*图 49.5 — 从字节到答案。Parquet 通过 Iceberg 或 Delta 变成表。随后，目录成为语义层和访问策略共同依赖的控制点。智能体通过 MCP 和检索接触数据，而这两条路径都从目录继承数据治理。谁拥有目录和策略层，谁就处在每一个 AI 回答的关键路径上，这正是 Databricks、Snowflake 和存储厂商都在争夺它的原因。*

## 值得随身携带的数字

以下是本章中仅有的数字。每个数字都带有日期和标签；引用时要么照此引用，要么干脆不引用。

| 指标 | 数值 | 口径与期间 | 条目 |
|---|---|---|---|
| Databricks 收入年化运行率 | >$7B，增速 >80% | 公司披露的年化运行率，2026 年 8 月 | 59、62 |
| Databricks 估值 | $190B（$5B 融资轮） | 公司披露，私募融资轮于 2026-08-13 完成 | 62 |
| Snowflake 产品收入 | 约 $1.49B，+37% | GAAP，Q2 FY2027（2026 年 5–7 月） | 63 |
| Snowflake NRR | 126% | 公司 KPI，Q2 FY2027 | 54 |
| Snowflake RPO | 约 $9.0B（FY2026 年末为 $9.77B） | GAAP，Q2 FY2027 | 55 |
| Snowflake EV/未来 12 个月收入 | 约 16.9x | 估算，基于指引推导的未来 12 个月收入，截至 2026-10-30 | 58 |
| Palantir EV/未来 12 个月收入 | 约 53x | 估算，FY2026 指引中值，截至 2026-10-30 | 58、70 |
| Confluent 收入 | $1,166.7M，+21% | GAAP，FY2025（日历年） | 68 |
| IBM–Confluent 交易 | 约 $11B | 披露的企业价值，2026-03-17 完成交割 | 22、68 |
| ClickHouse 估值 | $15B | 媒体报道，2026 年 1 月 | 66 |
| Fivetran + dbt Labs ARR | 接近 $600M | 公司披露，2026 年 6 月 | 69 |
| Everpure–1touch | $125.0M | 披露的现金对价（10-Q），2026-05-07 完成交割 | 71 |

*图 49.6 — 值得随身携带的数字。十二行中出现了四种不同的标签（GAAP、公司披露、媒体报道、估算），把它们混为一谈，是一个听起来正确的数字变成错误论断最常见的方式。*

## 最常被混淆的概念对

| 人们常说 | 实际情况 | 为何重要 | 条目 |
|---|---|---|---|
| 说 Databricks "ARR 为 $7B" | 这是公司披露的**收入年化运行率**（近期收入的年化值，包含用量收入），既不是 ARR，也不是 GAAP 收入 | 把 ARR 倍数套用到用量型年化运行率上，会高估收入的持久性 | 59 |
| 把"数据湖"和"湖仓一体"当作同义词 | 湖仓一体是数据湖**加上**提供事务和数据治理的表格式与目录 | 价值以及厂商锁定都存在于元数据层 | 10 |
| 把任何向量检索都叫作"向量数据库" | 向量**索引**是一种数据结构。向量**数据库**是围绕索引构建的完整系统 | 如今大多数在位厂商都提供向量索引，这挤压了独立向量数据库的空间 | 39 |
| "零 ETL 意味着没有副本" | 它的意思是**无需你自建管道**。数据仍然被复制并存储两份 | 存储和出口流量费并不会消失 | 27 |
| "RPO 就是明年的收入" | RPO 是**全部**已签约但未确认的收入，其中只有一部分落在未来 12 个月内 | RPO 下降而收入上升，可能是健康的额度消耗，而不是需求崩塌 | 55 |
| "开源意味着谁都可以托管它" | SSPL 和 BSL 是**源码可见**许可，禁止提供竞争性的托管服务 | 许可证的选择决定了超大规模云厂商能否拿走这部分收入 | 61 |
| "脱敏和令牌化是一回事" | 脱敏是在**查询时**隐藏值。令牌化是替换**存储的**值 | 只有令牌化能保护下游副本 | 35 |
| "MCP 是一个智能体框架" | MCP 是智能体与工具或数据之间的**连接协议** | 价值归属于拥有服务器及其背后权限的一方 | 46 |
| "EU AI Act 高风险规则自 2026 年 8 月起适用" | 2026 年的 Omnibus 已将其推迟至 **2027 年 12 月 2 日和 2028 年 8 月 2 日** | 弄错合规日期会削弱任何数据治理方面的推介 | 36 |

*图 49.7 — 最常被混淆的概念对。每一行都是一条"不要这样说"。中间一列是 30 秒内的纠正说法，条目编号指向完整的一句话解释。*

## 关键术语

- [OLTP](../glossary.md#oltp) 与 [OLAP](../glossary.md#olap) — 事务型工作负载与分析型工作负载。
- [B 树（B-tree）](../glossary.md#b-tree)与 [LSM 树（LSM-tree）](../glossary.md#lsm-tree) — 读优化与写优化的索引结构。
- [MVCC](../glossary.md#mvcc) — 保留多个行版本，使读者与写入者互不阻塞。
- [列式存储（Columnar storage）](../glossary.md#columnar-storage)与[向量化执行（Vectorized execution）](../glossary.md#vectorized-execution) — 分析引擎速度快的两个原因。
- [存算分离（Separation of storage and compute）](../glossary.md#separation-of-storage-and-compute) — 共享的持久化存储，弹性的计算。
- [Apache Parquet](../glossary.md#apache-parquet) 与 [Apache Arrow](../glossary.md#apache-arrow) — 磁盘上和内存中的列式格式。
- [预写日志（Write-ahead log）](../glossary.md#write-ahead-log) — 持久化的变更日志，同时为 CDC 提供数据。
- [湖仓一体（Lakehouse）](../glossary.md#lakehouse)与[数据湖（Data lake）](../glossary.md#data-lake) — 有或没有表格式与目录层的开放文件。
- [开放表格式（Open table format）](../glossary.md#open-table-format)、[Apache Iceberg](../glossary.md#apache-iceberg)、[Delta Lake](../glossary.md#delta-lake) 与 [Apache Hudi](../glossary.md#apache-hudi) — 把文件变成表的元数据层。
- [数据目录（Data catalog）](../glossary.md#data-catalog)、[Unity Catalog](../glossary.md#unity-catalog) 与 [Apache Polaris](../glossary.md#apache-polaris) — 湖仓一体的控制点。
- [时间旅行（Time travel）](../glossary.md#time-travel)与[压缩合并（Compaction）](../glossary.md#compaction) — 快照查询与表维护。
- [ETL](../glossary.md#etl)、[ELT](../glossary.md#elt)、[反向 ETL（Reverse ETL）](../glossary.md#reverse-etl)与[零 ETL（Zero-ETL）](../glossary.md#zero-etl) — 主要的数据移动模式。
- [变更数据捕获（Change data capture）](../glossary.md#change-data-capture)、[Apache Kafka](../glossary.md#apache-kafka) 与 [Apache Flink](../glossary.md#apache-flink) — 基于日志的捕获、事件传输与流计算。
- [dbt](../glossary.md#dbt) 与[编排器（Orchestrator）](../glossary.md#orchestrator) — 以代码方式进行数据转换，以及运行它的调度器。
- [数据契约（Data contract）](../glossary.md#data-contract)、[数据可观测性（Data observability）](../glossary.md#data-observability)与[数据血缘（Data lineage）](../glossary.md#data-lineage) — 预防、发现和追溯坏数据。
- [语义层（Semantic layer）](../glossary.md#semantic-layer) — 面向 BI 和 AI 的受治理业务定义。
- [基于角色的访问控制（Role-based access control）](../glossary.md#role-based-access-control)与[基于属性的访问控制（Attribute-based access control）](../glossary.md#attribute-based-access-control) — 角色授权与属性驱动的策略。
- [数据安全态势管理（Data security posture management）](../glossary.md#data-security-posture-management)与[数据分类（Data classification）](../glossary.md#data-classification) — 发现敏感数据并为其贴标签。
- [动态数据脱敏（Dynamic data masking）](../glossary.md#dynamic-data-masking)与[令牌化（Tokenization）](../glossary.md#tokenization) — 隐藏视图与替换存储值。
- [EU AI Act](../glossary.md#eu-ai-act) — 欧盟按风险分级的 AI 监管法规，包含训练数据治理义务。
- [权限感知检索（Permission-aware retrieval）](../glossary.md#permission-aware-retrieval) — 按用户强制执行源系统访问权限的检索。
- [嵌入（Embedding）](../glossary.md#embedding)、[向量索引（Vector index）](../glossary.md#vector-index)、[向量数据库（Vector database）](../glossary.md#vector-database)、[HNSW](../glossary.md#hnsw) 与 [DiskANN](../glossary.md#diskann) — 语义向量及检索它们的结构。
- [检索增强生成（Retrieval-augmented generation）](../glossary.md#retrieval-augmented-generation)、[重排序器（Reranker）](../glossary.md#reranker)、[GraphRAG](../glossary.md#graphrag) 与[混合检索（Hybrid search）](../glossary.md#hybrid-search) — 面向 LLM 的检索模式。
- [上下文工程（Context engineering）](../glossary.md#context-engineering)与[模型上下文协议（Model Context Protocol）](../glossary.md#model-context-protocol) — 什么内容进入模型的上下文窗口，以及连接工具和数据的标准接口。
- [文本转 SQL（Text-to-SQL）](../glossary.md#text-to-sql)与[特征存储（Feature store）](../glossary.md#feature-store) — 自然语言查询与一致的机器学习特征。
- [人类反馈强化学习（Reinforcement learning from human feedback）](../glossary.md#reinforcement-learning-from-human-feedback)与[偏好数据（Preference data）](../glossary.md#preference-data) — 把人类判断作为训练信号。
- [DBU](../glossary.md#dbu) 与 [Snowflake credit](../glossary.md#snowflake-credit) — 两种主要的用量计量单位。
- [按用量计费（Consumption pricing）](../glossary.md#consumption-pricing) — 按使用量付费，而不是按席位或许可证付费。
- [净收入留存率（Net revenue retention）](../glossary.md#net-revenue-retention)与[剩余履约义务（Remaining performance obligations）](../glossary.md#remaining-performance-obligations) — 客户群组扩张与已签约的积压订单。
- [云 COGS（Cloud COGS）](../glossary.md#cloud-cogs)与[40 法则（Rule of 40）](../glossary.md#rule-of-40) — 毛利率背后的超大规模云厂商账单，以及"增长加现金"测试。
- [EV/未来 12 个月收入（EV to NTM revenue）](../glossary.md#ev-to-ntm-revenue)、[收入年化运行率（Revenue run-rate）](../glossary.md#revenue-run-rate)与[年度经常性收入（Annual recurring revenue）](../glossary.md#annual-recurring-revenue) — 估值倍数以及两个最常被混淆的收入指标。
- [开放核心（Open core）](../glossary.md#open-core)、[SSPL](../glossary.md#sspl) 与 [Business Source License](../glossary.md#business-source-license) — 开源商业模式，以及阻止超大规模云厂商转售的许可证。
- [Microsoft Fabric](../glossary.md#microsoft-fabric)、[OneLake](../glossary.md#onelake) 与 [BigQuery](../glossary.md#bigquery) — 超大规模云厂商的分析平台。
