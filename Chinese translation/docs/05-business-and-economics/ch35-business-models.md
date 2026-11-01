# 35. 商业模式：按用量计费、订阅、开放核心与托管云
> **深度：** L2 · **阅读时间：** 约 17 分钟 · **最后核实：** 2026-11-01 · **前置阅读：** [第 25 章 — Databricks](../04-company-deep-dives/ch25-databricks.md)，[第 26 章 — Snowflake](../04-company-deep-dives/ch26-snowflake.md)

## 要点速览（TL;DR）

- 数据基础设施的销售方式基本有四种。[按用量计费（consumption pricing）](../glossary.md#consumption-pricing)对实际完成的工作计量（credit、DBU、slot、扫描字节数）。[订阅定价（subscription pricing）](../glossary.md#seat-based-pricing)按席位、节点或已连接数据源收费。[开放核心（open core）](../glossary.md#open-core)免费提供引擎，围绕引擎出售功能、支持或托管服务。托管云服务（managed cloud service）替客户运行软件，同时对软件和基础设施收费。如今大多数大额合同都是混合形态：以按用量计量的消耗来扣减一笔[容量承诺（capacity commitment）](../glossary.md#capacity-commitment)。
- 会计处理决定了业务的行为方式。订阅收入按期（ratably）确认，因此收入平滑、可见性高。按用量计费的收入只有在计量表转动时才确认，因此逐周跟踪客户活动。Snowflake 的 FY2026 10-K 显示，按需（on-demand）计费仅占收入约 1%。即便如此，其几乎全部收入都按消耗确认，因为预付容量只有在被使用时才转为收入。[^sf-10k26]
- 按用量计费的收入具有双向弹性。Snowflake 产品收入在 FY2022（2021 年 2 月–2022 年 1 月）增长 106%。到 FY2024，随着客户优化支出、以及厂商自身性能提升降低了账单，增速降至 38%。[^sf-hist] 管理层此前已就自身平台改进给出约 $97M 的 FY2023 收入逆风指引。[^sf-fy22]
- 毛利率取决于谁来支付云账单。当客户直接向 AWS 付费（"classic"或自管部署）时，厂商获得的收入接近于特许权使用费（royalty），毛利率接近软件水平。当厂商付费时（如无服务器或托管服务），单工作负载收入上升，毛利率百分比下降。Snowflake 的非 GAAP 产品毛利率约为 75%。GitLab 这类按席位定价的软件约为 86%。[^sf-q2][^comps]
- 对 Everpure 而言，Evergreen//One 本身已是类按用量计费的模式：以预留承诺（reserve commitment）作为计费下限，超出部分按需计费，两者都计入其 Subscription ARR KPI。[^ep-10k] 向技术栈上层的数据智能延伸，带来一个新问题：按什么单位收费。可选项包括按 TB、按查询或按受治理资产，而每种单位意味着不同的波动性、毛利率和竞争暴露。

## 为何重要（商业 + Everpure 视角）

商业模式是厂商成本结构与客户预算之间的契约。在数据基础设施领域，这一契约决定了投资者关心的三件事：收入波动有多大、毛利率能有多高、销售团队如何行事。两家产品相同、年收入相同的公司，价值可能相差悬殊。一家出售每年续约的 $500K 席位；另一家出售 $500K 的计量表，当客户工程师调优查询时，它可能在一个季度内下降 20%。[第 36 章](ch36-unit-economics-kpis.md)介绍解读这类业务所用的指标。[第 37 章](ch37-public-comps-valuation.md)介绍市场如何为它们定价。

商业模式还决定了竞争格局。按用量计费让厂商无需走采购流程即可小规模切入、逐步扩张。但它也让超大规模云厂商（hyperscaler）可以在同一计量单位上压价。开放核心以低成本建立采用度，却引来云厂商托管免费引擎。正是这种担忧催生了 [第 38 章](ch38-open-source-strategy.md)所述的 2018–2021 年许可证变更潮。席位定价可预测，但收入受限于员工人数，而 AI 智能体正在威胁员工人数。

对 Everpure 而言，这个问题非常现实。其 Evergreen//One 存储即服务已表现为容量承诺与按用量计费的混合体：预留承诺、超出部分按需计费，并附带服务等级保障。[^ep-e1] 10-K 将 Subscription ARR 定义为包含年化的按需计费额，因此该 KPI 已有一部分随用量变动。[^ep-10k] 进入数据管理与数据智能领域（1touch，现为 Everpure Data Intelligence）意味着要为位于存储之上的软件选择定价单位。按 TB 定价与存量客户群一致，但容易导致商品化。按查询定价与价值一致，但会引入 Snowflake 式的波动。按资产或按数据源的数据治理定价与数据目录厂商一致，但面向的是不同的买方。下文"Everpure 视角：在技术栈上层选择计费单位"一节，将这些权衡作为基于公开信息、战略团队可能评估的选项加以阐述。

## 工作原理

### 四种模式，各用一段话说明

**按用量计费。** 厂商定义一个工作单位，按秒或按字节计量。Snowflake [credit](../glossary.md#snowflake-credit) 按规格计量虚拟仓库运行时间。Databricks [DBU](../glossary.md#dbu) 按实例类型和工作负载 SKU 计量处理能力。BigQuery 要么按扫描的 TiB 收费，要么按预留容量的 [slot](../glossary.md#slot)-小时收费。[^bq] MongoDB Atlas 按集群小时、存储和数据传输计费。[^mdb-10k24] Confluent Cloud 按弹性容量单位（[eCKU](../glossary.md#ecku)）加网络与存储计费。[^cflt-pricing] 收入在客户消耗时确认。

**订阅。** 厂商出售在一定期限内使用软件的权利。价格随某个价值代理指标（用户、节点、核数或已连接数据源）缩放，收入按期确认。商业智能（BI）席位、Collibra 和 Alation 等数据目录厂商（按版本、用户和已连接数据源定价；见[第 33 章](../04-company-deep-dives/ch33-governance-catalog-security-companies.md)）以及 dbt 的开发者席位都采用这种方式。[^dbt-pricing] 云时代之前的 Informatica 出售永久许可证外加支持年费，这是一种更早期的变体，见[第 29 章](../04-company-deep-dives/ch29-operational-database-vendors.md)。此后它转向了池化的 [Informatica Processing Unit](../glossary.md#informatica-processing-unit)，这是一种按用量计费的单位。[^infa-ipu]

**开放核心。** 核心引擎免费：MongoDB Community、Elasticsearch、Apache Kafka、dbt Core、Airbyte 的连接器。收入来自引擎周边：可以是带安全与管理功能的企业版（Confluent Platform、MongoDB Enterprise Advanced）、支持服务，或利润最高的托管服务。免费层就是营销预算。它在任何销售人员登门之前，就培养出了熟悉产品的开发者。

**托管云服务。** 厂商在云上运营软件，并对结果收费。这既适用于厂商自有引擎（Atlas、Elastic Cloud、Confluent Cloud），也适用于由超大规模云厂商运营的"开源即服务"（Amazon RDS for PostgreSQL、ElastiCache for Valkey）。开放核心的经济性成败系于托管服务。谁运营服务，谁就拥有客户关系和基础设施利润。当超大规模云厂商来运营时，项目作者可能一无所获。

### 计费单位：每种计量表到底在计什么

| # | 单位 | 厂商 / 产品 | 计量内容 | 代表性标价（美国，截至检索时） | 模式 |
|---|---|---|---|---|---|
| 1 | Credit | Snowflake | 按规格缩放的虚拟仓库小时（XS = 1 credit/小时，每升一档翻倍）；无服务器与 AI 功能折算为 credit | 因版本和区域而异；见[第 26 章](../04-company-deep-dives/ch26-snowflake.md)[^sf-cost] | 按用量计费 |
| 2 | DBU | Databricks | 按实例类型和 SKU 计的每小时处理能力 | 每 DBU 约 $0.15（Jobs，classic）至约 $0.70（Serverless SQL）（第三方汇编）[^dbx-pricing] | 按用量计费 |
| 3 | Slot-小时 | Google BigQuery editions | 预留或自动扩缩的查询算力 | 每 slot-小时 Standard $0.04、Enterprise $0.06、Enterprise Plus $0.10[^bq] | 按用量计费 / 容量 |
| 4 | 每扫描 TiB 美元 | BigQuery 按需 | 每次查询处理的字节数 | 每 TiB $6.25；每月前 1 TiB 免费[^bq] | 按用量计费 |
| 5 | RPU-小时 | Amazon Redshift Serverless | 查询运行期间的 Redshift Processing Unit | 每 RPU-小时 $0.375（US East）；最低 4 RPU[^redshift] | 按用量计费 |
| 6 | eCKU-小时 | Confluent Cloud | 弹性 Kafka 集群容量，另加按 GB 计的网络与存储 | Confluent 计算器：每 eCKU-小时 Standard $0.75、Enterprise $2.25；主定价页隐含的月度下限不同[^cflt-pricing] | 按用量计费 |
| 7 | 实例小时 + GB | MongoDB Atlas | 集群档位（计算、内存）、存储、数据传输 | 按集群规模分档；大客户按年承诺[^mdb-10k24] | 按用量计费 / 托管 |
| 8 | MAR | Fivetran | 每个连接分档计价的变更[月活跃行数（monthly active rows）](../glossary.md#monthly-active-rows) | 首档每百万 MAR $500，超过 10 亿后降至 $1.18[^ft-pricing] | 按用量计费 |
| 9 | IPU | Informatica IDMC | 在集成、数据质量、数据目录之间共用的池化单位 | 费率未公开[^infa-ipu] | 预付按用量计费 |
| 10 | Data Worker | Airbyte（Pro / Enterprise Flex） | 预留的并行同步容量 | 仅限询价；2025 年 2 月推出[^ab-capacity] | [基于容量的定价（capacity-based）](../glossary.md#capacity-based-pricing) |
| 11 | vCPU 或实例小时 | Classic 计算、RDS 式托管开源 | 客户租用的虚拟机 | 客户自己的云账单 | 直通（pass-through） |
| 12 | 存储 每 TB-月美元 | Snowflake、Evergreen//One | 存储或预留的容量 | Evergreen//One 归档层每 GiB-月 $0.018 起（≈ 每 TiB-月 $18），最低 500 TiB，36 个月[^ep-e1] | 按用量计费 / 承诺 |
| 13 | 出口流量 每 GB 美元 | AWS 及同类厂商 | 离开区域或云的数据 | 100 GB 免费后，每月前 10 TB 约 $0.09/GB（US East）[^aws-egress] | 按用量计费 |
| 14 | 席位 | dbt 平台、BI 工具 | 具名开发者或查看者 | dbt Starter 每开发者席位每月 $100，含 15,000 次成功的模型构建[^dbt-pricing] | 订阅 + 用量 |
| 15 | 对话 / 动作 | Salesforce Agentforce | 智能体对话，或通过 [Flex Credits](../glossary.md#flex-credits) 计量的动作 | 每次对话 $2（2024 年标价）；每个动作 $0.10（每 100,000 credit $500）；按用户附加包约 $125/月（第三方汇编）[^af-price] | 按用量计费 / 席位混合 |
| 16 | 数据源或资产 | Collibra、Alation、Atlan | 用户、已连接数据源、受治理资产 | 仅限询价；按版本[^ch33] | 订阅 |

*图 35.1 — 十六种计量表，没有公分母。每家厂商选择的单位，要么映射到自身成本驱动因素（计算时间、字节、容量），要么映射到客户价值的代理指标（席位、资产、对话）。标价是上限，而非大客户实际支付的价格。*

> **类比：按用量计费即使用特许权费。** 按用量计费合同在经济上最接近 **Arm 的按芯片特许权费**。Arm 一次性授权其架构，然后对每颗出货芯片收取特许权费，因此其收入随客户的出货量起落，而不是随新签许可证变动。在 FY2026（截至 2026 年 3 月的财年），Arm 收入增长 23% 至 $4.92B。特许权费收入增长 21%，受益于 Armv9 设计更高的单芯片费率（GAAP）。[^arm-20f] Snowflake 和 Databricks 以同样方式对客户的分析活动收取"特许权费"。分析师的模型也相同：存量客户群 × 使用强度 × 单位费率。单位费率升级（Armv9；无服务器 SKU）是独立于用量的增长杠杆。
