# The Maastricht Study

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

正式目录、申请入口；两项研究核实同人视网膜结构/血管与全脑指标。

当前核验的影像与模态范围 — Fundus \| OCT \| brain MRI

Image availability — Fundus/OCT pixels collected; study data request portal does not promise raw pixel export; specify raw images separately.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | ext-maastricht-study |
| Name / 名称 | The Maastricht Study |
| Acronym / 缩写 | Unknown |
| Official resource | [https://www.demaastrichtstudie.nl/research/data-guidelines](https://www.demaastrichtstudie.nl/research/data-guidelines) |
| Country or region / 国家地区 | Netherlands |
| Institution / 机构 | Maastricht University / Maastricht UMC+ |
| Reported year / 年份口径 | 2023 |
| Publication date | Unknown |
| Date scope | Unknown |
| Date evidence | Unknown |
| Date reviewed | Unknown |
| Original citation | van der Heide FCT et al. Thinner inner retinal layers are associated with lower cognitive performance, lower brain volume, and altered white matter network structure. Alzheimers Dement. 2024 (online 2023). |
| Publication DOI | [10.1002/alz.13442](https://doi.org/10.1002/alz.13442) |
| Dataset DOI | Unknown |
| Import origin | Extension |
| Original EyeDataHub ID | Unknown |
| Dataset family | The Maastricht Study |
| Family or derivative relation | Multiple publications and partial visits/subsets from one parent study. |
| Independence / overlap | Patient overlap unverified |
| Upstream family ID | Unknown |
| Upstream resource role | Unknown |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 2 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | Unknown |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | Fundus \| OCT \| brain MRI |
| Images / 图像数及口径 | Unknown |
| Participants / 参与者数及口径 | 3,436 in OCT/cognition analysis; MRI only a subset. Separate fundus/brain white matter analysis includes 4,010; bilateral caliber measurements available in 54.7% of that analysis. |
| Eyes / 眼别 | Fundus photos both eyes; before Nov 2013 caliber often one eye. |
| Device / 设备 | Nidek AFC-230 45°; 3T Siemens Prisma-fit for MRI. |
| Resolution / 分辨率 | Unknown |
| Quality / 质量控制 | Unknown |
| Multiple visits / 多时点 | Unknown |
| Multiple modalities / 多模态 | Yes |
| Multiple centers / 多中心 | Unknown |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Application |
| Access or application route | [https://www.demaastrichtstudie.nl/research/data-guidelines](https://www.demaastrichtstudie.nl/research/data-guidelines) |
| Image files / 影像文件 | Fundus/OCT pixels collected; study data request portal does not promise raw pixel export; specify raw images separately. |
| Individual labels / 个体标签 | Research plan reviewed; published analyses use cognitive scores, brain morphometry and metabolic covariates. |
| Data license / 数据许可 | Unknown |
| Research use / 科研条件 | Formal proposal through portal; external researchers encouraged to work with management member/domain expert. |
| Commercial use / 商业用途 | Unknown |
| Terms scope | Unknown |
| Terms evidence | Unknown |
| Upstream route review date | Unknown |
| Upstream acquisition support | Unknown |
| Upstream access friction | Unknown |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | OCT thickness paired with global cognition; MRI introduced Dec 2013, subset only. Fundus caliber vs 3T connectivity separate. Request intersected denominator and exam dates. |
| Strengths / 主要优点 | 正式目录、申请入口；两项研究核实同人视网膜结构/血管与全脑指标。 |
| Limitations / 关键缺陷 | 糖尿病超采样；MRI 非全体；横断面认知评分不能替代 AD 诊断。 |
| Suggested experiments / 建议实验 | 按糖代谢状态分层，评估 OCT 层厚与认知评分、MRI 灰白质体积，并在分析前规定两次采集允许的时间差。 |
| Retinal Aging suitability | A: 年龄、OCT 个体配对。 \| Pixel gate: Fundus/OCT pixels collected; study data request portal does not promise raw pixel export; specify raw images separately. |
| Stroke / CSVD suitability | C: 子集已配对视网膜、脑 MRI。 \| Pixel gate: Fundus/OCT pixels collected; study data request portal does not promise raw pixel export; specify raw images separately. |
| AD / Dementia suitability | D: 多域认知评分；无 AD 病例依据。 \| Pixel gate: Fundus/OCT pixels collected; study data request portal does not promise raw pixel export; specify raw images separately. |
| Multicenter model suitability | Unknown |
| Screening rationale / 筛查理由 | 年龄、OCT 个体配对。 \| Pixel gate: Fundus/OCT pixels collected; study data request portal does not promise raw pixel export; specify raw images separately. \| 子集已配对视网膜、脑 MRI。 \| Pixel gate: Fundus/OCT pixels collected; study data request portal does not promise raw pixel export; specify raw images separately. \| 多域认知评分；无 AD 病例依据。 \| Pixel gate: Fundus/OCT pixels collected; study data request portal does not promise raw pixel export; specify raw images separately. \| 糖代谢状态及眼底血管测量。 \| Pixel gate: Fundus/OCT pixels collected; study data request portal does not promise raw pixel export; specify raw images separately. |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 2 | Tier 1 | 年龄、OCT 个体配对。 \| Pixel gate: Fundus/OCT pixels collected; study data request portal does not promise raw pixel export; specify raw images separately. | [s1](#evidence-1) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Tier 2 | Tier 1 | 子集已配对视网膜、脑 MRI。 \| Pixel gate: Fundus/OCT pixels collected; study data request portal does not promise raw pixel export; specify raw images separately. | [s2](#evidence-2) |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Tier 2 | Tier 1 | 多域认知评分；无 AD 病例依据。 \| Pixel gate: Fundus/OCT pixels collected; study data request portal does not promise raw pixel export; specify raw images separately. | [s1](#evidence-1) |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Tier 2 | Tier 1 | 糖代谢状态及眼底血管测量。 \| Pixel gate: Fundus/OCT pixels collected; study data request portal does not promise raw pixel export; specify raw images separately. | [s5](#evidence-5) |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Unknown | Unknown | No topic-specific finding | Unknown |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | 连续年龄 | [s1](#evidence-1) |
| Sex / 性别 | Confirmed | 个体协变量 | [s1](#evidence-1) |
| Hypertension / 高血压 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Diabetes / 糖尿病 | Confirmed | 糖耐量及糖尿病状态 | [s5](#evidence-5) |
| Cardiovascular disease / 心血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Stroke type / 卒中分型 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Stroke timing / 卒中事件时间 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Brain MRI / 脑 MRI | Confirmed | 体积及白质网络结构 | [s1](#evidence-1) |
| CSVD / 脑小血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Alzheimer’s disease / 阿尔茨海默病 | Uncertain | 认知评分非 AD 病例标签 | [s1](#evidence-1) |
| Dementia / 痴呆 | Uncertain | 该研究未确认痴呆事件 | [s1](#evidence-1) |
| Cognition / 认知功能 | Confirmed | global cognitive performance | [s1](#evidence-1) |
| Parkinson’s disease / 帕金森病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Frailty / 衰弱 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Health status / 健康状态 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Mortality / 死亡结局 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Follow-up / 纵向随访 | Uncertain | 队列前瞻，引用的眼脑分析横断面，未证实可追踪该分析集神经结局 | [s5](#evidence-5) |

## Counting evidence

Unknown — 本快照没有单独的图像或参与者数量核验表，已知数量及其口径见 Imaging and cohort。

## Family and derivative ledger

Unknown — 未记录具体的资源关系边。患者或影像重叠情况仍见 Identity and provenance。

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Eye–Neurodegeneration — 域认知评分 | 15 / 63.75 | Not eligible / 46.25 | 3 / 2 / 3 / 1 / 1 | OCT与认知分母 | 地区人群及糖尿病富集；申请需指明影像格式。 |
| Eye–Stroke — 白质脑影像关联 | 21 / 51.25 | Not eligible / 41.25 | 3 / 2 / 1 / 1 / 1 | MRI 子集与可分级双眼分母待重算 | 地区人群及糖尿病富集；申请需指明影像格式。 |
| Retinal Aging — 年龄 | 23 / 63.75 | Not eligible / 46.25 | 3 / 2 / 3 / 1 / 1 | OCT与认知分母 | 地区人群及糖尿病富集；申请需指明影像格式。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://www.demaastrichtstudie.nl/research/data-guidelines)

## Sources

<a id="evidence-1"></a>

### s1

[Open original source](https://pubmed.ncbi.nlm.nih.gov/37611119/)

Methods: 3,436; age, sex, T2D oversampling; OCT layers linked to cognitive scores and MRI metrics; MRI subgroups vary by endpoint.

Recorded check date — 2026-11-03.

<a id="evidence-2"></a>

### s2

[Open original source](https://pmc.ncbi.nlm.nih.gov/articles/PMC11056139/)

Methods, retinal calibers and MRI: fundus camera/eyes; bilateral available for 54.7% of 4,010 analysis subjects; whole brain connectivity.

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s3

[Open original source](https://www.demaastrichtstudie.nl/research/data-guidelines)

Data guidelines: formal request with research plan; external investigator local collaboration encouraged.

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### s4

[Open original source](https://www.demaastrichtstudie.nl/research/data-dictionary)

Portal directs users to searchable dictionary; check ownership and requested object type with management.

Recorded check date — 2026-11-03.

<a id="evidence-5"></a>

### s5

[Open original source](https://pmc.ncbi.nlm.nih.gov/articles/PMC7286946/)

Methods: 2,876 with retinal caliber and measured glucose status; office blood pressure, sex and age covariates; 176 photography visits substantially later.

Recorded check date — 2026-11-03.

<a id="evidence-6"></a>

### s6

[Open original source](https://alz-journals.onlinelibrary.wiley.com/doi/10.1002/alz.13442)

Methods, MRI available only in subset beginning December 2013.

Recorded check date — 2026-11-03.
