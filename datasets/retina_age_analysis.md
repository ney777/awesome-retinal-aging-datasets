# Retina Age Analysis (Hugging Face upload)

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

公开模式可供设计 ID 与数据泄漏检查。

当前核验的影像与模态范围 — Color fundus photography

Image availability — Public images directory on uploader repository; rights chain unresolved.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | retina\_age\_analysis |
| Name / 名称 | Retina Age Analysis (Hugging Face upload) |
| Acronym / 缩写 | Unknown |
| Official resource | [https://huggingface.co/datasets/ramankamran/retina-age-analysis](https://huggingface.co/datasets/ramankamran/retina-age-analysis) |
| Country or region / 国家地区 | Unknown |
| Institution / 机构 | Unknown |
| Reported year / 年份口径 | 2025 (initial\_public\_release) |
| Publication date | 2025 |
| Date scope | initial\_public\_release |
| Date evidence | [https://huggingface.co/datasets/ramankamran/retina-age-analysis/raw/main/README.md](https://huggingface.co/datasets/ramankamran/retina-age-analysis/raw/main/README.md) |
| Date reviewed | 2026-09-11 |
| Original citation | ramankamran/retina-age-analysis. Hugging Face dataset, accessed 2026-07. |
| Publication DOI | Unknown |
| Dataset DOI | Unknown |
| Import origin | EyeDataHub v0.7.0 |
| Original EyeDataHub ID | retina\_age\_analysis |
| Dataset family | retina\_age\_analysis |
| Family or derivative relation | current\_dataset |
| Independence / overlap | Independence unverified |
| Upstream family ID | retina\_age\_analysis |
| Upstream resource role | current\_dataset |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 2 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | Fundus images and age labels for retinal age prediction and regression. |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | Color fundus photography |
| Images / 图像数及口径 | 9,857 images (card) |
| Participants / 参与者数及口径 | 5,393 individuals (card) |
| Eyes / 眼别 | exam\_eye |
| Device / 设备 | camera field; examples list Canon CR |
| Resolution / 分辨率 | Unknown |
| Quality / 质量控制 | Unknown |
| Multiple visits / 多时点 | Unknown |
| Multiple modalities / 多模态 | Unknown |
| Multiple centers / 多中心 | Unknown |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Open download |
| Access or application route | [https://huggingface.co/datasets/ramankamran/retina-age-analysis](https://huggingface.co/datasets/ramankamran/retina-age-analysis) |
| Image files / 影像文件 | Public images directory on uploader repository; rights chain unresolved. |
| Individual labels / 个体标签 | Patient\_id, patient\_age, patient\_sex and image\_id in split CSVs/viewer. |
| Data license / 数据许可 | Uploader labels repository MIT; underlying image origin and authorization not established. |
| Research use / 科研条件 | Original source agreement unresolved; hold independent use pending provenance. |
| Commercial use / 商业用途 | Unknown; MIT card insufficient to establish underlying image rights. |
| Terms scope | unknown |
| Terms evidence | [https://huggingface.co/datasets/ramankamran/retina-age-analysis](https://huggingface.co/datasets/ramankamran/retina-age-analysis) |
| Upstream route review date | 2026-07-21 |
| Upstream acquisition support | standard\_platform\_supported |
| Upstream access friction | self\_service\_authenticated |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | Repository CSV has image\_id, patient\_id, patient\_age; card describes patient-level splits. Clinical field structure resembles BRSET; no verified crosswalk or reuse permission. |
| Strengths / 主要优点 | 公开模式可供设计 ID 与数据泄漏检查。 |
| Limitations / 关键缺陷 | 原始图像出处和再分发权未核实，不作为独立外部测试集。 |
| Suggested experiments / 建议实验 | 只做来源与跨库重复核验；待许可和患者独立性确认后纳入评测。 |
| Retinal Aging suitability | A: 行键明确，原始来源与合法可用范围待核。 |
| Stroke / CSVD suitability | Unknown |
| AD / Dementia suitability | Unknown |
| Multicenter model suitability | Unknown |
| Screening rationale / 筛查理由 | 行键明确，原始来源与合法可用范围待核。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 2 | Tier 2 | 行键明确，原始来源与合法可用范围待核。 | [d](#evidence-2) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Unknown | Unknown | No topic-specific finding | Unknown |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | patient\_age | [d](#evidence-2) |
| Sex / 性别 | Confirmed | patient\_sex | [d](#evidence-2) |
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
| Follow-up / 纵向随访 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |

## Counting evidence

| Count | Unit | Scope | Evidence basis | Exactness | Source |
| --- | --- | --- | --- | --- | --- |
| 9857 | images | Primary quantity reported in the reviewed catalog source | legacy\_catalog\_field | not\_assessed | [Quantity source](https://huggingface.co/datasets/ramankamran/retina-age-analysis) |

## Family and derivative ledger

| Source resource | Relation | Target resource | Confidence | Scope | Evidence |
| --- | --- | --- | --- | --- | --- |
| [retina\_age\_analysis](retina_age_analysis.md) | possible\_overlap | [brset](brset.md) | Uncertain | 字段、文件名模式提示应查来源；未确认重用或许可，不合并人数。 | [Relationship evidence](https://huggingface.co/datasets/ramankamran/retina-age-analysis) |

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Retinal Aging — 年龄，来源隔离 | 38 / 26.25 | Not eligible / 16.25 | 2 / 1 / 0 / 0 / 0 | 卡片声称人数；归属、重用权待核 | 来源/授权链及 BRSET 潜在重叠未证。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://huggingface.co/datasets/ramankamran/retina-age-analysis)

## Sources

<a id="evidence-1"></a>

### base

[Open original source](https://huggingface.co/datasets/ramankamran/retina-age-analysis)

EyeDataHub v0.7.0 → retina\_age\_analysis; catalog fields and dated source review, not a new clinical audit.

Recorded check date — 2026-07-21.

<a id="evidence-2"></a>

### d

[Open original source](https://huggingface.co/datasets/ramankamran/retina-age-analysis)

Data Fields, Data Splits and viewer: patient/image keys, age and sex; 9857 images/5393 patients; uploader license does not document upstream chain.

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### p

[Open original source](https://physionet.org/content/brazilian-ophthalmological/1.0.2/)

BRSET data dictionary uses matching clinical field names; similar schema is a potential overlap signal only.

Recorded check date — 2026-11-03.
