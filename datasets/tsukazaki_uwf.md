# Tsukazaki Optos Public Project (TOPP)

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

日本医院 UWF 域；适用于核验广角域偏移。

当前核验的影像与模态范围 — Ultra-widefield fundus photography

Image availability — Hospital lists original project; linked old landing page did not resolve in this audit. New use requires custodian clarification.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | tsukazaki\_uwf |
| Name / 名称 | Tsukazaki Optos Public Project (TOPP) |
| Acronym / 缩写 | TOPP |
| Official resource | [https://www.tsukazaki-hp.jp/diseases/gakujyutu.html](https://www.tsukazaki-hp.jp/diseases/gakujyutu.html) |
| Country or region / 国家地区 | Japan |
| Institution / 机构 | Tsukazaki Hospital |
| Reported year / 年份口径 | Unknown |
| Publication date | Unknown |
| Date scope | Unknown |
| Date evidence | Unknown |
| Date reviewed | Unknown |
| Original citation | Nagasawa T et al., 'Automatic detection of multiple retinal diseases in ultra-widefield fundus images using deep learning', Nature Machine Intelligence 2022. https://www.nature.com/articles/s42256-022-00566-5 — Data: https://github.com/DateCazuki/Fundus\_Diagnosis |
| Publication DOI | Unknown |
| Dataset DOI | Unknown |
| Import origin | EyeDataHub v0.7.0 |
| Original EyeDataHub ID | tsukazaki\_uwf |
| Dataset family | tsukazaki\_uwf |
| Family or derivative relation | current\_dataset |
| Independence / overlap | Independence unverified |
| Upstream family ID | tsukazaki\_uwf |
| Upstream resource role | current\_dataset |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 3 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | 13,047 ultra-widefield fundus photographs (Optos, 200° FOV) from Tsukazaki Hospital, annotated with 8 binary disease labels: AO, AMD, DR, Glaucoma, MH, RD, RP, RVO. Associated with Scientific Data 2024. |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | Ultra-widefield fundus photography |
| Images / 图像数及口径 | 13047 images (Primary quantity reported in the reviewed catalog source) |
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
| Access category / 获取方式 | Author contact |
| Access or application route | [https://www.tsukazaki-hp.jp/diseases/gakujyutu.html](https://www.tsukazaki-hp.jp/diseases/gakujyutu.html) |
| Image files / 影像文件 | Hospital lists original project; linked old landing page did not resolve in this audit. New use requires custodian clarification. |
| Individual labels / 个体标签 | Ophthalmic disease labels documented, subject-level continuous age / visit key not verified for an externally obtainable package. |
| Data license / 数据许可 | Research only — contact authors for data access |
| Research use / 科研条件 | Source reports research-only use; inspect cited terms. |
| Commercial use / 商业用途 | Unknown |
| Terms scope | dataset\_files |
| Terms evidence | [https://github.com/DateCazuki/Fundus\_Diagnosis](https://github.com/DateCazuki/Fundus_Diagnosis) |
| Upstream route review date | 2026-07-21 |
| Upstream acquisition support | manual\_access\_blocked |
| Upstream access friction | author\_contact |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | Image-to-clinical age / visit linkage in a licensed release unknown. |
| Strengths / 主要优点 | 日本医院 UWF 域；适用于核验广角域偏移。 |
| Limitations / 关键缺陷 | 原始公开链接本次未取得有效页面；分类器仓库不能证明当前取得数据或患者年龄。 |
| Suggested experiments / 建议实验 | 向管理方确认本次可获版本、跨境条件、年龄/日期/眼别清单，再考虑年龄分析。 |
| Retinal Aging suitability | Unknown |
| Stroke / CSVD suitability | Unknown |
| AD / Dementia suitability | Unknown |
| Multicenter model suitability | G: 医院与设备域辅助资源。 |
| Screening rationale / 筛查理由 | 医院与设备域辅助资源。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Tier 3 | Tier 3 | 医院与设备域辅助资源。 | [i](#evidence-4) |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Uncertain | No verified age field in accessible manifest. | [i](#evidence-4) |
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
| Follow-up / 纵向随访 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |

## Counting evidence

| Count | Unit | Scope | Evidence basis | Exactness | Source |
| --- | --- | --- | --- | --- | --- |
| 13047 | images | Primary quantity reported in the reviewed catalog source | legacy\_catalog\_field | not\_assessed | [Quantity source](https://github.com/DateCazuki/Fundus_Diagnosis) |

## Family and derivative ledger

Unknown — 未记录具体的资源关系边。患者或影像重叠情况仍见 Identity and provenance。

## Research priorities

Unknown — 本资源未进入当前三个科研方向的候选排名。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://www.tsukazaki-hp.jp/diseases/gakujyutu.html)

## Sources

<a id="evidence-1"></a>

### base

[Open original source](https://github.com/DateCazuki/Fundus_Diagnosis)

EyeDataHub v0.7.0 → tsukazaki\_uwf; catalog fields and dated source review, not a new clinical audit.

Recorded check date — 2026-07-21.

<a id="evidence-2"></a>

### h

[Open original source](https://www.tsukazaki-hp.jp/diseases/gakujyutu.html)

Hospital research achievements records TOPP dataset and old landing page.

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### p

[Open original source](https://pmc.ncbi.nlm.nih.gov/articles/PMC13522753/)

Data availability of TOPP re-use study: images subject to Japanese restrictions and direct request to Hitoshi Tabuchi and project co-authors.

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### i

[Open original source](https://khosravipooya.com/EyeDataHub/datasets/tsukazaki_uwf/)

Snapshot records UWF and eight ocular disease labels; age dictionary not supplied.

Recorded check date — 2026-11-03.
