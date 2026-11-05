# OculoScope: Fairer AI in Ophthalmology Dataset

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

广角眼底与年龄分层公平性。

当前核验的影像与模态范围 — Ultra-widefield fundus photography

Image availability — Zenodo record visible; files restricted.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | oculoscope |
| Name / 名称 | OculoScope: Fairer AI in Ophthalmology Dataset |
| Acronym / 缩写 | OculoScope |
| Official resource | [https://zenodo.org/records/10403889](https://zenodo.org/records/10403889) |
| Country or region / 国家地区 | China |
| Institution / 机构 | Unknown |
| Reported year / 年份口径 | 2023 (initial\_public\_release) |
| Publication date | 2023-12-03 |
| Date scope | initial\_public\_release |
| Date evidence | [https://zenodo.org/api/records/10403889](https://zenodo.org/api/records/10403889) |
| Date reviewed | 2026-09-11 |
| Original citation | Fairer AI in ophthalmology via implicit fairness learning for mitigating sexism and ageism. Nature Communications (2024). |
| Publication DOI | [10.1038/s41467-024-48972-0](https://doi.org/10.1038/s41467-024-48972-0) |
| Dataset DOI | [10.5281/zenodo.10403889](https://doi.org/10.5281/zenodo.10403889) |
| Import origin | EyeDataHub v0.7.0 |
| Original EyeDataHub ID | oculoscope |
| Dataset family | oculoscope |
| Family or derivative relation | current\_dataset |
| Independence / overlap | Independence unverified |
| Upstream family ID | oculoscope |
| Upstream resource role | current\_dataset |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 2 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | 16,530 ultra-widefield fundus images from 8,405+ patients (age 0–90) annotated for 38 ophthalmic diseases and 67 fundus features. Released alongside the FairerOPTH study on sexism and ageism in ophthalmic AI (Nature Communications 2024). |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | Ultra-widefield fundus photography |
| Images / 图像数及口径 | 16,530 UWF images |
| Participants / 参与者数及口径 | &gt;8,405 per paper (do not treat as paired age count) |
| Eyes / 眼别 | Unknown |
| Device / 设备 | Unknown |
| Resolution / 分辨率 | 512 × 648; original-resolution subset for testing |
| Quality / 质量控制 | Unknown |
| Multiple visits / 多时点 | Unknown |
| Multiple modalities / 多模态 | Unknown |
| Multiple centers / 多中心 | Unknown |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Controlled access |
| Access or application route | [https://zenodo.org/records/10403889](https://zenodo.org/records/10403889) |
| Image files / 影像文件 | Zenodo record visible; files restricted. |
| Individual labels / 个体标签 | Disease and fundus feature annotations documented. Exact ages vs age bands and shared patient key in approved archive require confirmation. |
| Data license / 数据许可 | CC BY 4.0 |
| Research use / 科研条件 | Unknown |
| Commercial use / 商业用途 | Unknown |
| Terms scope | dataset\_files |
| Terms evidence | [https://figshare.com/s/926c2c2ef9e77ab5eb9d](https://figshare.com/s/926c2c2ef9e77ab5eb9d) |
| Upstream route review date | 2026-07-21 |
| Upstream acquisition support | guided\_instructions\_only |
| Upstream access friction | self\_service\_authenticated |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | Paper evaluates fairness by age and sex; released continuous age plus patient grouping not established. |
| Strengths / 主要优点 | 广角眼底与年龄分层公平性。 |
| Limitations / 关键缺陷 | 受限文件；不能由论文年龄跨度推定逐人实足年龄可获取。 |
| Suggested experiments / 建议实验 | 获得可用字段后比较年龄组的校准，先验证患者分组和年龄粒度。 |
| Retinal Aging suitability | A: 年龄分层见论文；逐人年龄与权限待核。 |
| Stroke / CSVD suitability | Unknown |
| AD / Dementia suitability | Unknown |
| Multicenter model suitability | G: UWF 多标签公平性与迁移。 |
| Screening rationale / 筛查理由 | 年龄分层见论文；逐人年龄与权限待核。 \| UWF 多标签公平性与迁移。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 2 | Tier 2 | 年龄分层见论文；逐人年龄与权限待核。 | [p](#evidence-3) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Tier 3 | Tier 3 | UWF 多标签公平性与迁移。 | [d](#evidence-2) |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Uncertain | Study stratification, external continuous age availability unresolved. | [p](#evidence-3) |
| Sex / 性别 | Uncertain | Used in study; delivery unknown. | [p](#evidence-3) |
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
| 16530 | images | Primary quantity reported in the reviewed catalog source | legacy\_catalog\_field | not\_assessed | [Quantity source](https://figshare.com/s/926c2c2ef9e77ab5eb9d) |

## Family and derivative ledger

Unknown — 未记录具体的资源关系边。患者或影像重叠情况仍见 Identity and provenance。

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Retinal Aging — 年龄分组公平性 | 40 / 22.5 | Not eligible / 25.0 | 2 / 0 / 0 / 1 / 1 | 年龄字段与患者键未知 | UWF 源档受控；年龄连续值与个体键未知。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://zenodo.org/records/10403889)

## Sources

<a id="evidence-1"></a>

### base

[Open original source](https://figshare.com/s/926c2c2ef9e77ab5eb9d)

EyeDataHub v0.7.0 → oculoscope; catalog fields and dated source review, not a new clinical audit.

Recorded check date — 2026-07-21.

<a id="evidence-2"></a>

### d

[Open original source](https://zenodo.org/records/10403889)

Description and Files &gt; Restricted. 16530 UWF photos; 38 disease and 67 image-feature labels.

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### p

[Open original source](https://doi.org/10.1038/s41467-024-48972-0)

OculoScope cohort; age- and sex-stratified fairness analyses; age bands do not imply release of continuous age.

Recorded check date — 2026-11-03.
