# JOIR / JSAIO fifth competition health-check subset

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

同人眼底、年龄和代谢综合征测量；日本体检人群。

当前核验的影像与模态范围 — Fundus photography

Image availability — Research request to corresponding author for consultation with custodian.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | ext-joir-japanese-checkup |
| Name / 名称 | JOIR / JSAIO fifth competition health-check subset |
| Acronym / 缩写 | JOIR / JSAIO |
| Official resource | [https://www.joir.jp/](https://www.joir.jp/) |
| Country or region / 国家地区 | Japan |
| Institution / 机构 | Japan Ocular Imaging Registry / Japanese Society of Artificial Intelligence in Ophthalmology |
| Reported year / 年份口径 | 2025 (descriptor) |
| Publication date | Unknown |
| Date scope | Unknown |
| Date evidence | Unknown |
| Date reviewed | Unknown |
| Original citation | Itoh T et al. Multi-task deep learning for predicting metabolic syndrome from retinal fundus images in a Japanese health checkup dataset. PLOS One 20:e0325337. |
| Publication DOI | [10.1371/journal.pone.0325337](https://doi.org/10.1371/journal.pone.0325337) |
| Dataset DOI | Unknown |
| Import origin | Extension |
| Original EyeDataHub ID | Unknown |
| Dataset family | JOIR |
| Family or derivative relation | Subset used in 5th JSAIO competition. Registry also releases an age model; those weights are not a data release. |
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
| Modalities / 影像模态 | Fundus photography |
| Images / 图像数及口径 | 5,000 photographs |
| Participants / 参与者数及口径 | Unknown (images do not identify total unique people) |
| Eyes / 眼别 | Unknown |
| Device / 设备 | Unknown |
| Resolution / 分辨率 | Unknown |
| Quality / 质量控制 | Unknown |
| Multiple visits / 多时点 | Unknown |
| Multiple modalities / 多模态 | Unknown |
| Multiple centers / 多中心 | Unknown |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Author contact |
| Access or application route | [https://www.joir.jp/](https://www.joir.jp/) |
| Image files / 影像文件 | Research request to corresponding author for consultation with custodian. |
| Individual labels / 个体标签 | Age, metabolic syndrome and measured covariates used in paper; exact licensed delivery requires approval. |
| Data license / 数据许可 | Unknown |
| Research use / 科研条件 | Applicant's own research only; onward redistribution prohibited. |
| Commercial use / 商业用途 | Unknown |
| Terms scope | Unknown |
| Terms evidence | Unknown |
| Upstream route review date | Unknown |
| Upstream acquisition support | Unknown |
| Upstream access friction | Unknown |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | Male health checkup photographs accompanied by age, waist circumference, blood pressure, lipids and fasting glucose for same examinations. |
| Strengths / 主要优点 | 同人眼底、年龄和代谢综合征测量；日本体检人群。 |
| Limitations / 关键缺陷 | 男性子集，不能由 5,000 张照片推断唯一人数；发布模型的许可不覆盖图像。 |
| Suggested experiments / 建议实验 | 按人和设备验证年龄估计及代谢综合征表型；报告男性样本的适用范围。 |
| Retinal Aging suitability | A: 同步年龄。 |
| Stroke / CSVD suitability | Unknown |
| AD / Dementia suitability | Unknown |
| Multicenter model suitability | Unknown |
| Screening rationale / 筛查理由 | 同步年龄。 \| 同期代谢综合征及组分；无已验证死亡结局。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 1 | Tier 1 | 同步年龄。 | [p](#evidence-1) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Tier 1 | Tier 1 | 同期代谢综合征及组分；无已验证死亡结局。 | [p](#evidence-1) |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Unknown | Unknown | No topic-specific finding | Unknown |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | Age | [p](#evidence-1) |
| Sex / 性别 | Confirmed | Male-only subset | [p](#evidence-1) |
| Hypertension / 高血压 | Uncertain | SBP/DBP measurements not equivalent to diagnosis. | [p](#evidence-1) |
| Diabetes / 糖尿病 | Uncertain | Fasting glucose; a diabetes diagnosis is not established. | [p](#evidence-1) |
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
| Follow-up / 纵向随访 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| metabolic\_syndrome | Confirmed | METS label and measured components | [p](#evidence-1) |

## Counting evidence

Unknown — 本快照没有单独的图像或参与者数量核验表，已知数量及其口径见 Imaging and cohort。

## Family and derivative ledger

Unknown — 未记录具体的资源关系边。患者或影像重叠情况仍见 Identity and provenance。

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Retinal Aging — 年龄、代谢综合征 | 37 / 38.75 | Not eligible / 35.0 | 3 / 1 / 0 / 1 / 1 | 5000 是照片数 | 日本男性体检子集；须项目方批准。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://www.joir.jp/)

## Sources

<a id="evidence-1"></a>

### p

[Open original source](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0325337)

Data availability, cohort and methods: male checkup subset, 5000 photos, clinical measurements; request own research use, prohibit redistribution.

Recorded check date — 2026-11-03.

<a id="evidence-2"></a>

### m

[Open original source](https://www.joir.jp/data/)

Registry's age-estimation model distribution page, distinct artifact from underlying clinical data.

Recorded check date — 2026-11-03.
