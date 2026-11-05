# Johns Hopkins OCT MS and Healthy Controls

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

右眼像素与 MS 病种、小样本但明确的逐人粒度。

当前核验的影像与模态范围 — OCT

Image availability — JHU IACL publicly links hosted OCT archive.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | oct\_ms\_jhu |
| Name / 名称 | Johns Hopkins OCT MS and Healthy Controls |
| Acronym / 缩写 | Unknown |
| Official resource | [https://iacl.ece.jhu.edu/index.php/Resources](https://iacl.ece.jhu.edu/index.php/Resources) |
| Country or region / 国家地区 | United States |
| Institution / 机构 | Johns Hopkins University |
| Reported year / 年份口径 | 2019 |
| Publication date | Unknown |
| Date scope | Unknown |
| Date evidence | Unknown |
| Date reviewed | Unknown |
| Original citation | He Y et al. Retinal layer parcellation of optical coherence tomography images: Data resource for multiple sclerosis and healthy controls. Data Brief. 2019. |
| Publication DOI | [10.1016/j.dib.2018.11.060](https://doi.org/10.1016/j.dib.2018.11.060) |
| Dataset DOI | Unknown |
| Import origin | EyeDataHub v0.7.0 |
| Original EyeDataHub ID | oct\_ms\_jhu |
| Dataset family | oct\_ms\_jhu |
| Family or derivative relation | current\_dataset |
| Independence / overlap | Independence unverified |
| Upstream family ID | oct\_ms\_jhu |
| Upstream resource role | current\_dataset |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 1 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | 35 Spectralis OCT volumes (1,715 B-scans) with 9 manually delineated retinal layer boundaries. 14 healthy controls, 21 MS subjects. |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | OCT |
| Images / 图像数及口径 | 35 volumes × 49 B-scans = 1,715 B-scans |
| Participants / 参与者数及口径 | 35 people (21 MS, 14 healthy controls). |
| Eyes / 眼别 | Right eye only, one volume per subject. |
| Device / 设备 | Heidelberg Spectralis |
| Resolution / 分辨率 | \[496, 1024\] |
| Quality / 质量控制 | Nine layer boundaries manually delineated per B-scan. |
| Multiple visits / 多时点 | One scan per subject |
| Multiple modalities / 多模态 | Unknown |
| Multiple centers / 多中心 | Unknown |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Open download |
| Access or application route | [https://iacl.ece.jhu.edu/index.php/Resources](https://iacl.ece.jhu.edu/index.php/Resources) |
| Image files / 影像文件 | JHU IACL publicly links hosted OCT archive. |
| Individual labels / 个体标签 | Direct archive inspection: group encoded in all 35 volume names; demographics CSV contains 35 rows ID, Age, Gender, Eye, Diagnosis. 26 exact, unique demographic→volume joins; 9 control IDs repeat hc0 (cannot disambiguate from filenames). |
| Data license / 数据许可 | CC BY-NC-ND (EyeDataHub dataset terms; consult IACL before redistribution) |
| Research use / 科研条件 | Check dataset NC-ND terms for derivative redistribution. |
| Commercial use / 商业用途 | Non-commercial per recorded data terms. |
| Terms scope | dataset\_files |
| Terms evidence | [https://iacl.ece.jhu.edu/~aaron/data/OCT\_Manual\_Delineations-2018\_June\_29\_b.zip](https://iacl.ece.jhu.edu/~aaron/data/OCT_Manual_Delineations-2018_June_29_b.zip) |
| Upstream route review date | 2026-07-21 |
| Upstream acquisition support | loader\_implemented\_not\_live\_tested |
| Upstream access friction | anonymous\_direct |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | 35 single right-eye volumes. Diagnosis from hc/ms prefixes; 26 unique subject-ID joins for age/sex, 9 controls with duplicated hc0 in CSV. Never guess row-order mapping. |
| Strengths / 主要优点 | 右眼像素与 MS 病种、小样本但明确的逐人粒度。 |
| Limitations / 关键缺陷 | 病例对照样本；9 份对照眼底的年龄/性别映射歧义，余下 26 人偏向 MS；不得跨数据集拼接脑 MRI。 |
| Suggested experiments / 建议实验 | 逐人分割验证与分层误差分析；可作小规模设备内复现。 |
| Retinal Aging suitability | A: 仅 26 份按唯一 ID 可可靠配到连续年龄；不得按行序补齐其余 9 人。 |
| Stroke / CSVD suitability | Unknown |
| AD / Dementia suitability | Unknown |
| Multicenter model suitability | G: 可用于层分割/表示外部测试。 |
| Screening rationale / 筛查理由 | 仅 26 份按唯一 ID 可可靠配到连续年龄；不得按行序补齐其余 9 人。 \| MS/健康病例对照 + 同一受试者 OCT。 \| 可用于层分割/表示外部测试。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 1 | Tier 1 | 仅 26 份按唯一 ID 可可靠配到连续年龄；不得按行序补齐其余 9 人。 | [s4](#evidence-5) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Tier 1 | Tier 1 | MS/健康病例对照 + 同一受试者 OCT。 | [s1](#evidence-2) |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Tier 3 | Tier 3 | 可用于层分割/表示外部测试。 | [s1](#evidence-2) |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | 人口学 CSV；26 张体积能唯一匹配，9 份对照 ID 歧义。 | [s4](#evidence-5) |
| Sex / 性别 | Confirmed | 人口学 CSV；26 张体积能唯一匹配，9 份对照 ID 歧义。 | [s4](#evidence-5) |
| Hypertension / 高血压 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Diabetes / 糖尿病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Cardiovascular disease / 心血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Stroke type / 卒中分型 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Stroke timing / 卒中事件时间 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Brain MRI / 脑 MRI | Uncertain | 未核实同人影像映射 | [s2](#evidence-3) |
| CSVD / 脑小血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Alzheimer’s disease / 阿尔茨海默病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Dementia / 痴呆 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Cognition / 认知功能 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Parkinson’s disease / 帕金森病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Frailty / 衰弱 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Health status / 健康状态 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Mortality / 死亡结局 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Follow-up / 纵向随访 | Not available | 此发布每人一个右眼体积 | [s1](#evidence-2) |

## Counting evidence

| Count | Unit | Scope | Evidence basis | Exactness | Source |
| --- | --- | --- | --- | --- | --- |
| 1715 | b\_scans | B-scans in 35 OCT volumes | associated\_publication | exact | [Quantity source](https://doi.org/10.1016/j.dib.2018.11.060) |
| 35 | volumes | Spectralis OCT volumes | associated\_publication | exact | [Quantity source](https://doi.org/10.1016/j.dib.2018.11.060) |

## Family and derivative ledger

Unknown — 未记录具体的资源关系边。患者或影像重叠情况仍见 Identity and provenance。

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Retinal Aging — 可唯一匹配的 OCT 年龄 | 34 / 45.0 | 7 / 60.0 | 3 / 1 / 1 / 3 / 1 | 仅 26 个唯一 ID 能匹配个体年龄 | 原 ZIP 标识核验；仅 26 个唯一年龄匹配。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://iacl.ece.jhu.edu/index.php/Resources)

## Sources

<a id="evidence-1"></a>

### base

[Open original source](https://iacl.ece.jhu.edu/~aaron/data/OCT_Manual_Delineations-2018_June_29_b.zip)

EyeDataHub v0.7.0 → oct\_ms\_jhu; catalog fields and dated source review, not a new clinical audit.

Recorded check date — 2026-07-21.

<a id="evidence-2"></a>

### s1

[Open original source](https://pmc.ncbi.nlm.nih.gov/articles/PMC6327073/)

Data section and Table 1: 35 right eyes (14 HC, 21 MS), 49 slices each, 9 manual boundaries; sex and age summary only in table.

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s2

[Open original source](https://iacl.ece.jhu.edu/index.php/Resources)

OCT MS and Healthy Controls under Retinal resources; separate brain challenge listed independently.

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### s3

[Open original source](https://khosravipooya.com/EyeDataHub/datasets/oct_ms_jhu/)

Catalog dataset file terms and download route.

Recorded check date — 2026-11-03.

<a id="evidence-5"></a>

### s4

[Open original source](https://iacl.ece.jhu.edu/~aaron/data/OCT_Manual_Delineations-2018_June_29_b.zip)

Direct ZIP index + demographics-2018\_June\_29.csv inspected. 35 .vol and CSV rows, ID/Age/Gender/Eye/Diagnosis. 26 unique exact ID joins; hc0 duplicated for nine controls, .vol are hc01–hc09. No image voxels transferred.

Recorded check date — 2026-11-03.
