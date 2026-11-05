# EyePACS full research cohort used for eyeAge

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

同一人的重复检查可研究年龄预测的重测误差与时间间隔。

当前核验的影像与模态范围 — Color fundus photography

Image availability — Full data requested from EyePACS, separately reviewed.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | ext-eyepacs-eyeage |
| Name / 名称 | EyePACS full research cohort used for eyeAge |
| Acronym / 缩写 | EyePACS |
| Official resource | [https://elifesciences.org/articles/82364](https://elifesciences.org/articles/82364) |
| Country or region / 国家地区 | USA (EyePACS program) |
| Institution / 机构 | EyePACS |
| Reported year / 年份口径 | 2023 |
| Publication date | Unknown |
| Date scope | Unknown |
| Date evidence | Unknown |
| Date reviewed | Unknown |
| Original citation | Ahadi S et al. Longitudinal fundus imaging and its genome-wide association analysis provide evidence for a human retinal aging clock. eLife 12:e82364 (2023). |
| Publication DOI | [10.7554/eLife.82364](https://doi.org/10.7554/eLife.82364) |
| Dataset DOI | Unknown |
| Import origin | Extension |
| Original EyeDataHub ID | Unknown |
| Dataset family | EyePACS program |
| Family or derivative relation | Full research pool; public EyePACS competition images are a subset; overlap not enumerated. UKB validation counted separately. |
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
| Modalities / 影像模态 | Color fundus photography |
| Images / 图像数及口径 | 217,289 train / 54,292 tune photographs |
| Participants / 参与者数及口径 | 100,692 train / 25,238 tune (individuals in paper) |
| Eyes / 眼别 | Typically bilateral per visit |
| Device / 设备 | Unknown |
| Resolution / 分辨率 | Unknown |
| Quality / 质量控制 | Quality-filtered evaluation; denominator changes after filtering. |
| Multiple visits / 多时点 | Yes — repeated examinations in subset |
| Multiple modalities / 多模态 | Unknown |
| Multiple centers / 多中心 | Unknown |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Author contact |
| Access or application route | [https://elifesciences.org/articles/82364\#data](https://elifesciences.org/articles/82364#data) |
| Image files / 影像文件 | Full data requested from EyePACS, separately reviewed. |
| Individual labels / 个体标签 | Full clinical age and revisit data under internal approval; competition subset has a separate scope. |
| Data license / 数据许可 | Unknown |
| Research use / 科研条件 | Internal EyePACS assessment and potential ethics review. |
| Commercial use / 商业用途 | Unknown |
| Terms scope | Unknown |
| Terms evidence | Unknown |
| Upstream route review date | Unknown |
| Upstream acquisition support | Unknown |
| Upstream access friction | Unknown |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | Paper splits by patient, averages eyes within visits and analyses subsequent visits in repeat patients. Death linkage in this paper is UKB, not established for EyePACS training data. |
| Strengths / 主要优点 | 同一人的重复检查可研究年龄预测的重测误差与时间间隔。 |
| Limitations / 关键缺陷 | 糖网筛查人群与健康人群不同；不能把合作样本的年龄列投射到公开竞赛。 |
| Suggested experiments / 建议实验 | 用重复人群进行配对差分、采集条件和随访间隔敏感性分析。 |
| Retinal Aging suitability | A: 实足年龄与多次眼底检查。 |
| Stroke / CSVD suitability | Unknown |
| AD / Dementia suitability | Unknown |
| Multicenter model suitability | Unknown |
| Screening rationale / 筛查理由 | 实足年龄与多次眼底检查。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 1 | Tier 1 | 实足年龄与多次眼底检查。 | [p](#evidence-1) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Unknown | Unknown | No topic-specific finding | Unknown |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | Age at imaging. | [p](#evidence-1) |
| Sex / 性别 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Hypertension / 高血压 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Diabetes / 糖尿病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Cardiovascular disease / 心血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Stroke type / 卒中分型 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Stroke timing / 卒中事件时间 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Brain MRI / 脑 MRI | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| CSVD / 脑小血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Alzheimer’s disease / 阿尔茨海默病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Dementia / 痴呆 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Cognition / 认知功能 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Parkinson’s disease / 帕金森病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Frailty / 衰弱 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Health status / 健康状态 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Mortality / 死亡结局 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Follow-up / 纵向随访 | Confirmed | Repeat retinal visits for a subset. | [p](#evidence-1) |

## Counting evidence

Unknown — 本快照没有单独的图像或参与者数量核验表，已知数量及其口径见 Imaging and cohort。

## Family and derivative ledger

| Source resource | Relation | Target resource | Confidence | Scope | Evidence |
| --- | --- | --- | --- | --- | --- |
| [ext-eyepacs-eyeage](ext-eyepacs-eyeage.md) | same\_program\_as | [eyepacs](eyepacs.md) | Confirmed program; exact person overlap Unknown | 竞赛子集来自完整项目；眼龄研究抽样与竞赛重合分母未知。 | [Relationship evidence](https://elifesciences.org/articles/82364) |

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Retinal Aging — 重复访视年龄 | 16 / 73.75 | Not eligible / 51.25 | 4 / 1 / 4 / 1 / 1 | 训练人数；调参另有 25238 | 论文多个访视；与竞赛包有重叠，需联系 EyePACS。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://elifesciences.org/articles/82364)

## Sources

<a id="evidence-1"></a>

### p

[Open original source](https://elifesciences.org/articles/82364)

Results prediction of age, Table 1, longitudinal analysis and Data availability: EyePACS train/tune, participant splits, full data by custodian request; UKB mortality analysis.

Recorded check date — 2026-11-03.
