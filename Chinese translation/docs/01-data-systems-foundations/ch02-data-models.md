# 2. 数据模型
> **深度：** L2 · **阅读时间：** 约 14 分钟 · **最后核实：** 2026-11-01 · **前置阅读：** [第 1 章 — 数据技术栈全景图](ch01-data-stack-map.md)

## 要点速览（TL;DR）

- **数据模型（data model）**是数据库保存数据的形态：表、文档、键值对、宽行、图、带时间戳的数据点、倒排索引或向量。这种形态决定了哪些问题问起来便宜、哪些问起来昂贵。没有哪种模型对所有问题都便宜。
- [关系模型](../glossary.md#relational-model)（Codd，1970）至今仍是默认选择。PostgreSQL 在 2024 年和 2025 年的 Stack Overflow 开发者调查中均位列使用率第一，DB-Engines 2026 年 7 月的流行度排名前四位也都是关系型引擎。[^codd][^so24][^so25][^dbe-jul]
- NoSQL 模型（文档、键值、宽列、图）各自放弃了关系模型的部分通用性，以换取规模、灵活性或遍历速度。搜索模型和向量模型做的是 SQL 从未为之设计的事情：它们按相关性或相似度对结果排序，而不是返回精确匹配。
- 行业正在向**多模型（multi-model）**引擎收敛。Postgres 在一个引擎中运行 JSONB 文档、pgvector 嵌入和 PostGIS 几何数据；MongoDB 在 Atlas 中提供向量检索，并自 2026 年 6 月起在其自管理的 Community Edition 中也提供该功能。[^pgvector][^mdb-vs] 流行的概括是"SQL 赢了"，但更准确的说法是 SQL 吸收了其他模型。
- **Everpure 视角：**数据模型决定 I/O 模式。键值和图工作负载发出小块随机读，分析发出大块顺序扫描，向量检索介于两者之间。AI 还提高了非结构化数据和向量的价值，这正是 Everpure 2026 年推出的 Data Intelligence 和 Data Stream 所瞄准的方向。[^ep-ds]

## 为何重要（商业视角 + Everpure 视角）

本书涉及的每一家数据库厂商，在销售产品之前首先销售的是一种数据模型。MongoDB 卖的是文档，Neo4j 卖的是图，Elastic 卖的是倒排索引，Pinecone 卖的是向量，Oracle 卖的是关系。当一个战略团队问某个品类能否独立生存时，它实际上是在问：这种模型是否足够与众不同，以至于通用引擎无法简单地把它作为一项功能加进来。第 29 章会逐个厂商地讨论这个问题（[第 29 章](../04-company-deep-dives/ch29-operational-database-vendors.md)）。

AI 改变了每种模型的价值。在大语言模型出现之前，钱都在结构化的行里：订单、账簿、库存。合同、工单、通话记录、图像等非结构化内容以低成本存储，却很少被查询。[嵌入（向量）](../glossary.md#embedding)把这些内容转换为可按语义检索的向量，非结构化数据因此第一次变得可查询。图模型的价值也在上升，因为 GraphRAG 之类的检索系统利用实体关系为模型提供更好的上下文（[第 19 章](../03-ai-data-stack/ch19-retrieval-architectures.md)）。

对 Everpure 而言，这种联系是具体的。Everpure 于 2026 年 5 月 7 日完成对 1touch 的收购，并把这项技术重新推出为 **Data Intelligence**，用于发现和分类结构化与非结构化数据。2026 年 6 月 17 日，它宣布推出 **Data Stream**，在 FlashBlade 上借助 NVIDIA GPU 为 AI 数据管道对选定数据进行向量化。[^ep-1touch][^ep-ds] 这两款产品都位于数据模型与存储交汇之处。一个战略团队应当了解客户的数据最终会落入哪种模型，以及该模型会产生什么样的 I/O。

## 工作原理

### 全景图

```mermaid
mindmap
  root((数据模型))
    关系型
      PostgreSQL
      Oracle
    文档
      MongoDB
      Couchbase
    键值
      Redis 与 Valkey
      DynamoDB
    宽列
      Cassandra
      Bigtable
    图
      Neo4j
      Amazon Neptune
    时间序列
      InfluxDB
      TimescaleDB
    搜索
      Elasticsearch
      OpenSearch
    向量
      Milvus
      pgvector
```

*图 2.1 — 八种数据模型，每种各列两个代表性产品。如今大多数旗舰产品都支持不止一种模型，因此这里列出的是每个产品的主要模型。*

### 关系型：表、键、连接

Edgar Codd 在 1970 年的论文中提出，把数据存储为**关系（relation）**，即由行组成的表。行与行之间通过值而不是物理指针相互关联。[^codd] 每一行都有一个[主键](../glossary.md#primary-key)。另一张表中的[外键](../glossary.md#foreign-key)引用它，而[连接（join）](../glossary.md#join)在查询时把相关的行重新组合起来。[规范化](../glossary.md#normalization)让每个事实只存储一次，因此更新只需在一处进行，各副本也就不会彼此偏离。

SQL 是一种[声明式查询](../glossary.md#declarative-query)语言：你描述想要的结果，由查询优化器选择索引、连接顺序和算法。正是这种分离，让一个 1970 年代的构想能够先后运行在大型机、x86 服务器上，如今又运行在云对象存储上。硬件变了，查询不必变。[第 3 章](ch03-database-internals.md) 解释引擎内部发生了什么。

```sql
SELECT p.name, SUM(ol.qty * ol.unit_price) AS revenue
FROM order_line ol
JOIN orders o   ON o.order_id = ol.order_id
JOIN product p  ON p.product_id = ol.product_id
WHERE o.order_date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY p.name ORDER BY revenue DESC LIMIT 10;
```

**擅长：**跨多个实体的事务、完整性约束，以及没人事先计划过的临时性问题。**旗舰产品：**Oracle、MySQL、SQL Server、PostgreSQL。**不宜使用的情形：**数据没有稳定的模式、连接必须以低延迟跨越数千台机器，或者主要问题是一次十跳的关系遍历。

> **类比：半导体。** 规范化就像对物料清单（BOM）去重。在一份干净的 BOM 中，一颗 0402 电容的料号和规格只存在于一条主记录中，所有使用它的电路板都指向这条记录。如果把规格复制到每块板的 BOM 上，那么一次供应商变更就意味着要修改数百行，漏改一行就会发错料。外键就是料号引用，而连接就是 BOM 展开。

### 文档：JSON 与读时模式

[文档数据库](../glossary.md#document-database)存储自包含的类 JSON 记录。MongoDB 以 BSON 格式存储它们，每个文档上限为 16 MiB。[^mdb-limits] 模式存在于应用程序中而非数据库中，这被称为[读时模式（schema-on-read）](../glossary.md#schema-on-read)。团队可以在不执行迁移的情况下新增字段。

关键的设计决策是**内嵌还是引用**。一起读取且增长有限的数据，例如订单的明细行，应当内嵌；被共享或无限增长的数据，例如商品的评论，应当引用。MongoDB 的建模指南也做了同样的划分。[^mdb-limits]

```javascript
db.orders.find({ customer_id: 42 }).sort({ order_date: -1 }).limit(5)
```

**擅长：**一次读取整个聚合、演进中的模式，以及让数据保持应用本来使用的形态。**旗舰产品：**MongoDB、Couchbase、Amazon DocumentDB。**不宜使用的情形：**以多对多关系为主，或需要跨实体的临时性分析。高度内嵌的设计会把这些操作变成应用侧的连接。

### 键值：数据中心规模的哈希表

[键值存储](../glossary.md#key-value-store)只做一件事：给定一个键，返回一个值。Redis 把数据保存在内存中，并增加了列表、集合、有序集合等数据结构。DynamoDB 借鉴了 Amazon 2007 年 Dynamo 论文的思想，但没有沿用其无主（leaderless）设计：每个分区都有一个通过 Multi-Paxos 选举出的主副本。它通过对[分区键](../glossary.md#partition-key)做哈希，把数据项分散到各个分区。[^ddb-atc] 它将单个数据项上限设为 400 KB，分区键上限设为 2,048 字节。[^ddb][^dynamo]

```text
GET session:7f3a9c      ->  {"user":42,"cart":[...],"ttl":1800}
```

**擅长：**缓存、会话、购物车、特征查找和限流器，适用于任何事先知道键且延迟最为关键的场景。**旗舰产品：**Redis、Valkey、DynamoDB、Memcached。**不宜使用的情形：**需要按键以外的任何条件进行查询。届时每一种新的访问模式都需要一个手工构建的二级索引。

> **类比：半导体。** 键值存储就是一张哈希表，用硬件术语说就是 CAM 或 TLB 查找。你给出一个标签，在常数时间内拿回对应条目。你无法在不遍历的情况下向 TLB 询问"进程 7 拥有的、脏位已置位的所有页"。键值数据库具有同样的特性。

许可证在这个品类中很重要。Redis 于 2024 年 3 月放弃了 BSD 许可证，Linux Foundation 将其分叉为 **Valkey**，而 Redis 8 于 2025 年 5 月增加了 AGPLv3 作为第三种许可选项。[^redis]

### 宽列：按键排序的稀疏行

Google 2006 年的 Bigtable 论文定义了一种**宽列（wide-column）**模型：一个从行键、列和时间戳映射到值的稀疏、有序映射。[^bigtable] Cassandra 把 Bigtable 的存储布局与 Dynamo 风格的分区结合起来，HBase 则是 Bigtable 的开源克隆。你需要围绕查询来设计表。分区键决定数据落在哪个节点，聚簇键（clustering key）决定行在分区内的排序。

```sql
-- Cassandra CQL：每个客户一个分区，最新的订单排在最前
SELECT * FROM orders_by_customer WHERE customer_id = 42 LIMIT 20;
```

**擅长：**极高的写入速率、多区域可用性、按时间排序的事件和物联网遥测数据。**旗舰产品：**Cassandra、ScyllaDB、Bigtable、HBase。**不宜使用的情形：**查询不可预测。一个不以分区键开头的问题会变成对整个集群的扫描。[第 4 章](ch04-distributed-databases.md) 介绍这一模型背后的分片与复制机制。

### 图：把关系作为一等数据

[属性图（property graph）](../glossary.md#property-graph)存储**节点**和**边**，两者都可以带有属性。[图遍历](../glossary.md#graph-traversal)直接沿着边从一个节点走到另一个节点，因此其成本随所触及的边数增长，而不是随整张表的大小增长。另一种图模型是 [RDF](../glossary.md#rdf)，它存储主语–谓语–宾语三元组，使用 SPARQL 查询，常见于生命科学和政府领域的知识图谱。

Neo4j 的 Cypher 曾是事实上的属性图语言。2024 年 4 月，ISO 发布了 **[GQL](../glossary.md#gql)**（ISO/IEC 39075:2024），这是继 SQL 之后第一种新的 ISO 数据库语言。其模式匹配语法大量借鉴了 Cypher 的 MATCH 子句，并吸收了 Oracle 的 PGQL 和 G-CORE 研究语言的意见。[^gql] Neo4j 在 2025.06 版本中推出了 Cypher 25，并表示 Cypher 现已覆盖 GQL 的大部分强制性特性。[^neo4j]

```cypher
MATCH (:Product {sku:'X1'})<-[:CONTAINS]-(:Order)<-[:PLACED]-(c:Customer)
      -[:PLACED]->(:Order)-[:CONTAINS]->(rec:Product)
WHERE rec.sku <> 'X1'
RETURN rec.name, count(DISTINCT c) AS buyers ORDER BY buyers DESC LIMIT 5;
```

**擅长：**欺诈团伙识别、推荐、网络与供应链拓扑、身份解析，以及用于 GraphRAG 的知识图谱。**旗舰产品：**Neo4j、Amazon Neptune、TigerGraph。**不宜使用的情形：**工作负载以聚合为主，例如按月求和。图引擎的扫描速度很慢，在这类查询上关系型或列式引擎会胜过它们。

> **类比：半导体。** 图遍历就像在片上网络（NoC）中路由一个数据包。每个路由器只知道它的邻居，数据包逐个 tile 跳转。延迟取决于跳数以及下一个 tile 是否在本地，而与芯片上有多少个 tile 无关。关系型的多跳查询则更像是在每一跳都从头重建路由表。

### 时间序列、搜索与向量

**时间序列。** [时间序列数据库](../glossary.md#time-series-database)存储以时间以及主机、传感器等标签为键、以追加为主的测量值。它会压缩相似值的连续序列，并对旧数据进行降采样。典型查询是求某个时间窗口内的速率、百分位数或移动平均。旗舰产品采取三种路径：InfluxDB 是专门构建的，TimescaleDB 是 Postgres 扩展，Prometheus 是拥有自己的 PromQL 语言的指标引擎。**不宜使用的情形：**数据没有时间戳，或必须原地更新。

```text
rate(http_requests_total{service="checkout"}[5m])     # PromQL
```

**搜索。** [倒排索引](../glossary.md#inverted-index)把每个词项映射到包含它的文档列表，就像书末的索引一样。Apache Lucene 负责构建这些索引，Elasticsearch、OpenSearch 和 Solr 都运行在 Lucene 之上。结果按 [BM25](../glossary.md#bm25) 排序：当某个查询词在一篇文档中出现频繁、但在整个语料库中较为罕见时，该文档得分更高，同时会对文档长度进行校正。BM25 在 Lucene 6 和 Elasticsearch 5 中取代了经典的 TF-IDF，成为默认算法。[^bm25] **不宜使用的情形：**需要它充当记录系统（system of record）。搜索索引通常以近实时方式刷新，并从主数据库重建。

**向量。** 向量存储保存嵌入，即由模型生成的、包含数百到数千个浮点数的数组，使得含义相近的内容在空间中彼此靠近。例如，OpenAI 的 text-embedding-3-small 输出 1,536 维向量。[^openai-emb] 查询的形式是"找到这个向量的 *k* 个最近邻"。在规模化场景下，这需要 HNSW 之类的[近似最近邻（ANN）](../glossary.md#approximate-nearest-neighbor)索引，以牺牲少量召回率换取数量级的速度提升。[^hnsw] **不宜使用的情形：**需要精确匹配，例如 SKU、日期范围或账户 ID。向量度量的是相似性而非同一性，而且存储成本高昂。[第 18 章](../03-ai-data-stack/ch18-embeddings-and-vector-search.md) 介绍各种索引结构。

```sql
SELECT review_id, body FROM review
ORDER BY embedding <=> $query_embedding LIMIT 10;   -- pgvector 余弦距离
```

## 实例演示：一个领域，四种模型

以一家拥有**客户**、**订单**、**商品**和**评论**的零售商为例。同样的事实可以用四种方式建模，而每种模型都能低成本地回答一组不同的问题。

**关系型。** 共有五张规范化的表。每条订单明细引用一个商品，每条评论引用一个客户和一个商品。

```mermaid
erDiagram
  CUSTOMER ||--o{ ORDERS : "下单"
  ORDERS ||--|{ ORDER_LINE : "包含"
  PRODUCT ||--o{ ORDER_LINE : "出现于"
  CUSTOMER ||--o{ REVIEW : "撰写"
  PRODUCT ||--o{ REVIEW : "收到"
  CUSTOMER {
    int customer_id PK
    string name
    string region
  }
  ORDERS {
    int order_id PK
    int customer_id FK
    date order_date
  }
  ORDER_LINE {
    int order_id FK
    int product_id FK
    int qty
    decimal unit_price
  }
  PRODUCT {
    int product_id PK
    string sku
    string name
  }
  REVIEW {
    int review_id PK
    int customer_id FK
    int product_id FK
    int stars
    string body
  }
```

*图 2.2 — 关系型版本中每个事实只存储一次，并通过连接重新组装订单，因此任何新问题都可以在不修改模式的情况下得到回答。*

**文档。** 一个订单文档内嵌其明细行，以及购买时每个商品名称和价格的快照。这是有意为之的[反规范化](../glossary.md#denormalization)，因为即便日后商品目录发生变化，发票也不能随之改变。评论存放在各自的集合中并引用商品 ID，因为一个热门商品可能积累数十万条评论，很快就会超出 16 MiB 的文档上限。[^mdb-limits]

**图。** 客户、订单和商品成为节点，PLACED（下单）、CONTAINS（包含）和 REVIEWED（评论）成为边。

```mermaid
flowchart LR
  C1(("客户：Ana"))
  C2(("客户：Ben"))
  O1["订单 1001"]
  O2["订单 1002"]
  O3["订单 1003"]
  P1{{"商品：耳机 X1"}}
  P2{{"商品：充电器 C2"}}
  P3{{"商品：保护壳 K3"}}
  C1 -->|PLACED| O1
  C1 -->|PLACED| O2
  C2 -->|PLACED| O3
  O1 -->|CONTAINS| P1
  O2 -->|CONTAINS| P2
  O3 -->|CONTAINS| P1
  O3 -->|CONTAINS| P3
  C2 -->|"REVIEWED 2 星"| P1
  C1 -->|"REVIEWED 5 星"| P2
```

*图 2.3 — 在图版本中，"购买了 X1 的客户还购买了……"是从一个节点出发、走四条边的遍历，其成本不会随订单表的规模增长。*

**向量。** 每条评论正文和商品描述都会生成嵌入。客服分析师现在可以查询"描述耳机过热的评论"，并得到"贴近耳朵时会发烫"或"电池摸起来温热"之类的评论。这些评论与查询没有任何共同关键词，因此 SQL 的 `LIKE` 和 BM25 都会漏掉它们。

| 问题 | 关系型 | 文档 | 图 | 向量 |
|---|---|---|---|---|
| 最近 30 天按商品统计收入 | **便宜**（连接 + 分组） | 中等（对内嵌明细行运行聚合管道） | 昂贵（以扫描为主） | 不适用 |
| 显示订单 1001 及其明细行 | 中等（三表连接） | **最便宜**（读取一个文档） | 中等（一跳展开） | 不适用 |
| "购买了 X1 的人还购买了……" | 昂贵（自连接随历史数据增长） | 昂贵（应用侧连接） | **便宜**（有界遍历） | 仅能近似（共同嵌入） |
| 关于过热的评论，措辞不限 | 无法实现（仅支持关键词） | 没有搜索索引则无法实现 | 无法实现 | **便宜**（k-NN 检索） |
| 在所有地方修改某个商品的价格 | **便宜**（一行） | 快照*不应*改变；实时价格字段需要扇出式更新 | 便宜（一个节点属性） | 仅当文本变化时才需重新嵌入 |
| 强制"每条评论都对应一个真实客户" | **内置**（外键） | 应用代码 | 部分支持（模式约束因产品而异） | 不适用 |

*图 2.4 — 同一领域的四种建模方式。每种模型让一组不同的问题变得便宜，因此严肃的应用最终都会组合使用其中几种。*
