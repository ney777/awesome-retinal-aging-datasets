# 眼底影像、衰老与全身疾病研究选题指南

2026 年 11 月 3 日核验。资源目录包含 479 条记录。451 条来自 EyeDataHub v0.7.0，另有 28 条扩展记录。49 条经过项目级来源复核，其中 21 条是对基线资源的补充或订正。使用一条记录时，先确定需要的输入是原始像素、影像派生测量还是阅片分级，再查看该终点的专题等级和访问条件。[离线检索](index.html) · [结构化主表](output/master.csv) · [三方向排名](output/rankings.csv)

## 三个方向如何启动

| 研究问题 | 优先推动的科学资源 | 当前能启动的工作 | 决定能否验证的字段 |
|---|---|---|---|
| 同一次眼底检查能多准确地预测实足年龄？重复检查的误差有多大？ | UK Biobank、SCONe 可把年龄与后续健康记录关联。完整 EyePACS 研究队列可分析重复访视，需要单独向数据方申请。 | 在 China-Fundus-CIMT 做患者级单次年龄基准，在 GRAPE 检验多次访视，在 MCFI 做同眼重测。PAPILA 可提供独立采集的双眼域。 | 患者 ID、左右眼、同次检查、真正的年龄字段、日期间隔、质量、族群和设备。 |
| 基线眼底能否补充传统卒中风险模型？眼底对 MRI 病灶有无增量信息？ | UK Biobank、ARIC、MESA、CHS 有已发表配对研究。上海 SDPP 有分开的静默脑梗死 MRI 样本与随访卒中样本。Rhineland 支持申请脑 MRI 和视网膜 OCT 影像。 | 此次核验没有找到同时满足近期准入门槛、原始眼底像素和新发卒中终点的队列。可先用公开 NHANES 分级做表格分析，用 China-Fundus-CIMT 检验连续颈动脉指标。 | 真正事件日期或距索引日时间、亚型、既往卒中、死亡和删失；MRI 与眼底时间差、病灶定义和判读方法。 |
| 眼底能否识别 AD 相关差异，或预测从认知障碍到痴呆的转归？ | UK Biobank 已有 OCT 与新发 AD/FTD 分析。新加坡记忆门诊研究有明确的基线认知风险集。SCONe 适合申请验证日常诊疗编码；AlzEye 限原团队分析个体系统疾病资料。 | TREND2 可验证 AD 标记与眼底文件的连接；Dryad 功能 OCT 可做早发 AD 病例对照分析。两者都适合小样本方法核验。 | AD 诊断标准、认知测试工具、基线无痴呆、事件定义、随访窗口、独立人数；代码日期不能直接替代起病日期。 |

科学榜和近期榜保留五维分值、结局名称、作为质量依据的人数及其口径。同分并列。Retinal Aging 的近期榜中 GRAPE、China-Fundus-CIMT 与 MCFI 靠前，三者分别适合纵向青光眼人群、单次年龄回归和短间隔重测。神经退行性疾病的近期榜只纳入两个小样本项目。高分代表适配当前问题；判定能否用于某个实验仍须读取该行的终点与分母。[逐行分数及证据](output/rankings.csv) · [评分细则](METHODS.md)

## 实验一　年龄预测与重测误差

**横断面年龄基准。** China-Fundus-CIMT 的 2,903 名住院患者均有双眼照片，共 5,806 张。按 JSON 患者主键读取左右眼文件名，目标取 `True_age`；另一个 `age` 已经过标准化。按原发布划分训练和验证，先报按患者汇总的 MAE、误差随年龄变化和年龄段校准，再比较单眼与双眼汇总。年龄回归不得将 `True_age`、标准化年龄或从年龄直接构造的变量作为输入。该样本来自内分泌住院人群，发布表没有足够的糖尿病或高血压病史来校正所有共病。Figshare v1 实际标注 CC0，与基线索引记录不同。[字典 Table 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC11968951/) · [Figshare v1](https://api.figshare.com/v2/articles/27907056/versions/1)

**纵向与重测。** GRAPE 有 144 人、263 眼、1,115 次访视和 631 张彩照；一次访视可以没有可用彩照。按受试者编号、眼别、访视号连接，后续年龄需由基线年龄和访问间隔推导。孟加拉国 MCFI 有 37 人、84 次会话、442 张图；全部 37 人均有同眼跨日影像，首末检查跨度中位数仅 35 天，11 人达到 180 天，7 人达到一年。将两眼、同一患者所有日期、同次连拍放在同一侧；用短间隔重复检查估算测量误差，另报长间隔子集及其不确定性。用这两个队列拟合的时间斜率不足以确立个体生物衰老速度。[GRAPE 数据说明](https://www.nature.com/articles/s41597-023-02424-4) · [MCFI 原始发布](https://data.mendeley.com/datasets/stskv6zjt9/1)

**外部域与效标。** PAPILA v2 的 244 个患者在左右眼表中的年龄一致，并能逐一匹配 488 个图像文件；年龄 15–90 岁。FDR26 的 3,000 张摩洛哥眼底图均有 20–85 岁的整数年龄，工作簿只有图像 ID。文件名前缀恰好形成 1,918 组，但尚无作者命名协议确认这些前缀就是患者。冻结模型后在 PAPILA 做患者级外部验证；将 FDR26 的身份键核验列为下一步。要研究“生物年龄”，需要另用独立人群中的健康事件、死亡或衰弱效标，并比较实足年龄和临床风险因子模型；横断面年龄误差本身只衡量实足年龄预测。[PAPILA v2](https://figshare.com/articles/dataset/PAPILA/14798004/2) · [FDR26 元数据](https://zenodo.org/records/23101200) · [EyePACS 和 UKB 的 eyeAge 研究及访问说明](https://elifesciences.org/articles/82364)

## 实验二　卒中、脑 MRI 与分级筛查

**将风险终点与参考标准分开。** UKB 一项工作在基线无卒中的 35,304 人中观察到 282 次卒中。应比较年龄、性别、血压等临床基准与加入眼底后的模型，预先定义首发缺血性卒中、出血性卒中及其他死亡竞争风险，报告随访窗、校准、时间依赖 AUC 和事件数。另一问题是当前是否存在 MRI 病灶，适合评价敏感度、特异度及在给定转诊容量下的阳性预测值。上海 SDPP 的 782 人有供静默脑梗死判定的 MRI，另有 29,160 人进入无 MRI 的纵向卒中子集；不能给后者填入伪造的 MRI 阴性标签。[UKB 卒中分析](https://pubmed.ncbi.nlm.nih.gov/36447293/) · [SDPP 组别、参考标准与访问条件](https://pmc.ncbi.nlm.nih.gov/articles/PMC12623247/)

**选择真正含相应病灶的子集。** ARIC 一项眼底与脑 MRI 研究有 1,684 人。LBC1936 的双眼与脑 MRI 分析有 603 人，另一个 Mild Stroke Study 的 155 人属于不同队列。Rhineland 有 3,395 人同时完成 MRI 和 SD-OCT，质控后的主分析为 2,872 人；该研究的结构和弥散指标不能直接标成 WMH、腔隙或微出血。预先规定同人检查允许的最大间隔、WMH 体积或分级、病灶读取方法、眼科共病处理和患者级置信区间。报告眼底检查人数、MRI 人数、同人交集以及最终病例数。[ARIC 配对研究](https://pubmed.ncbi.nlm.nih.gov/12090864/) · [LBC1936 与 Mild Stroke Study 分组](https://www.nature.com/articles/s41598-019-42534-x) · [Rhineland 方法与质控](https://pmc.ncbi.nlm.nih.gov/articles/PMC8854401/)

**短期可复现的替代实验。** NHANES 2005–2008 可按 `SEQN` 对接 OPXRET 阅片分级、年龄、自报既往卒中和相应死亡随访文件；两调查周期须按抽样设计、权重和分层处理。可以估计阅片体征与既往卒中或死亡之间的关联。该开放路线未证实提供可训练 CNN 的原始眼底 TIFF。China-Fundus-CIMT 提供原始眼底和同期超声 CIMT，适合比较加入眼底后的 CIMT 估计误差；该发布没有卒中事件日期。[CDC 阅片文件与调查说明](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/OPXRET_D.htm) · [China-Fundus-CIMT 发布字典](https://pmc.ncbi.nlm.nih.gov/articles/PMC11968951/)

## 实验三　认知、痴呆与其他神经疾病

**把病例对照当作流程验证。** TREND2 的 28 个 TIFF 文件标识全部与临床表中的 ID-eye 匹配，其中 7 个标记 AD、18 个标记高血压、8 个标记 2 型糖尿病。独立参与者数及逐人的实足年龄未证实。Dryad 功能 OCT 的早发 AD 对照实验为 14 对 14，公开年龄以区间表示；实验内光暗刺激重复不构成长程随访。先按患者和采集条件复核特征差异，保留全部排除理由；双眼、多层扫描和重复刺激不能产生额外患者。如此小的样本不宜给出可推广的临床诊断精度。[TREND2 数据与临床表](https://zenodo.org/records/7678656) · [Dryad 功能 OCT 及实验分组](https://datadryad.org/dataset/doi:10.5061/dryad.msbcc2ftc)

**把转归分析限定到真正的风险人群。** 新加坡两个记忆门诊的 491 人用于认知下降分析，212 名基线已有认知功能受损但尚无痴呆的参与者构成新发痴呆分析的风险集。这一队列与人群抽样的 SEED/EDIS 应分别记录。UKB 的另一项研究在 30,573 人中分析基线 OCT 与新发痴呆；其脑 MRI 分析使用更小的子集。纵向实验宜固定首次合格眼底日期，把后续诊断、既往诊断和临床评分分开，并按年龄、就诊来源、眼病与影像质量分析选择偏倚。[新加坡记忆门诊研究](https://doi.org/10.1093/braincomms/fcac212) · [UKB OCT 与痴呆研究](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2024.1513302/full)

**编码病例和原始影像要分别核验。** SCONe 早期已关联样本报告 2,495 个卒中编码病例、1,630 个痴呆编码病例、309 个 AD 编码病例及 288 个 PD 编码病例，组别可重叠。后期交付的 131,678 人不能用作每个疾病的实际影像分母；原始数据在苏格兰 National Safe Haven 内使用。AlzEye 有研究内个体级配对，但按队列协议只有 AlzEye 研究团队可以直接分析个体系统疾病资料。两项 PD 的 Figshare 发布分别只有组汇总或个体派生厚度表；ROSE-1 来源研究含 AD 病例，尚无可供本项目验证的逐图 AD 标签映射。JHU 的 MS 资源则确有 35 人的 OCT 和 MS/对照分组，但只有 26 人能唯一连接年龄，应排除重复 ID 的年龄匹配。[SCONe 描述与 Table 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC12083377/) · [AlzEye 数据协议](https://doi.org/10.1136/bmjopen-2021-058552) · [PD 个体测量发布](https://doi.org/10.26188/24138420.v2) · [ROSE](https://imed.nimte.ac.cn/dataofrose.html) · [JHU OCT](https://iacl.ece.jhu.edu/index.php/OCT_Data)

## 四组种子资源的访问判断

| 资源 | 已核实的可用内容 | 需要解决的获取问题 |
|---|---|---|
| UK Biobank | Showcase 21015/21016 是左右眼 CFP，21017/21018 为 OCT 切片。已有同人健康记录和影像分析。 | 截至本次核验，官网暂停新申请，预计 2026 年末恢复，未给出确定开放日。获批团队按许可字段在 RAP 使用，另有算力与存储费用。[影像目录](https://biobank.ndph.ox.ac.uk/ukb/label.cgi?id=725) · [准入状态](https://www.ukbiobank.ac.uk/use-our-data/apply-for-access/) |
| NHANES | NHANES III 与 2005–2008 均有视网膜检查和人级关联证据；后者公开 XPT 分级，两者为不同调查设计。 | 不可把其他周期的认知电池拼到旧周期眼底参与者。原始像素交付待证。[CDC 眼底文档](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/OPXRET_D.htm) |
| BRSET、mBRSET、ODIR | BRSET 1.0.2 为 16,266 张/8,524 人，有年龄缺失；mBRSET 为 5,164 张/1,291 人。ODIR 主办方记载 5,000 名患者，基线索引的 8,000 患者说法保留在原始快照中。 | BRSET 系列需 PhysioNet 认证、培训与 DUA。ODIR 项目说明支持年龄和双眼，复用条款仍待核。衍生 embedding 与增强版不能充当独立外测。[BRSET](https://physionet.org/content/brazilian-ophthalmological/1.0.2/) · [mBRSET](https://physionet.org/content/mbrset/1.0/) · [ODIR 主办方](https://odir2019.grand-challenge.org/dataset/) |
| AREDS / AREDS2 | AREDS 可经映射表连接 F2 照片。AREDS2 v3 的 4,203 名入组者中 4,201 名有映射到眼部 DICOM；512,713 个唯一文件名包括标注/迁移版本和不同成像内容。SAD 卒中裁定表仅 137 人，最终眼底×终点交集未知。 | AREDS2 的 WGS 1,363 人子集中有 488 人也参加过 AREDS。申请需核实 dbGaP 用途组、适格机构与所需临床表。NIH 现行通知限制位于中国（含香港、澳门）等列明地区的机构取得 NIH 受控库及其关联数据；此限制不应外推到 NHANES 的公开表。[AREDS2 v3 说明](https://ftp.ncbi.nlm.nih.gov/dbgap/studies/phs002015/phs002015.v3.p1/release_notes) · [AREDS2 研究及用途组](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs002015.v3.p1) · [NIH 通知](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-083.html) |

## 多中心与可信协作

先为每个可用项目生成许可范围内的本地清单，保留项目别名、原始提供方、数据版本、患者键、眼别、访视、中心、设备、分级标准和排除原因。同一提供方的增强图、掩膜、临床文本或 embedding 与原照片可共用患者，要在划分前沿关系表排查。公开证据未确认的跨库重合应标记 `Unknown`；不得以“两个仓库名”宣称独立验证。[基线证据边](output/relationships.csv) · [补充家族与重叠记录](output/extensions_relationships.csv)

跨设备实验可选 GRAPE 的三种相机，或用 BRSET 与手机 mBRSET 比较设备和人群变化，但设备域、医院域、地理域和患者独立性分别核实。留出整个中心或设备后，仅在源中心调参、校准并选融合权重。统一报告各中心结果和最差中心表现，置信区间按患者重采样；无法取得真实站点 ID 时，注明只能评价按数据来源划分的域迁移。受控队列是否允许模型进域、梯度交换或导出参数，应在获取许可后确认。本库只完成资源核验和设计，不包含模型训练、数据申请或临床验证结果。[GRAPE 数据说明](https://www.nature.com/articles/s41597-023-02424-4) · [SCONe 数据治理](https://clinical-sciences.ed.ac.uk/ophthalmology/scone/about-scone)
