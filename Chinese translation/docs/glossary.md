# 术语表

> **共 712 个术语**，按 A–Z 排列。每个词条给出一条 L1 定义（一句可直接用于交流的话），并链接到详细讲解该术语的章节。本文件由 `scripts/build_glossary.py` 根据各章撰稿人提交的内容自动生成；如需修改，请编辑 `meta/glossary-terms.md` 或 `meta/glossary-extra.md`，而不是本文件。

[A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [Q](#q) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [Z](#z)

## A

<a id="access-control-list"></a>
### 访问控制列表（Access control list）

列出哪些用户和用户组可以访问某项资源、以及各自拥有何种权限的清单（ACL）。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="acid"></a>
### ACID

原子性、一致性、隔离性和持久性：保障数据库事务安全的四项特性。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="acl-propagation"></a>
### ACL 传播（ACL propagation）

将源文档的权限一并带到由其派生的每个文本块、向量和缓存答案上。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="acquihire"></a>
### 人才收购（Acquihire）

以招揽团队为主要目的、而非收购业务或产品的交易。*参见 [第 20 章](03-ai-data-stack/ch20-training-data-supply-chain.md)。*

<a id="active-metadata"></a>
### 主动元数据（Active metadata）

能够触发告警、策略变更或为智能体提供上下文等动作的元数据，而不仅仅是在目录门户中展示。*参见 [第 33 章](04-company-deep-dives/ch33-governance-catalog-security-companies.md)。*

<a id="adbc"></a>
### ADBC

Arrow Database Connectivity，一种以 Arrow 批次返回结果的数据库客户端 API，可视为 JDBC/ODBC 的列式对应物。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

<a id="adjusted-free-cash-flow"></a>
### 调整后自由现金流（Adjusted free cash flow）

在自由现金流基础上加回公司特定项目（例如因员工股权交易而缴纳的工资税）后的数值。*参见 [第 36 章](05-business-and-economics/ch36-unit-economics-kpis.md)。*

<a id="agent-bricks"></a>
### Agent Bricks

Databricks 推出的工具集，用于在受治理的企业数据上构建、评估并自动优化 AI 智能体。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="agent-memory"></a>
### 智能体记忆（Agent memory）

AI 智能体存放在上下文窗口之外、并可在后续步骤或会话中调取的信息。*参见 [第 22 章](03-ai-data-stack/ch22-agents-and-data.md)。*

<a id="agent2agent-protocol"></a>
### Agent2Agent 协议（Agent2Agent protocol）

一种开放协议（A2A），由 Google 于 2025 年推出、现归属 Linux Foundation，使 AI 智能体能够将任务委派给其他智能体。*参见 [第 22 章](03-ai-data-stack/ch22-agents-and-data.md)。*

<a id="agentforce"></a>
### Agentforce

Salesforce 的 AI 智能体平台，于 2024 年推出，起初按对话次数计费，后来改为按操作次数计费。*参见 [第 34 章](04-company-deep-dives/ch34-application-giants-data-platforms.md)。*

<a id="agentic-ai-foundation"></a>
### Agentic AI Foundation

Linux Foundation 旗下的定向基金，由 Anthropic、Block 和 OpenAI 共同创立，自 2025 年 12 月起负责治理 MCP。*参见 [第 22 章](03-ai-data-stack/ch22-agents-and-data.md)。*

<a id="agentic-identity"></a>
### 智能体身份（Agentic identity）

将 AI 智能体视为独立、可审计的主体，其权限永远不超过它所服务的用户。*参见 [第 22 章](03-ai-data-stack/ch22-agents-and-data.md)。*

<a id="agentic-rag"></a>
### 智能体式 RAG（Agentic RAG）

把检索作为一种工具开放给 AI 智能体反复调用，智能体不断改写查询、切换数据源，直到获得足够证据。*参见 [第 19 章](03-ai-data-stack/ch19-retrieval-architectures.md)。*

<a id="agentless-scanning"></a>
### 无代理扫描（Agentless scanning）

通过云服务商 API 和快照扫描云端数据，无需在主机上安装软件；这是 DSPM 的默认部署模式。*参见 [第 33 章](04-company-deep-dives/ch33-governance-catalog-security-companies.md)。*

<a id="aggregate-awareness"></a>
### 聚合感知（Aggregate awareness）

查询引擎在预先构建的较小汇总表足以回答请求时，将请求路由到该汇总表的能力。*参见 [第 14 章](02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)。*

<a id="agpl"></a>
### AGPL

GNU Affero 通用公共许可证，一种经 OSI 认可的著佐权（copyleft）许可证，其源代码共享义务同样适用于通过网络提供服务的软件。*参见 [第 29 章](04-company-deep-dives/ch29-operational-database-vendors.md)。*

<a id="ai-agent"></a>
### AI 智能体（AI agent）

由模型驱动、能够规划并调用工具（包括数据查询）以完成任务的程序。*参见 [第 01 章](01-data-systems-foundations/ch01-data-stack-map.md)。*

<a id="ai-factory"></a>
### AI 工厂（AI factory）

一个专用的 GPU 集群，连同其存储、网络和数据管道，用于大规模产出 AI 结果（训练或推理）。*参见 [第 44 章](06-history-and-future/ch44-future-trends.md)。*

<a id="ai-gateway"></a>
### AI 网关（AI gateway）

位于多家模型提供商之前的代理层，负责路由、故障切换、凭证管理、限流、缓存和支出上限控制。*参见 [第 21 章](03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)。*

<a id="all-stock-merger"></a>
### 全股票合并（All-stock merger）

一方公司的股东获得另一方公司股票的合并方式，因此不会形成现金价格或新的估值。*参见 [第 30 章](04-company-deep-dives/ch30-data-movement-streaming-companies.md)。*

<a id="analytics-engineering"></a>
### 分析工程（Analytics engineering）

将软件工程实践（版本控制、代码评审、CI、测试）应用于 SQL 数据转换的专业领域。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

<a id="annual-recurring-revenue"></a>
### 年度经常性收入（Annual recurring revenue）

某一时点上经常性订阅合同或承诺合同的年化价值（ARR）。*参见 [第 36 章](05-business-and-economics/ch36-unit-economics-kpis.md)。*

<a id="apache-arrow"></a>
### Apache Arrow

一种与编程语言无关的内存列式数据布局，使不同工具无需转换即可共享数据。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

<a id="apache-avro"></a>
### Apache Avro

一种面向行的二进制文件与序列化格式，文件中内嵌模式（schema），并定义了如何读取按旧版模式写入的数据的规则。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

<a id="apache-flink"></a>
### Apache Flink

开源流处理引擎，可在事件流上持续执行连接、聚合和窗口计算，具备托管状态和精确一次（exactly-once）保证。*参见 [第 49 章](07-conversation-toolkit/ch49-explain-in-30-seconds.md)。*

<a id="apache-hadoop"></a>
### Apache Hadoop

以 Google 的 GFS 和 MapReduce 论文为蓝本的开源分布式文件系统（HDFS）与 MapReduce 框架。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="apache-hudi"></a>
### Apache Hudi

诞生于 Uber 的开放表格式，围绕表操作时间线构建，针对更新插入（upsert）和流式数据摄取进行了优化。*参见 [第 49 章](07-conversation-toolkit/ch49-explain-in-30-seconds.md)。*

<a id="apache-iceberg"></a>
### Apache Iceberg

诞生于 Netflix 的开放表格式，通过由元数据文件和清单（manifest）文件组成的树来跟踪表状态。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="apache-kafka"></a>
### Apache Kafka

开源的分布式分区日志：生产者将事件追加到主题（topic），多个消费者各自独立读取；它是事件流的默认骨干。*参见 [第 49 章](07-conversation-toolkit/ch49-explain-in-30-seconds.md)。*

<a id="apache-orc"></a>
### Apache ORC

Optimized Row Columnar（优化行列式），由 Hortonworks 与 Facebook 于 2013 年合作创建的列式文件格式，用于加速 Hive。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

<a id="apache-parquet"></a>
### Apache Parquet

分析领域默认的开放列式文件格式，由 Twitter 与 Cloudera 于 2013 年基于 Dremel 的嵌套数据编码创建。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

<a id="apache-polaris"></a>
### Apache Polaris

Snowflake 于 2024 年捐赠的开源 Iceberg REST 目录，于 2026 年成为 Apache 顶级项目。*参见 [第 27 章](04-company-deep-dives/ch27-databricks-vs-snowflake.md)。*

<a id="apache-ranger"></a>
### Apache Ranger

开源框架，用于在 Hive、HDFS 和 Kafka 等 Hadoop 时代平台上定义并执行数据访问策略。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="apache-spark"></a>
### Apache Spark

诞生于加州大学伯克利分校 AMPLab 的分布式数据处理引擎，也是 Databricks 的基础。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="apache-xtable"></a>
### Apache XTable

处于孵化阶段的 Apache 项目，可在 Iceberg、Delta Lake 和 Hudi 之间转换表元数据，而无需复制数据文件。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="append-only-log"></a>
### 仅追加日志（Append-only log）

一种只允许追加写入的有序记录序列，读取方通过偏移量（offset）跟踪自己的读取位置。*参见 [第 11 章](02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。*

<a id="approximate-nearest-neighbor"></a>
### 近似最近邻（Approximate nearest neighbor）

一种以少量召回率换取大幅速度提升的相似性检索，使用 HNSW 等索引。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="aries"></a>
### ARIES

IBM 于 1992 年提出的基于预写日志的恢复算法，包含分析、重做（redo）和撤销（undo）三个阶段。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="arithmetic-intensity"></a>
### 算术强度（Arithmetic intensity）

一项作业每移动一个字节所执行的运算次数；它决定了该作业是计算受限还是带宽受限。*参见 [第 24 章](03-ai-data-stack/ch24-data-meets-compute-and-storage.md)。*

<a id="arrow-flight"></a>
### Arrow Flight

基于 gRPC 的协议，用于在服务之间流式传输 Arrow 记录批次，无需逐行序列化。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

<a id="atlas"></a>
### Atlas

MongoDB 的全托管、按用量计费的数据库服务，运行在 AWS、Azure 和 Google Cloud 上。*参见 [第 29 章](04-company-deep-dives/ch29-operational-database-vendors.md)。*

<a id="attach-rate"></a>
### 附加购买率（Attach rate）

同时购买某一附加产品的客户或交易所占的比例。*参见 [第 45 章](06-history-and-future/ch45-storage-moving-up-the-stack.md)。*

<a id="attribute-based-access-control"></a>
### 基于属性的访问控制（Attribute-based access control）

一种在请求时根据用户、数据、操作和上下文的属性来决定是否授予访问权限的模型。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="azure-consumption-commitment"></a>
### Azure 消费承诺（Azure Consumption Commitment）

Microsoft 的承诺消费额度协议（MACC），标注为“Azure benefit eligible”的云市场采购可 100% 计入该承诺。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

## B

<a id="b-tree"></a>
### B 树（B-tree）

一种由固定大小页面组成、层数少而扇出宽的有序树，用于索引和表；常见的 B+ 树变体将所有数据保存在从左到右相互链接的叶子页中。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="backfill"></a>
### 回填（Backfill）

重新处理历史数据，以填补缺口或将修正后的逻辑应用于过往期间。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="benchmark-decontamination"></a>
### 基准去污染（Benchmark decontamination）

从训练数据中移除评测题目及答案，以免基准测试分数虚高。*参见 [第 20 章](03-ai-data-stack/ch20-training-data-supply-chain.md)。*

<a id="bi-encoder"></a>
### 双编码器（Bi-encoder）

分别对查询和文档进行嵌入的模型，因此文档向量可以预先计算并被快速检索。*参见 [第 19 章](03-ai-data-stack/ch19-retrieval-architectures.md)。*

<a id="bigquery"></a>
### BigQuery

Google Cloud 的无服务器数据仓库，源自 Google 内部的 Dremel 引擎。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="billings"></a>
### 开票额（Billings）

收入加上递延收入的变动额，即某一期间内开具发票的金额。*参见 [第 36 章](05-business-and-economics/ch36-unit-economics-kpis.md)。*

<a id="binary-quantization"></a>
### 二值量化（Binary quantization）

每个向量维度只存储 1 个比特，体积缩小 32 倍，通常随后进行重新打分（rescoring）。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="binlog"></a>
### Binlog

MySQL 记录已提交变更的二进制日志，用于复制和变更数据捕获。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="bird-benchmark"></a>
### BIRD 基准（BIRD benchmark）

一个文本转 SQL 基准测试，包含大型、杂乱的数据库及外部知识提示，人类基线的执行准确率约为 93%。*参见 [第 22 章](03-ai-data-stack/ch22-agents-and-data.md)。*

<a id="bit-packing"></a>
### 位打包（Bit-packing）

仅用整数取值范围所需的最少比特数来存储整数。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="bitmap-index"></a>
### 位图索引（Bitmap index）

为列中每个不同取值存储一个位向量的索引，适用于低基数的分析型过滤条件。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="bloom-filter"></a>
### 布隆过滤器（Bloom filter）

一种紧凑的概率型数据结构，对某个键给出“肯定不存在”或“可能存在”的回答。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="bm25"></a>
### BM25

Lucene、Elasticsearch 和 OpenSearch 所使用的标准关键词相关性打分函数。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="book-to-bill"></a>
### 订单出货比（Book-to-bill）

某一期间内收到的订单除以已出货确认的收入；大于 1 意味着积压订单在增长。*参见 [第 36 章](05-business-and-economics/ch36-unit-economics-kpis.md)。*

<a id="breakage"></a>
### 未使用额度收入（Breakage）

预付容量到期未被使用时，供应商据此确认的收入。*参见 [第 35 章](05-business-and-economics/ch35-business-models.md)。*

<a id="bring-your-own-cloud"></a>
### 自带云（Bring your own cloud）

一种部署模式（BYOC），供应商的数据平面运行在客户自己的云账户内。*参见 [第 11 章](02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。*

<a id="broker"></a>
### 代理节点（Broker）

存储分区并处理生产者写入与消费者读取的 Kafka 服务器。*参见 [第 11 章](02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。*

<a id="buffer-pool"></a>
### 缓冲池（Buffer pool）

数据库自身用于缓存数据页和索引页的内存区域。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="burn-multiple"></a>
### 烧钱倍数（Burn multiple）

净现金消耗除以同期新增净 ARR；数值越低，说明以越高的效率“买到”增长。*参见 [第 46 章](07-conversation-toolkit/ch46-talking-with-data-people.md)。*

<a id="business-catalog"></a>
### 业务目录（Business catalog）

帮助人们通过搜索、业务术语表和数据管理（stewardship）流程来发现、理解并信任数据的工具（例如 Collibra、Alation、Atlan）。*参见 [第 08 章](01-data-systems-foundations/ch08-catalogs-and-metastores.md)。*

<a id="business-data-cloud"></a>
### Business Data Cloud

SAP 的数据服务（2025 年），将应用数据打包为带语义的数据产品，并内嵌 Databricks。*参见 [第 34 章](04-company-deep-dives/ch34-application-giants-data-platforms.md)。*

<a id="business-source-license"></a>
### 商业源代码许可证（Business Source License）

一种源代码可见（source-available）许可证（BSL），在设定期限内限制某些生产用途，期满后代码转为开源许可证。*参见 [第 29 章](04-company-deep-dives/ch29-operational-database-vendors.md)。*

## C

<a id="cac-payback"></a>
### CAC 回收期（CAC payback）

需要多少个月由新增收入带来的毛利，才能收回为获取这些收入而投入的销售与营销费用。*参见 [第 36 章](05-business-and-economics/ch36-unit-economics-kpis.md)。*

<a id="cache-tier"></a>
### 缓存层（Cache tier）

位于较慢的对象存储之前、用于存放热工作集的快速本地存储（SSD 或内存）。*参见 [第 24 章](03-ai-data-stack/ch24-data-meets-compute-and-storage.md)。*

<a id="cagra"></a>
### CAGRA

NVIDIA 针对 GPU 优化的图向量索引，属于 cuVS 库的一部分。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="cap-theorem"></a>
### CAP 定理（CAP theorem）

该结论指出：复制系统在遭遇网络分区时，必须在一致性和可用性之间作出取舍。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="capacity-commitment"></a>
### 容量承诺（Capacity commitment）

客户承诺在多年内按约定价格购买一定金额的用量，预先开票，并随消耗逐步扣减。*参见 [第 35 章](05-business-and-economics/ch35-business-models.md)。*

<a id="capacity-contract"></a>
### 容量合同（Capacity contract）

在合同期内消耗一定金额供应商用量单位的预付或承诺协议，只有在实际消耗时才确认为收入。*参见 [第 26 章](04-company-deep-dives/ch26-snowflake.md)。*

<a id="capacity-based-pricing"></a>
### 按容量计费（Capacity-based pricing）

按预留的处理容量计费，而不是按移动的数据量计费。*参见 [第 10 章](02-pipelines-and-governance/ch10-ingestion-and-integration.md)。*

<a id="cardinality-estimation"></a>
### 基数估计（Cardinality estimation）

预测查询计划中每一步将产生多少行。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="catalog-federation"></a>
### 目录联邦（Catalog federation）

由一个目录发现、治理并查询在另一个目录中注册的表，而无需复制这些表。*参见 [第 08 章](01-data-systems-foundations/ch08-catalogs-and-metastores.md)。*

<a id="catalog-managed-table"></a>
### 目录托管表（Catalog-managed table）

一种 Delta Lake 表（4.1 及以上版本），其提交由目录而非文件系统来确认。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="change-data-capture"></a>
### 变更数据捕获（Change data capture）

读取数据库的事务日志，将每一项已提交的变更作为事件发送给下游系统。*参见 [第 01 章](01-data-systems-foundations/ch01-data-stack-map.md)。*

<a id="channel-conflict"></a>
### 渠道冲突（Channel conflict）

当供应商自有产品与转售、嵌入或集成该产品的合作伙伴形成竞争时产生的摩擦。*参见 [第 45 章](06-history-and-future/ch45-storage-moving-up-the-stack.md)。*

<a id="channel-partner-private-offer"></a>
### 渠道合作伙伴私有报价（Channel partner private offer）

一种 AWS Marketplace 私有报价（CPPO），由经销商或系统集成商（SI）代表软件供应商完成交易，需额外收取 0.5 个百分点的费用。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

<a id="checkpoint"></a>
### 检查点（Checkpoint）

数据库将脏页刷写到磁盘的时间点，使崩溃恢复可以从此处开始，而不必从日志开头开始。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="chunk-overlap"></a>
### 分块重叠（Chunk overlap）

在相邻文本块的边界处重复部分文本，以免在切分处丢失上下文。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="chunking"></a>
### 分块（Chunking）

将文档切分为可检索的单元，每个单元各自生成嵌入向量。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="cloud-cogs"></a>
### 云销售成本（Cloud COGS）

云软件供应商计入营业成本的超大规模云厂商计算、存储和网络费用。*参见 [第 36 章](05-business-and-economics/ch36-unit-economics-kpis.md)。*

<a id="cloud-marketplace"></a>
### 云市场（Cloud marketplace）

超大规模云厂商的线上商店，客户可通过其云账单购买第三方软件。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="cloud-repatriation"></a>
### 云回迁（Cloud repatriation）

将工作负载或数据从公有云迁回本地或私有基础设施。*参见 [第 24 章](03-ai-data-stack/ch24-data-meets-compute-and-storage.md)。*

<a id="cloud-services-layer"></a>
### 云服务层（Cloud services layer）

Snowflake 位于计算集群之上的共享多租户层，负责元数据、查询优化、安全和事务。*参见 [第 26 章](04-company-deep-dives/ch26-snowflake.md)。*

<a id="clustered-index"></a>
### 聚簇索引（Clustered index）

按主键排序、以 B 树形式存储的表，叶子节点中保存完整的行（如 InnoDB）。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="co-sell"></a>
### 联合销售（Co-sell）

超大规模云厂商或合作伙伴的销售人员协助供应商完成交易并因此获得业绩认定的联合销售方式。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

<a id="codasyl"></a>
### CODASYL

1960–70 年代的行业委员会，其网状模型规范将 IDMS 等基于指针链接的数据库标准化。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="codebook"></a>
### 码本（Codebook）

经学习得到的一组代表性子向量，乘积量化编码即指向这些子向量。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="cohort-analysis"></a>
### 同期群分析（Cohort analysis）

长期跟踪一组固定客户，以区分来自存量客户的增长和来自新客户的增长。*参见 [第 36 章](05-business-and-economics/ch36-unit-economics-kpis.md)。*

<a id="column-chunk"></a>
### 列块（Column chunk）

Parquet 中某一行组（row group）内单列的连续字节，进一步划分为页。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

<a id="column-level-lineage"></a>
### 列级血缘（Column-level lineage）

追踪每个下游列由哪些上游列提供数据，通常通过解析 SQL 获得。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

<a id="column-level-security"></a>
### 列级安全（Column-level security）

根据请求者身份屏蔽或脱敏特定列的策略。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="columnar-replica"></a>
### 列式副本（Columnar replica）

行存储数据的列格式副本，通过复制保持最新，在 HTAP 系统中用于承担分析型读取（例如 TiFlash）。*参见 [第 23 章](03-ai-data-stack/ch23-real-time-analytics-htap.md)。*

<a id="columnar-storage"></a>
### 列式存储（Columnar storage）

将每一列的值连续存放，使分析查询只需读取所需的列。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="committed-spend"></a>
### 承诺消费额度（Committed spend）

一种多年期合同：客户承诺在某云服务商处达到最低消费额以换取折扣，未用足的差额仍需付费。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="committed-use-discount"></a>
### 承诺使用折扣（Committed use discount）

Google Cloud 针对客户在一定期限内承诺特定资源用量或支出所提供的折扣（CUD）。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

<a id="committed-spend-drawdown"></a>
### 承诺消费扣减（Committed-spend drawdown）

通过使用量或符合条件的采购（包括云市场软件）来消耗预付或承诺的支出额度。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

<a id="compaction"></a>
### 压缩合并（Compaction）

一种维护作业，将大量小文件或含大量删除记录的文件重写为数量更少、体积更大且通常已排序的文件。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="company-guidance"></a>
### 公司指引（Company guidance）

管理层随业绩发布的、对未来某一期间收入或利润率的自身预测。*参见 [第 00.1 章](00-start-here/ch00-1-how-to-use.md)。*

<a id="compare-and-swap"></a>
### 比较并交换（Compare-and-swap）

一种原子操作：仅当某个值仍等于预期值时才更新它；这是表格式提交所依赖的基本原语。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="composable-data-stack"></a>
### 可组合数据栈（Composable data stack）

用 Arrow、Velox 和 DataFusion 等共享、可互换的组件来构建数据系统。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="compute-plane"></a>
### 计算平面（Compute plane）

实际处理数据的层级；在 Databricks 中，它位于客户的云账户内（经典模式）或供应商的云账户内（无服务器模式）。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="compute-in-memory"></a>
### 存内计算（Compute-in-memory）

将处理逻辑放在内存旁边或内存内部，使数据无需移动到独立的处理器。*参见 [第 32 章](04-company-deep-dives/ch32-ai-native-data-companies.md)。*

<a id="conditional-write"></a>
### 条件写入（Conditional write）

一种仅在前提条件成立时（例如对象尚不存在）才会成功的对象存储写入操作。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="conformed-dimension"></a>
### 一致性维度（Conformed dimension）

日期或产品等维度只定义一次，并以相同含义在多个事实表之间共享。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="connector"></a>
### 连接器（Connector）

从某一类数据源（SaaS API、数据库、文件）抽取数据并向目标端输出标准化记录的代码。*参见 [第 10 章](02-pipelines-and-governance/ch10-ingestion-and-integration.md)。*

<a id="connector-sdk"></a>
### 连接器 SDK（Connector SDK）

用于编写自定义连接器的开发工具包，这些连接器由供应商的托管运行时承载并计量。*参见 [第 10 章](02-pipelines-and-governance/ch10-ingestion-and-integration.md)。*

<a id="consensus"></a>
### 共识（Consensus）

一组副本在节点崩溃和消息延迟的情况下，就单一有序操作日志达成一致的协议。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="consistent-hashing"></a>
### 一致性哈希（Consistent hashing）

将节点和键放置在哈希环上，使增加或移除节点时只需迁移一小部分键。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="consumer-group"></a>
### 消费者组（Consumer group）

一组在彼此之间分配某个主题各分区的消费者，由该组自行跟踪已提交的偏移量。*参见 [第 11 章](02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。*

<a id="consumption-pricing"></a>
### 按用量计费（Consumption pricing）

按完成的工作单位（credit、DBU、扫描字节数、行数）收费，收入随客户消耗而确认。*参见 [第 35 章](05-business-and-economics/ch35-business-models.md)。*

<a id="consumption-based-pricing"></a>
### 基于用量的计费（Consumption-based pricing）

按使用单位（credit、DBU、token、智能体操作）收费，而不是按指定用户数收费。*参见 [第 44 章](06-history-and-future/ch44-future-trends.md)。*

<a id="content-hash"></a>
### 内容哈希（Content hash）

文件字节内容的指纹，用于在同步过程中检测变更和重复。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="context-engineering"></a>
### 上下文工程（Context engineering）

在每次调用模型时，决定哪些指令、检索到的数据、工具结果和历史记录进入模型的上下文窗口。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="context-precision"></a>
### 上下文精确率（Context precision）

一项检索指标，衡量检索到的段落中相关段落所占的比例，并对排名靠前的结果赋予更高权重。*参见 [第 19 章](03-ai-data-stack/ch19-retrieval-architectures.md)。*

<a id="context-rot"></a>
### 上下文腐化（Context rot）

随着输入长度增加，即使是简单任务，模型可靠性也会下降的现象（Chroma，2025）。*参见 [第 19 章](03-ai-data-stack/ch19-retrieval-architectures.md)。*

<a id="contrastive-learning"></a>
### 对比学习（Contrastive learning）

一种训练方法：在向量空间中拉近匹配的样本对（例如问题与答案段落），推远不匹配的样本对。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="contributor-concentration"></a>
### 贡献者集中度（Contributor concentration）

开源项目的提交或维护者中，来自单一公司或少数个人的比例。*参见 [第 47 章](07-conversation-toolkit/ch47-diligence-checklist.md)。*

<a id="contributor-license-agreement"></a>
### 贡献者许可协议（Contributor license agreement）

贡献者据此向项目所有者授予其代码相关权利的合同，正是这一点使所有者日后能够变更许可证。*参见 [第 38 章](05-business-and-economics/ch38-open-source-strategy.md)。*

<a id="control-plane"></a>
### 控制平面（Control plane）

由供应商托管、负责管理、调度和治理工作的服务，与数据实际被处理的位置相分离。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="control-point"></a>
### 控制点（Control point）

其他所有组件都必须经过的一层，使其拥有者获得定价权和策略主导权（在数据领域：目录、语义层、智能体接口）。*参见 [第 00.2 章](00-start-here/ch00-2-market-map.md)。*

<a id="control-premium"></a>
### 控制权溢价（Control premium）

收购方为取得目标公司控制权而在其未受干扰股价之上多支付的金额。*参见 [第 37 章](05-business-and-economics/ch37-public-comps-valuation.md)。*

<a id="converged-index"></a>
### 融合索引（Converged index）

Rockset 的设计：将每个字段同时存入行索引、列索引和搜索索引。*参见 [第 23 章](03-ai-data-stack/ch23-real-time-analytics-htap.md)。*

<a id="conversational-analytics"></a>
### 对话式分析（Conversational analytics）

在 BI 工具或数据平台内，基于受治理数据进行自然语言问答。*参见 [第 14 章](02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)。*

<a id="coopetition"></a>
### 竞合（Coopetition）

与同一家公司同时竞争与合作，正如超大规模云厂商与 Databricks 和 Snowflake 之间的关系。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="copy-on-write"></a>
### 写时复制（Copy-on-write）

通过完整重写受影响的数据文件来应用行级变更，写入成本高，但读取简单。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="copyleft"></a>
### 著佐权（Copyleft）

一种许可证条件，要求衍生作品必须以相同的许可条款分发。*参见 [第 38 章](05-business-and-economics/ch38-open-source-strategy.md)。*

<a id="cortex-ai"></a>
### Cortex AI

Snowflake 托管的 LLM 函数、搜索和智能体服务，在受治理数据旁运行，并以 credit 计费。*参见 [第 26 章](04-company-deep-dives/ch26-snowflake.md)。*

<a id="cosine-similarity"></a>
### 余弦相似度（Cosine similarity）

用两个向量之间的夹角来衡量其相似程度；对于单位长度向量，它等于点积。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="covering-index"></a>
### 覆盖索引（Covering index）

包含查询所需全部列的索引，因此无需读取表本身。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="credential-vending"></a>
### 凭证分发（Credential vending）

由目录向其已授权的引擎签发短期有效、范围限定于某张表路径前缀的存储凭证。*参见 [第 08 章](01-data-systems-foundations/ch08-catalogs-and-metastores.md)。*

<a id="cross-encoder"></a>
### 交叉编码器（Cross-encoder）

将查询与段落一起读入并输出单一相关性分数的模型；准确度高，但速度太慢，无法在整个语料库上运行。*参见 [第 19 章](03-ai-data-stack/ch19-retrieval-architectures.md)。*

<a id="cudf"></a>
### cuDF

RAPIDS 的 GPU 数据框（dataframe）库，其 pandas 加速模式可在 GPU 上运行 pandas 代码，并支持回退到 CPU。*参见 [第 24 章](03-ai-data-stack/ch24-data-meets-compute-and-storage.md)。*

<a id="cuobject"></a>
### cuObject

NVIDIA 的一组库，通过 RDMA 将 S3 对象数据载荷传入 GPU 或主机内存，同时 S3 控制路径仍走 HTTP。*参见 [第 24 章](03-ai-data-stack/ch24-data-meets-compute-and-storage.md)。*

<a id="current-remaining-performance-obligations"></a>
### 当期剩余履约义务（Current remaining performance obligations）

公司预计在未来十二个月内确认为收入的那部分 RPO（cRPO）。*参见 [第 36 章](05-business-and-economics/ch36-unit-economics-kpis.md)。*

<a id="cursor-field"></a>
### 游标字段（Cursor field）

连接器用来查找已变更记录的列，例如 updated_at。*参见 [第 10 章](02-pipelines-and-governance/ch10-ingestion-and-integration.md)。*

<a id="customer-concentration"></a>
### 客户集中度（Customer concentration）

公司收入中来自最大客户的比例，用于衡量单个续约对业务的影响程度。*参见 [第 47 章](07-conversation-toolkit/ch47-diligence-checklist.md)。*

<a id="cuvs"></a>
### cuVS

RAPIDS 中用于在 GPU 上构建和检索向量索引的库，已集成到 Faiss、Milvus 和 OpenSearch 中。*参见 [第 24 章](03-ai-data-stack/ch24-data-meets-compute-and-storage.md)。*

<a id="cyber-resilience"></a>
### 网络韧性（Cyber resilience）

检测、抵御勒索软件等攻击并从中恢复的能力，主要依靠受保护的不可变副本和异常检测。*参见 [第 45 章](06-history-and-future/ch45-storage-moving-up-the-stack.md)。*

<a id="cypher"></a>
### Cypher

Neo4j 的声明式属性图查询语言，也是 ISO GQL 的主要基础。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

## D

<a id="dark-data"></a>
### 暗数据（Dark data）

组织并不清楚其内容和业务价值的已存储数据。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="data-access-governance"></a>
### 数据访问治理（Data access governance）

分析并合理收敛“谁能访问哪些数据”，尤其针对文件共享、Microsoft 365 和 SaaS 内容。*参见 [第 33 章](04-company-deep-dives/ch33-governance-catalog-security-companies.md)。*

<a id="data-catalog"></a>
### 数据目录（Data catalog）

横跨数据栈各层、登记数据资产及其所有者、血缘和访问策略的注册库。*参见 [第 01 章](01-data-systems-foundations/ch01-data-stack-map.md)。*

<a id="data-classification"></a>
### 数据分类（Data classification）

按类型和敏感程度为数据打标签（例如电子邮件地址、银行卡号、健康数据），以便策略据此执行。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="data-clean-room"></a>
### 数据洁净室（Data clean room）

两方或多方在约定规则下分析合并数据、但彼此看不到对方明细行的环境。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="data-cloud"></a>
### Data Cloud

Salesforce 支撑 Agentforce 的客户数据与湖仓层，据报道已于 2025 年更名为 Data 360。*参见 [第 34 章](04-company-deep-dives/ch34-application-giants-data-platforms.md)。*

<a id="data-contract"></a>
### 数据契约（Data contract）

由数据生产方负责并强制执行的、关于数据集模式、语义、质量规则和 SLA 的约定。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

<a id="data-curation"></a>
### 数据整理（Data curation）

对原始数据进行抽取、过滤、去重、质量打分和清洗，使其成为可直接用于训练的形式。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="data-detection-and-response"></a>
### 数据检测与响应（Data detection and response）

监控数据访问模式，针对异常或恶意活动发出告警并作出响应。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="data-diff"></a>
### 数据比对（Data diff）

对一张表的两个版本进行逐行比较，在 CI 或迁移中用于在发布前发现回归问题。*参见 [第 13 章](02-pipelines-and-governance/ch13-data-quality-observability-lineage.md)。*

<a id="data-discovery"></a>
### 数据发现（Data discovery）

查明整个 IT 资产范围内有哪些数据存储及其中的敏感数据分布在何处。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="data-downtime"></a>
### 数据宕机（Data downtime）

数据延迟、缺失、错误或以其他方式不可靠的时段，类比于应用宕机。*参见 [第 13 章](02-pipelines-and-governance/ch13-data-quality-observability-lineage.md)。*

<a id="data-drift"></a>
### 数据漂移（Data drift）

线上模型输入的分布相对于训练数据发生的变化。*参见 [第 21 章](03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)。*

<a id="data-flywheel"></a>
### 数据飞轮（Data flywheel）

一种循环：产品使用产生数据（日志、追踪、反馈），这些数据改进产品，进而吸引更多使用。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="data-gravity"></a>
### 数据引力（Data gravity）

大型数据集倾向于把应用、算力和更多数据吸引到其所在位置的现象。*参见 [第 01 章](01-data-systems-foundations/ch01-data-stack-map.md)。*

<a id="data-inlining"></a>
### 数据内联（Data inlining）

DuckLake 的一项技术：将非常小的插入、更新和删除直接存入目录数据库，而不是写入新文件。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="data-intelligence"></a>
### 数据智能（Data intelligence）

能够发现、分类数据并为其添加语义上下文、以供目录、策略引擎和智能体使用的软件；也是 Everpure 为原 1touch 技术所取的产品名称。*参见 [第 45 章](06-history-and-future/ch45-storage-moving-up-the-stack.md)。*

<a id="data-lake"></a>
### 数据湖（Data lake）

以低成本保存多种格式原始文件的存储，仅在读取时才赋予结构。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="data-leakage"></a>
### 数据泄漏（Data leakage）

预测时本不可获得的信息混入训练数据，导致离线准确率虚高。*参见 [第 21 章](03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)。*

<a id="data-lineage"></a>
### 数据血缘（Data lineage）

描述数据如何从源头经过各项转换流向仪表板、模型和索引等消费方的有向图。*参见 [第 13 章](02-pipelines-and-governance/ch13-data-quality-observability-lineage.md)。*

<a id="data-loss-prevention"></a>
### 数据防泄漏（Data loss prevention）

检测并阻止敏感数据流出经批准边界的控制措施。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="data-marketplace"></a>
### 数据市场（Data marketplace）

数据平台的线上商店，提供方在其中为该平台客户上架数据集、模型和应用。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

<a id="data-mart"></a>
### 数据集市（Data mart）

服务于单个部门或业务流程的、面向特定主题的数据仓库数据子集。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="data-metric-function"></a>
### 数据指标函数（Data metric function）

一种按计划在表上运行的 Snowflake 函数，用于度量行数、新鲜度或空值数等质量指标。*参见 [第 13 章](02-pipelines-and-governance/ch13-data-quality-observability-lineage.md)。*

<a id="data-mirroring"></a>
### 数据镜像（Data mirroring）

由供应商托管、将业务数据库持续复制到分析平台的机制（例如 Fabric 镜像、Snowflake Postgres 镜像）。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="data-mixture"></a>
### 数据配比（Data mixture）

模型训练各阶段所使用的各类数据来源（网页、代码、数学、书籍、合成数据）的比例。*参见 [第 20 章](03-ai-data-stack/ch20-training-data-supply-chain.md)。*

<a id="data-observability"></a>
### 数据可观测性（Data observability）

对数据集元数据（新鲜度、数据量、模式、分布、血缘）进行自动化监控，以发现、分诊并解释数据问题。*参见 [第 13 章](02-pipelines-and-governance/ch13-data-quality-observability-lineage.md)。*

<a id="data-poisoning"></a>
### 数据投毒（Data poisoning）

向训练数据或检索数据中注入恶意样本，以植入不期望的模型行为。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="data-room"></a>
### 数据室（Data room）

受控的文件库（通常为虚拟形式），收购目标在其中向潜在买方提供尽职调查文件。*参见 [第 47 章](07-conversation-toolkit/ch47-diligence-checklist.md)。*

<a id="data-security-posture-management"></a>
### 数据安全态势管理（Data security posture management）

持续发现敏感数据、谁能访问这些数据以及其暴露位置，并按风险排序。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="data-slo"></a>
### 数据 SLO（Data SLO）

针对数据集新鲜度、完整性或准确性设定的内部服务水平目标。*参见 [第 13 章](02-pipelines-and-governance/ch13-data-quality-observability-lineage.md)。*

<a id="data-sovereignty"></a>
### 数据主权（Data sovereignty）

要求某些数据必须在特定司法辖区内存储和处理的法律要求。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="data-subject-access-request"></a>
### 数据主体访问请求（Data subject access request）

个人依法提出的、查看某组织所持有的其个人数据的请求。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="data-swamp"></a>
### 数据沼泽（Data swamp）

因缺乏元数据、质量控制和治理而变得无法使用的数据湖。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="data-test"></a>
### 数据测试（Data test）

构建完成后针对生产数据运行的显式断言，例如非空、唯一或取值在允许范围内。*参见 [第 13 章](02-pipelines-and-governance/ch13-data-quality-observability-lineage.md)。*

<a id="data-versioning"></a>
### 数据版本管理（Data versioning）

记录数据集不可变、可寻址的版本（例如 lakeFS 提交、表快照），以便复现运行结果。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="data-warehouse"></a>
### 数据仓库（Data warehouse）

为分析而构建、从业务系统加载数据的独立数据库，使报表查询不会拖慢事务处理。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="data-warehouse-appliance"></a>
### 数据仓库一体机（Data warehouse appliance）

预装在专用硬件上、作为单一系统出售的数据库软件，Teradata 和 Netezza 即采用此模式。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="database-at-hyperscaler"></a>
### 超大规模云上的数据库（Database at hyperscaler）

Oracle 的一种模式：在 Azure、Google Cloud 和 AWS 的数据中心内运行基于 Exadata 的 Oracle Database，并通过宿主云销售（Oracle Database@Azure、@Google Cloud、@AWS）。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="database-branching"></a>
### 数据库分支（Database branching）

即时创建数据库的写时复制分叉，用于测试、预览或智能体作业。*参见 [第 22 章](03-ai-data-stack/ch22-agents-and-data.md)。*

<a id="dbpaas"></a>
### dbPaaS

以托管云服务形式提供的数据库（数据库平台即服务），目前已占 DBMS 支出的大部分。*参见 [第 41 章](05-business-and-economics/ch41-market-sizing.md)。*

<a id="dbt"></a>
### dbt

开源框架，将 SQL 加 Jinja 编写的“模型”编译为依赖图，并在数据仓库或湖仓内运行。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

<a id="dbu"></a>
### DBU

Databricks Unit（Databricks 单位），Databricks 按工作负载 SKU 计量和定价的标准化每小时处理单位。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="deal-registration"></a>
### 交易报备（Deal registration）

合作伙伴对某一销售机会的正式登记，用以保护其业绩认定、利润空间和激励。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

<a id="deal-spread"></a>
### 交易价差（Deal spread）

目标公司交易价格与约定收购价格之间的差额，反映时间价值以及交易失败的风险。*参见 [第 37 章](05-business-and-economics/ch37-public-comps-valuation.md)。*

<a id="declarative-pipeline"></a>
### 声明式数据管道（Declarative pipeline）

按其应产出的表、而非需执行的步骤来定义的数据管道，例如 Lakeflow Spark Declarative Pipelines。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

<a id="declarative-query"></a>
### 声明式查询（Declarative query）

只说明所需结果、将执行方式交由数据库优化器决定的查询，SQL 即是如此。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="delete-file"></a>
### 删除文件（Delete file）

Iceberg v2 中按文件位置或按列值记录已删除行的文件。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="deletion-vector"></a>
### 删除向量（Deletion vector）

一种紧凑的位图，标记某个数据文件中哪些行位置已被删除，Delta Lake 和 Iceberg v3 均使用此机制。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="delta-checkpoint"></a>
### Delta 检查点（Delta checkpoint）

汇总 Delta 表在某一版本完整状态的 Parquet 文件，使读取方无需重放整个日志。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="delta-encoding"></a>
### 差值编码（Delta encoding）

存储相邻值之间的差值而非值本身的压缩方法。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="delta-lake"></a>
### Delta Lake

Databricks 的开放表格式：Parquet 数据文件加上 JSON 事务日志，在对象存储上实现 ACID 提交。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="delta-log"></a>
### Delta 日志（Delta log）

由编号的 JSON 提交文件组成的 `_delta_log` 目录，记录 Delta Lake 表的每一次变更。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="delta-sharing"></a>
### Delta Sharing

开放的 REST 协议（2021 年），通过向接收方提供指向底层文件的短期签名 URL 来共享表；现已更名为 OpenSharing。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="denormalization"></a>
### 反范式化（Denormalization）

有意在多条记录之间重复存储数据，以降低常见读取的成本，代价是更新更加困难。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="depth-label"></a>
### 深度标签（Depth label）

本知识库用于标示讲解深入程度的标记：L1（术语）、L2（机制）或 L3（实现）。*参见 [第 00.1 章](00-start-here/ch00-1-how-to-use.md)。*

<a id="dictionary-encoding"></a>
### 字典编码（Dictionary encoding）

用较小的整数编码加一张查找表来替代重复值的压缩方法。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="differential-privacy"></a>
### 差分隐私（Differential privacy）

在结果中加入经过校准的统计噪声，使其几乎不泄露任何单个个体的信息。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="digital-twin"></a>
### 数字孪生（Digital twin）

镜像物理实体或业务实体、并可将变更回写给它们的实时软件模型。*参见 [第 31 章](04-company-deep-dives/ch31-analytical-engine-challengers-legacy.md)。*

<a id="dimension"></a>
### 维度（Dimension）

用于对度量值进行分组或过滤的属性，例如地区或财季。*参见 [第 14 章](02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)。*

<a id="dimensional-modeling"></a>
### 维度建模（Dimensional modeling）

Kimball 提出的数据仓库设计方法：按业务流程构建星型模式，并通过一致性维度相互关联。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="direct-preference-optimization"></a>
### 直接偏好优化（Direct preference optimization）

一种后训练方法，直接从“被选/被拒”答案对中学习，无需单独的奖励模型（DPO）。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="directed-acyclic-graph"></a>
### 有向无环图（Directed acyclic graph）

由单向依赖边连接任务或模型、且不含环的图，用于确定运行顺序。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

<a id="disaggregated-shared-everything"></a>
### 解耦式全共享架构（Disaggregated shared-everything）

VAST Data 的存储架构：无状态服务器通过 NVMe 网络访问所有闪存机箱，使性能与容量可独立扩展。*参见 [第 32 章](04-company-deep-dives/ch32-ai-native-data-companies.md)。*

<a id="disaggregated-storage"></a>
### 解耦存储（Disaggregated storage）

将无状态计算与共享存储服务分离的架构；在 Aurora 和 Neon 中，存储层直接消费数据库日志。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="diskann"></a>
### DiskANN

Microsoft 的驻留 SSD 的图向量索引，将压缩向量保存在 DRAM 中，将完整向量和图结构保存在闪存上。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="diskless-kafka"></a>
### 无盘 Kafka（Diskless Kafka）

以对象存储为主存储、Broker 无状态的 Kafka 兼容设计（例如 WarpStream、KIP-1150）。*参见 [第 11 章](02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。*

<a id="distillation"></a>
### 蒸馏（Distillation）

用较大的“教师”模型的输出来训练较小的“学生”模型。*参见 [第 20 章](03-ai-data-stack/ch20-training-data-supply-chain.md)。*

<a id="document-database"></a>
### 文档数据库（Document database）

存储自包含的类 JSON 记录（文档）的数据库，例如 MongoDB。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="document-parsing"></a>
### 文档解析（Document parsing）

将文件转换为有序文本及标题、表格、页码引用等结构信息。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="double-counting"></a>
### 重复计算（Double counting）

在价值链的不同层级中将同一笔支出计算不止一次，例如同时计入 SaaS 供应商的收入及其支付的云费用。*参见 [第 41 章](05-business-and-economics/ch41-market-sizing.md)。*

<a id="dpu-hour"></a>
### DPU 小时（DPU-hour）

AWS Glue 的计费单位：一个数据处理单元（DPU）的算力运行一小时。*参见 [第 10 章](02-pipelines-and-governance/ch10-ingestion-and-integration.md)。*

<a id="ducklake"></a>
### DuckLake

DuckDB 团队推出的湖仓格式，将全部表元数据存放在 SQL 数据库中，数据则以 Parquet 存储。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="durable-execution"></a>
### 持久化执行（Durable execution）

一种运行时模型，持久化保存工作流的每一步，使代码在崩溃或长时间等待后能从中断处精确恢复。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

<a id="dynamic-data-masking"></a>
### 动态数据脱敏（Dynamic data masking）

在查询时改写敏感值（例如显示为 j***@example.com），而不改变已存储的数据。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="dynamic-table"></a>
### 动态表（Dynamic table）

由一条查询和一个目标延迟定义的 Snowflake 表，引擎会自动刷新，并尽可能采用增量方式。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

## E

<a id="ecku"></a>
### eCKU

Elastic Confluent Unit for Kafka（Kafka 弹性 Confluent 单元），Confluent Cloud 用于计量集群使用量的容量单位。*参见 [第 30 章](04-company-deep-dives/ch30-data-movement-streaming-companies.md)。*

<a id="edp"></a>
### EDP

AWS Enterprise Discount Program（AWS 企业折扣计划），AWS 对其承诺消费额度折扣合同的历史称谓。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="efficiency-headwind"></a>
### 效率逆风（Efficiency headwind）

按用量计费的厂商因自身性能提升、使客户完成同样工作所需支付的费用下降而损失的收入。*参见 [第 26 章](04-company-deep-dives/ch26-snowflake.md)。*

<a id="egress-fee"></a>
### 出口流量费（Egress fee）

云服务商对离开其网络或区域的数据按 GB 收取的费用。*参见 [第 24 章](03-ai-data-stack/ch24-data-meets-compute-and-storage.md)。*

<a id="elastic-license-20"></a>
### Elastic License 2.0

一种简短的源代码可见（source-available）许可证（ELv2），允许内部使用，但禁止将软件作为托管服务提供或规避许可证密钥。*参见 [第 38 章](05-business-and-economics/ch38-open-source-strategy.md)。*

<a id="elt"></a>
### ELT

抽取、加载、转换（Extract, load, transform）：先落地原始数据，再在数据仓库或湖仓内部进行数据转换。*参见 [第 01 章](01-data-systems-foundations/ch01-data-stack-map.md)。*

<a id="embedding"></a>
### 嵌入（Embedding）

由模型生成的数值向量，使语义相近的对象在向量空间中彼此靠近。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="end-user-spending"></a>
### 终端用户支出（End-user spending）

一种市场规模测算口径，统计买方实际支付的金额（包括硬件、设备和服务），而非软件厂商确认的收入。*参见 [第 41 章](05-business-and-economics/ch41-market-sizing.md)。*

<a id="enterprise-advanced"></a>
### Enterprise Advanced

MongoDB 的自管理订阅产品，包含管理工具、安全功能和技术支持。*参见 [第 29 章](04-company-deep-dives/ch29-operational-database-vendors.md)。*

<a id="enterprise-ai-search"></a>
### 企业 AI 搜索（Enterprise AI search）

具备权限感知能力的搜索与 AI 助手，可对企业自有的应用、文档和聊天记录建立索引。*参见 [第 32 章](04-company-deep-dives/ch32-ai-native-data-companies.md)。*

<a id="enterprise-data-warehouse"></a>
### 企业数据仓库（Enterprise data warehouse）

Inmon 提出的单一、规范化、覆盖全公司的数据仓库，作为中枢向各部门数据集市供数。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="enterprise-discount-program"></a>
### 企业折扣计划（Enterprise Discount Program）

AWS 的多年期承诺消费额度合同（EDP，又称 Private Pricing Agreement），以消费承诺换取折扣。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

<a id="enterprise-value"></a>
### 企业价值（Enterprise value）

市值加债务减现金，即经营业务对全体资本提供方的价值。*参见 [第 27 章](04-company-deep-dives/ch27-databricks-vs-snowflake.md)。*

<a id="entity-resolution"></a>
### 实体解析（Entity resolution）

将跨系统的记录和检测结果关联到同一个现实世界中的人或事物。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="equality-delete"></a>
### 等值删除（Equality delete）

以列值表达的删除操作（例如 id = 5），对流式写入方成本低，但对读取方成本高。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="equity-value"></a>
### 股权价值（Equity value）

为公司全部股份支付的价格；企业价值在此基础上再加上净债务。*参见 [第 39 章](05-business-and-economics/ch39-ma-history.md)。*

<a id="erasure-coding"></a>
### 纠删码（Erasure coding）

将数据存储为数据分片加校验分片，以低于完整复制的容量开销在故障中保全数据。*参见 [第 24 章](03-ai-data-stack/ch24-data-meets-compute-and-storage.md)。*

<a id="etl"></a>
### ETL

抽取、转换、加载（Extract, transform, load）：数据先在独立系统上清洗和重塑，再加载进数据仓库。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="eu-ai-act"></a>
### 欧盟《人工智能法》（EU AI Act）

即 Regulation (EU) 2024/1689，欧盟按风险分级的 AI 法律；其高风险义务包括训练数据治理（第 10 条），经 2026 年 AI Omnibus 调整后，现自 2027 年 12 月和 2028 年 8 月起适用。*参见 [第 49 章](07-conversation-toolkit/ch49-explain-in-30-seconds.md)。*

<a id="ev-to-ntm-revenue"></a>
### EV/未来 12 个月收入（EV to NTM revenue）

企业价值除以未来十二个月的预期收入，是软件公司的标准估值倍数。*参见 [第 27 章](04-company-deep-dives/ch27-databricks-vs-snowflake.md)。*

<a id="event-streaming"></a>
### 事件流（Event streaming）

通过持久化、分区、仅追加的日志（如 Apache Kafka）在系统之间持续传递事件。*参见 [第 01 章](01-data-systems-foundations/ch01-data-stack-map.md)。*

<a id="event-time"></a>
### 事件时间（Event time）

事件实际发生的时间，区别于系统观察到该事件时的处理时间（processing time）。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="eventual-consistency"></a>
### 最终一致性（Eventual consistency）

一种一致性模型，仅承诺在写入停止后各副本最终收敛一致。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="evergreen-one"></a>
### Evergreen One

Everpure 的存储即服务产品（Evergreen//One），按预留承诺加按需用量计费，并提供服务等级保障。*参见 [第 35 章](05-business-and-economics/ch35-business-models.md)。*

<a id="exact-data-match"></a>
### 精确数据匹配（Exact data match）

通过将内容与已知参照表的哈希值进行比对来检测敏感数据。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="exactly-once-semantics"></a>
### 精确一次语义（Exactly-once semantics）

一种数据管道保证：即便存在重试，每个事件对最终结果也只产生一次影响，通过去重或事务实现。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="exadata"></a>
### Exadata

Oracle 的软硬件一体化数据库设备，将 SQL 过滤下推至通过 RDMA 互联的存储服务器。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="execution-accuracy"></a>
### 执行准确率（Execution accuracy）

一种文本转 SQL 基准指标：生成的 SQL 与参考查询返回相同结果的问题所占比例。*参见 [第 22 章](03-ai-data-stack/ch22-agents-and-data.md)。*

<a id="experiment-tracking"></a>
### 实验追踪（Experiment tracking）

记录每次训练运行的参数、指标、代码版本和产物，以便比较和复现各次运行。*参见 [第 21 章](03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)。*

<a id="expert-data"></a>
### 专家数据（Expert data）

由工程师、医生或律师等领域专家（而非众包工作者）撰写或评判的训练、示范和评估数据。*参见 [第 32 章](04-company-deep-dives/ch32-ai-native-data-companies.md)。*

<a id="expert-network"></a>
### 专家网络（Expert network）

按小时出租具备资质的专家（博士、医生、工程师）来撰写或评分训练数据的数据供应商。*参见 [第 20 章](03-ai-data-stack/ch20-training-data-supply-chain.md)。*

<a id="explain"></a>
### EXPLAIN

显示查询优化器所选执行计划的 SQL 命令，可选附带实际运行时统计信息。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="exposure"></a>
### 暴露（Exposure）

在 dbt 项目图中登记的、已声明的 dbt 模型下游消费者（仪表板、机器学习模型、应用）。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

<a id="external-consistency"></a>
### 外部一致性（External consistency）

保证事务提交顺序在整个系统范围内与真实时间顺序一致，如 Spanner 所提供的那样。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="external-location"></a>
### 外部位置（External location）

Unity Catalog 中将存储路径与凭证绑定的对象，使受治理的表和文件可以存放在该位置。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="external-volume"></a>
### 外部卷（External volume）

Snowflake 中将 Iceberg 表指向客户自有对象存储（包括 S3 兼容存储）的对象。*参见 [第 26 章](04-company-deep-dives/ch26-snowflake.md)。*

## F

<a id="fabless"></a>
### 无晶圆厂（Fabless）

只设计芯片、租用制造产能的半导体公司；本书用作 Databricks 和 Snowflake 的类比。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="fail-safe"></a>
### 故障安全期（Fail-safe）

Snowflake 在时间旅行（Time Travel）期满后的七天恢复期，期间只有 Snowflake 支持团队可以恢复数据。*参见 [第 26 章](04-company-deep-dives/ch26-snowflake.md)。*

<a id="fair-source"></a>
### 公平源代码（Fair source）

由 Sentry 自 2024 年起推广的标签，指在固定延迟后转为开源的源代码可见许可证，例如为期两年的 Functional Source License。*参见 [第 38 章](05-business-and-economics/ch38-open-source-strategy.md)。*

<a id="fair-use"></a>
### 合理使用（Fair use）

美国版权法中的抗辩事由，综合权衡使用目的、作品性质、使用数量以及对市场的影响。*参见 [第 20 章](03-ai-data-stack/ch20-training-data-supply-chain.md)。*

<a id="fair-value-hierarchy"></a>
### 公允价值层级（Fair value hierarchy）

ASC 820 对估值输入值的分级：第 1 层级为报价，第 2 层级为可观察输入值，第 3 层级为不可观察的模型输入值（如私募轮次定价）。*参见 [第 37 章](05-business-and-economics/ch37-public-comps-valuation.md)。*

<a id="faithfulness"></a>
### 忠实度（Faithfulness）

一种 RAG 指标，衡量答案中的每一项陈述是否都有检索到的上下文作为支撑。*参见 [第 19 章](03-ai-data-stack/ch19-retrieval-architectures.md)。*

<a id="falsifier"></a>
### 证伪条件（Falsifier）

预先声明的某个结果，一旦观察到即表明某项预测是错误的。*参见 [第 44 章](06-history-and-future/ch44-future-trends.md)。*

<a id="fan-out"></a>
### 扇出（Fan-out）

树形索引中每个内部页所持有的子指针数量，决定了树的高度。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="feature-absorption"></a>
### 功能吸收（Feature absorption）

独立产品的核心功能变成更大平台的捆绑功能，从而压缩独立厂商的定价权。*参见 [第 32 章](04-company-deep-dives/ch32-ai-native-data-companies.md)。*

<a id="feature-store"></a>
### 特征存储（Feature store）

一次性定义模型特征、并向训练和在线推理同时提供一致特征值的系统。*参见 [第 21 章](03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)。*

<a id="finops"></a>
### FinOps

通过工程与财务共担成本责任来管理和降低云支出的实践。*参见 [第 41 章](05-business-and-economics/ch41-market-sizing.md)。*

<a id="first-party-service"></a>
### 第一方服务（First-party service）

由云服务商自己销售、计费和提供支持的合作伙伴产品，例如 Azure Databricks。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="fiscal-year"></a>
### 财年（Fiscal year）

公司报告所依据的 12 个月期间，常与日历年不一致（Snowflake 的 FY2027 = 2026 年 2 月至 2027 年 1 月）。*参见 [第 00.1 章](00-start-here/ch00-1-how-to-use.md)。*

<a id="five-pillars-of-data-observability"></a>
### 数据可观测性五大支柱（Five pillars of data observability）

Monte Carlo 提出的监控信号框架：新鲜度、数据量、模式、分布和数据血缘。*参见 [第 13 章](02-pipelines-and-governance/ch13-data-quality-observability-lineage.md)。*

<a id="fixed-size-chunking"></a>
### 固定大小分块（Fixed-size chunking）

不考虑文档结构、每 N 个 token 切分一次文本。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="flex-credits"></a>
### Flex Credits

Salesforce 为 Agentforce 设立的用量计费货币，按智能体动作定价。*参见 [第 34 章](04-company-deep-dives/ch34-application-giants-data-platforms.md)。*

<a id="foreign-key"></a>
### 外键（Foreign key）

取值必须与另一张表的主键匹配的列，用于关联相关的行。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="format-preserving-encryption"></a>
### 保格式加密（Format-preserving encryption）

输出保持输入格式的加密方式，例如 16 位数字加密后仍为 16 位数字。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="free-cash-flow-margin"></a>
### 自由现金流利润率（Free cash flow margin）

经营现金流减资本开支，再除以收入。*参见 [第 36 章](05-business-and-economics/ch36-unit-economics-kpis.md)。*

<a id="freight-cluster"></a>
### Freight 集群（Freight cluster）

Confluent Cloud 的一种集群类型，直接写入对象存储，以更高的延迟换取大幅降低的成本。*参见 [第 30 章](04-company-deep-dives/ch30-data-movement-streaming-companies.md)。*

<a id="fsync"></a>
### Fsync

强制将某文件的缓冲写入落到稳定存储上的操作系统调用。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

## G

<a id="gaap"></a>
### GAAP

美国公认会计原则（US Generally Accepted Accounting Principles）；在本书中，指依据该准则在 SEC 文件或财报中披露的数字所使用的标签。*参见 [第 00.1 章](00-start-here/ch00-1-how-to-use.md)。*

<a id="gen2-warehouse"></a>
### Gen2 仓库（Gen2 warehouse）

Snowflake 新一代虚拟仓库，采用更快的硬件和软件，沿用相同的基于 credit 的计费方式。*参见 [第 26 章](04-company-deep-dives/ch26-snowflake.md)。*

<a id="genie"></a>
### Genie

Databricks 的自然语言分析智能体，可将问题转换为受治理的 SQL，2026 年扩展为 Genie One。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="global-namespace"></a>
### 全局命名空间（Global namespace）

跨越多个存储系统、站点和云的单一文件系统视图。*参见 [第 32 章](04-company-deep-dives/ch32-ai-native-data-companies.md)。*

<a id="golden-set"></a>
### 黄金测试集（Golden set）

经过精选、带版本管理的测试输入及参考答案集合，用于对 AI 应用进行回归测试。*参见 [第 21 章](03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)。*

<a id="goodwill-impairment"></a>
### 商誉减值（Goodwill impairment）

当被收购业务的价值低于其账面价值时，对收购商誉进行的减记。*参见 [第 39 章](05-business-and-economics/ch39-ma-history.md)。*

<a id="gpudirect-storage"></a>
### GPUDirect Storage

NVIDIA 的一项技术，通过 DMA 将数据从存储直接搬入 GPU 显存，绕过经主机 DRAM 的一次拷贝。*参见 [第 24 章](03-ai-data-stack/ch24-data-meets-compute-and-storage.md)。*

<a id="gql"></a>
### GQL

图查询语言（Graph Query Language），即用于查询属性图的 ISO/IEC 39075:2024 标准，在很大程度上基于 Cypher。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="granule"></a>
### 颗粒（Granule）

ClickHouse 读取数据的最小单位，默认 8,192 行，由一条稀疏索引条目寻址。*参见 [第 23 章](03-ai-data-stack/ch23-real-time-analytics-htap.md)。*

<a id="graph-traversal"></a>
### 图遍历（Graph traversal）

沿着边从一个节点走到另一个节点来回答查询，成本与所触及的边数成正比。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="graphrag"></a>
### GraphRAG

Microsoft Research 于 2024 年提出的方法：由 LLM 抽取实体图，将其聚类为社区，并预先撰写摘要，用于回答面向整个语料库的问题。*参见 [第 19 章](03-ai-data-stack/ch19-retrieval-architectures.md)。*

<a id="gross-revenue-retention"></a>
### 总收入留存率（Gross revenue retention）

上一年度客户群在扣除缩减和流失后（不计扩张）保留下来的支出占比，上限为 100%。*参见 [第 36 章](05-business-and-economics/ch36-unit-economics-kpis.md)。*

<a id="group-commit"></a>
### 组提交（Group commit）

通过一次日志刷盘让多个并发提交的事务同时获得持久性。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="growth-adjusted-multiple"></a>
### 增长调整倍数（Growth-adjusted multiple）

估值倍数除以收入增长率，用于比较增速不同的公司。*参见 [第 27 章](04-company-deep-dives/ch27-databricks-vs-snowflake.md)。*

<a id="guardrails"></a>
### 护栏（Guardrails）

对输入和输出进行的检查，用于拦截提示词注入、数据泄露，或不安全、不合规的 LLM 响应。*参见 [第 21 章](03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)。*

## H

<a id="hdfs"></a>
### HDFS

Hadoop 分布式文件系统（Hadoop Distributed File System），将大文件以多副本数据块的形式存放在集群服务器的本地磁盘上。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="headless-bi"></a>
### 无头 BI（Headless BI）

与任何单一可视化工具解耦、通过 API 服务众多消费方的语义层。*参见 [第 14 章](02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)。*

<a id="hidden-partitioning"></a>
### 隐藏分区（Hidden partitioning）

Iceberg 的做法：通过列变换推导分区值，使查询只需对普通列过滤，而无需引用分区。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="hierarchical-database"></a>
### 层次型数据库（Hierarchical database）

一种导航式数据库，以父子树结构存储记录，例如 IBM IMS。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="hive-metastore"></a>
### Hive Metastore

Apache Hive 基于 Thrift、以关系型数据库为后端的服务，记录表、列和分区信息；是第一个被广泛共享的湖仓目录。*参见 [第 08 章](01-data-systems-foundations/ch08-catalogs-and-metastores.md)。*

<a id="hnsw"></a>
### HNSW

分层可导航小世界（Hierarchical Navigable Small World），一种分层邻近图向量索引，从稀疏层到稠密层进行贪心下降搜索。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="holdback"></a>
### 留存对价（Holdback）

交易对价中被扣留或与继续任职挂钩的部分，通常作为薪酬费用化处理，而不计入交易价格。*参见 [第 39 章](05-business-and-economics/ch39-ma-history.md)。*

<a id="horizon-catalog"></a>
### Horizon Catalog

Snowflake 内置的数据与 AI 对象数据治理、数据发现和访问控制层。*参见 [第 27 章](04-company-deep-dives/ch27-databricks-vs-snowflake.md)。*

<a id="hot-spot"></a>
### 热点（Hot spot）

承受不成比例流量、从而限制整个集群吞吐量的分片或键。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="htap"></a>
### HTAP

混合事务分析处理（Hybrid transactional/analytical processing）：由一个系统在新鲜数据上同时服务 OLTP 和 OLAP 工作负载（该术语由 Gartner 于 2014 年提出）。*参见 [第 01 章](01-data-systems-foundations/ch01-data-stack-map.md)。*

<a id="hudi-timeline"></a>
### Hudi 时间线（Hudi timeline）

Apache Hudi 对表操作（提交、压缩、清理）的有序记录，每个操作依次经历 requested、inflight、completed 三个状态。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="hybrid-data-platform"></a>
### 混合数据平台（Hybrid data platform）

设计为在本地和公有云中均可运行、使用相同工具和数据治理的单一数据软件栈。*参见 [第 31 章](04-company-deep-dives/ch31-analytical-engine-challengers-legacy.md)。*

<a id="hybrid-logical-clock"></a>
### 混合逻辑时钟（Hybrid logical clock）

将物理时钟时间与逻辑计数器相结合的时间戳，CockroachDB 和 YugabyteDB 用它在无需专用硬件的情况下对事件排序。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="hybrid-search"></a>
### 混合检索（Hybrid search）

将关键词（BM25）检索与向量检索相结合，通常随后再接一个重排序器。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="hybrid-table"></a>
### 混合表（Hybrid table）

Snowflake 的行存表类型（Unistore），在分析之外支持低延迟的事务型读写。*参见 [第 26 章](04-company-deep-dives/ch26-snowflake.md)。*

<a id="hyde"></a>
### HyDE

假设文档嵌入（Hypothetical Document Embeddings）：用 LLM 撰写的假设性答案的嵌入向量（而非原始问题）进行检索。*参见 [第 19 章](03-ai-data-stack/ch19-retrieval-architectures.md)。*

<a id="hyperscaler"></a>
### 超大规模云厂商（Hyperscaler）

在全球数据中心规模上运营的云服务商，主要是 AWS、Microsoft Azure 和 Google Cloud，常常也把 Oracle OCI 计入。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

## I

<a id="iceberg-rest-catalog"></a>
### Iceberg REST 目录（Iceberg REST catalog）

开放的 HTTP API 规范，各引擎通过它加载 Iceberg 表、向其提交，并越来越多地借助它规划扫描。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="icehouse"></a>
### Icehouse

Starburst 对一种湖仓的命名：基于 Trino 引擎和对象存储上的 Apache Iceberg 表构建。*参见 [第 31 章](04-company-deep-dives/ch31-analytical-engine-challengers-legacy.md)。*

<a id="idempotency"></a>
### 幂等性（Idempotency）

一项操作执行多次与执行一次产生相同结果的性质。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="idempotent-producer"></a>
### 幂等生产者（Idempotent producer）

为批次打上序列号的 Kafka 生产者，借助 broker 端去重使重试无害。*参见 [第 11 章](02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。*

<a id="identity-propagation"></a>
### 身份传递（Identity propagation）

在每一跳中传递终端用户的身份，使下游系统执行该用户的权限，而非服务账号的权限。*参见 [第 22 章](03-ai-data-stack/ch22-agents-and-data.md)。*

<a id="illiquidity-discount"></a>
### 流动性折价（Illiquidity discount）

对无法在公开市场自由出售的股份所施加的价值折减。*参见 [第 27 章](04-company-deep-dives/ch27-databricks-vs-snowflake.md)。*

<a id="impact-analysis"></a>
### 影响分析（Impact analysis）

利用下游数据血缘，找出受拟议或实际变更影响的每一项资产及其负责人。*参见 [第 13 章](02-pipelines-and-governance/ch13-data-quality-observability-lineage.md)。*

<a id="in-process-database"></a>
### 进程内数据库（In-process database）

以库的形式运行在应用进程内部、没有独立服务器的数据库引擎（例如 SQLite、DuckDB）。*参见 [第 23 章](03-ai-data-stack/ch23-real-time-analytics-htap.md)。*

<a id="in-sync-replicas"></a>
### 同步副本（In-sync replicas）

与分区 leader 完全保持同步的副本（ISR）；在 acks=all 确认之前，所有同步副本都必须持有该写入。*参见 [第 11 章](02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。*

<a id="incremental-model"></a>
### 增量模型（Incremental model）

只处理新增或变更的行、并将其合并进现有表而非重建整表的数据转换。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

<a id="incremental-snapshot"></a>
### 增量快照（Incremental snapshot）

对表进行分块、无锁的拷贝，并借助水位标记与实时 CDC 流交错进行（DBLog/Debezium）。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="incremental-sync"></a>
### 增量同步（Incremental sync）

只拉取自上次成功同步以来发生变化的记录。*参见 [第 10 章](02-pipelines-and-governance/ch10-ingestion-and-integration.md)。*

<a id="informatica-processing-unit"></a>
### Informatica Processing Unit

Informatica 预付费、池化的用量单位，可在 IDMC 各项服务之间通用。*参见 [第 10 章](02-pipelines-and-governance/ch10-ingestion-and-integration.md)。*

<a id="integrated-device-manufacturer"></a>
### 垂直整合制造商（Integrated device manufacturer）

既设计又制造自家芯片的半导体公司（IDM）；本书用作超大规模云厂商的类比。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="integration-tax"></a>
### 集成税（Integration tax）

将众多厂商拼接在一起的隐性成本：额外的合同、故障点、重复的元数据，以及没有单一责任方对结果负责。*参见 [第 43 章](06-history-and-future/ch43-modern-data-stack.md)。*

<a id="inter-az-data-transfer"></a>
### 跨可用区数据传输（Inter-AZ data transfer）

同一区域内不同可用区之间网络流量的按 GB 云计费。*参见 [第 11 章](02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。*

<a id="inverted-index"></a>
### 倒排索引（Inverted index）

将每个词项映射到包含该词项的文档列表的搜索索引。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="ipaas"></a>
### iPaaS

集成平台即服务（integration platform as a service），主要用于通过 API 和事件连接业务应用。*参见 [第 10 章](02-pipelines-and-governance/ch10-ingestion-and-integration.md)。*

<a id="isolation-level"></a>
### 隔离级别（Isolation level）

定义数据库允许事务观察到哪些并发异常的设置。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="isv-accelerate"></a>
### ISV Accelerate

AWS 面向在 AWS Marketplace 上架和销售的软件厂商的联合销售计划。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

<a id="ivf"></a>
### IVF

倒排文件索引（Inverted file index）：用 k-means 对向量聚类，只搜索距离查询最近的若干簇（由 nprobe 设定）。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="ivf-pq"></a>
### IVF-PQ

将 IVF 聚类与乘积量化向量相结合的向量索引，是在单机或单 GPU 上进行十亿级检索的标准方案。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

## J

<a id="jaccard-similarity"></a>
### Jaccard 相似度（Jaccard similarity）

两个集合交集的大小除以并集的大小，用于衡量近似重复文本。*参见 [第 20 章](03-ai-data-stack/ch20-training-data-supply-chain.md)。*

<a id="jevons-paradox"></a>
### 杰文斯悖论（Jevons paradox）

这一观察：降低单位成本的效率提升，反而可能增加资源的总消耗量。*参见 [第 35 章](05-business-and-economics/ch35-business-models.md)。*

<a id="jinja"></a>
### Jinja

dbt 用于宏、控制流以及 ref() 等函数的 Python 模板语言。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

<a id="join"></a>
### 连接（Join）

按匹配的键值将两张或多张表中的行组合起来的查询操作。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

## K

<a id="k-nearest-neighbors"></a>
### k 最近邻（k-nearest neighbors）

精确查找与查询最接近的 k 个已存向量，需要与每一个向量进行比较。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="key-person-risk"></a>
### 关键人物风险（Key-person risk）

若少数个人（如创始人或核心工程师）离开，公司将损失的价值。*参见 [第 47 章](07-conversation-toolkit/ch47-diligence-checklist.md)。*

<a id="key-value-store"></a>
### 键值存储（Key-value store）

按唯一键存取不透明值的数据库，类似分布式哈希表。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="knowledge-catalog"></a>
### Knowledge Catalog

Google Cloud 的数据治理与元数据目录，2026 年由 Dataplex Universal Catalog 更名而来。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="knowledge-graph"></a>
### 知识图谱（Knowledge graph）

存储实体及其之间带类型关系的存储，通过遍历进行查询。*参见 [第 19 章](03-ai-data-stack/ch19-retrieval-architectures.md)。*

<a id="kraft"></a>
### KRaft

Kafka 内置的基于 Raft 的元数据仲裁机制，取代了 ZooKeeper，并在 Kafka 4.0 中成为必选项。*参见 [第 11 章](02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。*

<a id="kv-cache"></a>
### KV 缓存（KV cache）

Transformer 为已处理 token 存储的注意力键和值，使其无需重新计算；其大小随上下文长度线性增长。*参见 [第 19 章](03-ai-data-stack/ch19-retrieval-architectures.md)。*

<a id="kv-cache-offload"></a>
### KV 缓存卸载（KV-cache offload）

将模型的 KV 缓存块从 GPU 显存移到 CPU 内存、本地闪存或网络存储，以便复用而非重新计算。*参见 [第 45 章](06-history-and-future/ch45-storage-moving-up-the-stack.md)。*

## L

<a id="lakebase"></a>
### Lakebase

Databricks 基于收购 Neon 构建的无服务器 Postgres 数据库，计算与以对象存储为后端的存储相分离。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="lakeflow"></a>
### Lakeflow

Databricks 用于数据摄取、声明式数据管道和作业编排的套件。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="lakehouse"></a>
### 湖仓一体（Lakehouse）

一种架构，在对象存储上的开放文件格式和表格式之上，提供数据仓库级的管理能力与性能。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="lance"></a>
### Lance

LanceDB 的开放列式文件格式及表层，专为快速随机访问、版本管理以及多模态/向量 AI 数据而设计。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

<a id="late-chunking"></a>
### 后期分块（Late chunking）

先用长上下文模型对整篇文档做嵌入，再将 token 向量池化为分块向量。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="late-data"></a>
### 迟到数据（Late data）

在水位线越过其所属窗口末端之后才到达的事件，会被丢弃或用于修正结果。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="late-materialization"></a>
### 延迟物化（Late materialization）

推迟完整行的组装，直到过滤条件把数据缩减到匹配的位置之后再进行。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="layout-analysis"></a>
### 版面分析（Layout analysis）

检测页面中的各个区域（标题、段落、表格、图片）及其相互关系。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="leaderless-replication"></a>
### 无主复制（Leaderless replication）

一种 Dynamo 风格的拓扑：客户端直接向副本的法定多数（quorum）读写，没有单一 leader。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="lethal-trifecta"></a>
### 致命三要素（Lethal trifecta）

在同一个智能体中同时具备以下三者的危险组合：可访问私有数据、接触不可信内容、拥有向外发送数据的通道。*参见 [第 22 章](03-ai-data-stack/ch22-agents-and-data.md)。*

<a id="license-and-hire"></a>
### 授权加招聘（License-and-hire）

一种交易方式：授权使用初创公司的技术并聘用其领导层，但不取得公司控制权（例如 2025 年 Google–Windsurf）。*参见 [第 39 章](05-business-and-economics/ch39-ma-history.md)。*

<a id="linearizability"></a>
### 线性一致性（Linearizability）

一种一致性模型，其中每个操作看起来都在某个与真实时间一致的瞬间生效。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="liquidation-preference"></a>
### 清算优先权（Liquidation preference）

优先股股东在出售或清算时先于普通股股东获得偿付的权利。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="listen-for-note"></a>
### 倾听要点（Listen-for note）

在第 48 章问题库中，对某个问题的优秀回答应包含哪些内容的简短描述，用作会后评分标准。*参见 [第 48 章](07-conversation-toolkit/ch48-question-bank.md)。*

<a id="listing-fee"></a>
### 上架费（Listing fee）

云市场对每笔交易抽取的合同金额百分比，目前大多数私有报价为 1.5–3%。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

<a id="llm-evaluation"></a>
### LLM 评估（LLM evaluation）

对 LLM 应用输出进行系统化评分，可离线基于精选测试集，也可在线基于抽样的生产流量。*参见 [第 21 章](03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)。*

<a id="llm-judge"></a>
### LLM 评审（LLM judge）

用于按评分细则给其他模型输出打分的语言模型。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="llm-trace"></a>
### LLM 追踪（LLM trace）

单次 LLM 或智能体请求中每一步骤、token 数量、延迟和成本的记录。*参见 [第 21 章](03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)。*

<a id="llm-as-judge"></a>
### LLM 即评审（LLM-as-judge）

使用语言模型按评分细则或参考答案给另一个模型的输出打分。*参见 [第 19 章](03-ai-data-stack/ch19-retrieval-architectures.md)。*

<a id="llmops"></a>
### LLMOps

适配 LLM 应用的 MLOps，主要管理提示词、追踪、评估、护栏和网关，而非以模型权重为主。*参见 [第 21 章](03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)。*

<a id="locality-sensitive-hashing"></a>
### 局部敏感哈希（Locality-sensitive hashing）

将相似对象放入同一个桶中的哈希方法，从而只需比较可能匹配的对象（LSH）。*参见 [第 20 章](03-ai-data-stack/ch20-training-data-supply-chain.md)。*

<a id="log-compaction"></a>
### 日志压缩（Log compaction）

Kafka 的一种保留模式，只保留每个键的最新记录，把主题变成反映当前状态的变更日志。*参见 [第 11 章](02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。*

<a id="log-based-cdc"></a>
### 基于日志的 CDC（Log-based CDC）

读取数据库恢复日志（Postgres WAL、MySQL binlog、Oracle redo）而非查询表的变更数据捕获。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="logo-churn"></a>
### 客户数流失率（Logo churn）

某一期间内流失客户所占比例，按客户账户数而非金额计算。*参见 [第 47 章](07-conversation-toolkit/ch47-diligence-checklist.md)。*

<a id="lookml"></a>
### LookML

Looker 基于代码、用 Git 管理版本的语言，用于定义可生成 SQL 的语义模型。*参见 [第 14 章](02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)。*

<a id="lost-in-the-middle"></a>
### 中间迷失（Lost in the middle）

一项研究发现（Liu et al., 2023）：语言模型对长输入开头和结尾信息的利用效果好于对中间信息的利用。*参见 [第 19 章](03-ai-data-stack/ch19-retrieval-architectures.md)。*

<a id="lsm-tree"></a>
### LSM 树（LSM-tree）

日志结构合并树（log-structured merge tree），一种为写入优化的结构，先缓冲写入，再在后台合并有序的数据段。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="luhn-checksum"></a>
### Luhn 校验（Luhn checksum）

一种校验位算法，用于验证疑似支付卡号并排除大多数随机数字串。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

## M

<a id="macc"></a>
### MACC

Microsoft Azure Consumption Commitment（Microsoft Azure 消费承诺），Microsoft 的承诺消费额度合同，符合条件的 Azure Marketplace 采购可从中抵扣。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="magic-number"></a>
### 魔法数字（Magic number）

某季度年化新增收入除以上一季度的销售与营销支出；用于检验市场进入效率。*参见 [第 36 章](05-business-and-economics/ch36-unit-economics-kpis.md)。*

<a id="managed-storage"></a>
### 托管存储（Managed storage）

数据仓库背后由厂商运营的分层存储（本地 SSD 缓存加对象存储），例如 Redshift RA3。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="manifest"></a>
### 清单文件（Manifest）

Iceberg 的 Avro 文件，列出数据文件或删除文件及其分区值和逐列统计信息。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="manifest-list"></a>
### 清单列表（Manifest list）

Iceberg 中列出构成某个快照的各清单文件的文件，附带用于跳过清单的分区范围摘要。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="mapreduce"></a>
### MapReduce

Google 于 2004 年提出的编程模型，以 map 步骤加 reduce 步骤的方式并行处理大型数据集。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="market-development-funds"></a>
### 市场开发基金（Market development funds）

厂商提供给合作伙伴、用于联合营销和需求生成的资金（MDF）。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

<a id="market-map"></a>
### 市场版图（Market map）

将公司和项目放置在行业技术栈各层中的示意图。*参见 [第 00.2 章](00-start-here/ch00-2-market-map.md)。*

<a id="marketplace-drawdown"></a>
### 云市场抵扣（Marketplace drawdown）

将通过云市场进行的采购计入客户对该云的承诺消费额度。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="marquez"></a>
### Marquez

LF AI & Data 旗下的开源参考实现，用于收集、存储和提供 OpenLineage 事件。*参见 [第 13 章](02-pipelines-and-governance/ch13-data-quality-observability-lineage.md)。*

<a id="massively-parallel-processing"></a>
### 大规模并行处理（Massively parallel processing）

将一个查询分散到多个节点，每个节点并行处理一部分数据（MPP）。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="master-data-management"></a>
### 主数据管理（Master data management）

将关于同一客户、产品或供应商的重复记录归并为一条可信"黄金记录"的软件和流程。*参见 [第 30 章](04-company-deep-dives/ch30-data-movement-streaming-companies.md)。*

<a id="materialization"></a>
### 物化方式（Materialization）

dbt 模型结果的持久化方式：视图、表、增量表或临时（ephemeral）CTE。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

<a id="materialized-view"></a>
### 物化视图（Materialized view）

随源数据变化而保持更新的已存储查询结果；在 ClickHouse 中，是一种写入预聚合行的插入触发器。*参见 [第 23 章](03-ai-data-stack/ch23-real-time-analytics-htap.md)。*

<a id="matryoshka-embedding"></a>
### 套娃嵌入（Matryoshka embedding）

经过特殊训练的嵌入，其前若干维即可构成一个可用的较短嵌入，从而允许截断。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="mcp-server"></a>
### MCP 服务器（MCP server）

封装某个系统、并通过 Model Context Protocol 向 AI 智能体暴露工具、资源和提示词的服务。*参见 [第 22 章](03-ai-data-stack/ch22-agents-and-data.md)。*

<a id="mdx"></a>
### MDX

多维表达式（Multidimensional Expressions），源自 Microsoft、用于 OLAP 多维数据集的查询语言。*参见 [第 14 章](02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)。*

<a id="measure"></a>
### 度量（Measure）

在语义模型中定义的、带业务规则的聚合（例如净收入 = 总收入减退款）。*参见 [第 14 章](02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)。*

<a id="medallion-architecture"></a>
### 奖章架构（Medallion architecture）

将数据分层为铜层（原始）、银层（清洗并统一口径）和金层（可直接用于业务）表。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="memtable"></a>
### 内存表（Memtable）

LSM 树中位于内存、有序的写缓冲区，写满后刷写到磁盘。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="merge-on-read"></a>
### 读时合并（Merge-on-read）

通过写入独立的删除或变更记录来应用行级变更，在压缩之前由读取方在查询时进行合并。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="merger-of-equals"></a>
### 对等合并（Merger of equals）

规模相近的公司之间进行的全股票合并，不含大额控制权溢价。*参见 [第 39 章](05-business-and-economics/ch39-ma-history.md)。*

<a id="mergetree"></a>
### MergeTree

ClickHouse 的核心表引擎：每次插入写入有序、不可变的列式数据部件（part），并在后台合并。*参见 [第 23 章](03-ai-data-stack/ch23-real-time-analytics-htap.md)。*

<a id="metadata-pointer"></a>
### 元数据指针（Metadata pointer）

目录中记录哪个元数据文件代表表当前版本的条目；以原子方式替换该指针即构成一次 Iceberg 提交。*参见 [第 08 章](01-data-systems-foundations/ch08-catalogs-and-metastores.md)。*

<a id="metastore"></a>
### 元数据存储（Metastore）

存储表定义、模式和位置、使查询引擎能够找到数据的服务；是 Hive 时代对技术目录的称呼。*参见 [第 08 章](01-data-systems-foundations/ch08-catalogs-and-metastores.md)。*

<a id="metric-view"></a>
### 指标视图（Metric view）

Databricks Unity Catalog 中的一种对象，用于定义受治理、可复用、可通过 SQL 查询的业务指标。*参见 [第 14 章](02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)。*

<a id="metricflow"></a>
### MetricFlow

dbt Semantic Layer 背后的 dbt 指标定义与 SQL 生成引擎，于 2025 年 10 月以 Apache 2.0 协议开源。*参见 [第 14 章](02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)。*

<a id="metrics-layer"></a>
### 指标层（Metrics layer）

一种专注于一次定义指标、跨工具复用的语义层；常与"语义层"互换使用。*参见 [第 14 章](02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)。*

<a id="micro-batch"></a>
### 微批（Micro-batch）

将流作为一连串快速的小批作业来处理，通常每隔几秒到几分钟一次。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="micro-partition"></a>
### 微分区（Micro-partition）

Snowflake 不可变的列式存储单元（未压缩时 50–500 MB），携带用于剪枝的逐列元数据。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="microsoft-fabric"></a>
### Microsoft Fabric

Microsoft 的 SaaS 分析套件（数据管道、Spark、数据仓库、实时分析、Power BI），构建于 OneLake 之上，采用容量计费。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="minhash"></a>
### MinHash

一种以低成本估算文档间集合相似度的哈希技术，用于网络规模的近似重复去除。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="mlops"></a>
### MLOps

使机器学习生命周期（数据、特征、训练、注册、服务、监控）可重复、受治理且受监控的实践与工具。*参见 [第 21 章](03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)。*

<a id="model-checkpoint"></a>
### 模型检查点（Model checkpoint）

模型权重和优化器状态的已保存快照，用于恢复、回滚或审计训练。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="model-collapse"></a>
### 模型崩溃（Model collapse）

模型在模型生成的数据上递归训练时出现的渐进式退化，会丢失真实分布中的稀有尾部。*参见 [第 20 章](03-ai-data-stack/ch20-training-data-supply-chain.md)。*

<a id="model-context-protocol"></a>
### Model Context Protocol

Anthropic 于 2024 年推出的开放标准（MCP），用于向 AI 智能体暴露工具和数据源。*参见 [第 01 章](01-data-systems-foundations/ch01-data-stack-map.md)。*

<a id="model-contract"></a>
### 模型契约（Model contract）

dbt 的一项功能：若模型输出的列或数据类型偏离声明的结构，则使该模型构建失败。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

<a id="model-registry"></a>
### 模型注册表（Model registry）

记录模型版本及其血缘、生命周期阶段和审批信息的目录，用于将模型推进到生产环境。*参见 [第 21 章](03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)。*

<a id="modern-data-stack"></a>
### 现代数据栈（Modern data stack）

2018–2022 年间由数据摄取、数据仓库、数据转换、BI 和数据激活等独立厂商组成的云端工具链。*参见 [第 39 章](05-business-and-economics/ch39-ma-history.md)。*

<a id="monthly-active-rows"></a>
### 月活跃行数（Monthly active rows）

Fivetran 的计费单位：一个月内被插入、更新或删除的不重复行数，自 2025 年 3 月起按每个连接分档计价。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="moving-up-the-stack"></a>
### 向技术栈上层延伸（Moving up the stack）

从较低的技术层（如存储）向其上方价值更高的软件层扩张。*参见 [第 45 章](06-history-and-future/ch45-storage-moving-up-the-stack.md)。*

<a id="mteb"></a>
### MTEB

大规模文本嵌入基准（Massive Text Embedding Benchmark），嵌入模型的标准公开排行榜（已扩展为 MMTEB）。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="multi-leader-replication"></a>
### 多主复制（Multi-leader replication）

多个副本都接受写入并相互交换写入的拓扑，因此必须解决冲突写入。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="multi-model-database"></a>
### 多模型数据库（Multi-model database）

支持多种数据模型（如表、JSON 文档和向量）的单一数据库引擎。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="multi-tenancy"></a>
### 多租户（Multi-tenancy）

用共享基础设施服务众多客户，同时使各客户的数据和工作负载相互隔离。*参见 [第 47 章](07-conversation-toolkit/ch47-diligence-checklist.md)。*

<a id="multiple-compression"></a>
### 估值倍数压缩（Multiple compression）

由利率或市场情绪（而非基本面变化）驱动的估值倍数（如 EV/未来 12 个月收入）下降。*参见 [第 37 章](05-business-and-economics/ch37-public-comps-valuation.md)。*

<a id="mvcc"></a>
### MVCC

多版本并发控制（multi-version concurrency control）：为一行数据保留多个版本，使读取方和写入方互不阻塞。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

## N

<a id="named-entity-recognition"></a>
### 命名实体识别（Named-entity recognition）

在自由文本中标注人名、地名、组织名等实体的机器学习技术。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="namespace"></a>
### 命名空间（Namespace）

在目录中对表进行分组的层级容器，例如数据库或 schema。*参见 [第 08 章](01-data-systems-foundations/ch08-catalogs-and-metastores.md)。*

<a id="navigational-database"></a>
### 导航式数据库（Navigational database）

程序沿着已存储的指针从一条记录走到另一条记录来查找数据的数据库，如 IMS 和 CODASYL 系统。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="ndjson"></a>
### NDJSON

换行分隔 JSON（Newline-delimited JSON）：每行一条自包含 JSON 记录的文本文件，便于流式处理，但解析成本高。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

<a id="needle-in-a-haystack"></a>
### 大海捞针（Needle in a haystack）

一种长上下文测试：将一条事实藏在填充文本中，要求模型将其找出；它衡量的是查找能力而非推理能力。*参见 [第 19 章](03-ai-data-stack/ch19-retrieval-architectures.md)。*

<a id="net-arr-expansion-rate"></a>
### 净 ARR 扩张率（Net ARR expansion rate）

MongoDB 基于 ARR 的留存指标：一年前已有客户的当前 ARR，除以一年前全部客户的 ARR。*参见 [第 36 章](05-business-and-economics/ch36-unit-economics-kpis.md)。*

<a id="net-revenue-retention"></a>
### 净收入留存率（Net revenue retention）

上一年度客户群今年的支出，除以该客户群一年前的支出。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="newsql"></a>
### NewSQL

在水平扩展下提供 SQL 和 ACID 事务的分布式数据库，又称分布式 SQL。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="nimble"></a>
### Nimble

Meta 的开源列式文件格式，面向超宽的机器学习特征表。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

<a id="non-gaap-operating-margin"></a>
### 非 GAAP 营业利润率（Non-GAAP operating margin）

加回股权激励费用、收购无形资产摊销及其他公司自定义项目后的营业利润率。*参见 [第 36 章](05-business-and-economics/ch36-unit-economics-kpis.md)。*

<a id="normalization"></a>
### 规范化（Normalization）

对关系表进行结构设计，使每条事实只存储一次，从而避免更新异常。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="nosql"></a>
### NoSQL

自 2009 年起流行的统称，指键值、文档、宽列和图存储等非关系型数据库。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="ntm-revenue-multiple"></a>
### NTM 收入倍数（NTM revenue multiple）

企业价值除以未来十二个月收入（通常取自公司指引或市场一致预期），是成长型软件公司的标准估值尺度。*参见 [第 37 章](05-business-and-economics/ch37-public-comps-valuation.md)。*

<a id="nvidia-ai-data-platform"></a>
### NVIDIA AI Data Platform

NVIDIA 于 2025 年推出的参考设计，存储合作伙伴据此打造面向 AI 的存储产品。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

<a id="nvidia-certified-storage"></a>
### NVIDIA-Certified Storage

NVIDIA 的存储验证计划，分为 Foundation、Enterprise 和 NCP 三个等级。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

## O

<a id="object-storage"></a>
### 对象存储（Object storage）

通过 HTTP 访问、按键寻址不可变对象的扁平化存储，例如 Amazon S3。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="odcs"></a>
### ODCS

开放数据契约标准（Open Data Contract Standard），由 Linux Foundation 旗下 Bitol 项目维护的数据契约 YAML 规范。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

<a id="oem"></a>
### OEM

原始设备制造商（Original equipment manufacturer）安排：一家厂商将另一家厂商的产品嵌入自身产品中并转售。*参见 [第 31 章](04-company-deep-dives/ch31-analytical-engine-challengers-legacy.md)。*

<a id="oem-partnership"></a>
### OEM 合作（OEM partnership）

一家公司嵌入或捆绑另一家公司的产品、并以自有品牌销售的合作安排。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

<a id="offline-store"></a>
### 离线存储（Offline store）

特征存储中保存完整、带时间戳特征历史的部分，通常为湖仓表，用于构建训练集。*参见 [第 21 章](03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)。*

<a id="offset"></a>
### 偏移量（Offset）

一条记录在分区内的顺序位置编号。*参见 [第 11 章](02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。*

<a id="olap"></a>
### OLAP

联机分析处理（Online analytical processing）：对历史数据进行大规模扫描和聚合，通常基于列式存储。*参见 [第 01 章](01-data-systems-foundations/ch01-data-stack-map.md)。*

<a id="olap-cube"></a>
### OLAP 多维数据集（OLAP cube）

为快速切片和切块分析而预聚合的多维数据结构，通常使用 MDX 查询。*参见 [第 14 章](02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)。*

<a id="oltp"></a>
### OLTP

联机事务处理（Online transaction processing）：大量小型、快速、准确的读写操作，用于记录订单、支付等业务事件。*参见 [第 01 章](01-data-systems-foundations/ch01-data-stack-map.md)。*

<a id="on-behalf-of-flow"></a>
### 代表用户流程（On-behalf-of flow）

一种 OAuth 令牌交换，服务或智能体借此获取代表特定用户行事的令牌。*参见 [第 22 章](03-ai-data-stack/ch22-agents-and-data.md)。*

<a id="onelake"></a>
### OneLake

Microsoft Fabric 覆盖整个租户的单一逻辑数据湖，以 Delta/Parquet 格式存储表。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="onelake-shortcut"></a>
### OneLake 快捷方式（OneLake shortcut）

一种指针，可将 ADLS、S3、Google Cloud Storage 或其他存储中的数据挂载进 OneLake，而无需拷贝。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="online-store"></a>
### 在线存储（Online store）

特征存储中将每个实体的最新特征值保存在低延迟键值数据库中、供推理使用的部分。*参见 [第 21 章](03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)。*

<a id="ontology"></a>
### 本体（Ontology）

对组织的业务对象及其属性、关联和允许操作进行受治理建模的模型，例如 Palantir 的 Foundry Ontology。*参见 [第 19 章](03-ai-data-stack/ch19-retrieval-architectures.md)。*

<a id="open-core"></a>
### 开放核心（Open core）

一种商业模式：免费提供开源核心产品，围绕它销售专有功能、技术支持或托管服务。*参见 [第 30 章](04-company-deep-dives/ch30-data-movement-streaming-companies.md)。*

<a id="open-policy-agent"></a>
### Open Policy Agent

CNCF 毕业项目，一种通用策略引擎，用于评估以 Rego 语言编写的规则。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="open-semantic-interchange"></a>
### Open Semantic Interchange

由 Snowflake 牵头召集的跨厂商倡议（2025 年）及采用 Apache 许可证的规范，旨在实现可移植的语义模型。*参见 [第 14 章](02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)。*

<a id="open-source-definition"></a>
### 开源定义（Open Source Definition）

Open Source Initiative 规定的、许可证必须满足才能称为开源的十项标准，包括不得歧视用户或使用领域。*参见 [第 38 章](05-business-and-economics/ch38-open-source-strategy.md)。*

<a id="open-table-format"></a>
### 开放表格式（Open table format）

一种开放治理的元数据层和提交协议，将对象存储上的一组文件转变为具备快照和模式演进能力的事务性表。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="open-weights"></a>
### 开放权重（Open weights）

公开发布的 AI 模型参数，其许可证未必符合开源定义。*参见 [第 38 章](05-business-and-economics/ch38-open-source-strategy.md)。*

<a id="openflow"></a>
### Openflow

Snowflake 基于 Apache NiFi 的数据摄取服务，源于 2024 年对 Datavolo 的收购。*参见 [第 26 章](04-company-deep-dives/ch26-snowflake.md)。*

<a id="openlineage"></a>
### OpenLineage

LF AI & Data 的开放规范，定义数据作业在运行时发出的血缘事件（运行、作业、输入和输出数据集、facet）。*参见 [第 13 章](02-pipelines-and-governance/ch13-data-quality-observability-lineage.md)。*

<a id="opensharing"></a>
### OpenSharing

Linux Foundation 的开放协议，用于跨平台共享数据和 AI 资产，是 Delta Sharing 的继任者（2026 年）。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="opm-backsolve"></a>
### OPM 倒推法（OPM backsolve）

一种期权定价模型方法，根据最近一轮优先股的价格反推包括普通股在内的各类股份的价值。*参见 [第 37 章](05-business-and-economics/ch37-public-comps-valuation.md)。*

<a id="optical-character-recognition"></a>
### 光学字符识别（Optical character recognition）

将文字图像转换为机器可读字符，通常为每个词附带置信度分数（OCR）。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="optimistic-concurrency-control"></a>
### 乐观并发控制（Optimistic concurrency control）

一种机制：写入方在无锁状态下工作，在提交时进行校验，若其他写入方已先行提交则重试。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="optimization-cycle"></a>
### 优化周期（Optimization cycle）

客户系统性削减按用量计费账单、从而压低按用量计费厂商增长的时期，如 2022–23 年。*参见 [第 35 章](05-business-and-economics/ch35-business-models.md)。*

<a id="orchestrator"></a>
### 编排器（Orchestrator）

对数据或应用工作流进行调度、触发、运行、重试和记录的软件。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

<a id="orphan-file"></a>
### 孤儿文件（Orphan file）

位于表的存储位置中、但没有任何快照引用的文件，通常由失败或被放弃的写入遗留。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="outcome-based-pricing"></a>
### 按成果计费（Outcome-based pricing）

按完成的业务成果（如已解决的支持工单）收费，而非按席位或计算单位收费。*参见 [第 44 章](06-history-and-future/ch44-future-trends.md)。*

<a id="overage"></a>
### 超额用量（Overage）

超出承诺额度的用量，按需价格或事先约定的费率计费。*参见 [第 35 章](05-business-and-economics/ch35-business-models.md)。*

## P

<a id="pacelc"></a>
### PACELC

Abadi 对 CAP 定理的扩展：发生网络分区（P）时，在可用性与一致性之间取舍；否则（E），在延迟与一致性之间取舍。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="page"></a>
### 页（Page）

固定大小的数据块（例如 PostgreSQL 中为 8 kB，InnoDB 中为 16 KB），是数据库进行 I/O 与缓存的基本单位。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="page-split"></a>
### 页分裂（Page split）

将一个已满的 B 树页拆分为两个页，并在父页中插入一个新的分隔键。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="pagedattention"></a>
### PagedAttention

vLLM 的一项技术：像虚拟内存一样，将注意力键值缓存（KV cache）存放在固定大小的页中，以提升 GPU 利用率。*参见 [第 21 章](03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)。*

<a id="parallel-nfs"></a>
### 并行 NFS（Parallel NFS）

NFS 协议的扩展（pNFS，NFS v4.1 及以上版本），允许客户端并行地在多台存储服务器上读写数据。*参见 [第 32 章](04-company-deep-dives/ch32-ai-native-data-companies.md)。*

<a id="parquet"></a>
### Parquet

分析领域占主导地位的开放列式文件格式，所有主流开放表格式的底层都使用它。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="partition"></a>
### 分区（Partition）

Kafka 主题（topic）中一个独立有序的分片，是并行处理与消息排序的基本单位。*参见 [第 11 章](02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。*

<a id="partition-evolution"></a>
### 分区演进（Partition evolution）

在不重写现有文件的前提下，为新写入的数据更改表的分区方案。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="partition-key"></a>
### 分区键（Partition key）

其哈希值决定一条记录存放在哪个分区或节点上的属性。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="partner-sourced-pipeline"></a>
### 合作伙伴来源的销售管线（Partner-sourced pipeline）

由合作伙伴发起的销售机会，区别于合作伙伴仅参与过的“合作伙伴影响型”销售管线。*参见 [第 46 章](07-conversation-toolkit/ch46-talking-with-data-people.md)。*

<a id="partner-sourced-revenue"></a>
### 合作伙伴来源收入（Partner-sourced revenue）

来自合作伙伴发起之交易的收入，区别于合作伙伴仅提供协助的“合作伙伴影响型”交易。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

<a id="paxos"></a>
### Paxos

Leslie Lamport 提出的共识协议；Spanner 及众多 Google 系统在生产中以 Multi-Paxos 形式使用它。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="permission-aware-retrieval"></a>
### 权限感知检索（Permission-aware retrieval）

在排序之前，依据调用者身份和已存储的 ACL（访问控制列表）过滤检索候选结果。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="permissive-license"></a>
### 宽松许可证（Permissive license）

Apache 2.0、MIT 或 BSD 等开源许可证，只附带极少条件即允许复用，包括用于专有产品和托管服务之中。*参见 [第 38 章](05-business-and-economics/ch38-open-source-strategy.md)。*

<a id="perpetual-license"></a>
### 永久许可（Perpetual license）

一次性支付的软件许可费，授予无限期使用权，通常此后还需按年支付维护费。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="personally-identifiable-information"></a>
### 个人身份信息（Personally identifiable information）

可识别个人身份的数据，例如姓名、证件号码或联系方式（PII）。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="pgvector"></a>
### pgvector

开源的 PostgreSQL 扩展，用于存储嵌入（向量）并执行精确或近似最近邻检索。*参见 [第 29 章](04-company-deep-dives/ch29-operational-database-vendors.md)。*

<a id="photon"></a>
### Photon

Databricks 用 C++ 编写的向量化查询引擎，对其支持的算子取代 Spark 基于 JVM 的执行。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="pii"></a>
### PII

个人身份信息，例如姓名、电子邮件地址和证件号码，必须予以删除或实施访问控制。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="point-tool"></a>
### 单点工具（Point tool）

只完成数据工作流中某一个环节、其余环节依赖其他厂商产品的产品。*参见 [第 43 章](06-history-and-future/ch43-modern-data-stack.md)。*

<a id="point-in-time-join"></a>
### 时点连接（Point-in-time join）

一种连接操作：为每条训练标签关联其时间戳当时已知的最新特征值，从而防止数据泄漏。*参见 [第 21 章](03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)。*

<a id="policy-engine"></a>
### 策略引擎（Policy engine）

评估访问规则，并向执行点返回允许、拒绝、过滤或脱敏决策的软件。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="post-filtering"></a>
### 后过滤（Post-filtering）

在向量检索之后再施加元数据过滤；实现简单，但可能导致返回结果过少。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="post-modern-data-stack"></a>
### 后现代数据栈（Post-modern data stack）

2025–26 年趋于整合的架构：对象存储上的开放表、一个负责治理的目录、少数几个平台，以及位于其上的 AI 智能体。*参见 [第 43 章](06-history-and-future/ch43-modern-data-stack.md)。*

<a id="post-money-valuation"></a>
### 投后估值（Post-money valuation）

最近一轮私募融资的每股价格乘以本轮融资后全部完全稀释股数。*参见 [第 27 章](04-company-deep-dives/ch27-databricks-vs-snowflake.md)。*

<a id="post-training"></a>
### 后训练（Post-training）

预训练之后的各个阶段（监督微调、偏好调优、强化学习），将基础模型转变为助手。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="postgres-extension"></a>
### Postgres 扩展（Postgres extension）

无需分叉核心引擎即可为 PostgreSQL 增加数据类型、索引方法或函数的附加模块。*参见 [第 29 章](04-company-deep-dives/ch29-operational-database-vendors.md)。*

<a id="pre-filtering"></a>
### 预过滤（Pre-filtering）

在向量检索之前先施加元数据过滤；结果精确，但可能使图索引碎片化。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="precedent-transaction"></a>
### 先例交易（Precedent transaction）

过往的收购交易，其价格倍数（例如 EV/收入）被用作为可比公司估值的基准。*参见 [第 30 章](04-company-deep-dives/ch30-data-movement-streaming-companies.md)。*

<a id="predicate-pushdown"></a>
### 谓词下推（Predicate pushdown）

利用文件或行组的统计信息（最小/最大值、空值计数）跳过查询过滤条件不可能匹配的数据。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

<a id="preference-data"></a>
### 偏好数据（Preference data）

按优劣标注的模型输出配对或排序，用于 RLHF 或 DPO。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="press-reported"></a>
### 媒体报道（Press-reported）

由商业媒体报道但未经公司证实的数字；本知识库五类数字标签之一。*参见 [第 00.1 章](00-start-here/ch00-1-how-to-use.md)。*

<a id="pretraining"></a>
### 预训练（Pretraining）

在规模极大的通用语料（例如经过过滤的网页文本）上训练模型预测下一个词元（token）。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="primary-key"></a>
### 主键（Primary key）

唯一标识表中每一行的一列或一组列。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="private-offer"></a>
### 私有报价（Private offer）

卖方向某一买方的云市场账户单独发布的定制价格与条款。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

<a id="product-gross-margin"></a>
### 产品毛利率（Product gross margin）

仅针对平台（产品）收入计算的毛利率，不含专业服务。*参见 [第 36 章](05-business-and-economics/ch36-unit-economics-kpis.md)。*

<a id="product-quantization"></a>
### 乘积量化（Product quantization）

一种向量压缩方法：把每个向量切分为若干片段，每个片段存储为指向一个学习得到的码本的索引。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="product-revenue"></a>
### 产品收入（Product revenue）

Snowflake 按消费确认的收入项目，不含专业服务。*参见 [第 35 章](05-business-and-economics/ch35-business-models.md)。*

<a id="project-aether"></a>
### Project Aether

NVIDIA 在 GTC 2025 上发布的工具，用于对 Spark 作业进行 GPU 加速适配评估、测试和调优。*参见 [第 24 章](03-ai-data-stack/ch24-data-meets-compute-and-storage.md)。*

<a id="project-management-committee"></a>
### 项目管理委员会（Project Management Committee）

依据贡献（merit）选举产生、负责治理一个 Apache 软件基金会项目的成员群体。*参见 [第 38 章](05-business-and-economics/ch38-open-source-strategy.md)。*

<a id="prompt-caching"></a>
### 提示缓存（Prompt caching）

在多次请求之间复用已处理过的提示前缀，以折扣后的词元价格和更低的延迟提供服务。*参见 [第 19 章](03-ai-data-stack/ch19-retrieval-architectures.md)。*

<a id="prompt-injection"></a>
### 提示注入（Prompt injection）

嵌入在 LLM 所读取内容中的恶意指令，使其做出违背用户利益的行为。*参见 [第 22 章](03-ai-data-stack/ch22-agents-and-data.md)。*

<a id="property-graph"></a>
### 属性图（Property graph）

由节点和边构成的图数据模型，节点和边都可以携带键值属性。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="pruning"></a>
### 剪枝（Pruning）

依据已存储的最小/最大值元数据，跳过可证明不可能匹配查询过滤条件的数据文件或分区。*参见 [第 26 章](04-company-deep-dives/ch26-snowflake.md)。*

<a id="pseudonymisation"></a>
### 假名化（Pseudonymisation）

对个人数据进行处理，使其在没有单独保存的附加信息时无法归属到具体个人；在 GDPR 下仍属个人数据。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="puffin-file"></a>
### Puffin 文件（Puffin file）

Iceberg 用于存放辅助数据块（例如统计摘要草图和 v3 删除向量）的文件格式。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="purpose-limitation"></a>
### 目的限制（Purpose limitation）

要求个人数据仅为特定且相容的目的而收集和使用的原则。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

## Q

<a id="quality-classifier"></a>
### 质量分类器（Quality classifier）

为文档的训练价值打分的小模型，只保留高分文本。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="query-compilation"></a>
### 查询编译（Query compilation）

为每个查询生成机器码，使各算子融合为紧凑的循环（例如 HyPer、Spark 全阶段代码生成）。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="query-federation"></a>
### 联邦查询（Query federation）

通过将查询下推到外部数据库、而非复制其数据，就地查询这些外部数据库。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="query-optimizer"></a>
### 查询优化器（Query optimizer）

为查询选择执行计划的数据库组件，通常基于成本估算。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="query-based-cdc"></a>
### 基于查询的 CDC（Query-based CDC）

通过轮询表中时间戳或 ID 更新的行来实现的变更数据捕获；实现简单，但会遗漏硬删除。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="query-log-mining"></a>
### 查询日志挖掘（Query-log mining）

解析数据仓库已执行 SQL 的历史记录，以推断数据血缘、使用情况和表的重要性。*参见 [第 13 章](02-pipelines-and-governance/ch13-data-quality-observability-lineage.md)。*

<a id="quorum"></a>
### 法定人数（Quorum）

一次操作被视为生效所需确认的最少副本数，通常为多数派。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="quota-retirement"></a>
### 配额抵扣（Quota retirement）

将合作伙伴的云市场交易计入超大规模云厂商销售人员自身的销售配额，这是联合销售的主要激励机制。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

## R

<a id="raft"></a>
### Raft

一种以易于理解为设计目标的共识协议，由领导者选举、日志复制和多数派提交三部分构成。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="rapids"></a>
### RAPIDS

NVIDIA 的开源 CUDA 库套件（cuDF、cuML、cuVS 等），用于 GPU 数据科学与数据处理。*参见 [第 24 章](03-ai-data-stack/ch24-data-meets-compute-and-storage.md)。*

<a id="rapids-accelerator-for-apache-spark"></a>
### RAPIDS Accelerator for Apache Spark

NVIDIA 的一款插件，可在用户无需修改代码的情况下，将 Spark SQL 和 DataFrame 算子替换为 GPU 版本。*参见 [第 24 章](03-ai-data-stack/ch24-data-meets-compute-and-storage.md)。*

<a id="ratable-recognition"></a>
### 按期平均确认（Ratable recognition）

无论实际用量如何，都在合同期内平均分摊确认订阅收入。*参见 [第 35 章](05-business-and-economics/ch35-business-models.md)。*

<a id="rate-limit"></a>
### 速率限制（Rate limit）

源系统对单位时间窗口内 API 调用次数施加的上限。*参见 [第 10 章](02-pipelines-and-governance/ch10-ingestion-and-integration.md)。*

<a id="rdf"></a>
### RDF

资源描述框架（Resource Description Framework），一种由“主语–谓语–宾语”三元组构成、使用 SPARQL 查询的图模型。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="re-ipo"></a>
### 重新上市（Re-IPO）

曾被私有化的公司重返公开市场（例如 Informatica，2021 年）。*参见 [第 39 章](05-business-and-economics/ch39-ma-history.md)。*

<a id="read-amplification"></a>
### 读放大（Read amplification）

数据库每完成一次逻辑查找所执行的存储读取次数。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="read-after-write-consistency"></a>
### 写后读一致性（Read-after-write consistency）

保证一次成功的写入对之后的每一次读取和列举操作立即可见；S3 自 2020 年 12 月起提供这一保证。*参见 [第 24 章](03-ai-data-stack/ch24-data-meets-compute-and-storage.md)。*

<a id="reading-order"></a>
### 阅读顺序（Reading order）

人类阅读页面各文本块的先后顺序，解析器必须依据字形位置将其重建出来。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="real-time-analytics"></a>
### 实时分析（Real-time analytics）

针对仅数秒前产生的数据进行亚秒级分析查询，并以高并发方式服务于应用、用户或智能体。*参见 [第 23 章](03-ai-data-stack/ch23-real-time-analytics-htap.md)。*

<a id="rebundling"></a>
### 再捆绑（Rebundling）

通过合并、收购或平台原生功能，把原本单独销售的产品重新组合为套件或平台。*参见 [第 43 章](06-history-and-future/ch43-modern-data-stack.md)。*

<a id="recall-at-k"></a>
### k 召回率（Recall at k）

在真实的 k 个最近邻中，近似索引实际返回的比例。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="reciprocal-rank-fusion"></a>
### 倒数排名融合（Reciprocal rank fusion）

一种合并多个排序列表的方法：每个条目的得分为其在各列表中 1/(k + 名次) 之和，按惯例 k = 60（RRF）。*参见 [第 19 章](03-ai-data-stack/ch19-retrieval-architectures.md)。*

<a id="recursive-chunking"></a>
### 递归分块（Recursive chunking）

按逐级变细的分隔符（段落、句子、单词）切分文本，直到各分块满足大小上限。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="red-teaming"></a>
### 红队测试（Red-teaming）

通过人工或自动化的对抗性测试，发现模型不安全或非预期的行为。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="reference-architecture"></a>
### 参考架构（Reference architecture）

针对特定工作负载、组合特定产品并附有容量规划指导的已发布且经过测试的设计方案。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

<a id="reference-call"></a>
### 客户参考访谈（Reference call）

尽职调查中与被评估公司现有客户进行的访谈，最好是与日常实际使用者交谈。*参见 [第 46 章](07-conversation-toolkit/ch46-talking-with-data-people.md)。*

<a id="reinforcement-learning-from-ai-feedback"></a>
### 基于 AI 反馈的强化学习（Reinforcement learning from AI feedback）

一种 RLHF 变体：由模型在书面原则的指导下生成偏好标签（RLAIF）。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="reinforcement-learning-from-human-feedback"></a>
### 人类反馈强化学习（Reinforcement learning from human feedback）

以从人类偏好排序中学得的奖励为目标，用强化学习调优模型（RLHF）。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="relational-model"></a>
### 关系模型（Relational model）

由 E. F. Codd 于 1970 年提出的数据存储方式：数据以由键值相互关联的行组成的表来存储，并以声明式方式查询。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="relicensing"></a>
### 许可证变更（Relicensing）

更改项目未来版本所适用的许可证，通常是为了限制云厂商等竞争者。*参见 [第 38 章](05-business-and-economics/ch38-open-source-strategy.md)。*

<a id="remaining-performance-obligations"></a>
### 剩余履约义务（Remaining performance obligations）

公司已签约但尚未确认的收入，即其披露的未交付订单（backlog）。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="remote-signing"></a>
### 远程签名（Remote signing）

由目录代表引擎对每个对象存储请求进行签名，而不是向引擎下发凭证。*参见 [第 08 章](01-data-systems-foundations/ch08-catalogs-and-metastores.md)。*

<a id="replication"></a>
### 复制（Replication）

在多个节点上保存同一数据的副本，以保障持久性和可用性。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="replication-lag"></a>
### 复制延迟（Replication lag）

一次写入在主节点（leader）提交后到在副本上可见之间的时间差。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="replication-slot"></a>
### 复制槽（Replication slot）

Postgres 中的一种对象，使主库保留预写日志（WAL），直到消费者确认已读取。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="request-pricing"></a>
### 请求计费（Request pricing）

对 PUT、GET、LIST 等对象存储操作按次收费，这使得大量小文件的成本变得高昂。*参见 [第 24 章](03-ai-data-stack/ch24-data-meets-compute-and-storage.md)。*

<a id="reranker"></a>
### 重排序器（Reranker）

第二阶段模型（通常为交叉编码器），按相关性对检索得到的候选短列表重新排序。*参见 [第 19 章](03-ai-data-stack/ch19-retrieval-architectures.md)。*

<a id="rescoring"></a>
### 重新打分（Rescoring）

对借助压缩向量找到的候选结果，使用其全精度向量重新排序。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="result-cache"></a>
### 结果缓存（Result cache）

Snowflake 存储近期查询结果的机制；当底层数据未发生变化时，无需启动计算即可直接返回结果。*参见 [第 26 章](04-company-deep-dives/ch26-snowflake.md)。*

<a id="retrieval-augmented-generation"></a>
### 检索增强生成（Retrieval-augmented generation）

在查询时获取相关内容并将其加入语言模型的提示中（RAG）。*参见 [第 01 章](01-data-systems-foundations/ch01-data-stack-map.md)。*

<a id="revenue-run-rate"></a>
### 收入年化运行率（Revenue run-rate）

将当期收入年化（例如季度收入乘以四）；并非经审计的年度收入。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="reverse-etl"></a>
### 反向 ETL（Reverse ETL）

将数据仓库中建模好的数据同步回 CRM、广告平台等运营型 SaaS 工具。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="reward-model"></a>
### 奖励模型（Reward model）

基于人类对输出的排序训练而成、在强化学习过程中为新输出打分的模型。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="right-to-erasure"></a>
### 删除权（Right to erasure）

GDPR 规定的、在特定情形下要求删除个人数据的权利（第 17 条）。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="rl-environment"></a>
### 强化学习环境（RL environment）

对某项任务、网站或软件系统的沙箱化复制，AI 智能体在其中行动并被自动评分。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="role-explosion"></a>
### 角色爆炸（Role explosion）

当用 RBAC 表达敏感级别、地区和用途的大量组合时，所产生的大量狭窄范围角色泛滥的现象。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="role-based-access-control"></a>
### 基于角色的访问控制（Role-based access control）

一种权限模型：权限授予角色，用户通过被分配角色获得访问权。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="rollover"></a>
### 余额结转（Rollover）

一种合同条款：将未用完的预付容量结转到后续订单中，通常以客户追加采购为条件。*参见 [第 35 章](05-business-and-economics/ch35-business-models.md)。*

<a id="row-group"></a>
### 行组（Row group）

Parquet 文件中按行横向切分的一段；谓词下推可以将其作为整体跳过的单位。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

<a id="row-lineage"></a>
### 行级血缘（Row lineage）

Iceberg v3 为每一行跟踪一个稳定的行 ID 及最近更新序列号的功能。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="row-store"></a>
### 行存储（Row store）

将一行的所有列共同存放在同一页上的布局，适合事务型读写。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="row-level-security"></a>
### 行级安全（Row-level security）

一种策略，静默地过滤给定用户能看到表中的哪些行。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="rpu"></a>
### RPU

Redshift 处理单元（Redshift Processing Unit），Amazon Redshift Serverless 按小时计费的计算单位。*参见 [第 35 章](05-business-and-economics/ch35-business-models.md)。*

<a id="rule-of-40"></a>
### 40 法则（Rule of 40）

一种经验法则：软件公司的收入增长率加上利润率（通常为 FCF 利润率）应至少达到 40%。*参见 [第 36 章](05-business-and-economics/ch36-unit-economics-kpis.md)。*

<a id="rum-conjecture"></a>
### RUM 猜想（RUM conjecture）

2016 年提出的论断：任何访问方法都无法同时将读取（Read）、更新（Update）和内存（Memory）开销降至最低。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="run-length-encoding"></a>
### 游程编码（Run-length encoding）

一种压缩方式：对连续重复的值只存储一次，并附上其连续重复的次数。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

## S

<a id="s3-express-one-zone"></a>
### S3 Express One Zone

AWS 的单可用区、低延迟 S3 存储类别，使用目录存储桶（directory bucket），常被用作表数据和训练数据的热存储层。*参见 [第 24 章](03-ai-data-stack/ch24-data-meets-compute-and-storage.md)。*

<a id="s3-tables"></a>
### S3 Tables

AWS 托管的 Apache Iceberg 表，存放在 S3 的“表存储桶”（table bucket）中，提供自动压缩合并和快照清理。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="s3-vectors"></a>
### S3 Vectors

AWS 内置于 S3 的向量存储与相似度检索能力，于 re:Invent 2025 正式发布（GA）。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="s3-compatible-storage"></a>
### S3 兼容存储（S3-compatible storage）

非 AWS 的对象存储，其对 Amazon S3 API 的实现足够完整，使各类引擎和工具可以直接使用。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

<a id="safetensors"></a>
### Safetensors

一种张量文件格式（JSON 头部加原始缓冲区），可进行内存映射，并且与 pickle 检查点不同，加载时不会执行代码。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

<a id="scalar-quantization"></a>
### 标量量化（Scalar quantization）

用更少的比特存储向量的每个坐标，例如用 int8 代替 float32，使体积缩小至 1/4。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="scale-to-zero"></a>
### 缩容至零（Scale-to-zero）

在数据库或服务空闲时释放全部计算资源，使其在下一次请求到来之前只产生存储费用。*参见 [第 22 章](03-ai-data-stack/ch22-agents-and-data.md)。*

<a id="scann"></a>
### ScaNN

Google 采用各向异性量化的向量检索方法，用于 AlloyDB 和 Vertex AI Vector Search。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="schema-drift"></a>
### 模式漂移（Schema drift）

数据源的列或数据类型发生计划外变化，数据管道必须检测并加以处理。*参见 [第 10 章](02-pipelines-and-governance/ch10-ingestion-and-integration.md)。*

<a id="schema-evolution"></a>
### 模式演进（Schema evolution）

在表的生命周期内安全地新增、删除、重命名、重排或拓宽列，而无需重写数据。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="schema-linking"></a>
### 模式链接（Schema linking）

在 LLM 生成 SQL 之前，从大型模式中挑选出相关的表、列和连接关系。*参见 [第 22 章](03-ai-data-stack/ch22-agents-and-data.md)。*

<a id="schema-registry"></a>
### 模式注册表（Schema Registry）

一种服务（例如 Confluent 的产品），为流处理主题存储带版本的模式，并拒绝会破坏消费者的变更。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

<a id="schema-on-read"></a>
### 读时模式（Schema-on-read）

一种在读取数据时才解释其结构、而不是在写入时强制约束结构的方式。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="seat-based-pricing"></a>
### 按席位计费（Seat-based pricing）

按具名用户收费；当 AI 智能体取代人类用户时，这种模式会让软件厂商面临风险。*参见 [第 34 章](04-company-deep-dives/ch34-application-giants-data-platforms.md)。*

<a id="secondary-index"></a>
### 二级索引（Secondary index）

建立在主键以外的列上、并指回表中各行的索引。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="secondary-sale"></a>
### 老股转让（Secondary sale）

现有股东向新投资者出售股份；公司本身不获得新资金。*参见 [第 32 章](04-company-deep-dives/ch32-ai-native-data-companies.md)。*

<a id="section-aware-chunking"></a>
### 按章节分块（Section-aware chunking）

沿着版面解析器识别出的标题、页面和表格进行切分。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="segment"></a>
### 段（Segment）

在 Apache Druid 和 Pinot 中，指一个不可变、按时间分区、带索引的列式数据文件。*参见 [第 23 章](03-ai-data-stack/ch23-real-time-analytics-htap.md)。*

<a id="self-correction-loop"></a>
### 自我纠错循环（Self-correction loop）

执行或试运行生成的 SQL，并将错误和合理性检查失败的信息反馈给模型以修复查询。*参见 [第 22 章](03-ai-data-stack/ch22-agents-and-data.md)。*

<a id="semantic-cache"></a>
### 语义缓存（Semantic cache）

一种缓存：当新提示与先前某个提示在语义上相近（通过嵌入相似度匹配）时，直接返回已存储的 LLM 回答。*参见 [第 29 章](04-company-deep-dives/ch29-operational-database-vendors.md)。*

<a id="semantic-chunking"></a>
### 语义分块（Semantic chunking）

在相邻句子之间嵌入相似度下降处设置分块边界。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="semantic-deduplication"></a>
### 语义去重（Semantic deduplication）

通过对嵌入进行聚类，删除含义几乎相同（即使措辞不同）的文档。*参见 [第 20 章](03-ai-data-stack/ch20-training-data-supply-chain.md)。*

<a id="semantic-layer"></a>
### 语义层（Semantic layer）

一套共享的指标与实体业务定义，供 BI 工具和 AI 智能体一致地使用。*参见 [第 01 章](01-data-systems-foundations/ch01-data-stack-map.md)。*

<a id="semantic-view"></a>
### 语义视图（Semantic view）

Snowflake 中位于模式（schema）层级的数据库对象，用于存储语义模型（指标、维度、关系）。*参见 [第 14 章](02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)。*

<a id="sensor"></a>
### 传感器（Sensor）

编排器中的一种任务，在下游工作启动前等待某个外部条件（文件到达、分区就绪、事件发生）满足。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

<a id="separation-of-storage-and-compute"></a>
### 存算分离（Separation of storage and compute）

将持久化数据保存在共享存储（通常为对象存储）中，而无状态的计算集群独立扩缩容。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="serverless-compute"></a>
### 无服务器计算（Serverless compute）

由厂商托管、几乎即时可用的计算资源，以包含底层云主机成本在内的一体化单价计费。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="serviceable-addressable-market"></a>
### 可服务市场（Serviceable addressable market）

TAM 中产品凭借现有产品方案、渠道和地域覆盖实际能够触达的部分（SAM）。*参见 [第 41 章](05-business-and-economics/ch41-market-sizing.md)。*

<a id="shadow-data"></a>
### 影子数据（Shadow data）

位于受治理、已编目系统之外的数据副本，例如导出文件、快照和临时存储桶。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="sharding"></a>
### 分片（Sharding）

将数据集拆分为存放在不同节点上的分区，使容量可以横向扩展。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="share-group"></a>
### 共享组（Share group）

Kafka 4.x 的队列式消费机制（KIP-932），多个消费者可以处理同一分区中的记录，并逐条确认。*参见 [第 11 章](02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。*

<a id="shared-nothing"></a>
### 无共享架构（Shared-nothing）

一种架构：每个节点拥有各自的 CPU、内存和磁盘，并持有数据的一个分区。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="sharedmergetree"></a>
### SharedMergeTree

ClickHouse Cloud 的 MergeTree 变体，将全部表数据保存在共享对象存储上，副本无状态。*参见 [第 23 章](03-ai-data-stack/ch23-real-time-analytics-htap.md)。*

<a id="shuffle"></a>
### 洗牌（Shuffle）

按键在节点之间重新分发行，使相关的行汇聚到一起以完成连接或聚合。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="signpost"></a>
### 路标信号（Signpost）

可观察、有明确日期的事件，它会强化或削弱某项预测，并提示你何时应更新该预测。*参见 [第 44 章](06-history-and-future/ch44-future-trends.md)。*

<a id="simd"></a>
### SIMD

单指令多数据（single instruction, multiple data）：一条 CPU 指令同时作用于宽寄存器中保存的多个值。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="singer"></a>
### Singer

一种开放规范，定义交换 JSON 记录的“tap”（数据源）和“target”（目标端）；Meltano 即以此为基础。*参见 [第 10 章](02-pipelines-and-governance/ch10-ingestion-and-integration.md)。*

<a id="slot"></a>
### 槽位（Slot）

BigQuery 的查询计算容量单位，可按预留（reservation）计费，或按需消耗。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="small-data"></a>
### 小数据（Small data）

一种论点：大多数分析查询所涉及的数据量小到足以在单台机器上处理。*参见 [第 23 章](03-ai-data-stack/ch23-real-time-analytics-htap.md)。*

<a id="small-files-problem"></a>
### 小文件问题（Small-files problem）

表中积累大量过小数据文件（通常源于频繁的流式提交）所导致的性能下降和额外开销。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="snapshot-expiration"></a>
### 快照过期（Snapshot expiration）

删除早于保留窗口的表快照，使仅被这些快照引用的文件可以被物理删除。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="snapshot-isolation"></a>
### 快照隔离（Snapshot isolation）

一种保证：每个读取者都看到数据的某个一致的已提交版本，不受正在进行的写入影响。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="snowflake-cowork"></a>
### Snowflake CoWork

Snowflake 面向业务用户的 AI 助手，在 Summit 2026 上由 Snowflake Intelligence 更名而来。*参见 [第 27 章](04-company-deep-dives/ch27-databricks-vs-snowflake.md)。*

<a id="snowflake-credit"></a>
### Snowflake 积分（Snowflake credit）

Snowflake 的计算消耗单位，按虚拟仓库规格每小时消耗，其美元单价因版本（edition）和区域而异。*参见 [第 27 章](04-company-deep-dives/ch27-databricks-vs-snowflake.md)。*

<a id="snowflake-postgres"></a>
### Snowflake Postgres

Snowflake 的托管 PostgreSQL 服务，基于 2025 年对 Crunchy Data 的收购构建，自 2026 年 6 月起正式可用（GA）。*参见 [第 27 章](04-company-deep-dives/ch27-databricks-vs-snowflake.md)。*

<a id="snowpark"></a>
### Snowpark

Snowflake 用于在平台内部运行 Python、Java 和 Scala 代码的运行时与 API。*参见 [第 26 章](04-company-deep-dives/ch26-snowflake.md)。*

<a id="software-fork"></a>
### 软件分叉（Software fork）

从另一个项目的代码副本（通常是其最后一个宽松许可版本）出发启动的独立项目。*参见 [第 38 章](05-business-and-economics/ch38-open-source-strategy.md)。*

<a id="software-mix"></a>
### 软件收入占比（Software mix）

公司收入中来自软件和订阅、而非硬件的比例。*参见 [第 45 章](06-history-and-future/ch45-storage-moving-up-the-stack.md)。*

<a id="software-defined-asset"></a>
### 软件定义资产（Software-defined asset）

Dagster 的核心抽象：在代码中声明的数据资产，连同其上游依赖关系及计算方式。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

<a id="source-available-license"></a>
### 源码可用许可证（Source-available license）

公开源代码但限制其使用的许可证，通常禁止提供具有竞争性的托管服务；按 OSI 的定义不属于开源。*参见 [第 29 章](04-company-deep-dives/ch29-operational-database-vendors.md)。*

<a id="sovereign-cloud"></a>
### 主权云（Sovereign cloud）

在当地司法管辖下运营、通常由当地常驻员工运维的云区域，用以满足数据主权规则。*参见 [第 24 章](03-ai-data-stack/ch24-data-meets-compute-and-storage.md)。*

<a id="space-amplification"></a>
### 空间放大（Space amplification）

磁盘上存储的字节数与有效（存活）数据字节数之比。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="spaced-repetition"></a>
### 间隔重复（Spaced repetition）

以逐渐拉长的间隔复习材料，并集中攻克答错的条目；第 50 章的闪卡正是为这种学习方法设计的。*参见 [第 50 章](07-conversation-toolkit/ch50-self-test-cheat-sheets.md)。*

<a id="spann"></a>
### SPANN

Microsoft 基于聚类的十亿级向量索引，质心保存在内存中，倒排列表（posting list）保存在磁盘上。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="sparse-primary-index"></a>
### 稀疏主索引（Sparse primary index）

每个行块（而非每一行）只保存一个条目的索引，体积小到足以常驻内存。*参见 [第 23 章](03-ai-data-stack/ch23-real-time-analytics-htap.md)。*

<a id="spfresh"></a>
### SPFresh

SPANN 的一种易于更新的扩展，可就地重新平衡聚类；turbopuffer 的索引即以此为基础。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="spider-2-0"></a>
<a id="spider-20"></a>
### Spider 2.0

2024–2025 年的文本转 SQL 基准测试，包含基于大型云端模式的 632 个真实企业工作流任务，2025 年表现最好的系统约能解决 21%。*参见 [第 22 章](03-ai-data-stack/ch22-agents-and-data.md)。*

<a id="sql"></a>
### SQL

结构化查询语言（Structured Query Language），源自 IBM 的 System R 的声明式查询语言，1986 年由 ANSI 首次标准化。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="sspl"></a>
### SSPL

MongoDB 的服务器端公共许可证（Server Side Public License，2018 年），要求任何以服务形式提供该软件的一方公开其整个服务栈的源代码。*参见 [第 29 章](04-company-deep-dives/ch29-operational-database-vendors.md)。*

<a id="sstable"></a>
### SSTable

有序字符串表（sorted string table）：由 LSM 树刷写（flush）或压缩合并（compaction）产生的、不可变且有序的磁盘文件。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="standard-essential-patent"></a>
### 标准必要专利（Standard-essential patent）

实施某项行业标准（例如蜂窝通信协议）时必须获得许可的专利。*参见 [第 39 章](05-business-and-economics/ch39-ma-history.md)。*

<a id="star-schema"></a>
### 星型模式（Star schema）

一种数据仓库设计：中心是存放度量值的事实表，四周环绕日期、产品、门店等维度表。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="star-tree-index"></a>
### Star-tree 索引（Star-tree index）

Apache Pinot 的一种索引，针对选定的维度组合预先聚合指标，以获得可预期的低延迟。*参见 [第 23 章](03-ai-data-stack/ch23-real-time-analytics-htap.md)。*

<a id="state-store"></a>
### 状态存储（State store）

数据管道记录其处理进度（游标值、日志偏移量）之处，使其能够在不留空缺、不产生重复的情况下恢复运行。*参见 [第 10 章](02-pipelines-and-governance/ch10-ingestion-and-integration.md)。*

<a id="static-data-masking"></a>
### 静态数据脱敏（Static data masking）

在数据副本中永久替换敏感值，通常用于测试或提供给供应商使用。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="stock-based-compensation"></a>
### 股权激励费用（Stock-based compensation）

以股权形式支付的员工薪酬，在 GAAP 下计入费用，但被大多数公司排除在其非 GAAP 利润指标之外。*参见 [第 26 章](04-company-deep-dives/ch26-snowflake.md)。*

<a id="stream-processing"></a>
### 流处理（Stream processing）

对无界事件流进行的过滤、连接和聚合等持续计算。*参见 [第 11 章](02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。*

<a id="streaming-database"></a>
### 流式数据库（Streaming database）

一种根据流入的数据流持续更新 SQL 物化视图的数据库（例如 RisingWave、Materialize）。*参见 [第 11 章](02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。*

<a id="subscription-arr"></a>
### 订阅 ARR（Subscription ARR）

Everpure 的关键绩效指标：有效的不可取消订阅的年化价值，加上最近一个季度按需（on-demand）账单金额乘以四。*参见 [第 35 章](05-business-and-economics/ch35-business-models.md)。*

<a id="supervised-fine-tuning"></a>
### 监督微调（Supervised fine-tuning）

用示例提示与理想回答配对的数据训练模型（SFT）。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="support-annuity"></a>
### 支持服务年金（Support annuity）

基于永久许可装机基础获得的经常性维护收入，例如 Oracle 的数据库支持服务收入。*参见 [第 29 章](04-company-deep-dives/ch29-operational-database-vendors.md)。*

<a id="syndicated-research"></a>
### 联合发布研究（Syndicated research）

研究机构向众多买家出售的市场报告，方法往往不透明，且不同机构之间分歧很大。*参见 [第 41 章](05-business-and-economics/ch41-market-sizing.md)。*

<a id="synthetic-data"></a>
### 合成数据（Synthetic data）

由模型生成、而非从人类或网络收集的训练数据。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="system-of-intelligence"></a>
### 智能系统（System of intelligence）

整合多个记录系统中的数据、使分析工具和 AI 智能体能够据此决策并行动的层。*参见 [第 34 章](04-company-deep-dives/ch34-application-giants-data-platforms.md)。*

<a id="system-of-record"></a>
### 记录系统（System of record）

其数据是某项业务事实权威版本的应用，例如客户数据以 CRM 为准、发票数据以 ERP 为准。*参见 [第 34 章](04-company-deep-dives/ch34-application-giants-data-platforms.md)。*

<a id="systems-integrator"></a>
### 系统集成商（Systems integrator）

设计并实施技术项目、并常常左右客户平台选型的咨询公司（SI）。*参见 [第 40 章](05-business-and-economics/ch40-gtm-partnerships.md)。*

## T

<a id="table-metadata-file"></a>
### 表元数据文件（Table metadata file）

Iceberg 的 JSON 根文件，保存表的模式、分区规范、属性和快照列表；目录指向当前的那一个元数据文件。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="tableflow"></a>
### Tableflow

Confluent 的一项功能，可将 Kafka 主题物化为对象存储中的 Apache Iceberg（或 Delta Lake）表，从而省去单独的 ETL 作业。*参见 [第 30 章](04-company-deep-dives/ch30-data-movement-streaming-companies.md)。*

<a id="tag-based-policy"></a>
### 基于标签的策略（Tag-based policy）

附加在标签上的访问或脱敏策略，会自动应用于每一个带有该标签的对象。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="tail-latency"></a>
### 尾部延迟（Tail latency）

最慢那部分请求的延迟（例如第 99 百分位，p99），它决定了系统给人的响应感受。*参见 [第 23 章](03-ai-data-stack/ch23-real-time-analytics-htap.md)。*

<a id="take-rate"></a>
### 抽成率（Take rate）

平台或人力外包型厂商在向承包方付款后，从总账单金额中留存的比例。*参见 [第 20 章](03-ai-data-stack/ch20-training-data-supply-chain.md)。*

<a id="take-or-pay"></a>
### 照付不议（Take-or-pay）

一种供应合同：无论买方是否实际提货，都须为承诺的数量付款。*参见 [第 28 章](04-company-deep-dives/ch28-hyperscaler-data-platforms.md)。*

<a id="take-private"></a>
### 私有化（Take-private）

通常由私募股权发起的收购，使上市公司退市，以便在摆脱季度业绩压力的环境下进行重组。*参见 [第 30 章](04-company-deep-dives/ch30-data-movement-streaming-companies.md)。*

<a id="technical-catalog"></a>
### 技术目录（Technical catalog）

位于访问路径上的服务，为每个引擎将表名解析为其当前元数据、仲裁原子提交并执行访问策略。*参见 [第 08 章](01-data-systems-foundations/ch08-catalogs-and-metastores.md)。*

<a id="tender-offer"></a>
### 要约收购（Tender offer）

向员工及其他持有人收购其现有股份的要约，私营公司常借此提供流动性。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="term-license"></a>
### 定期许可（Term license）

有期限的软件许可（例如 MongoDB Enterprise Advanced），其许可部分在 ASC 606 下于期初一次性确认为收入。*参见 [第 29 章](04-company-deep-dives/ch29-operational-database-vendors.md)。*

<a id="text-to-sql"></a>
### 文本转 SQL（Text-to-SQL）

由 LLM 将自然语言问题直接翻译为 SQL 查询。*参见 [第 14 章](02-pipelines-and-governance/ch14-semantic-layers-and-bi.md)。*

<a id="tfrecord"></a>
### TFRecord

TensorFlow 用于存放训练样本的顺序记录流文件格式。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

<a id="tiered-storage"></a>
### 分层存储（Tiered storage）

将较旧的日志段从 broker 磁盘卸载到对象存储，同时将近期数据保留在本地（Kafka KIP-405）。*参见 [第 11 章](02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。*

<a id="time-travel"></a>
### 时间旅行（Time travel）

按表在某个较早快照、版本或时间戳时的状态对其进行查询（历史版本查询）。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="time-series-database"></a>
### 时序数据库（Time-series database）

针对带时间戳、以追加为主的测量数据和窗口聚合进行优化的数据库。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="timestamp-oracle"></a>
### 时间戳预言机（Timestamp oracle）

签发严格递增事务时间戳的中心服务，例如 Percolator 以及 TiDB 的 Placement Driver。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="token"></a>
### 词元（Token）

语言模型读取和预测的子词单位；英文文本平均约每四个字符为一个词元。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="tokenization"></a>
### 令牌化（Tokenization）

用代理令牌替换敏感值，只有具备特权的服务或密钥才能将其映射回原值。*参见 [第 15 章](02-pipelines-and-governance/ch15-governance-security-privacy.md)。*

<a id="tombstone"></a>
### 墓碑标记（Tombstone）

在 LSM 树中写入的一种标记，用于记录删除操作，直到压缩合并将该键移除。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="topic"></a>
### 主题（Topic）

Kafka 中具名的数据流，由一个或多个分区组成。*参见 [第 11 章](02-pipelines-and-governance/ch11-streaming-and-event-platforms.md)。*

<a id="total-addressable-market"></a>
### 总可服务市场（Total addressable market）

假如产品赢得其所定义类别中所有可能客户时可获得的收入（TAM）；公司披露的 TAM 未经审计。*参见 [第 41 章](05-business-and-economics/ch41-market-sizing.md)。*

<a id="trace"></a>
### 运行轨迹（Trace）

一次 AI 或智能体运行的记录：提示、检索到的上下文、工具调用、输出及结果。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="training-serving-skew"></a>
### 训练–服务偏差（Training-serving skew）

模型在训练时看到的特征值与其在生产环境中接收到的特征值之间的不一致。*参见 [第 21 章](03-ai-data-stack/ch21-ml-platforms-feature-stores-llmops.md)。*

<a id="trigger-based-cdc"></a>
### 基于触发器的 CDC（Trigger-based CDC）

利用数据库触发器将每次变更复制到影子表中的变更数据捕获方式，代价是每次写入都会增加开销。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="truetime"></a>
### TrueTime

Google 以 GPS 和原子钟为支撑的时钟 API，返回一个有界的“当前时间可能取值”区间。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="tuck-in-acquisition"></a>
### 补强型收购（Tuck-in acquisition）

并入现有产品线的小型收购，通常不披露价格。*参见 [第 39 章](05-business-and-economics/ch39-ma-history.md)。*

<a id="two-phase-commit"></a>
### 两阶段提交（Two-phase commit）

一种原子提交协议：协调者先收集各参与者的准备（prepare）投票，再发出提交指令；若协调者在协议中途故障，则会发生阻塞。*参见 [第 04 章](01-data-systems-foundations/ch04-distributed-databases.md)。*

<a id="two-phase-locking"></a>
### 两阶段锁（Two-phase locking）

一种悲观并发控制协议：按需获取锁，并且只在提交之后才释放。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

## U

<a id="unbundling"></a>
### 拆分解绑（Unbundling）

将一体化套件的各项功能拆分为单独销售的“同类最佳”产品。*参见 [第 43 章](06-history-and-future/ch43-modern-data-stack.md)。*

<a id="undo-log"></a>
### 回滚日志（Undo log）

保存被修改行的修改前映像的存储，用于回滚以及读取较旧的快照（Oracle、InnoDB）。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="uniform"></a>
### UniForm

Delta Lake 的通用格式（Universal Format）功能，会在 Delta 日志旁同时写入 Iceberg（及 Hudi）元数据，使其他引擎能够读取同一份数据。*参见 [第 07 章](01-data-systems-foundations/ch07-open-table-formats.md)。*

<a id="unit-test"></a>
### 单元测试（Unit test）

针对模拟输入行对数据转换逻辑进行的测试，在开发或 CI 环境中运行，而不是在生产数据上运行。*参见 [第 13 章](02-pipelines-and-governance/ch13-data-quality-observability-lineage.md)。*

<a id="unity-catalog"></a>
### Unity Catalog

Databricks 面向表、文件、模型和函数的治理目录，负责权限、数据血缘、审计以及凭证下发（credential vending）。*参见 [第 25 章](04-company-deep-dives/ch25-databricks.md)。*

<a id="unstructured-data"></a>
### 非结构化数据（Unstructured data）

没有预定义模式的内容，例如文档、电子邮件、图像、音频和视频。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="upsert"></a>
### 插入或更新（Upsert）

一种操作：插入一行；若已存在相同键的行，则更新该行。*参见 [第 23 章](03-ai-data-stack/ch23-real-time-analytics-htap.md)。*

<a id="user-facing-analytics"></a>
### 面向用户的分析（User-facing analytics）

嵌入在产品中、由其终端用户或客户（而非内部分析师）发起查询的分析功能。*参见 [第 23 章](03-ai-data-stack/ch23-real-time-analytics-htap.md)。*

## V

<a id="vacuum"></a>
### Vacuum

PostgreSQL 的后台进程，用于回收失效行版本所占用的空间。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="valkey"></a>
### Valkey

Linux 基金会于 2024 年 3 月创建的、基于 BSD 许可证的 Redis 7.2.4 分叉。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="value-migration"></a>
### 价值迁移（Value migration）

利润池从价值链的一层转移到另一层，例如从存储字节转向目录和语义上下文。*参见 [第 44 章](06-history-and-future/ch44-future-trends.md)。*

<a id="vamana"></a>
### Vamana

DiskANN 背后的单层图构建算法，会保留部分长边以缩短检索路径。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="vector-database"></a>
### 向量数据库（Vector database）

主要为存储、索引和查询嵌入（并支持元数据过滤）而构建的数据库。*参见 [第 18 章](03-ai-data-stack/ch18-embeddings-and-vector-search.md)。*

<a id="vector-index"></a>
### 向量索引（Vector index）

用于对嵌入进行快速近似最近邻检索的数据结构。*参见 [第 01 章](01-data-systems-foundations/ch01-data-stack-map.md)。*

<a id="vectorized-execution"></a>
### 向量化执行（Vectorized execution）

在算子之间传递与缓存大小相当的批量数值、而非逐行处理的查询处理方式。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="vendor-lock-in"></a>
### 厂商锁定（Vendor lock-in）

客户在摆脱某厂商的数据格式、目录或合同时所面临的成本与困难。*参见 [第 47 章](07-conversation-toolkit/ch47-diligence-checklist.md)。*

<a id="vendor-revenue-basis"></a>
### 厂商收入口径（Vendor revenue basis）

一种市场规模测算口径：加总各厂商在某类别中确认的收入，如 Gartner 的市场份额报告。*参见 [第 41 章](05-business-and-economics/ch41-market-sizing.md)。*

<a id="verifiable-reward"></a>
### 可验证奖励（Verifiable reward）

通过自动检查计算得出的强化学习奖励，例如单元测试通过或数学答案匹配。*参见 [第 16 章](03-ai-data-stack/ch16-ai-data-lifecycle.md)。*

<a id="virtual-data-environment"></a>
### 虚拟数据环境（Virtual data environment）

SQLMesh 在带版本的物理表之上构建的视图层，使开发和 CI 环境能够复用未发生变化的生产数据。*参见 [第 12 章](02-pipelines-and-governance/ch12-transformation-and-orchestration.md)。*

<a id="virtual-warehouse"></a>
### 虚拟仓库（Virtual warehouse）

Snowflake 中可独立调整规格、读取共享表数据的无状态计算集群。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="vision-language-model"></a>
### 视觉语言模型（Vision-language model）

以图像和文本为输入的模型，可用于将渲染后的页面图像直接解析为 Markdown 或 JSON（VLM）。*参见 [第 17 章](03-ai-data-stack/ch17-unstructured-data-processing.md)。*

<a id="vitess"></a>
### Vitess

在 YouTube 构建的开源 MySQL 分片系统，2019 年从 CNCF 毕业，由 PlanetScale 进行商业化。*参见 [第 29 章](04-company-deep-dives/ch29-operational-database-vendors.md)。*

<a id="volcano-iterator-model"></a>
### Volcano 迭代器模型（Volcano iterator model）

经典的逐元组执行设计，每个算子通过 next() 从其子算子拉取一行。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="volcano-model"></a>
### Volcano 模型（Volcano model）

逐行执行查询的方式，每个算子通过调用 next() 从其子算子拉取行。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="vortex"></a>
### Vortex

由 SpiralDB 创建、自 2025 年起由 LF AI & Data 基金会托管的压缩列式文件、内存及 IPC 格式。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

## W

<a id="watermark"></a>
### 水位线（Watermark）

流处理器对“截至某一事件时间的事件均已到达”的动态估计，用于决定何时输出窗口计算结果。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="webdataset"></a>
### WebDataset

一种训练数据格式，将样本打包成 tar 分片，从而在分片被打乱顺序的同时保持顺序读取。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

<a id="wedge"></a>
### 切入点（Wedge）

初创公司做得比任何人都好的第一项细分且痛点突出的工作，用于赢得首批客户，再向外扩张。*参见 [第 46 章](07-conversation-toolkit/ch46-talking-with-data-people.md)。*

<a id="what-goes-around-comes-around"></a>
### What Goes Around Comes Around

Stonebraker 与 Hellerstein 2005 年的论文（Stonebraker 与 Pavlo 于 2024 年发表续篇），论证关系模型一再吸收各类挑战者数据模型。*参见 [第 42 章](06-history-and-future/ch42-history-of-databases.md)。*

<a id="wide-column-store"></a>
### 宽列存储（Wide-column store）

一种由稀疏行组成、按分区键分组并按聚簇键排序的数据库，源自 Google Bigtable。*参见 [第 02 章](01-data-systems-foundations/ch02-data-models.md)。*

<a id="workflow-data-fabric"></a>
### Workflow Data Fabric

ServiceNow 的数据层，为其智能体整合了 RaptorDB、零拷贝连接器和一个目录。*参见 [第 34 章](04-company-deep-dives/ch34-application-giants-data-platforms.md)。*

<a id="workload"></a>
### 工作负载（Workload）

软件读写数据的模式（操作的规模、频率、延迟和并发度）。*参见 [第 01 章](01-data-systems-foundations/ch01-data-stack-map.md)。*

<a id="write-amplification"></a>
### 写放大（Write amplification）

物理写入存储的字节数与应用逻辑写入字节数之比。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="write-skew"></a>
### 写偏斜（Write skew）

一种异常：两个事务读取重叠的数据、各自写入不同的行，合起来违反了一条单独任何一个事务都不会违反的规则。*参见 [第 03 章](01-data-systems-foundations/ch03-database-internals.md)。*

<a id="write-ahead-log"></a>
### 预写日志（Write-ahead log）

在数据库确认事务之前先持久化的顺序变更日志；用于崩溃恢复、复制和 CDC。*参见 [第 01 章](01-data-systems-foundations/ch01-data-stack-map.md)。*

<a id="write-back"></a>
### 回写（Write-back）

智能体或工具在源应用中修改数据，并须遵守该应用的业务规则和审批流程。*参见 [第 34 章](04-company-deep-dives/ch34-application-giants-data-platforms.md)。*

## Z

<a id="zero-copy"></a>
### 零拷贝（Zero-copy）

通过共享同一块内存缓冲区、而非复制或转换数据，在组件之间传递数据。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*

<a id="zero-copy-cloning"></a>
### 零拷贝克隆（Zero-copy cloning）

通过复制指向不可变文件的元数据指针、而非复制数据本身，来创建表或数据库的副本。*参见 [第 26 章](04-company-deep-dives/ch26-snowflake.md)。*

<a id="zero-copy-data-sharing"></a>
### 零拷贝数据共享（Zero-copy data sharing）

授予另一个账户或组织就地查询数据的权限，而无需复制数据。*参见 [第 09 章](02-pipelines-and-governance/ch09-pipeline-patterns.md)。*

<a id="zero-etl"></a>
### 零 ETL（Zero-ETL）

由厂商托管的、从运营型数据库到分析系统的复制，对用户隐藏了数据管道。*参见 [第 01 章](01-data-systems-foundations/ch01-data-stack-map.md)。*

<a id="zone-map"></a>
### 区域映射（Zone map）

引擎检查的按数据块统计的最小/最大值信息，用以跳过不可能匹配过滤条件的数据。*参见 [第 05 章](01-data-systems-foundations/ch05-analytical-engines.md)。*

<a id="zstandard"></a>
### Zstandard

一种通用压缩编解码器（zstd），在解压速度与 Snappy 相近的情况下提供更高的压缩率。*参见 [第 06 章](01-data-systems-foundations/ch06-file-formats.md)。*
