# 1. 数据技术栈全景图
> **深度：** L2 · **阅读时间：** 约 15 分钟 · **最后核实：** 2026-11-01 · **前置阅读：** 无（第一章）

## 要点速览（TL;DR）

- 企业数据工作可分为四类工作负载：**OLTP**（快速、正确地记录每一笔业务事件）、**OLAP**（扫描历史数据以回答问题）、**流处理（streaming）**（在事件发生时传输事件并做出响应）以及 **AI**（准备训练数据、对内容做嵌入与检索、为智能体提供上下文）。每一类对底层系统的要求都不同，因此各自发展出了独立的产品与厂商。
- 一笔客户订单在 AI 智能体能够谈论它之前，可能要经过六到八个系统。每经过一跳，它的形态都会改变（行、变更事件、列式文件、指标、向量），延迟会增加（从毫秒到秒，再到分钟），并且会再被复制一次。
- 技术栈之所以分化，是因为没有任何单一引擎能很好地服务所有访问模式。Stonebraker 与 Çetintemel 在 2005 年提出了这一论点，而市场在此后 15 年里证明了他们是对的。[^stonebraker]
- 大约从 2020 年起，技术栈开始重新聚合。推动这一趋势的有四股力量：湖仓一体（lakehouse，在对象存储上保存一份开放表）、HTAP、带扩展的 Postgres，以及需要在同一处同时获取运营数据与分析数据的 AI 智能体。厂商们如今争夺的是对合并后各层的控制权。
- 存储位于每一跳之下，目录与数据治理层则横跨所有环节。这两个横向层是控制权与数据引力不断积聚的地方，也是与 Everpure 最相关的部分。

## 为何重要（商业视角 + Everpure 视角）

数据行业的大多数争论，本质上都是关于一层在哪里结束、下一层从哪里开始的争论。Snowflake 对 Databricks、Postgres 对其他所有数据库、IBM 收购 Confluent、Fivetran 与 dbt Labs 合并：每一项都是在押注哪些环节会合并，以及谁将拥有合并后的那一层。IBM 于 2026-03-17 完成对 Confluent 的收购，企业价值约 $11B（已披露）。[^ibm-confluent] Fivetran 与 dbt Labs 于 2026-06-01 完成全股票合并，合并后的 ARR "接近 $600M"（公司披露）。[^fivetran-dbt] 这两笔交易都把下文所述数据旅程中的两跳压缩进了同一家厂商。只要手里有一张各跳的地图，交易逻辑就一目了然。

这张地图之所以重要还有第二个原因：预算跟着数据走。每一跳都是一个独立的费用项：数据库许可证或托管服务、按行计费的连接器费用、流处理集群、数据仓库 credits、BI 席位、向量数据库、模型 token。首席数据官的降本计划，大部分其实是一份减少环节或副本的计划。厂商推销的也是同一件事，只不过换成了"零 ETL"或"一份数据"的说法。

对 Everpure（原 Pure Storage；NYSE: P，原代码 PSTG）而言，关键在于存储并不是其中的某一跳，而是位于所有环节之下。OLTP 数据库的日志、Kafka broker 的磁盘、湖仓的对象存储、向量索引的闪存层，全都是存储，而且各自的性能特征不同。Everpure 在 2026 年的举措恰好落在这张地图正在变化的位置。它于 2026-02-23 更名，并以 $125.0M 现金收购了数据发现与分类公司 1touch（已披露；2026-05-07 完成交割）。[^everpure-1touch] 2026 年 6 月，它推出了 Data Stream 功能，在 FlashBlade 上借助 NVIDIA GPU 为 AI 数据管道对数据进行向量化。[^everpure-datastream] 这两项举措都是试图从最底层进入数据治理与 AI 环节。基于公开信息，一个战略团队会想知道：存储厂商可以可信地进入哪些环节，又应当通过合作进入哪些环节。后续章节将在 [第 24 章](../03-ai-data-stack/ch24-data-meets-compute-and-storage.md) 和 [第 45 章](../06-history-and-future/ch45-storage-moving-up-the-stack.md) 中回到这一话题。

## 工作原理

### 四类工作负载

**工作负载（workload）**是指软件读写数据的模式。四种模式几乎涵盖了全部企业数据工作，而它们把系统设计拉向相反的方向。

[OLTP](../glossary.md#oltp)（联机事务处理）记录业务事件：一笔订单、一次付款、一次库存调整。每个事务只涉及少量行，必须在毫秒级完成，并且绝不能丢失或重复执行。成千上万的用户同时进行这类操作。代表系统：PostgreSQL、MySQL、Oracle Database、SQL Server、Amazon Aurora、MongoDB、DynamoDB。其核心设计手段是[预写日志](../glossary.md#write-ahead-log)（WAL）：在数据库确认成功之前，每一项变更都会被追加到持久存储上的顺序日志中，因此即使崩溃也不会丢失已确认的订单。[第 3 章](ch03-database-internals.md) 和 [第 4 章](ch04-distributed-databases.md) 会做更深入的讨论。

[OLAP](../glossary.md#olap)（联机分析处理）回答跨越历史数据的问题，例如"过去三年按地区、按周统计的收入"。每个查询读取数百万乃至数十亿行，但只涉及少数几列，运行这类查询的是少数分析师或仪表盘。其设计手段是列式存储、压缩与并行扫描。代表系统：Snowflake、Databricks SQL、BigQuery、Redshift、ClickHouse、DuckDB，以及在[对象存储](../glossary.md#object-storage)上使用 Iceberg、Delta 等[开放表格式](../glossary.md#open-table-format)的[湖仓一体](../glossary.md#lakehouse)模式。参见 [第 5 章](ch05-analytical-engines.md)、[第 6 章](ch06-file-formats.md) 和 [第 7 章](ch07-open-table-formats.md)。

[事件流](../glossary.md#event-streaming)在系统之间持续传输事件，让软件能在数秒内做出反应：欺诈检测、库存告警、向数据仓库供数。其核心抽象是一个只追加、分区的日志，许多读取方可以按各自的节奏消费。LinkedIn 2011 年的 Kafka 论文描述了这一抽象，至今仍是范本。[^kafka] 代表系统：Apache Kafka（Confluent，现属 IBM）、Redpanda、Amazon Kinesis，以及用于流处理的 Apache Flink。参见 [第 11 章](../02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。

**AI 工作负载**是最新的一类，实际上包含三种子模式。*训练数据准备*受吞吐量约束，需要对以非结构化数据为主的海量数据进行扫描与转换。*嵌入与向量检索*把文本、图像和记录转换为[嵌入（向量）](../glossary.md#embedding)，并存入[向量索引](../glossary.md#vector-index)，以在数十毫秒内完成最近邻查找。*智能体上下文*是最新的子模式：[AI 智能体](../glossary.md#ai-agent)调用工具获取受治理的最新事实，而[模型上下文协议](../glossary.md#model-context-protocol)（MCP）已成为这类调用的标准接口。这一类工作负载的重要性超出了初看时的印象。一项被广泛引用、由 Box 赞助的 IDC 估算认为，2022 年各组织生成的数据中约 90% 是非结构化数据。[^idc] 经典的 OLTP 到 OLAP 数据管道从来不是为这类数据而建的。参见 [第 16 章](../03-ai-data-stack/ch16-ai-data-lifecycle.md)、[第 18 章](../03-ai-data-stack/ch18-embeddings-and-vector-search.md) 和 [第 22 章](../03-ai-data-stack/ch22-agents-and-data.md)。

| 维度 | OLTP（运营型） | OLAP（分析型） | 流处理 / 事件 | AI（准备、检索、智能体） |
|---|---|---|---|---|
| 核心问题 | "正确记录这一事件" | "在全部历史中发生了什么？" | "现在正在发生什么，谁需要知道？" | "哪些内容相关，模型应该看到什么？" |
| 典型延迟目标 | 每个事务个位数到数十毫秒 | 每个查询亚秒到数分钟 | 端到端毫秒到秒级 | 检索数十到数百毫秒；训练准备数小时到数天 |
| 每次操作涉及的数据 | 少量行 | 数百万到数十亿行，少数几列 | 一次一个事件，持续不断 | 批量准备：整个语料库；检索：top-k 文本块 |
| 并发度 | 数千到数百万用户 | 数十到数千个查询 | 每个主题有大量生产者与消费者 | 智能体每个任务可发出大量小查询 |
| 新鲜度 | 本身就是事实来源 | 滞后数分钟到一天 | 滞后数秒 | 滞后数分钟到数天，除非智能体查询实时系统 |
| 典型数据量 | GB 到数十 TB | TB 到 PB | 每天流转 TB 级，保留数天到数周 | 训练集达 PB 级；检索需数十亿向量 |
| 存储布局 | 行式页面、B 树或 LSM 树索引、WAL | 列式文件（Parquet），压缩、分区 | 只追加的分区日志段 | 准备阶段用文件与对象；向量用图或聚类索引 |
| 主要成本驱动因素 | 预置 IOPS、内存、高可用 | 每次扫描的计算（credits/DBU）、规模化存储 | Broker 计算、网络、跨可用区复制 | 用于嵌入与推理的 GPU；索引内存或闪存 |
| 代表系统 | Postgres、Aurora、MySQL、Oracle、MongoDB、DynamoDB | Snowflake、Databricks、BigQuery、Redshift、ClickHouse | Kafka、Confluent、Redpanda、Kinesis、Flink | Pinecone、pgvector、Elasticsearch、S3 Vectors、LanceDB、MCP 服务器 |

*图 1.1 — 四类工作负载的优化目标截然相反：OLTP 追求小而快且正确的写入；OLAP 追求宽表扫描；流处理追求持续传输；AI 追求在以非结构化为主的内容中找到相关性。*

```mermaid
quadrantChart
    title 延迟要求与数据量（示意性定位）
    x-axis "数据量小" --> "数据量极大"
    y-axis "延迟要求宽松" --> "延迟要求严格"
    quadrant-1 "难点 大规模下仍要快"
    quadrant-2 "运营型最佳区间"
    quadrant-3 "部门级报表"
    quadrant-4 "批量分析与训练"
    "Postgres OLTP": [0.18, 0.90]
    "MongoDB 与 DynamoDB": [0.35, 0.86]
    "Kafka 事件流": [0.58, 0.80]
    "RAG 向量检索": [0.62, 0.70]
    "实时 OLAP ClickHouse": [0.70, 0.62]
    "HTAP 引擎": [0.45, 0.72]
    "云数据仓库 BI": [0.75, 0.38]
    "湖仓批量 ETL": [0.85, 0.20]
    "LLM 训练数据准备": [0.95, 0.10]
    "电子表格与桌面 BI": [0.10, 0.25]
```

*图 1.2 — 大多数工作负载位于对角线附近；右上象限（超大数据量且延迟要求严格）是成本高昂的前沿地带，流处理、实时 OLAP 和向量检索如今都在这里竞争。*

> **类比：存储器层次结构。** 可以把这四类工作负载看作缓存层次结构中的各个层级。OLTP 是寄存器堆和 L1 缓存：容量小、数据热、延迟预算极小，正确性高于一切。数据仓库或湖仓是 DRAM，再往下是 NAND：容量大得多，以宽幅顺序扫描方式读取，每字节更便宜，也能容忍更高的延迟。存放在冷对象存储中的归档历史数据则相当于磁带和 HDD 层。连比例都相当吻合：一次 DRAM 访问约 100 ns，而一次 SSD 随机读取约 150 µs，慢约 1,500 倍。[^dean] OLTP 提交与数据仓库查询之间也相差类似的倍数。与芯片设计一样，数据按照温度在各层之间升级和降级，而大部分成本工程都在于让热数据保持小规模。

### 一个字节的旅程：一笔订单的端到端路径

以一家中等规模的在线零售商为例（示意）。下文所有时间与副本数量均为典型云部署下的**示意性估算**，并非对任何特定厂商的实测。一位客户在 10:00:00.000 于手机 App 中点击"下单"。

```mermaid
flowchart LR
    subgraph OPS["运营层"]
        A["手机 App"] --> B["OLTP 数据库<br/>Postgres 或 Aurora<br/>行 + WAL"]
    end
    subgraph MOVE["数据移动层"]
        B --> C["CDC<br/>Debezium 或 Fivetran"]
        C --> D["事件流<br/>Kafka 主题"]
    end
    subgraph ANALYTICS["分析层"]
        D --> E["湖仓原始表<br/>Iceberg 或 Delta"]
        E --> F["数据转换<br/>dbt 模型"]
        F --> G["语义层<br/>指标"]
        G --> H["BI 仪表盘"]
    end
    subgraph AI["AI 层"]
        F --> I["嵌入<br/>向量索引"]
        I --> J["RAG 检索"]
        G --> K["通过 MCP 的 AI 智能体"]
        J --> K
    end
    subgraph SPAN["横跨每一跳"]
        L["目录、数据血缘、<br/>访问策略"]
        M["存储：块、文件、<br/>对象、闪存"]
    end
    L -.-> B
    L -.-> E
    L -.-> G
    L -.-> K
    M -.-> B
    M -.-> D
    M -.-> E
    M -.-> I
```

*图 1.3 — 一个字节的旅程（SV-2）：一笔订单依次经过运营层、数据移动层、分析层和 AI 层，而目录层与存储层贯穿于每一跳之下。*

**第 1 跳 — App 到 OLTP（约 5–20 ms）。** App 调用订单服务。该服务对 Postgres 或 Aurora（如果订单以文档形式存储，则为 MongoDB）执行一个事务：插入订单行、插入订单明细、扣减库存、记录支付授权。在数据库回复"已提交"之前，它会把变更追加到 WAL 并刷写到持久存储。数据形态：行式页面中少量规范化的行。负责方：应用团队与运营型数据库厂商（[第 29 章](../04-company-deep-dives/ch29-operational-database-vendors.md)）。Aurora 还维护只读副本，AWS 称其复制延迟通常远低于 100 ms。[^aurora] 这是客户唯一需要等待的一跳。

**第 2 跳 — OLTP 到变更数据捕获（约 0.5–2 s）。** [变更数据捕获](../glossary.md#change-data-capture)（CDC）读取数据库自身的日志，而不是查询表。例如，Debezium 的 Postgres 连接器从 WAL 读取逻辑解码输出，把每一条已提交的行变更转换为一个变更事件，默认每张表对应一个 Kafka 主题。[^debezium] 形态发生变化：一行变成了一个*事件*，包含变更前后的值、操作类型和日志位置。Fivetran 等托管工具按计划执行同样的工作。其文档列明，Enterprise 和 Business Critical 套餐支持 1 分钟同步，其他套餐为 5 分钟同步。[^fivetran] 负责方：数据集成厂商（[第 9 章](../02-pipelines-and-governance/ch09-pipeline-patterns.md)、[第 10 章](../02-pipelines-and-governance/ch10-ingestion-and-integration.md)）。

**第 3 跳 — 流（增加毫秒级延迟，保留数天）。** 事件落入一个已复制的 Kafka 分区。欺诈评分、数据仓库加载程序、库存服务等下游读取方各自按自己的节奏读取。Kafka broker 的延迟很小。Confluent 自己在 2020 年的基准测试报告称，在 200 MB/s 下 p99 延迟为 5 ms（厂商自行测试）。[^confluent-bench] 形态：不可变、有序的日志记录。负责方：流处理平台（[第 30 章](../04-company-deep-dives/ch30-data-movement-streaming-companies.md)）。

**第 4 跳 — 落入湖仓或数据仓库（数秒到数分钟）。** 一个 sink 把事件写入对象存储上的 Iceberg 或 Delta 表，或写入数据仓库的原生表。这是第一次重大的形态变化：逐行的事件变成了*列式 Parquet 文件*加表元数据。如果每个事件都提交一次，就会产生数百万个小文件，因此写入方会进行批处理，这也是为什么这一跳是一个在新鲜度与效率之间权衡的调节旋钮。Snowflake 称其高性能 Snowpipe Streaming 的摄取到可查询时间为 5–10 秒。[^snowpipe] 湖仓每一到五分钟进行一次批量提交是常见做法（示意）。负责方：Databricks、Snowflake、超大规模云厂商（[第 25 章](../04-company-deep-dives/ch25-databricks.md)、[第 26 章](../04-company-deep-dives/ch26-snowflake.md)、[第 28 章](../04-company-deep-dives/ch28-hyperscaler-data-platforms.md)）。

**第 5 跳 — 数据转换（数分钟到一小时）。** dbt 模型（以依赖图组织的 SQL 文件）对原始变更事件进行清洗：去重、应用删除、把订单与客户和产品维度关联，并生成 `fct_orders` 之类整洁的事实表。这就是 [ELT](../glossary.md#elt) 模式：先加载，再在数据仓库内部转换。每 15–60 分钟运行一次增量任务是典型做法（示意）。负责方：数据转换与编排工具（[第 12 章](../02-pipelines-and-governance/ch12-transformation-and-orchestration.md)）。

**第 6 跳 — 语义层与 BI（每个仪表盘查询约 1–5 s）。** [语义层](../glossary.md#semantic-layer)对"净收入"或"活跃客户"只定义一次，从而让每个仪表盘和每个智能体都用同样的方式计算。订单变成了一个*聚合值*：对今天收入卡片的一份贡献。负责方：BI 与语义层厂商（[第 14 章](../02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)）。

**第 7 跳 — 嵌入与索引（数分钟到一天）。** 为了 AI 用途，订单的文本上下文会被切块、由模型生成嵌入，并写入向量索引。这些上下文包括产品描述、客户日后提交的客服工单以及适用的退货政策。形态：每个文本块对应一个由数百到数千个数字组成的*向量*，外加用于过滤的元数据。负责方：向量数据库、搜索与云厂商。Amazon 的 S3 Vectors 自 2025 年 12 月正式发布（GA），宣称每个索引最多支持 2B 个向量，查询延迟约 100 ms（公司披露）。[^s3-vectors] 参见 [第 17 章](../03-ai-data-stack/ch17-unstructured-data-processing.md) 和 [第 18 章](../03-ai-data-stack/ch18-embeddings-and-vector-search.md)。

**第 8 跳 — 检索与智能体（每个回答约 1–10 s）。** 三天后，客户问客服智能体："我的订单到哪了？那件夹克可以退吗？"智能体使用[检索增强生成](../glossary.md#retrieval-augmented-generation)（RAG）从向量索引中取出退货政策文本块；它调用一个 MCP 工具获取受治理的"订单状态"指标，或查询 OLTP 副本获取实时状态，然后组织答案。负责方：模型提供商、智能体平台，以及每一家推出 MCP 服务器的数据厂商（[第 19 章](../03-ai-data-stack/ch19-retrieval-architectures.md)、[第 22 章](../03-ai-data-stack/ch22-agents-and-data.md)）。

```mermaid
sequenceDiagram
    autonumber
    participant App as 手机 App
    participant DB as Postgres 或 Aurora
    participant CDC as Debezium CDC
    participant K as Kafka
    participant LH as 湖仓表
    participant T as dbt 数据转换
    participant BI as 语义层与 BI
    participant AG as AI 智能体
    App->>DB: 下单事务
    DB->>DB: 追加到 WAL 并刷写
    DB-->>App: 约 10 ms 内提交
    DB->>CDC: 通过逻辑解码读取 WAL 变更
    CDC->>K: 约 1 s 内发布变更事件
    K->>LH: Sink 每 1 到 5 分钟提交一批
    T->>LH: 每 15 到 60 分钟运行一次增量模型
    LH-->>BI: 一小时内刷新收入卡片
    Note over LH,AG: 嵌入任务每小时或每天为相关文本建立索引
    AG->>BI: 通过 MCP 工具调用获取受治理的订单指标
    AG->>DB: 可选，在副本上查询实时状态
    BI-->>AG: 约 1 s 内返回回答上下文
```

*图 1.4 — 订单示例的时间线（示意）：客户只需等待第一跳；之后的每一跳都以牺牲新鲜度换取更便宜、更广泛的访问。*

| 跳 | 数据形态 | 新增延迟（示意） | 相对成本驱动因素 | 该层的负责方 |
|---|---|---|---|---|
| 1. App → OLTP | 规范化的行 + WAL 记录 | 5–20 ms | 预置 IOPS、内存、高可用副本 | 运营型数据库厂商、超大规模云厂商 |
| 2. CDC | 变更事件（变更前/后、操作、日志位置） | 0.5 s 到 5 分钟 | 按行或按连接器收费 | 集成厂商、开源项目 |
| 3. 流 | 有序、已复制的日志记录 | 毫秒级（另加保留期） | Broker、网络、跨可用区流量 | 流处理平台 |
| 4. 落地 | 列式 Parquet 文件 + 表元数据 | 数秒到数分钟 | 对象存储、摄取计算 | 湖仓与数据仓库厂商 |
| 5. 数据转换 | 清洗后的事实表与维度表 | 15–60 分钟 | 每次运行的数据仓库计算 | 数据转换工具 |
| 6. 语义层/BI | 指标与聚合值 | 每个查询 1–5 s | 查询计算、BI 席位 | BI 与语义层厂商 |
| 7. 嵌入/索引 | 向量 + 元数据 | 数分钟到一天 | GPU 或 API 嵌入、索引内存/闪存 | 向量数据库、搜索、云厂商 |
| 8. 检索/智能体 | 提示词中的检索文本块 + 工具结果 | 每个回答 1–10 s | 模型 token、检索查询 | 模型与智能体平台 |

*图 1.5 — 每一跳都会改变数据的形态，并带来一个新的负责方和一张新的账单；到最后，这笔订单在各系统中大约存在六到八份副本（示意）。*

> **类比：晶圆穿过晶圆厂。** 一个字节的旅程就像一片晶圆依次经过各道工序。每一步（光刻、刻蚀、沉积、测试）都会增加下一步所依赖的价值，增加成本和周期时间，也会产生一个可能损失良率的环节。一次破坏 CDC 的模式变更就是一次失败的刻蚀，所有下游步骤都会继承这个缺陷。晶圆厂经济学揭示的两条教训，数据团队如今也在学习：交接越少，周期时间越短，良率损失越少；而量测（在这里指数据血缘与数据质量检查）只有覆盖每一个步骤，才能收回成本。

### 数据治理与目录位于何处

数据治理不是某一跳，而是一个触及每一跳的横向层。[数据目录](../glossary.md#data-catalog)记录每张表、每个主题、每个索引是什么、归谁所有以及是如何派生而来的（数据血缘）。策略引擎决定谁可以读取哪一列，例如对分析师隐藏客户的卡号，但对支付服务不隐藏。目录在开放湖仓中更加重要：当许多引擎读取同一批 Iceberg 表时，目录就成为提交表版本和执行访问控制的唯一场所。如今，策略往往在多个环节被重复实现：数据库授权、Kafka ACL、数据仓库角色、向量存储过滤器。这种重复正是数据治理厂商的机会，也是在技术栈底层对数据进行分类的存储厂商的机会。参见 [第 8 章](ch08-catalogs-and-metastores.md)、[第 13 章](../02-pipelines-and-governance/ch13-data-quality-observability-lineage.md) 和 [第 15 章](../02-pipelines-and-governance/ch15-governance-security-privacy.md)。

## 设计选择与权衡

### 技术栈为何走向分化

2005 年，Michael Stonebraker 与 Uğur Çetintemel 提出，作为万能解决方案出售的传统行存关系型数据库，终将输给为单一访问模式而打造的专用引擎。他们举的例子是流处理、列存数据仓库和文本检索。[^stonebraker] 其道理是物理层面的：让 10 行插入变得廉价的行式布局，会让 100 亿行的列扫描变得昂贵，反之亦然。为严格正确性而设计的加锁与日志机制，会拖慢批量分析。这篇论文在 2015 年获得了 ICDE 十年最具影响力论文奖。[^stonebraker] 此后 15 年验证了这一论断。列存（Vertica，之后是 Redshift 和 Snowflake）、NoSQL（MongoDB、Cassandra、DynamoDB）、流处理（Kafka）、搜索（Elasticsearch）以及后来的向量数据库，都从通用 RDBMS 手中夺走了份额。到 2020 年，a16z 那份广为流传的参考架构在数据源与仪表盘之间画了几十个方框。[^a16z] 这种专业化是理性的，但每多一个方框，就多一条数据管道、一份副本和一份契约。

### 技术栈为何重新聚合

四股力量正在把各个环节重新折叠到一起：

1. **湖仓一体。** CIDR 2021 的湖仓论文提出，把数据仓库的功能（ACID 事务、模式、索引）直接构建在廉价对象存储中的开放文件之上，这样一份副本就能同时服务 BI、数据科学和机器学习。[^lakehouse] 开放表格式让这一做法可以跨引擎工作，从而把第 4–5 跳中数据湖加数据仓库的两份独立副本合而为一。
2. **HTAP 与零 ETL。** Gartner 在 2014 年创造了混合事务分析处理（[HTAP](../glossary.md#htap)）一词，用来指在新鲜数据上同时运行两类工作负载的系统。[^htap] 如今的实现形式大多是隐藏第 2–4 跳的托管复制：Aurora 零 ETL 到 Redshift、BigQuery 从 Spanner 和 AlloyDB 复制、Snowflake 的 Postgres 镜像。参见 [第 23 章](../03-ai-data-stack/ch23-real-time-analytics-htap.md)。
3. **Postgres 加扩展。** Postgres 已成为默认的通用数据库。据报道，2025 年 Stack Overflow 调查发现 55.6% 的全体受访者和 58.2% 的专业开发者在使用它（二手报道；参见 [第 2 章](ch02-data-models.md)）。[^so2025] pgvector（向量）、TimescaleDB（时间序列）和列式插件等扩展，让一个引擎就能覆盖过去需要多个独立系统的工作负载。两家湖仓龙头都在 2025 年收购了 Postgres 公司。Databricks 收购了 Neon（约 $1B，媒体报道），现在报告 Lakebase 的收入年化运行率超过 $100M（公司披露）。Snowflake 收购了 Crunchy Data。[^databricks-lakebase][^crunchy]
4. **智能体。** 一个要回答"我的订单在哪里，我的客户终身价值是多少？"的智能体，需要在同一轮对话中同时获取实时运营状态和受治理的历史数据。这有利于那些在同一个访问控制模型下同时持有两者的平台。MCP 由 Anthropic 于 2024 年 11 月推出，并于 2025 年 12 月捐赠给 Linux Foundation 旗下的一个基金，它为每一层提供了一个统一的、供智能体调用的接口。[^mcp]

| 设计选择 | 专业化的最佳组合技术栈 | 融合平台 | 谁应该偏好哪一种 |
|---|---|---|---|
| 单一工作负载性能 | 最高：每个引擎都契合其访问模式 | 对多数场景足够好；在极端场景较弱 | 极端规模或延迟 → 专业化 |
| 副本与数据管道 | 很多；每一跳都复制数据 | 较少；尽可能只保留一份受治理的副本 | 对成本和合规敏感 → 融合 |
| 新鲜度 | 受最慢的管道环节限制 | 通过平台内复制达到秒到分钟级 | 智能体与运营分析 → 融合 |
| 厂商议价力 | 买方议价力高；任何方框都可替换 | 锁定程度更高，由开放格式部分抵消 | 拥有强大平台团队的企业 → 专业化 |
| 数据治理 | 每个系统重复实现 | 若共享目录，则只需一个策略模型 | 受监管行业 → 融合 |
| 创新速度 | 新品类以初创公司形式出现 | 平台复制或收购它们 | 早期采用者 → 专业化 |

*图 1.6 — 专业化在峰值性能和买方议价力上胜出；融合在副本数、新鲜度和数据治理上胜出。市场正朝着融合方向移动，但不会走到底。*

专业化的最强版本论证依然成立。融合以前就被许诺过。Oracle"一个数据库包揽一切"的说法从未终结专业化；一个在向量检索或高吞吐流处理上表现平庸的融合平台，会把这些工作负载输给专注型厂商。可能的结局是：少数几个以开放格式为核心的平台，再加上在性能值得付费的边缘地带活跃的专业厂商。

## 主要参与者

| 层（跳） | 代表系统与厂商 | 定位说明 |
|---|---|---|
| OLTP 数据库 | PostgreSQL（社区版；由 AWS、Azure、Google、Neon/Databricks、Supabase、Crunchy/Snowflake 提供托管）、Oracle、SQL Server、MySQL、MongoDB、DynamoDB、Aurora | Postgres 是引力中心；分析型平台如今也在销售 OLTP |
| CDC 与数据摄取 | Debezium（开源）、Fivetran（现已与 dbt Labs 合并）、Airbyte、Qlik/Striim、云原生零 ETL | 正被平台吸收，并与数据转换合并 |
| 流处理 | Apache Kafka、Confluent（自 2026 年 3 月起属于 IBM）、Redpanda、Amazon Kinesis、Apache Flink | 正迁移到对象存储上；向大厂商产品组合整合 |
| 湖仓与数据仓库 | Databricks、Snowflake、BigQuery、Redshift、Microsoft Fabric、ClickHouse、Starburst/Trino | 分析支出、并日益成为 AI 支出的引力中心 |
| 数据转换与编排 | dbt、SQLMesh、Apache Airflow、Dagster | 核心逻辑层；dbt 现已并入 Fivetran 合并体 |
| 语义层与 BI | Power BI、Tableau、Looker、dbt Semantic Layer、Cube、AtScale | 语义层被重新定位为"智能体的上下文" |
| 向量与检索 | Pinecone、Weaviate、Qdrant、Milvus/Zilliz、Elasticsearch、pgvector、S3 Vectors、LanceDB | 被夹在平台与对象存储向量层之间 |
| 智能体与 MCP | 模型提供商、智能体框架、数据厂商提供的 MCP 服务器 | 所有其他层的最新消费者 |
| 目录与数据治理（横跨各层） | Unity Catalog、Apache Polaris、Snowflake Horizon、AWS Glue/SageMaker Catalog、Collibra、Alation、Atlan、DSPM 厂商 | 开放湖仓的控制点 |
| 存储（位于每一跳之下） | 超大规模云厂商的对象存储与块存储、Everpure、NetApp、Dell、VAST Data 等 | 正向上进入数据分类与 AI 数据准备 |

*图 1.7 — 按环节划分的厂商类别。后续每一章各讲其中一行；第 4 部分对相关公司做专题剖析。*

## 历史与发展轨迹

```mermaid
timeline
    title 从一个数据库到多个数据库，再回归
    1970s to 1990s : 关系型 OLTP 占据主导 : 数据仓库每晚复制 OLTP 数据
    2005 : Stonebraker 与 Cetintemel 提出一刀切的时代已经结束
    2006 to 2012 : Hadoop 数据湖与 NoSQL 普及 : Kafka 在 LinkedIn 诞生
    2012 to 2016 : 云数据仓库实现存算分离 : Debezium 推广基于日志的 CDC
    2020 : a16z 现代数据栈参考架构 : 大量专用方框
    2021 : 湖仓论文发表于 CIDR : 开放表格式势头渐起
    2024 to 2025 : MCP 推出 : 平台收购 Postgres 公司
    2026 : IBM 完成收购 Confluent : Fivetran 与 dbt Labs 合并 : 存储厂商进军数据智能
```

*图 1.8 — 技术栈大约在 2005 年至 2020 年间走向分化，此后一直在重新聚合；2026 年的交易都是聚合型交易。*

这条轨迹可分为三个阶段。在**单体时代**（1970s–2000s），一个关系型数据库支撑整个业务；另有一个数据仓库每晚接收批量副本，所以"昨天"就是最新的分析答案。在**专业化时代**（约 2005–2020），Stonebraker 的论断得到印证：每种访问模式都有了自己的引擎和厂商，2010 年代后期的"现代数据栈"把云数据仓库、托管数据摄取、dbt 和 BI 工具拼接在一起。a16z 在 2020 年绘制了这张图，后来又做了更新。[^a16z] 分化对风险投资人来说是门好生意：每个方框都是一家初创公司。**融合时代**（2020 年至今）始于湖仓一体，并在 2025–2026 年随着平台收购 Postgres 公司、IBM–Confluent、Fivetran–dbt，以及需要一次性掌握整张地图的 AI 智能体而加速。[第 42 章](../06-history-and-future/ch42-history-of-databases.md) 和 [第 43 章](../06-history-and-future/ch43-modern-data-stack.md) 讲述完整的故事，[第 44 章](../06-history-and-future/ch44-future-trends.md) 评估融合会走多远。

## 关键数字

| 指标 | 数值 | 口径 | 来源 / 日期 |
|---|---|---|---|
| 组织数据中非结构化数据的占比 | ~90%（2022） | 分析师估算（IDC，Box 赞助） | IDC，经 StorageNewsletter，2023-09-07[^idc] |
| DRAM 访问与 SSD 随机读取 | ~100 ns 对 ~150 µs | 工程经验法则（约 2012 年） | Jeff Dean 延迟表[^dean] |
| Aurora 副本延迟 | 通常远低于 100 ms | 厂商文档 | AWS Aurora 文档[^aurora] |
| Kafka 在 200 MB/s 下的 p99 延迟 | 5 ms | 厂商自行测试的基准（2020，Kafka 2.6） | Confluent 博客[^confluent-bench] |
| Fivetran 最快同步间隔 | 1 分钟（Enterprise 及以上），5 分钟（其他套餐） | 厂商文档 | Fivetran 文档[^fivetran] |
| Snowpipe Streaming 摄取到可查询 | 5–10 s | 厂商文档（目标值，非 SLA） | Snowflake 文档，GA 2025-09-23[^snowpipe] |
| S3 Vectors 规模与延迟 | 每个索引最多 2B 个向量，查询 ~100 ms | 公司披露 | AWS，2025-12[^s3-vectors] |
| 开发者中的 Postgres 使用率 | 全体受访者 55.6%；专业开发者 58.2%（2025） | 调查，媒体报道 | Stack Overflow 调查，经二手来源[^so2025] |
| IBM–Confluent | 企业价值 ~$11B；2026-03-17 完成交割 | 已披露 | IBM 新闻稿，经 Stock Titan[^ibm-confluent] |
| Fivetran + dbt Labs 合并 ARR | "接近 $600M" | 公司披露 | Fivetran，2026-06-01[^fivetran-dbt] |
| Databricks Lakebase（Postgres） | 收入年化运行率 >$100M | 公司披露的年化运行率 | Databricks，2026-08-13[^databricks-lakebase] |

*图 1.9 — 延迟比例源于物理规律且相对稳定；市场数据每季度都会变化，使用前应重新核实。*

## 存储桥接

> **存储桥接。** 每一跳都运行在不同的存储特征之上。OLTP 需要低延迟、同步写入的块存储来承载 WAL。Kafka 需要顺序写入吞吐，并越来越多地使用对象存储来实现分层保留。湖仓需要高吞吐、兼容 S3 的对象存储，并具备良好的小对象和元数据性能。向量索引越来越多地放在闪存而非 DRAM 上。副本在整个旅程中不断倍增，因此存储容量随环节数量增长，而不仅仅随数据量增长。这是[数据引力](../glossary.md#data-gravity)的根源之一：Dave McCrory 约在 2010 年提出这一术语，指大型数据集会把应用和计算吸引到自己身边。[^mccrory] 关于介质与协议的细节，请参阅配套的 *Everpure Tech Atlas*。关于出口流量费与数据引力的经济学，参见 [第 24 章](../03-ai-data-stack/ch24-data-meets-compute-and-storage.md)；关于战略选项，参见 [第 45 章](../06-history-and-future/ch45-storage-moving-up-the-stack.md)。

## 如何阅读本书其余部分

| 部分 | 涵盖内容 | 从这里开始 |
|---|---|---|
| 第 0 部分 — 从这里开始 | 阅读路径与完整市场地图 | [第 0.2 章 市场地图](../00-start-here/ch00-2-market-map.md) |
| 第 1 部分 — 数据系统基础 | 数据模型、数据库内部机制、分析引擎、文件与表格式、目录 | [第 2 章 数据模型](ch02-data-models.md) |
| 第 2 部分 — 数据管道与数据治理 | CDC、数据摄取、流处理、数据转换、数据质量、语义层、安全 | [第 9 章 数据管道模式](../02-pipelines-and-governance/ch09-pipeline-patterns.md) |
| 第 3 部分 — AI 数据栈 | AI 数据生命周期、向量、RAG、智能体、HTAP、计算与存储 | [第 16 章 AI 数据生命周期](../03-ai-data-stack/ch16-ai-data-lifecycle.md) |
| 第 4 部分 — 公司深度剖析 | Databricks、Snowflake、超大规模云厂商、运营型数据库、流处理、AI 原生公司 | [第 25 章 Databricks](../04-company-deep-dives/ch25-databricks.md) |
| 第 5 部分 — 商业与经济 | 定价模式、KPI、可比公司、开源、并购史、GTM、市场规模 | [第 35 章 商业模式](../05-business-and-economics/ch35-business-models.md) |
| 第 6 部分 — 历史与未来 | 数据库史、现代数据栈、趋势、存储向上层演进 | [第 42 章 数据库史](../06-history-and-future/ch42-history-of-databases.md) |
| 第 7 部分 — 对话工具包 | 与数据从业者交流、尽职调查、问题库、一句话要点、记忆卡片 | [第 46 章 与数据从业者交流](../07-conversation-toolkit/ch46-talking-with-data-people.md) |

*图 1.10 — 一个字节的旅程是本书的主线：第 1–3 部分解释各个环节，第 4 部分讲述其负责方，第 5 部分讲经济学，第 6 部分讲演进方向。[第 39 章](../05-business-and-economics/ch39-ma-history.md) 汇总相关交易，[第 48 章](../07-conversation-toolkit/ch48-question-bank.md) 汇总相关问题。*

## 对话手册

**向产品经理提出的三个问题**

1. "请带我走一遍：一条记录是如何从你们客户的运营型数据库到达你们的产品的？中间有多少跳、多少份副本，你们消除了哪些？"好的回答会点出各个环节，坦承哪些环节仍然存在，并量化新鲜度（"Postgres 数据源端到端不到一分钟"）。
2. "哪一类工作负载是你们的核心，哪些是你们正在新增的？"好的回答会把他们为之打造引擎的核心工作负载，与他们现在能够"够用地"支持的相邻工作负载区分开来。这就是被诚实表述的融合叙事。
3. "策略在哪里执行：在你们的产品里、在目录里，还是在每一跳？"好的回答会指向一个通过开放目录共享的统一策略模型，而不是又一套新的角色体系。

**向工程师提出的三个问题**

1. "从提交到可查询，你们的端到端新鲜度是多少？由什么决定：CDC 轮询、流批处理还是表提交？"好的回答会点出瓶颈环节以及小文件方面的权衡。
2. "从数据源一直到向量索引，你们如何处理模式变更和删除？"好的回答会提到 CDC 对 DDL 的处理、表格式中的读时合并（merge-on-read）删除，以及对向量重新嵌入或打墓碑标记。很多团队对最后一步给不出答案，这本身就很说明问题。
3. "如果必须削减 30% 的成本，你会先压缩哪些环节？"好的回答通常针对重复副本（数据湖加数据仓库）、过于频繁的数据转换或闲置的流处理集群，而不是 OLTP 层。

**不要这样说**

- "OLAP 只不过是一个大号的 OLTP 数据库。"两者的物理布局恰恰相反，这正是 Stonebraker 的全部论点。
- "流处理会取代批处理。"大多数分析数据仍以分钟到小时级的批次进行转换。流处理为批处理供数，并负责实时的那一部分。
- "向量数据库是一个将取代数据仓库的新数据库品类。"检索只是一种访问模式，而且其中很大一部分正在迁移到 Postgres、搜索引擎、湖仓和对象存储中。
- "零 ETL 意味着没有数据管道。"它意味着厂商替你运行数据管道。各个环节依然存在，依然要花钱。
- "存储是技术栈底下的大宗商品。"每一跳都有独特的存储特征，而且副本会随环节倍增。

## 深入阅读

> **深入（L3）。** 阅读 2005 年 Stonebraker–Çetintemel 的论文以了解最初的性能论证，并阅读 CIDR 2021 的湖仓论文了解支持融合的反方论证。[^stonebraker][^lakehouse] 关于基于日志的 CDC 内部机制，请阅读 Debezium Postgres 连接器文档中关于复制槽、快照和逻辑解码的内容。[^debezium] 关于把日志作为核心抽象，请阅读 2011 年的 Kafka 论文，然后阅读 [第 11 章](../02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。关于 WAL 与 MVCC 的内部机制，参见 [第 3 章](ch03-database-internals.md)。

## 关键术语

- [OLTP](../glossary.md#oltp) — 联机事务处理：大量小规模、快速、正确的读写操作，用于记录业务事件。
- [OLAP](../glossary.md#olap) — 联机分析处理：跨历史数据的大规模扫描与聚合，通常基于列式存储。
- [预写日志](../glossary.md#write-ahead-log) — 在事务确认前先持久化的顺序变更日志；CDC 读取的数据源。
- [变更数据捕获](../glossary.md#change-data-capture) — 读取数据库日志，把每一项已提交的变更作为事件发送给下游系统。
- [事件流](../glossary.md#event-streaming) — 通过 Kafka 之类持久、分区、只追加的日志持续传输事件。
- [湖仓一体](../glossary.md#lakehouse) — 在对象存储的开放文件之上提供数据仓库功能（事务、模式、数据治理），用一份副本同时服务 BI 和 AI。
- [开放表格式](../glossary.md#open-table-format) — 一种元数据规范（Iceberg、Delta、Hudi），把一组 Parquet 文件变成一张支持事务的表。
- [对象存储](../glossary.md#object-storage) — 以 HTTP 寻址、扁平组织的不可变对象存储（S3 及兼容产品）；湖仓的基础。
- [ELT](../glossary.md#elt) — 抽取、加载，然后在数据仓库或湖仓内部进行转换。
- [语义层](../glossary.md#semantic-layer) — 对指标和实体的共享业务定义，供 BI 工具和智能体共同使用。
- [嵌入（向量）](../glossary.md#embedding) — 表示一段内容含义的数值向量。
- [向量索引](../glossary.md#vector-index) — 用于在嵌入上进行快速近似最近邻检索的数据结构。
- [检索增强生成](../glossary.md#retrieval-augmented-generation) — 在查询时获取相关内容并将其加入模型的提示词中。
- [AI 智能体](../glossary.md#ai-agent) — 由模型驱动、通过规划和调用工具（包括数据查询）来完成任务的程序。
- [模型上下文协议](../glossary.md#model-context-protocol) — 一项向 AI 智能体开放工具与数据的开放标准（MCP）。
- [HTAP](../glossary.md#htap) — 混合事务分析处理：由一个系统在新鲜数据上同时服务 OLTP 和 OLAP。
- [数据目录](../glossary.md#data-catalog) — 横跨整个技术栈、记录数据资产、所有者、数据血缘和访问策略的登记册。
- [数据引力](../glossary.md#data-gravity) — 大型数据集吸引应用、计算和更多数据向其靠拢的倾向。

## 资料来源

[^stonebraker]: Michael Stonebraker and Uğur Çetintemel, "'One Size Fits All': An Idea Whose Time Has Come and Gone," *Proceedings of the 21st International Conference on Data Engineering (ICDE 2005)*, Tokyo, pp. 2–11, IEEE, https://doi.org/10.1109/ICDE.2005.1，发布于 2005-04；获奖背景：Brown University CS, "Ugur Cetintemel Wins IEEE Data Engineering (ICDE) 2015 Influential Paper Award," https://cs.brown.edu/news/2015/02/27/ugur-cetintemel-wins-icde-2015-influential-paper-award/，发布于 2015-02-27；检索于 2026-11-01。[VERIFY: 核实该 DOI 是否指向这篇论文]
[^lakehouse]: Michael Armbrust, Ali Ghodsi, Reynold Xin, Matei Zaharia, "Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics," CIDR 2021, https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf，发布于 2021-01；检索于 2026-11-01。
[^debezium]: Debezium project, "Debezium connector for PostgreSQL"（参考文档）, https://debezium.io/documentation/reference/connectors/postgresql.html，无日期（持续更新的文档）；检索于 2026-11-01。
[^kafka]: Jay Kreps, Neha Narkhede, Jun Rao (LinkedIn), "Kafka: a Distributed Messaging System for Log Processing," NetDB 2011, Athens, https://people.csail.mit.edu/matei/courses/2015/6.S897/readings/kafka.pdf，发布于 2011-06；检索于 2026-11-01。
[^idc]: StorageNewsletter, "What Every Executive Needs to Know About Unstructured Data"（IDC 白皮书 *Untapped Value* 的摘要，由 Box 赞助）, https://www.storagenewsletter.com/2023/09/07/what-every-executive-needs-to-know-about-unstructured-data/，发布于 2023-09-07；检索于 2026-11-01。分析师估算；厂商赞助。
[^a16z]: Matt Bornstein, Jennifer Li, Martin Casado, "Emerging Architectures for Modern Data Infrastructure," Andreessen Horowitz, https://a16z.com/2020/10/15/emerging-architectures-for-modern-data-infrastructure/，发布于 2020-10-15；更新版见 https://a16z.com/emerging-architectures-for-modern-data-infrastructure/，发布于 2022 [VERIFY: 更新版的确切日期]；检索于 2026-11-01。
[^aurora]: Amazon Web Services, "Replication with Amazon Aurora," Amazon Aurora User Guide, https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html，无日期；检索于 2026-11-01。
[^confluent-bench]: Confluent, "Benchmarking Apache Kafka, Apache Pulsar, and RabbitMQ: Which is the Fastest?", https://www.confluent.io/blog/kafka-fastest-messaging-system/，发布于 2020 [VERIFY: 确切发布日期]；检索于 2026-11-01。厂商自行测试的基准。
[^fivetran]: Fivetran, "Sync Overview"（文档）, https://fivetran.com/docs/core-concepts/syncoverview，无日期；检索于 2026-11-01。
[^snowpipe]: Snowflake, "Snowpipe Streaming: High-Performance Architecture," https://docs.snowflake.com/en/user-guide/snowpipe-streaming-high-performance-overview，无日期；以及发布说明 "Snowpipe Streaming with high-performance architecture (General availability)," https://docs.snowflake.com/en/release-notes/2025/other/2025-09-23-snowpipe-streaming-high-performance-architecture，发布于 2025-09-23；检索于 2026-11-01。
[^s3-vectors]: Amazon Web Services, "Top announcements of AWS re:Invent 2025," AWS News Blog, https://aws.amazon.com/blogs/aws/top-announcements-of-aws-reinvent-2025，发布于 2025-12；Blocks & Files, "AWS piles on S3 upgrades from vector search to 50 TB objects," https://www.blocksandfiles.com/ai-ml/2025/12/03/aws-piles-on-s3-upgrades-from-vector-search-to-50-tb-objects/1704690，发布于 2025-12-03；检索于 2026-11-01。公司披露。
[^dean]: Jeff Dean (originally Peter Norvig), "Latency numbers every programmer should know," 社区转录版, https://gist.github.com/rtomayko/2847627，约 2012 年；检索于 2026-11-01。近似的工程经验法则；现代硬件有所不同。
[^htap]: Gartner, "Hybrid Transaction/Analytical Processing Will Foster Opportunities for Dramatic Business Innovation" (M. Pezzini, D. Feinberg, N. Rayner, R. Edjlali)，发布于 2014-01-28（付费内容；经 Wikipedia 引用, "Hybrid transactional/analytical processing," https://en.wikipedia.org/wiki/Hybrid_transactional/analytical_processing）；检索于 2026-11-01。二手来源。
[^so2025]: Enstacked, "Stack Overflow Developer Survey 2025 – Part 2," https://enstacked.com/stack-overflow-developer-survey-insights/，发布于 2025；检索于 2026-11-01。二手摘要 [VERIFY: 对照 survey.stackoverflow.co/2025 核实 58.2%]。
[^databricks-lakebase]: Databricks, "Databricks Grows >80% YoY, Surpasses $7B Revenue Run-Rate…," press release, https://www.databricks.com/company/newsroom/press-releases/databricks-grows-80-yoy-surpasses-7b-revenue-run-rate-scales，发布于 2026-08-13；Neon 收购价：TechRepublic, "Databricks to acquire Neon," https://www.techrepublic.com/article/news-databricks-neon-acquisition/，发布于 2025-05；检索于 2026-11-01。年化运行率为公司披露；Neon 收购价为媒体报道。
[^crunchy]: Snowflake Inc., Form 10-Q for the quarter ended 2025-10-31（Crunchy Data 收购，2025-06-06 完成交割）, SEC EDGAR, https://www.sec.gov/Archives/edgar/data/1640147/000164014725000211/snow-20251031.htm，发布于 2025-12；检索于 2026-11-01。
[^mcp]: Anthropic, "Introducing the Model Context Protocol," https://www.anthropic.com/news/model-context-protocol，发布于 2024-11-25；Anthropic, "Donating the Model Context Protocol and establishing the Agentic AI Foundation," https://anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation，发布于 2025-12-09；检索于 2026-11-01。
[^ibm-confluent]: IBM, "IBM Completes Acquisition of Confluent…," press release as syndicated by Stock Titan, https://www.stocktitan.net/news/IBM/ibm-completes-acquisition-of-confluent-making-real-time-data-the-lbuwdbharsqe.html，发布于 2026-03-17；检索于 2026-11-01。数值依据 `data/ma_deals.csv`（已披露，企业价值约 $11B）。
[^fivetran-dbt]: Fivetran, "Fivetran & dbt Labs Complete Merger to Create the Data Infrastructure for Trusted AI Agents," press release, https://www.fivetran.com/press/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents，发布于 2026-06-01；检索于 2026-11-01。ARR 为公司披露。
[^everpure-1touch]: World Wide Technology（转载 Pure Storage 新闻稿）, "Pure Storage rebrands to Everpure and announces intent to acquire 1touch," https://www.wwt.com/news/pure-storage-rebrands-to-everpure-and-announces-intent-to-acquire-1touch，发布于 2026-02-23；Everpure, Inc., Form 10-Q for the quarter ended 2026-05-03, SEC EDGAR, https://www.sec.gov/Archives/edgar/data/0001474432/000147443226000061/pstg-20260503.htm，发布于 2026-06；检索于 2026-11-01。
[^everpure-datastream]: Everpure via PR Newswire, "Everpure Unveils Data-Primacy Architecture for the AI Era," https://www.prnewswire.com/news-releases/everpure-unveils-data-primacy-architecture-for-the-ai-era-302803097.html，发布于 2026-06-17；检索于 2026-11-01。
[^mccrory]: InfoQ (Japan), "Data Gravity formula"（关于 Dave McCrory 2010 年提出的概念及其 2012 年的公式化）, https://www.infoq.com/jp/news/2012/07/datagravity-formula，发布于 2012-07；检索于 2026-11-01。二手来源。
