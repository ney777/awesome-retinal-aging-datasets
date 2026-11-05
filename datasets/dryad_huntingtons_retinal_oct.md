# Huntington retinal OCT study (individual measurements)

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

HD 与正常对照的逐人 UHDRS、CAG 和眼底层厚字典。

当前核验的影像与模态范围 — OCT-derived retinal measurements only

Image availability — Not available in deposit; data.csv and README.md only.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | dryad\_huntingtons\_retinal\_oct |
| Name / 名称 | Huntington retinal OCT study (individual measurements) |
| Acronym / 缩写 | Unknown |
| Official resource | [https://datadryad.org/dataset/doi:10.5061/dryad.ncjsxksxr](https://datadryad.org/dataset/doi:10.5061/dryad.ncjsxksxr) |
| Country or region / 国家地区 | Czechia |
| Institution / 机构 | Charles University / General University Hospital in Prague |
| Reported year / 年份口径 | 2025 |
| Publication date | 2025-10-07 |
| Date scope | initial\_public\_release |
| Date evidence | [https://doi.org/10.5061/dryad.ncjsxksxr](https://doi.org/10.5061/dryad.ncjsxksxr) |
| Date reviewed | 2026-09-11 |
| Original citation | Dusek P et al. Data from: Is retina affected in Huntington’s disease? Is optical coherence tomography a good biomarker? Dryad. 2025. |
| Publication DOI | Unknown |
| Dataset DOI | [10.5061/dryad.ncjsxksxr](https://doi.org/10.5061/dryad.ncjsxksxr) |
| Import origin | EyeDataHub v0.7.0 |
| Original EyeDataHub ID | dryad\_huntingtons\_retinal\_oct |
| Dataset family | dryad\_huntingtons\_retinal\_oct |
| Family or derivative relation | current\_dataset |
| Independence / overlap | Independence unverified |
| Upstream family ID | dryad\_huntingtons\_retinal\_oct |
| Upstream resource role | current\_dataset |
| Review depth | Source-reviewed |
| Best recorded topic tier | Excluded |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | The named CSV and README form a direct human retinal OCT biomarker resource. |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | OCT-derived retinal measurements only |
| Images / 图像数及口径 | Unknown |
| Participants / 参与者数及口径 | Unknown |
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
| Access category / 获取方式 | Registration |
| Access or application route | [https://datadryad.org/dataset/doi:10.5061/dryad.ncjsxksxr](https://datadryad.org/dataset/doi:10.5061/dryad.ncjsxksxr) |
| Image files / 影像文件 | Not available in deposit; data.csv and README.md only. |
| Individual labels / 个体标签 | record\_id, group, age group, eye, visit, UHDRS and OCT-derived measures; no pixel images. |
| Data license / 数据许可 | CC0 1.0 (EyeDataHub catalog dataset terms) |
| Research use / 科研条件 | Unknown |
| Commercial use / 商业用途 | Unknown |
| Terms scope | dataset\_files |
| Terms evidence | [https://doi.org/10.5061/dryad.ncjsxksxr](https://doi.org/10.5061/dryad.ncjsxksxr) |
| Upstream route review date | 2026-08-01 |
| Upstream acquisition support | standard\_platform\_supported |
| Upstream access friction | self\_service\_authenticated |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | record\_id, eye, visit identify tabular observations. First vs second measurement is documented; longitudinal interval not established. |
| Strengths / 主要优点 | HD 与正常对照的逐人 UHDRS、CAG 和眼底层厚字典。 |
| Limitations / 关键缺陷 | 派生表，不可训练图像编码器；年龄是区间。 |
| Suggested experiments / 建议实验 | 复核 RNFL/TMV 与 UHDRS 的关联；每人双眼合并或建混合模型。 |
| Retinal Aging suitability | A: 年龄为区间；无眼底像素。 |
| Stroke / CSVD suitability | Unknown |
| AD / Dementia suitability | Unknown |
| Multicenter model suitability | Unknown |
| Screening rationale / 筛查理由 | 年龄为区间；无眼底像素。 \| HD 表型辅助，当前版本仅测量表。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Excluded | Excluded | 年龄为区间；无眼底像素。 | [s1](#evidence-2) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Excluded | Excluded | HD 表型辅助，当前版本仅测量表。 | [s1](#evidence-2) |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Unknown | Unknown | No topic-specific finding | Unknown |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | 分组年龄 | [s1](#evidence-2) |
| Sex / 性别 | Confirmed | 性别 | [s1](#evidence-2) |
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
| Health status / 健康状态 | Confirmed | 仅 HD 功能与运动量表，非一般健康指数 | [s1](#evidence-2) |
| Mortality / 死亡结局 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Follow-up / 纵向随访 | Uncertain | visit 表示第 1/2 次测量，时距不明 | [s1](#evidence-2) |

## Counting evidence

Unknown — 本快照没有单独的图像或参与者数量核验表，已知数量及其口径见 Imaging and cohort。

## Family and derivative ledger

Unknown — 未记录具体的资源关系边。患者或影像重叠情况仍见 Identity and provenance。

## Research priorities

Unknown — 本资源未进入当前三个科研方向的候选排名。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://datadryad.org/dataset/doi:10.5061/dryad.ncjsxksxr)

## Sources

<a id="evidence-1"></a>

### base

[Open original source](https://doi.org/10.5061/dryad.ncjsxksxr)

EyeDataHub v0.7.0 → dryad\_huntingtons\_retinal\_oct; catalog fields and dated source review, not a new clinical audit.

Recorded check date — 2026-08-01.

<a id="evidence-2"></a>

### s1

[Open original source](https://datadryad.org/dataset/doi:10.5061/dryad.ncjsxksxr)

Files and variables: data.csv and README only; record\_id, group, gender, age range, visit, eye, UHDRS, CAG and RNFL measurements.

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s2

[Open original source](https://khosravipooya.com/EyeDataHub/datasets/dryad_huntingtons_retinal_oct/)

Access route/terms: Dryad authenticated API and CC0.

Recorded check date — 2026-11-03.
