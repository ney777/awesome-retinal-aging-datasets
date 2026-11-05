# Shanghai Diabetes Prevention Program (SDPP; DeepRETStroke subsets)

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

中国受试者的真值 MRI 子集可与单独的卒中随访分析区分。

当前核验的影像与模态范围 — Fundus \| brain MRI

Image availability — Deidentified fundus photographs can be requested for non-profit use; raw MRI transfer not promised.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | ext-shanghai-sdpp |
| Name / 名称 | Shanghai Diabetes Prevention Program (SDPP; DeepRETStroke subsets) |
| Acronym / 缩写 | SDPP |
| Official resource | [https://pmc.ncbi.nlm.nih.gov/articles/PMC12623247/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12623247/) |
| Country or region / 国家地区 | China |
| Institution / 机构 | Shanghai Sixth People's Hospital and study collaborators |
| Reported year / 年份口径 | 2025 |
| Publication date | Unknown |
| Date scope | Unknown |
| Date evidence | Unknown |
| Date reviewed | Unknown |
| Original citation | Jiang et al. A deep learning system for detecting silent brain infarction and predicting stroke risk. Nat Biomed Eng. 2025. |
| Publication DOI | [10.1038/s41551-025-01413-9](https://doi.org/10.1038/s41551-025-01413-9) |
| Dataset DOI | Unknown |
| Import origin | Extension |
| Original EyeDataHub ID | Unknown |
| Dataset family | Shanghai Diabetes Prevention Program |
| Family or derivative relation | SDPP-MRI and non-MRI SDPP are distinct analysis subsets of the same parent; other DeepRETStroke cohorts (including UKB and AREDS) remain separate. |
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
| Modalities / 影像模态 | Fundus \| brain MRI |
| Images / 图像数及口径 | 1,564 in 782 internal SDPP-MRI; 58,320 photos in separate 29,160 longitudinal subset. |
| Participants / 参与者数及口径 | 782 SDPP-MRI for SBI detection; separate 29,160 in longitudinal non-MRI internal set for incident stroke. |
| Eyes / 眼别 | Paired left/right fundus images. |
| Device / 设备 | Unknown |
| Resolution / 分辨率 | Unknown |
| Quality / 质量控制 | Study QC of retinal photographs; clinical reference MRI only in MRI subset. |
| Multiple visits / 多时点 | Unknown |
| Multiple modalities / 多模态 | Yes (MRI subset) |
| Multiple centers / 多中心 | Unknown |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Author contact |
| Access or application route | [https://pmc.ncbi.nlm.nih.gov/articles/PMC12623247/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12623247/) |
| Image files / 影像文件 | Deidentified fundus photographs can be requested for non-profit use; raw MRI transfer not promised. |
| Individual labels / 个体标签 | Related clinical information request reviewed by data management committee; verify release of dates and MRI grading field. |
| Data license / 数据许可 | Unknown |
| Research use / 科研条件 | Request T.Y. Wong (wongtienyin@tsinghua.edu.cn); institutional committee and formal DTA. |
| Commercial use / 商业用途 | Published request route limited to non-profit use. |
| Terms scope | Unknown |
| Terms evidence | Unknown |
| Upstream route review date | Unknown |
| Upstream acquisition support | Unknown |
| Upstream access friction | Unknown |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | Person-level fundus and MRI-defined silent brain infarction in SDPP-MRI; separate longitudinal non-MRI sample predicts incident stroke. Pseudo-labels in non-MRI sample are not MRI diagnoses. |
| Strengths / 主要优点 | 中国受试者的真值 MRI 子集可与单独的卒中随访分析区分。 |
| Limitations / 关键缺陷 | 申请式分发；不保证原始 MRI。勿把筛查阳性或模型伪标签当作确诊卒中。 |
| Suggested experiments / 建议实验 | MRI 子集评估检出静默性脑梗死；在独立随访子集中检验首次卒中风险并报告校准及时间依赖 AUC。 |
| Retinal Aging suitability | A: 配对年龄和眼底。 |
| Stroke / CSVD suitability | B: 随访子集卒中事件。 \| C: MRI 子集有静默性脑梗死参照。 |
| AD / Dementia suitability | Unknown |
| Multicenter model suitability | Unknown |
| Screening rationale / 筛查理由 | 配对年龄和眼底。 \| 随访子集卒中事件。 \| MRI 子集有静默性脑梗死参照。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 1 | Tier 1 | 配对年龄和眼底。 | [s2](#evidence-2) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Tier 1 | Tier 1 | 随访子集卒中事件。 | [s1](#evidence-1) |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Tier 1 | Tier 1 | MRI 子集有静默性脑梗死参照。 | [s1](#evidence-1) |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Unknown | Unknown | No topic-specific finding | Unknown |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | 分析特征 | [s2](#evidence-2) |
| Sex / 性别 | Confirmed | 分析特征 | [s2](#evidence-2) |
| Hypertension / 高血压 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Diabetes / 糖尿病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Cardiovascular disease / 心血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Stroke type / 卒中分型 | Uncertain | SBI 和发生卒中已确认；未从该资料核实临床卒中各亚型字段 | [s1](#evidence-1) |
| Stroke timing / 卒中事件时间 | Confirmed | 5 年卒中风险；具体日期格式需批准 | [s1](#evidence-1) |
| Brain MRI / 脑 MRI | Confirmed | SDPP-MRI 子集 | [s1](#evidence-1) |
| CSVD / 脑小血管病 | Confirmed | MRI 诊断的 SBI；不等价于全套 CSVD 评分 | [s1](#evidence-1) |
| Alzheimer’s disease / 阿尔茨海默病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Dementia / 痴呆 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Cognition / 认知功能 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Parkinson’s disease / 帕金森病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Frailty / 衰弱 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Health status / 健康状态 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Mortality / 死亡结局 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Follow-up / 纵向随访 | Confirmed | 非 MRI 子集有事件随访 | [s1](#evidence-1) |

## Counting evidence

Unknown — 本快照没有单独的图像或参与者数量核验表，已知数量及其口径见 Imaging and cohort。

## Family and derivative ledger

Unknown — 未记录具体的资源关系边。患者或影像重叠情况仍见 Identity and provenance。

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Eye–Stroke — 新发卒中与 MRI 静默梗死 | 9 / 86.25 | Not eligible / 58.75 | 4 / 3 / 4 / 1 / 1 | 卒中子集；静默梗死 MRI 子集782，分开 | 非营利定向申请；MRI 子集与事件子集分别计。 |
| Retinal Aging — 年龄与未来卒中 | 13 / 80.0 | Not eligible / 55.0 | 4 / 2 / 4 / 1 / 1 | 非 MRI 卒中队列 | 非营利定向申请；MRI 子集与事件子集分别计。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC12623247/)

## Sources

<a id="evidence-1"></a>

### s1

[Open original source](https://pmc.ncbi.nlm.nih.gov/articles/PMC12623247/)

Fig 1 and Table 1; separate internal MRI and non-MRI samples; development workflow distinguishes MRI labels from pseudo-labels; Data availability requires committee + DTA for nonprofit fundus images/clinical data.

Recorded check date — 2026-11-03.

<a id="evidence-2"></a>

### s2

[Open original source](https://pure.qub.ac.uk/files/642367133/Jiang_DL_DeepStroke_Silent_and_Clinical_Stroke_Nature_BME_2025.pdf)

Figure 1 / Methods: 782 participants/1,564 fundus images MRI arm; 29,160/58,320 separate longitudinal arm; two eyes. Table 1 reports demographics and metabolic risks.

Recorded check date — 2026-11-03.
