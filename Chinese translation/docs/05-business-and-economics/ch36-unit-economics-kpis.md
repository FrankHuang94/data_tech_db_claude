# 36. 单位经济与 KPI
> **深度：** L2 · **阅读时间：** 约 14 分钟 · **最后核实：** 2026-11-01 · **前置阅读：** [第 35 章 商业模式](ch35-business-models.md)

## 要点速览（TL;DR）

- **解读数据平台的损益表大约要看十个 KPI，其中大多数由公司自行定义、未经审计且不可直接比较。** Snowflake 的净收入留存率（NRR）和 MongoDB 的"净 ARR 扩张率（net ARR expansion rate）"回答的都是"去年的客户今年多花了多少？"，但它们使用不同的客户群组、不同的单位和不同的时间窗口。比较两个数字之前，务必先读 10-K 中的定义。
- **在按用量计费（consumption）模式下，NRR 是增长方程中的主导项。** Snowflake 的 NRR 从 178%（FY2022）降至 126%（FY2025），产品收入增速也随之下滑。此后 NRR 稳定在 125–126%，而 Q2 FY2027（2026 年 5–7 月）产品收入增速重新加速至 37%（GAAP）。[^sf-q2][^fin-csv]
- **剩余履约义务（RPO）是已签约的积压订单，而不是收入预测。** 在截至 2026 年 7 月的两个季度里，Snowflake 的 RPO 从 $9.77B *降至*约 $9.0B，而同期收入在加速。客户消耗预付容量的速度快于签订新承诺的速度。[^fin-csv][^sf-10q]
- **对大多数软件公司而言，GAAP 与非 GAAP 之间的差距才是真正的看点。** Q2 FY2027，Snowflake 的 GAAP 营业利润率为 −17.0%，非 GAAP 营业利润率为 +15.3%。这 32 个百分点的差距主要来自约 $424M 的股权激励费用（SBC），约占收入的 27%（媒体报道）。MongoDB 的差距约为 20 个百分点，Everpure 约为 14 个百分点。[^sf-q2][^secapi][^mdb-q2][^ep-q2]
- **40 法则（Rule of 40）是一族公式，而非单一数字。** 对 Snowflake 而言，根据所用的利润率口径和期间，得分从约 18（Q2 FY2027 增速加 GAAP 营业利润率）、约 20（FY2026，扣除 SBC 后的 FCF）、约 41（季度调整后 FCF）到约 58（FY2027 调整后 FCF 指引）不等（作者计算）。经 SBC 调整的版本是 CFA 式的保守解读。按此口径，鲜有高增长数据公司能超过 40。

## 为何重要（商业 + Everpure 视角）

企业发展团队用这些 KPI 为并购标的、合作伙伴和竞争对手定价。每一个 KPI 都是对未来的一个浓缩判断。NRR 表明存量客户将持续增加支出。RPO 表明其中部分支出已有合同约束。毛利率表明每一美元在付完超大规模云厂商的账单后还剩多少。魔力数字（magic number）表明新增收入是以多高的效率"买来"的。误读一个定义，就会给交易定错价。典型的错误是把两年滚动群组口径的 NRR 与基于 ARR 的扩张率相比较，或把 GAAP 与非 GAAP 利润率相比较。

对 Everpure 而言，这一视角有两面。**由外向内：**本书中的每一个数据平台合作伙伴或标的（Snowflake、Databricks、MongoDB 以及[第 32 章](../04-company-deep-dives/ch32-ai-native-data-companies.md)中的 AI 原生厂商）都用这套语言披露业绩。**由内向外：**Everpure 已经披露一组混合 KPI：截至 Q2 FY2027（截至 2026-08-02 的季度），产品收入、订阅服务收入、订阅年度经常性收入（ARR）$2.1B（+20%）以及 RPO $4.1B（+44%）。[^ep-q2] 如果公司进一步进入数据管理和数据服务领域，市场将开始要求下文所述的软件 KPI，并以此评判 Everpure。"工作原理"的最后一节说明了会有哪些变化。

## 工作原理

### KPI 树

本章的每个指标都会影响两个结果之一：收入增长有多快，以及多少收入转化为自由现金流（FCF）。下面的树状图就是地图，本章其余部分从左到右逐一走过。

```mermaid
flowchart TB
  V["价值创造：增长加 FCF 利润率（40 法则）"]
  RG["收入增长"]
  FCF["FCF 利润率"]
  NRR["NRR：存量群组支出增长"]
  NEW["新客户数乘以爬坡速度"]
  EXP["扩张：更多工作负载、更多 credit"]
  CON["收缩：优化、降价"]
  CH["流失：失去的客户"]
  LEAD["领先信号：RPO、cRPO、$1M+ 客户、G2000 数量"]
  OM["营业利润率（GAAP vs 非 GAAP）"]
  WC["营运资本：预先开票、递延收入"]
  CAPEX["资本开支与资本化软件"]
  GM["毛利率"]
  COGS["云 COGS：超大规模云厂商的计算与存储"]
  SM["销售与营销：魔力数字、CAC 回收期"]
  RD["研发"]
  SBC["SBC：非现金但具有稀释性"]
  RG --> V
  FCF --> V
  NRR --> RG
  NEW --> RG
  EXP --> NRR
  CON --> NRR
  CH --> NRR
  LEAD --> RG
  OM --> FCF
  WC --> FCF
  CAPEX --> FCF
  GM --> OM
  COGS --> GM
  SM --> OM
  RD --> OM
  SBC --> OM
```

*图 36.1 — KPI 树。收入增长 = NRR 加新客户贡献。FCF 利润率 = 经营运资本和资本开支调整后的营业利润率。SBC 在 GAAP 下计入营业费用，但在非 GAAP 下被剔除，这就是两种利润率出现背离的原因。*

### 净收入留存率：一个数字浓缩的群组分析

[净收入留存率（net revenue retention）](../glossary.md#net-revenue-retention)（NRR，也称净美元留存率或 NDR）选取一组固定的客户，用他们当前的支出除以一年前的支出。流失的客户按原支出留在分母中，在分子中计为零。新客户不计入。NRR 为 126% 意味着该群组在扣除扩张、收缩和流失之后，*净*多花了 26%。

各家定义的差异至关重要：

- **Snowflake** 使用两年滚动窗口。群组为在第一年*第一个月*内任意时点使用过平台的容量合同客户。NRR 等于该群组第二年的产品收入除以第一年的产品收入。实际上，它比较的是两个连续的 12 个月滚动产品收入窗口。近年的 10-K 说明，该群组包括通过经销商购买的最终客户，历史数据已针对收购和分拆进行调整。[^sf-10k26][^sf-10k21] 由于它是两个 12 个月总和之比，因此平滑且转向缓慢。
- **MongoDB** 披露"净 ARR 扩张率"。它用一年前已是客户的客户当前 ARR，除以一年前*全部*客户（包括已流失客户）的 ARR。截至 2026 年 1 月 31 日约为 121%，高于一年前的约 119%。MongoDB 常在业绩电话会上对其作宽泛描述（例如"高于 120%"）或给出近似值，而不是在固定的季度表格中披露。[^mdb-10k] 它是一个 ARR 时点快照，而非收入流量，Atlas 的消耗需经年化处理才能得出。

**总收入留存率（gross revenue retention，GRR）**剔除了扩张：（上年支出 − 收缩 − 流失）÷ 上年支出，上限为 100%。它衡量的是底线，即在没有任何客户增长时存量客户群的黏性。在本章查阅的新闻稿中，Snowflake 和 MongoDB 都没有披露数值化的总留存率。尽职调查时应主动索要。一个示意性的例子（作者数字，非公司数据）：一个支出 $100M 的群组增长到 $126M，其中扩张增加 $32M、收缩减少 $4M、流失减少 $2M。NRR 为 126%，GRR 为 94%。NRR 相同的两家公司，GRR 可能差异很大；GRR 较低的那家依赖少数大客户足够快地扩张，以弥补漏损。

> **类比：同店销售与群组收益率。** NRR 就是软件公司的同店销售（comps）：它反映一年前已存在门店的增长，忽略新开门店。固定收益分析师会把它看作一个成熟资产池（seasoned pool）。GRR 是存续曲线（1 减去提前还款和违约），扩张则是票息上调。零售商可以靠新店实现强劲的总增长，而同店销售转负；SaaS 公司也可以靠新客户做到这一点，而 NRR 在侵蚀。同店销售告诉你存量业务是否健康。

**为什么在按用量计费模式下 NRR 领先于收入增长。** Snowflake 只在客户消耗 credit 时确认产品收入，因此去年的客户贡献了今年大部分收入。新客户起步小，需要数个季度爬坡。近似地，产品收入增速 ≈（NRR − 1）×（群组贡献的收入占比）+ 群组以外客户的贡献。NRR 为 126% 且群组贡献大部分收入时，仅存量客户就带来约 20–26 个百分点的增长。Q2 FY2027 37% 的产品收入增速中，剩余约 11 个百分点或更多来自新客户的爬坡（作者近似估算；由于 NRR 为 12 个月滚动口径、增速为季度同比口径，两者窗口不同）。[^sf-q2] 由于群组支出具有持续性，稳定或上升的 NRR 为下一年的增长设定了底线。NRR 下降是增长底线正在下移的最早的硬证据。

![Snowflake 各财务期净收入留存率折线图：从 FY2020 的 158% 和 FY2022 178% 的峰值，降至 FY2024 的 131%，并自 FY2025 至 Q2 FY2027 稳定在 125–126%](../assets/charts/snowflake_nrr.png)

*图 36.2 — Snowflake NRR（公司披露 KPI）。2022–2024 年 NRR 从 178% 滑落至 131%，同期增速从 106% 降至 38%。NRR 在 125–126% 企稳，恰逢增速稳定在 29% 左右，随后在 Q2 FY2027 重新加速至 37%。来源：`data/company_financials.csv`。*

应将这张图作为一个群组故事来解读。产品收入增速在 FY2022（2021 年 2 月–2022 年 1 月）为 106%，FY2024 为 38%，FY2025 和 FY2026 分别为 30% 和 29%（GAAP；作者依据 CSV 计算）。[^fin-csv] 下行阶段 NRR 与增速同步，因为客户在 2021 年的繁荣后优化了消耗。回升阶段两者的关系变松了：Q1 和 Q2 FY2027 增速分别重新加速至 34% 和 37%，而 NRR 持平于 126%。[^fin-csv] 由于 NRR 是两个窗口的滚动比率，它对季度拐点的反应滞后数个季度。因此，分析师会把 NRR 的环比趋势与 $1M+ 客户数一起作为确认信号。

### RPO 与 cRPO：已签约积压

[剩余履约义务（remaining performance obligations）](../glossary.md#remaining-performance-obligations)（RPO）是已签约但尚未确认的收入金额，按照 ASC 606 在每份 10-Q 的收入附注中披露。当期 RPO（cRPO）是预计在十二个月内确认的部分。截至 2026 年 7 月 31 日，Snowflake 的 RPO 约为 $9.0B，同比 +30%。Snowflake 预计其中约 54%，即约 $4.9B（作者计算），将在未来十二个月内确认。公司提示，确认时点取决于客户消耗，且未使用的容量有时可结转至合同期限之后。[^sf-10q]

RPO 增速可能高于收入，原因很简单：多年期容量交易在签约时就把全部承诺额计入 RPO，而收入只在客户消耗时才到来。一笔三年期、$300M 的承诺在一个季度内为 RPO 增加 $300M，而每年为收入增加的或许只有 $100M。极端案例是 Oracle。凭借 AI 基础设施合同，其 RPO 在 Q1 FY2027（2026 年 6–8 月）达到 $664B，而 FY2027 收入指引至少为 $90B。[^comps] 反向情况也会发生。Snowflake 的 RPO 在 2026 年 1 月 31 日达到 $9.77B 的峰值（包括公司历史上最大的一笔交易），随后两个季度降至 $9.21B 和约 $9.0B，而同期收入在加速。[^fin-csv] 客户消耗预付容量的速度快于补充速度。这对近期收入是利好，对积压覆盖度则是中性偏谨慎。

![Snowflake 各财务期剩余履约义务柱状图：从 FY2021 约 $1.3B 升至 FY2026 末 $9.77B 的峰值，并在 Q2 FY2027 回落至约 $9.0B](../assets/charts/snowflake_rpo.png)

*图 36.3 — Snowflake RPO（GAAP 披露）。五年间积压增长约七倍，但呈波动性。一笔大额多年期交易对它的影响就可能超过一个季度的收入，因此应看四个季度的趋势，而不是季度环比变化。来源：`data/company_financials.csv`。*

> **类比：半导体积压订单与订单出货比。** RPO 就是芯片厂商的积压订单，只是规则更严格：ASC 606 只计入可执行的合同，而半导体积压订单常包含可取消订单。cRPO ÷ 未来十二个月收入的作用类似订单出货比（book-to-bill）覆盖度。Snowflake 的 cRPO（约 $4.9B）约覆盖 FY2027 产品收入指引（$6.07B）的 80%（作者估算），而对真正的未来十二个月收入覆盖更少，因为截至 2026 年 7 月 31 日，FY2027 已有一半收入确认完毕；其余部分必须来自按需使用和新承诺。RPO 下降而收入上升，相当于出货火爆时订单出货比低于 1。持续一两个季度无妨，若持续下去则是警示信号。

### 开票额，以及按用量计费公司为何淡化它

开票额（billings）等于收入加递延收入的变动，即当期开出的发票金额。对按席位计费的 SaaS 以及销售多年期支持服务的硬件厂商而言，开票额是订单额的合理代理指标。NetApp 仍以此为首要指标：Q1 FY2027（2026 年 5–7 月）开票额为 $2.06B，+36%（由 GAAP 数据推算）。[^ntap] 按用量计费的公司则淡化开票额。Snowflake 对容量合同开票，通常每年预先开票，因此开票额随合同期限和开票时点波动，而收入跟随用量。一位签订更大三年期交易但按年开票的客户，开票额变化不大。一位一次性预付两年的客户则制造了一个尖峰，却丝毫不反映消耗情况。对 Snowflake 而言，RPO 和 NRR 承载了订阅公司中开票额所承载的信息。

### 毛利率与云 COGS

云数据平台的收入成本主要是超大规模云厂商的账单：为运行客户查询而向 AWS、Azure 和 Google Cloud 购买的虚拟机、对象存储和网络出口流量，外加支持人员和资本化软件的摊销。Snowflake 将产品毛利率与总毛利率分开披露。Q2 FY2027，产品毛利率 GAAP 为 70.9%、非 GAAP 为 74.7%（差额为收入成本中的 SBC 和摊销）。由于 AI 工作负载的计算成本更高，全年非 GAAP 指引被下调至 74%。[^sf-q2][^fin-csv] 同一季度，MongoDB 的总毛利率 GAAP 为 74%、非 GAAP 为 76%。该数字混合了承担云 COGS、毛利率较低的 Atlas，与高毛利的自管许可证 Enterprise Advanced 以及服务。[^mdb-q2] 随着 Atlas 增至约占收入的 73%（FY2026），收入结构向低毛利产品倾斜。[^fin-csv]

[第 35 章](ch35-business-models.md)和[第 25 章](../04-company-deep-dives/ch25-databricks.md)所述的无服务器效应也朝同一方向推动。当厂商在自己的云账户中运行计算时，全部虚拟机成本转入其 COGS。单位收入上升，毛利率百分比下降，而毛利额仍可能上升。应以毛利额而非毛利率百分点来评判这一取舍。

> **类比：云 COGS 就是无晶圆厂公司的晶圆成本。** Snowflake 向超大规模云厂商购买算力，就像 NVIDIA 向 TSMC 购买晶圆。毛利率是相对于一项公司无法控制的成本的溢价。有三个杠杆：对投入品的议价能力（多年期承诺消费额度折扣相当于云时代的晶圆产能分配协议）、架构效率（更好的查询引擎如同更高的单片晶圆良率），以及产品结构（AI 推理工作负载类似先进制程、低良率的产品）。一家代工厂同时也是其竞争对手的无晶圆厂公司，存在明显的张力。一个其超大规模云厂商同时销售竞品数据仓库的数据平台，也是如此。

### 销售与营销效率：魔力数字与 CAC 回收期

**[魔力数字（magic number）](../glossary.md#magic-number)** 回答的是每一美元销售与营销（S&M）支出买来了多少新增年化收入。该术语于 2005 年由后来的 Scale Venture Partners 提出，季度公式自 2008 年起流行开来。[^scale] 一个常见版本是（本季度收入 − 上季度收入）× 4 ÷ 上季度 S&M。高于约 1.0 为高效，约 0.7 是通常的"健康"门槛。[^scale] **[CAC 回收期（CAC payback）](../glossary.md#cac-payback)** 将同样的输入换算成月数：12 ÷（魔力数字 × 毛利率）。它回答的是新增收入带来的毛利需要多长时间才能收回获客支出。

要从 10-Q 计算这两个指标，从利润表中取连续两个季度的总收入，从营业费用项中取 S&M（GAAP 口径，因此包含 SBC 和收购无形资产摊销），并从同一报表中取毛利率。下面的算例正是这样做的。主要有两个陷阱。第一，按用量计费的收入对天数敏感：Snowflake 的 Q1（2–4 月）有 89 天，Q2（5–7 月）有 92 天，这会美化环比魔力数字。第二，GAAP S&M 项包含非现金的 SBC，而许多卖方模型使用非 GAAP S&M，因此得出的数字更高。

### SBC 与稀释

[股权激励费用（stock-based compensation）](../glossary.md#stock-based-compensation)是以股票形式支付的员工薪酬。它在 GAAP 下计为费用，但在非 GAAP 营业利润和经营现金流中被加回。Snowflake FY2026 的 SBC 为 $1,599.5M，占收入 34%，低于 FY2025 的 $1,479.3M（41%）（GAAP；百分比为作者计算）。[^sf-10k26][^fin-csv] Q2 FY2027 约为 $424M，占收入 27.4%（媒体报道，引自 10-Q）。[^secapi]

CFA 的观点是：SBC 是真实的费用。用股票而非现金支付工程师，并不会让劳动变成免费的，它只是把成本从利润表转移到了股本数量上。有两项交叉核对能让分析保持诚实。(1) **稀释：**将稀释后股数增长与回购进行比较。Snowflake 在 FY2026 以平均 $177.37 回购约 4.9M 股，约 $874M（作者计算），约为当年 SBC 费用的 55%；在 FY2027 上半年以约 $300M 回购约 1.7M 股。[^sf-10k26][^sf-10q] (2) **现金成本：**抵消稀释的回购就是 SBC 的现金成本。它们体现在筹资现金流中，位于 FCF 线以下，因此"FCF 减回购"或"FCF 减 SBC"是更干净的股东盈余（owner earnings）衡量。

> **类比：SBC 与研发资本化之争。** 半导体分析师争论研发是否应资本化，因为它构建的是多年期资产。SBC 引出了镜像问题：它是一项以股权而非现金支付的经营成本。把 SBC 加回，就像把研发资本化后却从不摊销。投入照样被消耗掉，只是用别人的所有权来支付。

### 40 法则、FCF 利润率与客户数

**[40 法则（Rule of 40）](../glossary.md#rule-of-40)** 认为收入增速加利润率应超过 40%。它由 Brad Feld 于 2015 年 2 月针对规模化 SaaS 公司推广开来。[^feld] 变体比法则本身更重要。增速可以是总收入或产品收入，季度或年度。利润率可以是 FCF、调整后 FCF、非 GAAP 营业利润率、GAAP 营业利润率或 EBITDA。Palantir 每季度公布一个公司自定义的得分：Q2 2026 为 155%，基于 93% 的增速和 63% 的调整后 FCF 利润率。[^pltr] ServiceNow 以固定汇率订阅收入增速和 FCF 利润率披露一个"Rule of"数字。[^now]

**FCF 利润率** =（经营现金流 − 资本开支）÷ 收入。公司随后会对其进行"调整"。Snowflake 的调整后 FCF 加回了与员工股票交易相关的工资税项目的净现金支出。其他公司则加回重组或收购成本。每年预先开票使 FCF 在季度间波动：Snowflake Q2 FY2027 调整后 FCF 利润率为 6.0%，Q4 FY2026 为 61%，FY2026 全年为 25.5%（非 GAAP）。[^fin-csv] 做任何 40 法则分析时，都应使用 12 个月滚动或全年数据。

![十二家数据与基础设施软件公司的收入增速与 FCF 利润率散点图，含 40 法则虚线；Palantir 远高于该线，为 156，Datadog 61、Snowflake 58、ServiceNow 56、Rubrik 53、Everpure 52、NetApp 50、MongoDB 48、Elastic 45、Nutanix 42，而 Workday 30 和 GitLab 24 位于线下](../assets/charts/ch36_rule_of_40.png)

*图 36.4 — 可比公司的 40 法则（最近一季增速，GAAP；FCF 利润率为非 GAAP，口径以标记形状区分）。按调整后 FCF 口径，大多数数据与基础设施公司现已超过 40。若换用季度 FCF 利润率（Snowflake 降至约 41）或扣除 SBC，排名会改变。来源：`data/ch36_rule_of_40.csv`；Everpure 的 FCF 利润率为依据指引中值的估算。*

**客户数**是最后一个领先指标。Snowflake 披露 12 个月滚动产品收入超过 $1M 的客户数：Q2 FY2027 为 828 家（+27%），而 FY2021 为 77 家。它还披露福布斯全球 2000 强（Forbes Global 2000）客户数：829 家，约占名单的 41%（作者计算）。[^sf-q2][^fin-csv][^pulse] MongoDB 披露总客户数（70,600+）和 ARR 超过 $100K 的客户数（2,999）。[^mdb-q2] 大客户数比总数更重要。在按用量计费模式下，大客户支撑着 NRR，因此 $1M+ 客户新增放缓往往先于 NRR 变化出现。

### 算例：解读 Snowflake 的 Q2 FY2027（2026 年 5–7 月）

FY2027 = 2026 年 2 月–2027 年 1 月。所有金额单位均为百万美元（US$M）。媒体报道的摘要引用了约 $263M 的 GAAP 营业亏损，与公司 −17.0% 的 GAAP 营业利润率完全吻合。

| # | 新闻稿 / 10-Q 中的项目 | 公式 | 数值 | 标签 |
|---|---|---|---|---|
| 1 | 产品收入 | 报告值 | 约 $1,490（同比 +37%） | GAAP |
| 2 | 总收入，Q2 FY2027 | 报告值 | $1,546.8（+35%，对比 $1,145.0） | GAAP |
| 3 | 总收入，Q1 FY2027 | 报告值 | 约 $1,390 | GAAP（取整） |
| 4 | S&M 费用，Q2 FY2027 | 10-Q 利润表 | $611.6（+22%，对比 $502.0） | GAAP |
| 5 | S&M 费用，Q1 FY2027 | 六个月 S&M（约 $1,200）− 第 4 行 | 约 $590 | 估算（推导） [VERIFY] |
| 6 | 魔力数字（环比） | （第 2 行 − 第 3 行）× 4 ÷ 第 5 行 | (156.8 × 4) ÷ 590 ≈ **1.06** | 估算 |
| 7 | 魔力数字，天数调整后 | 将 Q2 收入按 Q1 的 89 天折算：1,546.8 × 89/92 = 1,496.4；(1,496.4 − 1,390) × 4 ÷ 590 | ≈ **0.72** | 估算 |
| 8 | CAC 回收期 | 12 ÷（第 6 行 × GAAP 产品毛利率 70.9%） | ≈ **16 个月**（天数调整后 ≈ 24） | 估算 |
| 9 | S&M 占收入百分比 | 第 4 行 ÷ 第 2 行 | 39.5%（一年前为 43.8%） | GAAP |
| 10 | SBC | 现金流量表 | 约 $424 | GAAP，媒体报道 |
| 11 | SBC 占收入百分比 | 第 10 行 ÷ 第 2 行 | **27.4%** | GAAP，媒体报道 |
| 12 | GAAP 营业利润 | 报告值 | 约 −$263（−17.0%） | GAAP |
| 13 | 其他非 GAAP 加回项 | 第 14 行 − 第 12 行 − 第 10 行 | 约 $76（4.9 个百分点） | 推导；收购无形资产摊销、股权相关工资税及其他 [VERIFY 拆分] |
| 14 | 非 GAAP 营业利润 | 报告值 | 约 $237（15.3%） | 非 GAAP |
| 15 | 调整后 FCF | 报告值 | $92.3（6.0%） | 非 GAAP |
| 16 | 40 法则（季度） | 总收入增速 35 + 调整后 FCF 利润率 6.0 | **41** | 混合：GAAP 增速，非 GAAP FCF |
| 17 | 40 法则（指引） | 35 + FY2027 调整后 FCF 利润率指引 23 | **58** | 依据公司指引推导 |
| 18 | 40 法则（扣除 SBC，FY2026） | FY2026 增速 29.2 +（调整后 FCF $1,192.7 − SBC $1,599.5）÷ $4,683.9 | 29.2 − 8.7 ≈ **20** | 估算 |

*图 36.5 — 10-Q 算例。来源：Snowflake Q2 FY2027 新闻稿及 10-Q；Q1 FY2027 新闻稿；FY2026 10-K；SBC 数据来自 sec-api.io。[^sf-q2][^sf-10q][^sf-q1][^sf-10k26][^secapi] 利润率桥接为 −17.0% + 27.4（SBC）+ 4.9（其他）= 15.3%。仅天数调整一项就抹去了表观 S&M 效率的约三分之一。*

解读结论：Snowflake 获取增长的效率高于一年前。S&M 增长 22%，而收入增长 35%，因此 S&M 占收入比重从 43.8% 降至 39.5%。按日历调整后，约 0.7 的魔力数字属于健康而非惊艳。SBC 占收入比重已从约 41% 降至约 27%，但它仍是 GAAP 亏损与非 GAAP 盈利之间差距的主要来源。按公司定义，合理的 40 法则区间约为 41–58；若将 SBC 视同现金，则约为 20。

### 一张表看 MongoDB，以及与 Everpure 的对比

| Q2 FY2027（2026 年 5–7 月）* | Snowflake | MongoDB | Everpure（原 Pure Storage） |
|---|---|---|---|
| 收入（GAAP） | $1,546.8M，+35% | $771.8M，+30% | 约 $1,186M（产品 $687M + 订阅服务 $499M），+38% |
| 毛利率 | 产品 GAAP 70.9% / 非 GAAP 74.7% | GAAP 74% / 非 GAAP 76%（总计） | GAAP 68.4% / 非 GAAP 69.9%（总计） |
| GAAP 营业利润率 | −17.0%（约 −$263M） | 3.7%（$28.4M） | 5.3%（$63M；作者计算） |
| 非 GAAP 营业利润率 | 15.3% | 24%（$185.9M） | 19.4% |
| GAAP 与非 GAAP 差距 | 约 32 个百分点 | 约 20 个百分点 | 约 14 个百分点 |
| 当季 FCF（非 GAAP） | 调整后 $92.3M（6.0%） | $137.6M（17.8%） | −$238M（FY2027 指引 $600–800M） |
| 留存 / 经常性 KPI | NRR 126% | 净 ARR 扩张率约 121%（2026 年 1 月 31 日，10-K；Q2 FY2027 约 122%，媒体报道） | 订阅 ARR $2.1B，+20% |
| 积压 | RPO 约 $9.0B，+30% | 未作为主要 KPI | RPO $4.1B，+44% |
| 大客户 KPI | 12 个月滚动收入 >$1M 客户 828 家；G2000 客户 829 家 | ARR ≥$100K 客户 2,999 家 | 未作为主要 KPI 披露 |
| 40 法则（作者计算） | 41（季度）/ 58（指引） | 约 48（季度） | 约 52（基于指引的估算） |

*图 36.6 — 三家公司损益表并列。\*Everpure 的季度截至 2026-08-02。Snowflake 和 MongoDB 承担云 COGS，且 SBC 差距较大。Everpure 承担硬件 COGS，SBC 差距较小，营运资本随库存波动。来源：公司新闻稿。[^sf-q2][^mdb-q2][^mdb-10k][^ep-q2]*

MongoDB 的这一季度展示了一个更成熟的按用量计费数据库的样貌。增速略低于 Snowflake，GAAP 与非 GAAP 差距更窄，且公司已实现 GAAP 盈利。自由现金流较一年前的 $69.9M 几乎翻倍。[^mdb-q2] 其留存 KPI 基于 ARR 且披露频率较低，因此无法依据公开数据与 Snowflake 进行同口径 NRR 比较。

**Everpure 视角：存储公司增加软件和数据服务后会有什么变化。** 存储公司的损益表建立在发货时确认的产品收入、随元器件（NAND）成本和产品结构变动的毛利率，以及随库存和递延收入波动的 FCF 之上。订阅业务（Evergreen 与存储即服务）已表现得像软件：经常性、以 ARR 计量，且毛利率高于产品。在过去的季度中，Everpure 的非 GAAP 订阅服务毛利率处于 70% 中段（mid-70s），而产品处于 60% 高段（high-60s）（媒体报道）。[^ep-seg] 基于公开信息，战略团队可能评估，增加数据管理或数据智能服务将从四个方面改变 KPI 组合。(1) 投资者会要求单独披露软件或数据服务 ARR，以及该业务线的留存率（NRR 和 GRR），仅有 Subscription ARR 是不够的。(2) 若软件为自管部署，毛利率会上升；若以承担云 COGS 的托管服务形式运行，则会下降，这与上文所述的无服务器取舍相同。(3) S&M 效率需要单独衡量，因为向数据团队销售软件与向基础设施采购方销售阵列是不同的销售模式。(4) SBC 占收入的比重很可能上升，因为软件人才市场以股权支付薪酬，这会扩大 GAAP 与非 GAAP 的差距。目前 Everpure 约 14 个百分点的差距，窄于 Snowflake 的约 32 和 MongoDB 的约 20。

> **存储桥接。** 存储厂商的订阅 ARR 与数据平台的 NRR 衡量的是不同的东西：ARR 是某一时点的年化合同价值，NRR 是一个固定群组支出的增长。Everpure 不公布 NRR。与之最接近的类比是订阅 ARR 增速（+20%）和 RPO 增速（+44%）。[^ep-q2] Evergreen 订阅的结构请参见配套的 *Everpure Tech Atlas*。

### KPI 速查卡

| KPI | 定义 | 公式 | 披露位置 | 陷阱 |
|---|---|---|---|---|
| NRR / NDR | 固定上年群组的支出增长 | 群组支出（第 2 年）÷ 群组支出（第 1 年） | 10-K"关键业务指标"、业绩新闻稿 | 各公司群组和窗口不同；滚动比率滞后；未经审计 |
| 净 ARR 扩张率（MongoDB） | 基于 ARR 的 NRR | 一年前客户的当前 ARR ÷ 一年前全部客户的 ARR | 10-K、不定期电话会评论 | 按用量计费的 ARR 是年化值；披露不规律 |
| 总收入留存率 | 不含扩张的 NRR | （上期支出 − 收缩 − 流失）÷ 上期支出 | 很少披露 | 被强劲的 NRR 掩盖；尽职调查时索要 |
| RPO | 已签约、未确认的收入 | 未履行履约义务之和 | 10-Q/10-K 收入附注（ASC 606） | 随大额交易波动；容量交易的确认时点取决于消耗 |
| cRPO | 12 个月内到期的 RPO | RPO × 预计 12 个月内确认的比例 | 10-Q 附注、部分新闻稿 | 基于历史消耗的估算；应与未来 12 个月收入比较，而非与 RPO 比较 |
| 开票额 | 开票金额 | 收入 + 递延收入变动 | 由报表推导；部分新闻稿 | 受开票时点和期限扭曲；对按用量计费模式用处较小 |
| 产品毛利率 | 核心平台的毛利率 | （产品收入 − 产品 COGS）÷ 产品收入 | 利润表、新闻稿 | GAAP vs 非 GAAP（SBC、摊销）；AI 和无服务器结构稀释 |
| 魔力数字 | S&M 效率 | 季度收入变动 × 4 ÷ 上季度 S&M | 由 10-Q 推导 | 天数；GAAP vs 非 GAAP S&M；单季度噪声大 |
| CAC 回收期 | 收回获客成本所需月数 | 12 ÷（魔力数字 × 毛利率） | 推导 | 继承魔力数字的全部噪声；忽略流失 |
| SBC 占收入百分比 | 以股权支付的成本强度 | SBC ÷ 收入 | 现金流量表、新闻稿调节表 | 被排除在非 GAAP 之外；需核查回购和稀释后股数增长 |
| GAAP vs 非 GAAP 营业利润率 | 含与不含 SBC 及其他项目的盈利能力 | 非 GAAP 加回 SBC、摊销及其他 | 新闻稿调节表 | 差距大小才是真正的信号；"其他"项目会逐渐膨胀 |
| FCF 利润率 / 调整后 FCF | 现金创造能力 | （经营现金流 − 资本开支 [− 资本化软件]）÷ 收入 | 新闻稿调节表 | 季度间有季节性；"调整后"定义各异；不含 SBC 成本 |
| 40 法则 | 增长与盈利的平衡 | 增速 % + 利润率 % | 部分公司自行披露 | 混用口径；季度 FCF；忽略 SBC |
| $1M+ 客户 / G2000 | 大客户渗透率 | 超过门槛的客户数（12 个月滚动收入） | 新闻稿、10-K | 门槛不同（$1M 12 个月滚动收入 vs $100K ARR） |

*图 36.7 — KPI 定义。"披露位置"一栏表明哪些数字经过审计（报表项目），哪些是公司自定义指标。SEC 2020 年的指引要求每个此类指标都有清晰的定义和一致的计算方法。[^sec-kpi]*

## 设计选择与权衡

公司会选择把哪些 KPI 放在显要位置，而这一选择本身就告诉你它们希望你关注什么。

| 选择 | 选项 A | 选项 B | 谁选什么 | 对较少被采用选项的最强版本论证 |
|---|---|---|---|---|
| 留存指标 | 基于收入的 NRR（Snowflake） | 基于 ARR 的扩张率（MongoDB） | 采用容量合同的按用量计费厂商倾向 A | ARR 具有前瞻性，可与按席位计费的 SaaS 比较 |
| 积压指标 | RPO/cRPO | 开票额 | 按用量计费与云：A；硬件与按席位计费 SaaS：B | 开票额与现金挂钩，更难通过长期合同美化 |
| 利润指标 | 非 GAAP 营业利润率 | GAAP 营业利润率 | 几乎所有成长型软件：A | GAAP 计入了由股东承担的 SBC |
| 40 法则所用利润率 | 调整后 FCF | 营业利润率或扣除 SBC 的 FCF | 大多数自行披露者：A | 扣除 SBC 的口径更接近股东盈余 |
| 大客户数 | 12 个月滚动收入 $1M+ | ARR $100K+ | Snowflake 选 A；MongoDB、Datadog 选 B | 较低门槛能更早捕捉中端市场的势头 |

*图 36.8 — 披露选择。公司偏好的选项通常是更好看的那个。这不是拒绝它的理由，但却是你自己重建另一个指标的理由。*

为非 GAAP 指标辩护的最有力理由是可比性。SBC 是非现金项目，其会计价值取决于授予时的股价，剔除它可以让股权结构不同的公司更易于比较。最有力的反驳是：稀释是永久的。股东关心的是每股价值，而一家从未实现 GAAP 盈利的公司，从未证明其单位经济能覆盖全部人工成本。

## 主要参与者

| 公司 | 重点强调的主要 KPI | 最新值（口径、日期） |
|---|---|---|
| Snowflake | NRR、产品收入、RPO、$1M+ 客户、G2000 | NRR 126%；RPO 约 $9.0B（Q2 FY2027）[^sf-q2] |
| MongoDB | Atlas 增速与占比、净 ARR 扩张率、$100K+ 客户 | Atlas +29%；≥$100K 客户 2,999 家（Q2 FY2027）[^mdb-q2] |
| Datadog | ARR $100K+ 客户、FCF | ≥$100K 客户约 4,720 家；FCF $279M（Q2 2026）[^r40] |
| Palantir | 自行披露的 40 法则、调整后 FCF | 155%（Q2 2026）[^pltr] |
| ServiceNow | cRPO、订阅收入增速、FCF 利润率 | cRPO $13.65B，+20.5%（Q3 2026）[^now] |
| Workday | 12 个月订阅积压 | $9.034B，+14.2%（Q2 FY2027）[^comps] |
| NetApp | 开票额、Public Cloud 收入 | 开票额 $2.06B，+36%（Q1 FY2027）[^ntap] |
| Everpure | 订阅 ARR、RPO、产品与订阅结构 | ARR $2.1B；RPO $4.1B（Q2 FY2027）[^ep-q2] |

*图 36.9 — 谁披露什么。每家公司都把自己看起来最强的 KPI 放在显要位置。跨公司比较意味着要从报表中重建一个共同指标。关于这些公司的估值倍数，见[第 37 章](ch37-public-comps-valuation.md)。*

## 历史与发展轨迹

```mermaid
timeline
    title 软件 KPI 的演进
    2005 : 魔力数字由后来的 Scale Venture Partners 提出
    2008 : 季度魔力数字公式在 SaaS 投资者中流行
    2015 : Brad Feld 推广 40 法则
    2020 : SEC 发布关于 MD&A 中 KPI 的指引
         : Snowflake IPO 让超过 150% 的 NRR 成为焦点
    2022 : Snowflake NRR 在 178% 见顶
    2023 : 消耗优化压低 NRR 与增速
    2025 : Snowflake NRR 稳定在 126% 附近
    2026 : AI 工作负载使增速重新加速并压低毛利率
```

*图 36.10 — KPI 的历史。这套语言是为按席位计费的 SaaS 构建的。按用量计费模式（NRR 作为群组流量、RPO 作为逐步消耗的容量），以及之后的 AI 工作负载（计算密集型 COGS），依次检验了每个指标背后的假设。*

魔力数字诞生于 2000 年代中期的风险投资实践，用作快速检验销售支出是否"奏效"的工具。[^scale] 40 法则随后于 2015 年出现，作为董事会层面平衡规模化阶段增长与利润的经验法则。[^feld] 两者都是为采用年度合同、收入确认大致线性的按席位订阅公司而设计的。2020 年 1 月，SEC 告知注册公司，MD&A 中的任何 KPI 都需要清晰的定义、说明其有用性的解释以及一致的计算方法，且变更需予以披露。[^sec-kpi] 这就是 NRR 定义如今出现在 10-K 中的原因。

按用量计费的时代对这套语言进行了压力测试。Snowflake 的 FY2021 10-K 显示 NRR 为 168%。FY2022 的 178% 是峰值，公司后来在群组调整后将其重述为 177%。[^sf-10k21][^fin-csv] 当客户在 2022–2023 年优化支出时，NRR 与增速同时下滑，表明按用量计费的收入没有合同底线。2025–2026 年阶段引入了新的张力。AI 工作负载提升了消耗和增速（Q2 FY2027 产品收入 +37%），但其计算成本更高，因此毛利率指引下调至 74%。[^fin-csv] 接下来要关注的 KPI 是单客户毛利额和每美元收入的 SBC，而不仅仅是表面增速。

## 关键数字

| 指标 | 数值 | 口径 | 来源 / 日期 |
|---|---|---|---|
| Snowflake 产品收入增速，Q2 FY2027 | +37%（约 $1.49B） | GAAP | 新闻稿，2026-09-02[^sf-q2] |
| Snowflake NRR | 126%（FY2022 峰值 178%） | 公司披露 KPI | 新闻稿；CSV[^sf-q2][^fin-csv] |
| Snowflake RPO / 12 个月内到期占比 | 约 $9.0B / 约 54% | GAAP 披露 | 10-Q，2026 年 7 月 31 日[^sf-10q] |
| Snowflake 产品毛利率 | GAAP 70.9% / 非 GAAP 74.7%；全年指引 74% | GAAP / 非 GAAP | 新闻稿[^sf-q2] |
| Snowflake GAAP vs 非 GAAP 营业利润率 | −17.0% vs 15.3% | GAAP / 非 GAAP | 新闻稿[^sf-q2] |
| Snowflake SBC 占收入百分比 | 约 27%（Q2 FY2027）；34%（FY2026） | GAAP；Q2 为媒体报道 | sec-api.io；10-K[^secapi][^sf-10k26] |
| Snowflake 魔力数字，Q2 FY2027 | 原始约 1.06 / 天数调整后约 0.72 | 估算 | 作者依据 10-Q 计算 |
| Snowflake $1M+ 客户 / G2000 | 828 / 829 | 公司披露 KPI | 新闻稿[^sf-q2][^pulse] |
| MongoDB 收入 / 非 GAAP 营业利润率 | $771.8M（+30%）/ 24% | GAAP / 非 GAAP | 新闻稿，2026-09-01[^mdb-q2] |
| MongoDB 净 ARR 扩张率 | 约 121%（2026 年 1 月 31 日）；Q2 FY2027 约 122%（媒体报道，Zacks） | 公司披露 KPI / 媒体报道 | FY2026 10-K[^mdb-10k]；`data/public_comps.csv`[^comps] |
| Everpure 非 GAAP 毛利率 / 营业利润率 | 69.9% / 19.4% | 非 GAAP | 新闻稿，2026-08-26[^ep-q2] |
| Everpure 订阅 ARR / RPO | $2.1B（+20%）/ $4.1B（+44%） | 公司披露 KPI / GAAP | 新闻稿[^ep-q2] |

## 对话手册

**向数据平台产品经理或产品财务负责人提出的三个问题**

1. "你们如何定义 NRR：用哪个群组、哪个窗口，是否包括经销商渠道的最终客户？" *好的回答*会说明群组纳入规则、该指标基于收入还是 ARR，以及滚动窗口如何使其平滑。如果对方主动提到总留存率，则更加分。
2. "RPO 中有多少预计在未来十二个月内确认？当前收入中有多少来自按需使用，而非从容量合同中扣减？" *好的回答*会给出 cRPO 对下一年收入的覆盖度，并解释结转条款。
3. "AI 工作负载如何改变产品毛利率？你们的定价是否保护了每 credit 的毛利额？" *好的回答*会区分毛利率百分比与毛利额，并指出成本驱动因素（GPU 或计算强度）。

**向工程师或 FinOps 架构师提出的三个问题**

1. "在你们的云账单中，一次典型查询的成本里计算、存储和出口流量各占多少？" *好的回答：*分析场景下计算占主导，存储占比很小。跨云共享时出口流量很重要。
2. "当你们把工作负载迁移到无服务器后，底层虚拟机的利用率会怎样？" *好的回答：*预热资源池和装箱调度提高了利用率，这就是无服务器能够保护毛利率的方式。
3. "你们把哪些引擎效率提升以降低 credit 消耗的形式让利给了客户？" *好的回答：*给出具体例子，并承认效率提升会短暂减少收入，之后弹性才会把收入拉回来。

**好的回答听起来是什么样的。** 先给定义再给数字，无需提醒就标注 GAAP 与非 GAAP，用毛利额和群组而非表面百分比来讨论问题。

**不要这样说**

- "Snowflake 的 NRR 是 126%，所以比 MongoDB 的 121% 好。" *群组、单位和窗口都不同。两者不能直接比较。*
- "RPO 就是明年的收入。" *只有 cRPO 部分（Snowflake 约 54%）预计在十二个月内确认，而且容量可以结转。*
- "Snowflake 是盈利的。" *按非 GAAP 口径是的（15.3%）。其 Q2 FY2027 的 GAAP 营业利润率为 −17.0%。*
- "SBC 是非现金项目，可以忽略。" *它以稀释的方式支付，而用于抵消稀释的回购是真金白银。*
- "他们通过了 40 法则。" *要说明用的是哪个增速、哪个利润率、哪个期间。同一家公司可以得 20 分，也可以得 58 分。*
- "开票额下降了，所以需求疲软。" *对按用量计费模式并非如此，开票额由开票时点和合同期限驱动。*

## 深入阅读

- 将 Snowflake FY2026 10-K 与 MongoDB FY2026 10-K 中的"Key Business Metrics（关键业务指标）"部分并排阅读，记下每一处定义差异。[^sf-10k26][^mdb-10k]
- 以四个季度滚动口径重建魔力数字以消除天数效应，并与图 36.5 中的环比数字进行比较。
- 关于估值（市场如何将这些 KPI 资本化为 EV/未来 12 个月收入倍数），请继续阅读[第 37 章](ch37-public-comps-valuation.md)。公司背景请参见[第 26 章 Snowflake](../04-company-deep-dives/ch26-snowflake.md)和[第 29 章](../04-company-deep-dives/ch29-operational-database-vendors.md)。

> **深入（L3）。** 要重建 cRPO 覆盖度，从收入附注中取 RPO，乘以披露的未来十二个月确认比例，再除以未来十二个月产品收入指引。以 Snowflake 为例：约 $9.0B × 54% ≈ $4.86B，÷ FY2027 产品收入指引 $6.07B ≈ 80%（作者估算；该指引覆盖的是财年，而非严格的未来十二个月）。未覆盖的部分必须来自按需消耗、新合同和超额用量，这正是预测风险所在。

## 关键术语

- [净收入留存率（net revenue retention）](../glossary.md#net-revenue-retention) — 去年客户群组今年的支出 ÷ 其一年前的支出。
- [总收入留存率（gross revenue retention）](../glossary.md#gross-revenue-retention) — 扣除收缩和流失后、不含扩张的上年支出留存。
- [净 ARR 扩张率（net ARR expansion rate）](../glossary.md#net-arr-expansion-rate) — MongoDB 基于 ARR 的 NRR 版本。
- [群组分析（cohort analysis）](../glossary.md#cohort-analysis) — 跟踪一组固定客户随时间的变化，以区分存量客户增长与新客户增长。
- [剩余履约义务（remaining performance obligations）](../glossary.md#remaining-performance-obligations) — 已签约但尚未确认的收入（ASC 606 披露）。
- [当期剩余履约义务（current remaining performance obligations）](../glossary.md#current-remaining-performance-obligations) — RPO 中预计在十二个月内确认的部分。
- [容量合同（capacity contract）](../glossary.md#capacity-contract) — 预付或承诺的消耗 credit 额度，随客户使用服务而扣减。
- [开票额（billings）](../glossary.md#billings) — 收入加递延收入变动；即一个期间内开出的发票金额。
- [订单出货比（book-to-bill）](../glossary.md#book-to-bill) — 收到的订单 ÷ 出货确认的收入；高于 1 意味着积压在增长。
- [产品毛利率（product gross margin）](../glossary.md#product-gross-margin) — 平台（产品）收入的毛利率，不含专业服务。
- [云 COGS（cloud COGS）](../glossary.md#cloud-cogs) — 计入云厂商收入成本的超大规模云厂商计算、存储和网络成本。
- [魔力数字（magic number）](../glossary.md#magic-number) — 每一美元上期销售与营销支出带来的年化新增收入。
- [CAC 回收期（CAC payback）](../glossary.md#cac-payback) — 收回获客成本所需的毛利月数。
- [股权激励费用（stock-based compensation）](../glossary.md#stock-based-compensation) — 以股权支付的员工薪酬；GAAP 下计为费用，非 GAAP 下加回。
- [非 GAAP 营业利润率（non-GAAP operating margin）](../glossary.md#non-gaap-operating-margin) — 剔除 SBC、收购无形资产摊销及其他项目后的营业利润率。
- [自由现金流利润率（free cash flow margin）](../glossary.md#free-cash-flow-margin) — （经营现金流 − 资本开支）÷ 收入。
- [调整后自由现金流（adjusted free cash flow）](../glossary.md#adjusted-free-cash-flow) — 加回公司特定项目（如员工股权相关工资税）后的 FCF。
- [40 法则（Rule of 40）](../glossary.md#rule-of-40) — 收入增速 % 加利润率 % 应至少为 40 的经验法则。
- [年度经常性收入（annual recurring revenue）](../glossary.md#annual-recurring-revenue) — 某一时点经常性合同的年化价值。
- [收入年化运行率（revenue run-rate）](../glossary.md#revenue-run-rate) — 当期收入的年化值；并非经审计的年度收入。

## 资料来源

[^sf-q2]: Snowflake Inc., "Snowflake Reports Financial Results for the Second Quarter of Fiscal 2027," https://www.nasdaq.com/press-release/snowflake-reports-financial-results-second-quarter-fiscal-2027-2026-09-02（另见 Business Wire, https://secure.businesswire.com/news/home/20260902386235/en/Snowflake-Reports-Financial-Results-for-the-Second-Quarter-of-Fiscal-2027），发布 2026-09-02；检索 2026-11-01。数值依据 `data/company_financials.csv`；GAAP 营业亏损约 $263M、非 GAAP 营业利润约 $237M 依据新闻稿的搜索摘录。FY2027 = 2026 年 2 月–2027 年 1 月。
[^sf-10q]: Snowflake Inc., "Form 10-Q for the quarter ended July 31, 2026," https://www.sec.gov/Archives/edgar/data/0001640147/000164014726000037/snow-20260731.htm，提交于 2026-09 [VERIFY: 确切提交日期]；检索 2026-11-01，经由搜索摘录（S&M $611.6M vs $502.0M；六个月 S&M 约 $1.20B；RPO 约 $9.0B，其中约 54% 预计在 12 个月内确认；六个月内以约 $300M 回购约 1.7M 股）。
[^sf-q1]: Snowflake Inc., "Snowflake Reports Financial Results for the First Quarter of Fiscal 2027," https://investors.snowflake.com/news/news-details/2026/Snowflake-Reports-Financial-Results-for-the-First-Quarter-of-Fiscal-2027/default.aspx，发布 2026-05-27；检索 2026-11-01（总收入约 $1.39B；产品收入 $1,334.3M；GAAP 营业亏损 $326.2M）。
[^sf-10k26]: Snowflake Inc., "Form 10-K for the fiscal year ended January 31, 2026," https://www.sec.gov/Archives/edgar/data/1640147/000164014726000008/snow-20260131.htm，提交于 2026-03 [VERIFY: 确切提交日期]；检索 2026-11-01（NRR 定义；FY2026 以加权平均 $177.37 回购约 4.9M 股；SBC 依据 `data/company_financials.csv`）。
[^sf-10k21]: Snowflake Inc., "Form 10-K for the fiscal year ended January 31, 2021," https://www.sec.gov/Archives/edgar/data/1640147/000164014721000073/snow-20210131.htm，提交于 2021-03；检索 2026-11-01（最初的 NRR 群组定义；NRR 168%）。之后的 10-K（FY2023，https://www.sec.gov/Archives/edgar/data/1640147/000164014723000030/snow-20230131.htm）显示经调整后 FY2022 NRR 为 177%。
[^fin-csv]: AI Data Atlas 数据集 `data/company_financials.csv`（Snowflake FY2020–Q2 FY2027 产品收入、NRR、RPO、$1M+ 客户、利润率、SBC；MongoDB Atlas 占比；各行来源：Snowflake 10-K 及业绩新闻稿，包括 https://www.sec.gov/Archives/edgar/data/1640147/000162828026011631/fy2026q4earnings.htm，发布 2026-02-25）；检索 2026-11-01。
[^secapi]: sec-api.io, "Snowflake (SNOW) stock after the $3.75bn convertible notes: Q2 FY2027 product revenue, RPO, insider sales and scenarios to FY2030," https://sec-api.io/insights/snowflake-snow-stock-after-the-3-75bn-convertible-notes-q2-fy2027-product-revenue-rpo-insider-sales-and-scenarios-to-fy2030，发布 2026-10-10；检索 2026-11-01。媒体报道（引用 10-Q 的二手分析）：SBC $424M，一年前为 $404M。
[^pulse]: Pulse 2.0, "Snowflake: Q2 Fiscal 2027 Revenue Rises 35% To $1.55 Billion As Product Revenue Guidance Is Raised," https://pulse2.com/snowflake-q2-fiscal-2027-revenue-rises-35-to-1-55-billion-as-product-revenue-guidance-is-raised/，发布 2026-09；检索 2026-11-01（交叉核对收入、RPO 及福布斯全球 2000 强客户数 829）。
[^mdb-q2]: MongoDB, Inc., "MongoDB, Inc. Announces Second Quarter Fiscal 2027 Financial Results," https://investors.mongodb.com/news-releases/news-release-details/mongodb-inc-announces-second-quarter-fiscal-2027-financial，发布 2026-09-01；检索 2026-11-01（收入 $771.8M；GAAP 营业利润 $28.4M；非 GAAP $185.9M，24%；FCF $137.6M，一年前为 $69.9M；客户 70,600+；ARR ≥$100K 客户 2,999 家）。FY2027 = 2026 年 2 月–2027 年 1 月。
[^mdb-10k]: MongoDB, Inc., "Form 10-K for the fiscal year ended January 31, 2026," https://www.sec.gov/Archives/edgar/data/1441816/000162828026016799/mdb-20260131.htm，提交于 2026-03 [VERIFY: 确切提交日期]；检索 2026-11-01（净 ARR 扩张率约 121% 及其定义）。
[^ep-q2]: Everpure, Inc., "Everpure Announces Second Quarter Fiscal 2027 Financial Results," https://investor.everpuredata.com/news-and-events/press-releases/press-release-details/2026/Everpure-Announces-Second-Quarter-Fiscal-2027-Financial-Results/default.aspx，发布 2026-08-26；检索 2026-11-01（产品 $687M；订阅服务 $499M；GAAP 毛利率 68.4%；非 GAAP 毛利率 69.9%；GAAP 营业利润 $63M；非 GAAP 营业利润率 19.4%；FCF −$238M；FY2027 FCF 指引 $600–800M；订阅 ARR $2.1B；RPO $4.1B；回购约 $69M）。季度截至 2026-08-02。
[^ep-seg]: Pure Storage (now Everpure), "Q3 FY26 Earnings Slide Deck," https://s21.q4cdn.com/687136699/files/doc_financials/2026/q3/Q3FY26-Earnings-Slide-Deck-FINAL.pdf，发布 2025-12 [VERIFY: 日期]；检索 2026-11-01。分部毛利率（Q2 FY2026 非 GAAP 产品约 68%、订阅服务约 76.5%；Q3 FY2026 产品 72.9%、订阅 75.5%）来自对公司材料的第三方摘要。媒体报道 [VERIFY: 与 10-Q 核对]。
[^comps]: AI Data Atlas 数据集 `data/public_comps.csv`（Oracle RPO $664B 及 FY2027 指引；Workday 12 个月订阅积压 $9.034B；MongoDB Q2 FY2027 净 ARR 扩张率 122%，媒体报道，经由 Zacks/Nasdaq），各行来源（stockanalysis.com 及公司新闻稿），截至 2026-10-16 至 2026-10-30；检索 2026-11-01。
[^r40]: AI Data Atlas 数据集 `data/ch36_rule_of_40.csv`，汇编自：Datadog Q2 2026 新闻稿（SEC 8-K Ex. 99.1）, https://www.sec.gov/Archives/edgar/data/0001561550/000162828026053829/ex-991x20260630x8k.htm，2026-08-06；CSV 中列出的 Workday、Elastic、GitLab、Rubrik、Nutanix 和 Everpure 新闻稿；检索 2026-11-01。
[^pltr]: Palantir Technologies Inc., "Q2 2026 results," Form 8-K Ex. 99.1, https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm，发布 2026-08-03（日期依据第 37 章引用）；检索 2026-11-01（收入 $1.935B，+93%；调整后 FCF $1.220B，63%；40 法则得分 155%）。
[^now]: ServiceNow, Inc., "ServiceNow Reports Third Quarter 2026 Financial Results," Form 8-K, https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000092/erq3fy26.htm，发布 2026-10 [VERIFY: 具体日期]；检索 2026-11-01（总收入 $4,106M，+20.5%；cRPO $13.65B；FY2026 FCF 利润率指引上调至 36%）。
[^ntap]: NetApp, Inc., "NetApp Reports First Quarter of Fiscal Year 2027 Results," https://netapp.com/newsroom/press-releases/news-rel-20260902-results-607632，发布 2026-09-02；检索 2026-11-01（收入 $2,025M，+30%；开票额 $2.06B，+36%；FCF $401M；该季度多一周，媒体报道）。NetApp 财年截至 4 月最后一个星期五。
[^feld]: Brad Feld, "The Rule of 40% For a Healthy SaaS Company," https://feld.com/archives/2015/02/rule-40-healthy-saas-company.html，发布 2015-02-02；检索 2026-11-01（经由二手摘要，例如 Tomasz Tunguz, https://tomtunguz.com/rule-of-40/）。
[^scale]: Scale Venture Partners, "A History of the Magic Number," https://www.scalevp.com/blog/a-history-of-the-magic-number，发布 [VERIFY: 日期]；检索 2026-11-01（该术语由 Rory O'Driscoll 于 2005 年提出；约 0.7 为健康基准）。
[^sec-kpi]: U.S. Securities and Exchange Commission, "Commission Guidance on Management's Discussion and Analysis of Financial Condition and Results of Operations," Release No. 33-10751, https://www.sec.gov/rules/final/33-10751.htm，发布 2020-01-30（2020-02-25 生效）；检索 2026-11-01。
