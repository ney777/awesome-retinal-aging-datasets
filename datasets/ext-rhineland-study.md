# Rhineland Study / Rheinland Studie

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

有精确的 MRI/OCT 交集及排除流程，适合评估完整病例选择偏倚。

当前核验的影像与模态范围 — OCT \| brain MRI

Image availability — DUAC accepts image-database requests; raw/minimally processed files for QC or method development.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | ext-rhineland-study |
| Name / 名称 | Rhineland Study / Rheinland Studie |
| Acronym / 缩写 | Unknown |
| Official resource | [https://www.rheinland-studie.de/en/participation/rules-of-use/](https://www.rheinland-studie.de/en/participation/rules-of-use/) |
| Country or region / 国家地区 | Germany |
| Institution / 机构 | German Center for Neurodegenerative Diseases (DZNE), Bonn |
| Reported year / 年份口径 | 2022 |
| Publication date | Unknown |
| Date scope | Unknown |
| Date evidence | Unknown |
| Date reviewed | Unknown |
| Original citation | Mauschitz MM et al. Retinal layer assessments as potential biomarkers for brain atrophy in the Rhineland Study. Sci Rep. 2022. |
| Publication DOI | [10.1038/s41598-022-06821-4](https://doi.org/10.1038/s41598-022-06821-4) |
| Dataset DOI | Unknown |
| Import origin | Extension |
| Original EyeDataHub ID | Unknown |
| Dataset family | Rhineland Study |
| Family or derivative relation | Unknown |
| Independence / overlap | Patient overlap unverified |
| Upstream family ID | Unknown |
| Upstream resource role | Unknown |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 1 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | Unknown |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | OCT \| brain MRI |
| Images / 图像数及口径 | Unknown |
| Participants / 参与者数及口径 | First 5,000; 3,505 MRI, 3,395 MRI and SD-OCT; 2,872 final complete-case after exclusions; 2,797 with selected diffusion measures. |
| Eyes / 眼别 | Unknown |
| Device / 设备 | Heidelberg Spectralis SD-OCT; MRI and diffusion sequences. |
| Resolution / 分辨率 | Unknown |
| Quality / 质量控制 | OCT signal ≥20 dB; missingness, neurological and retinal conditions excluded. |
| Multiple visits / 多时点 | Unknown |
| Multiple modalities / 多模态 | Yes |
| Multiple centers / 多中心 | Unknown |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Application |
| Access or application route | [https://www.rheinland-studie.de/en/participation/rules-of-use/](https://www.rheinland-studie.de/en/participation/rules-of-use/) |
| Image files / 影像文件 | DUAC accepts image-database requests; raw/minimally processed files for QC or method development. |
| Individual labels / 个体标签 | QC research database separately requestable; specify fields and join in protocol. |
| Data license / 数据许可 | Unknown |
| Research use / 科研条件 | Consent coverage and data minimization; research collaboration normally required; review purpose against raw image database rules. |
| Commercial use / 商业用途 | Unknown |
| Terms scope | Unknown |
| Terms evidence | Unknown |
| Upstream route review date | Unknown |
| Upstream acquisition support | Unknown |
| Upstream access friction | Unknown |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | Community participants seen in Bonn; same participant OCT and MRI; no universal denominator across diffusion and structural indices. |
| Strengths / 主要优点 | 有精确的 MRI/OCT 交集及排除流程，适合评估完整病例选择偏倚。 |
| Limitations / 关键缺陷 | 本项分析排除了自报卒中，结局为结构/扩散指标；不能据此做 AD 或卒中事件监督。 |
| Suggested experiments / 建议实验 | 在 2,872 人原始分析框架内比较视网膜层厚和年龄对海马/灰白质体积的增量解释度。 |
| Retinal Aging suitability | A: 30–94 岁，个体眼底层厚。 |
| Stroke / CSVD suitability | C: 结构/扩散脑 MRI 匹配。 |
| AD / Dementia suitability | Unknown |
| Multicenter model suitability | Unknown |
| Screening rationale / 筛查理由 | 30–94 岁，个体眼底层厚。 \| 结构/扩散脑 MRI 匹配。 \| 高血压、糖尿病为配对协变量。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 1 | Tier 1 | 30–94 岁，个体眼底层厚。 | [s1](#evidence-1) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Tier 1 | Tier 1 | 结构/扩散脑 MRI 匹配。 | [s1](#evidence-1) |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Tier 1 | Tier 1 | 高血压、糖尿病为配对协变量。 | [s1](#evidence-1) |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Unknown | Unknown | No topic-specific finding | Unknown |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | 连续年龄 | [s1](#evidence-1) |
| Sex / 性别 | Confirmed | 个体协变量 | [s1](#evidence-1) |
| Hypertension / 高血压 | Confirmed | 个体协变量 | [s1](#evidence-1) |
| Diabetes / 糖尿病 | Confirmed | 个体协变量 | [s1](#evidence-1) |
| Cardiovascular disease / 心血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Stroke type / 卒中分型 | Uncertain | 自报卒中史为排除条件，未提供卒中分型 | [s1](#evidence-1) |
| Stroke timing / 卒中事件时间 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Brain MRI / 脑 MRI | Confirmed | 灰质/白质/海马及弥散指标 | [s1](#evidence-1) |
| CSVD / 脑小血管病 | Uncertain | 弥散指标不等于分级的 WMH、微出血/腔隙标签 | [s1](#evidence-1) |
| Alzheimer’s disease / 阿尔茨海默病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Dementia / 痴呆 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Cognition / 认知功能 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Parkinson’s disease / 帕金森病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Frailty / 衰弱 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Health status / 健康状态 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Mortality / 死亡结局 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Follow-up / 纵向随访 | Uncertain | 前瞻性母队列；本分析横断面 | [s1](#evidence-1) |

## Counting evidence

Unknown — 本快照没有单独的图像或参与者数量核验表，已知数量及其口径见 Imaging and cohort。

## Family and derivative ledger

Unknown — 未记录具体的资源关系边。患者或影像重叠情况仍见 Identity and provenance。

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Eye–Stroke — 结构与扩散 MRI；特定 CSVD 病灶未确立 | 14 / 76.25 | Not eligible / 63.75 | 3 / 3 / 4 / 2 / 1 | 协议和质控后 MRI 交集 | 社区研究、MRI/OCT 质控；DUAC 受理影像申请。 |
| Retinal Aging — 年龄 | 18 / 70.0 | Not eligible / 60.0 | 3 / 2 / 4 / 2 / 1 | 质控后 OCT 与 MRI 样本 | 社区研究、MRI/OCT 质控；DUAC 受理影像申请。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://www.rheinland-studie.de/en/participation/rules-of-use/)

## Sources

<a id="evidence-1"></a>

### s1

[Open original source](https://pmc.ncbi.nlm.nih.gov/articles/PMC8854401/)

Methods/Data analyses: SD-OCT+MRI overlap (3,395); age, sex, HTN, diabetes, BMI, smoking; scan QC ≥20 dB; analytical 2,872; stroke excluded.

Recorded check date — 2026-11-03.

<a id="evidence-2"></a>

### s2

[Open original source](https://www.rheinland-studie.de/en/participation/rules-of-use/)

Data Use and Access Policy §1 and introduction: DUAC; identifiable image vs QC research database scopes; minimization, consent, collaborative access.

Recorded check date — 2026-11-03.
