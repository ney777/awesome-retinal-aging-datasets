# Scottish Collaborative Optometry-Ophthalmology Network e-research (SCONe)

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

Direct clinical-code linkage for stroke, clinical AD/dementia and PD; repeated fundus, multiple devices and spatially distributed community sites.

当前核验的影像与模态范围 — Fundus

Image availability — Confirmed within Scottish National Safe Haven for approved SCONe researchers/projects only. External researchers need a project-specific partnership; raw export not offered.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | ext-scone-scotland |
| Name / 名称 | Scottish Collaborative Optometry-Ophthalmology Network e-research (SCONe) |
| Acronym / 缩写 | SCONe |
| Official resource | [https://clinical-sciences.ed.ac.uk/ophthalmology/scone/about-scone](https://clinical-sciences.ed.ac.uk/ophthalmology/scone/about-scone) |
| Country or region / 国家地区 | United Kingdom (Scotland) |
| Institution / 机构 | University of Edinburgh, Scottish community optometry practices, Public Health Scotland/eDRIS National Safe Haven |
| Reported year / 年份口径 | 2025 (cohort descriptor); Feb 2026 (phase 2 scope update) |
| Publication date | Unknown |
| Date scope | Unknown |
| Date evidence | Unknown |
| Date reviewed | Unknown |
| Original citation | Tochel C et al. SCONe: a community-acquired retinal image repository enabling ocular, cardiovascular and neurodegenerative disease prediction. BMJ Health Care Inform. 2025;32:e101236. |
| Publication DOI | [10.1136/bmjhci-2024-101236](https://doi.org/10.1136/bmjhci-2024-101236) |
| Dataset DOI | Unknown |
| Import origin | Extension |
| Original EyeDataHub ID | Unknown |
| Dataset family | SCONe |
| Family or derivative relation | Phase 1/2 and 2025 published linked subset overlap. No additional cohort for each practice or outcome. |
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
| Modalities / 影像模态 | Fundus |
| Images / 图像数及口径 | Phase-2 report: 1,499,677 images delivered; nearly 800,000 linked to NHS records at that report. Earlier published cohort: &gt;367,000 matched images. Distinct snapshots, not additive. |
| Participants / 参与者数及口径 | 131,678 people in phase-2 delivery; linked person count not given for the ~800,000 image update. 2025 descriptor reports &gt;36,000 matched patients. |
| Eyes / 眼别 | Usually left + right per date; coded outcomes assigned to the person, not eye-specific. |
| Device / 设备 | 2025 subset: typically 45° CFP; Topcon (~90%), Canon (~5%), Nikon (~4%). Device shares should not be generalized to all future submissions. |
| Resolution / 分辨率 | Unknown |
| Quality / 质量控制 | Approximately 9,500 images read for AMD, quality and pathology in phase-2 report; not all images clinically graded. |
| Multiple visits / 多时点 | Yes, repeated community optometry dates for some individuals; date/follow-up heterogeneity. |
| Multiple modalities / 多模态 | Fundus + healthcare records. Neither routine brain MRI nor OCT pixels established by cohort descriptor. |
| Multiple centers / 多中心 | Yes; multiple community optometry practices and camera systems across Scotland. |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Controlled access |
| Access or application route | [https://clinical-sciences.ed.ac.uk/ophthalmology/scone/about-scone](https://clinical-sciences.ed.ac.uk/ophthalmology/scone/about-scone) |
| Image files / 影像文件 | Confirmed within Scottish National Safe Haven for approved SCONe researchers/projects only. External researchers need a project-specific partnership; raw export not offered. |
| Individual labels / 个体标签 | Confirmed linked coded hospital/general ophthalmic/death records for approved Safe Haven work; not an open individual-level table. |
| Data license / 数据许可 | Public Health Scotland governance; no publicly redistributable patient/image licence. |
| Research use / 科研条件 | Collaborative inquiry with SCONe, approved institution/research project, governance training and Safe Haven-controlled analysis; only checked non-disclosive outputs can leave. |
| Commercial use / 商业用途 | Unknown |
| Terms scope | Unknown |
| Terms evidence | Unknown |
| Upstream route review date | Unknown |
| Upstream acquisition support | Unknown |
| Upstream access friction | Unknown |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | PHS/eDRIS links images via approved patient identity matching to routine health records. Research uses deidentified person, image date and earliest disease-code date (clinical onset unknown). More than one image/eye/date possible. Linked subset is smaller than phase-2 delivered inventory. |
| Strengths / 主要优点 | Direct clinical-code linkage for stroke, clinical AD/dementia and PD; repeated fundus, multiple devices and spatially distributed community sites. |
| Limitations / 关键缺陷 | Optometry attenders, older population and incomplete medical history. First code is a dated proxy; do not assume it is incident onset or model same-day dual-eye images as independent people. Safe Haven access is project specific. |
| Suggested experiments / 建议实验 | On an approved Safe Haven project, train a patient-split age model and evaluate whether a frozen age gap improves prediction of first recorded stroke/dementia beyond clinical covariates. Require adequate pre-index observation, treat death as competing risk, reserve a practice/device and monitor coding completeness. |
| Retinal Aging suitability | A: Participant age, dated retina, repeated optometry subset. |
| Stroke / CSVD suitability | B: Table 2 verifies same patients with coded stroke and retina, relative first-code dates. |
| AD / Dementia suitability | D: AD, dementia and cognitive decline coded in linked patients, not validated cognitive test scores. |
| Multicenter model suitability | G: Community practice/device heterogeneity; data remain in the National Safe Haven. |
| Screening rationale / 筛查理由 | Participant age, dated retina, repeated optometry subset. \| Table 2 verifies same patients with coded stroke and retina, relative first-code dates. \| AD, dementia and cognitive decline coded in linked patients, not validated cognitive test scores. \| PD code groups matched to retina at person/date. \| Coded hypertension/heart disease, diabetes and linked death records in repository. \| Community practice/device heterogeneity; data remain in the National Safe Haven. |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 1 | Tier 1 | Participant age, dated retina, repeated optometry subset. | [s1](#evidence-1) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Tier 1 | Tier 1 | Table 2 verifies same patients with coded stroke and retina, relative first-code dates. | [s1](#evidence-1) |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Tier 1 | Tier 1 | AD, dementia and cognitive decline coded in linked patients, not validated cognitive test scores. | [s1](#evidence-1) |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Tier 1 | Tier 1 | PD code groups matched to retina at person/date. | [s1](#evidence-1) |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Tier 1 | Tier 1 | Coded hypertension/heart disease, diabetes and linked death records in repository. | [s1](#evidence-1) |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Tier 3 | Tier 3 | Community practice/device heterogeneity; data remain in the National Safe Haven. | [s1](#evidence-1) |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | Individual ages linked to capture dates; cohort access is controlled. | [s1](#evidence-1) |
| Sex / 性别 | Confirmed | Patient demographics in linked health records. | [s1](#evidence-1) |
| Hypertension / 高血压 | Confirmed | Hypertension/hypertensive heart disease code grouping. | [s1](#evidence-1) |
| Diabetes / 糖尿病 | Confirmed | Coded diagnosis. | [s1](#evidence-1) |
| Cardiovascular disease / 心血管病 | Confirmed | Ischaemic heart disease, hypertension/heart disease and pulmonary heart disease codes. | [s1](#evidence-1) |
| Stroke type / 卒中分型 | Uncertain | Table 2 reports any stroke; subtype label coverage not established. | [s1](#evidence-1) |
| Stroke timing / 卒中事件时间 | Confirmed | Dated first recorded stroke code, not adjudicated clinical onset. | [s1](#evidence-1) |
| Brain MRI / 脑 MRI | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| CSVD / 脑小血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Alzheimer’s disease / 阿尔茨海默病 | Confirmed | Clinical AD code, not gold-standard pathology. | [s1](#evidence-1) |
| Dementia / 痴呆 | Confirmed | Clinical coded dementia. | [s1](#evidence-1) |
| Cognition / 认知功能 | Uncertain | Cognitive decline code confirmed; individual standardized cognitive scores not confirmed. | [s1](#evidence-1) |
| Parkinson’s disease / 帕金森病 | Confirmed | PD code. | [s1](#evidence-1) |
| Frailty / 衰弱 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Health status / 健康状态 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Mortality / 死亡结局 | Confirmed | National Records of Scotland Death Register linkage; availability of cause/timing by project must be verified. | [s1](#evidence-1) |
| Follow-up / 纵向随访 | Confirmed | Dated historical health records and repeated imagery in a subset. | [s1](#evidence-1) |

## Counting evidence

Unknown — 本快照没有单独的图像或参与者数量核验表，已知数量及其口径见 Imaging and cohort。

## Family and derivative ledger

Unknown — 未记录具体的资源关系边。患者或影像重叠情况仍见 Identity and provenance。

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Eye–Neurodegeneration — 痴呆、AD、PD 代码 | 3 / 81.25 | Not eligible / 66.25 | 3 / 3 / 4 / 2 / 3 | 痴呆代码人数；AD、PD 另计，不相加 | 社区验光多门店多设备；须项目团队合作在苏格兰安全环境内运行。 |
| Eye–Stroke — 首次医学编码日期，非裁定发病日 | 8 / 87.5 | Not eligible / 70.0 | 3 / 4 / 4 / 2 / 3 | 描述论文 stroke 代码阳性人数，非全部随访交集 | 社区验光多门店多设备；须项目团队合作在苏格兰安全环境内运行。 |
| Retinal Aging — 年龄、多次采集及编码结局 | 1 / 97.5 | Not eligible / 76.25 | 4 / 4 / 4 / 2 / 3 | 早期描述超过36000名匹配患者，取保守下界 | 社区验光多门店多设备；须项目团队合作在苏格兰安全环境内运行。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://clinical-sciences.ed.ac.uk/ophthalmology/scone/about-scone)

## Sources

<a id="evidence-1"></a>

### s1

[Open original source](https://pmc.ncbi.nlm.nih.gov/articles/PMC12083377/)

Tochel et al., Methods; results Table 2 and Figs 2–3. Patient/date matching, sex/age, camera distribution, repeat dates. In earlier linked cohort: 2,495 stroke, 1,630 dementia, 309 AD, 288 Parkinson, 703 cognitive-decline code groups; overlap possible. Earliest code a proxy, not validated incident onset.

Recorded check date — 2026-11-03.

<a id="evidence-2"></a>

### s2

[Open original source](https://clinical-sciences.ed.ac.uk/sites/default/files/2026-03/Summary%20of%20the%20second%20phase%20of%20the%20SCONe%20project%2C%202022%20to%202025.pdf)

Phase-2 report, data collection/curation: 1,499,677 images, 131,678 persons delivered, nearly 800,000 images linked to NHS records, around 9,500 graded; do not use counts as complete phenotype denominators.

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s3

[Open original source](https://clinical-sciences.ed.ac.uk/ophthalmology/scone/about-scone)

Official governance: Public Health Scotland controls access within the National Safe Haven; data not shared outwith secure facility.

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### s4

[Open original source](https://accord.scot/scottish-universities-transform-eye-health-research-with-retinal-imaging-resource)

University/NHS research office (24 Oct 2025): approved members of SCONe team only have access; external partnership must be confirmed.

Recorded check date — 2026-11-03.

<a id="evidence-5"></a>

### s5

[Open original source](https://doi.org/10.1186/s12874-024-02143-3)

Study-team linkage methodology, also referenced in phase-2 report; linkage results and impact of incomplete matches must be assessed.

Recorded check date — 2026-11-03.

<a id="evidence-6"></a>

### s6

[Open original source](https://pubmed.ncbi.nlm.nih.gov/40374195/)

2025 published cohort snapshot; &gt;367,000 matched retinal images, &gt;36,000 matched patients. Separate from phase-2 larger delivered inventory.

Recorded check date — 2026-11-03.
