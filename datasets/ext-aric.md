# Atherosclerosis Risk in Communities (ARIC) retinal ancillary studies

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

Direct correspondence among retinal signs, WML/infarcts, later clinical stroke, cognitive test trajectories and study-defined dementia.

当前核验的影像与模态范围 — Fundus; later OCT/OCTA-related ancillary eye variables; brain MRI in a subset

Image availability — Uncertain for raw retinal/brain images via standard BioLINCC release. Public data dictionary documents study IDs, derived measures and flags, not distribution of image files.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | ext-aric |
| Name / 名称 | Atherosclerosis Risk in Communities (ARIC) retinal ancillary studies |
| Acronym / 缩写 | ARIC |
| Official resource | [https://biolincc.nhlbi.nih.gov/studies/aric/](https://biolincc.nhlbi.nih.gov/studies/aric/) |
| Country or region / 国家地区 | United States |
| Institution / 机构 | NHLBI; ARIC Coordinating Center, University of North Carolina and four field communities |
| Reported year / 年份口径 | 2002 (paired eye–MRI–stroke publication) |
| Publication date | Unknown |
| Date scope | Unknown |
| Date evidence | Unknown |
| Date reviewed | Unknown |
| Original citation | Wong TY et al. Cerebral white matter lesions, retinopathy, and incident clinical stroke. JAMA. 2002;288:67–74. See also retinal-stroke analysis, PMID 11597667 (2001). |
| Publication DOI | [10.1001/jama.288.1.67](https://doi.org/10.1001/jama.288.1.67) |
| Dataset DOI | Unknown |
| Import origin | Extension |
| Original EyeDataHub ID | Unknown |
| Dataset family | ARIC |
| Family or derivative relation | V3, V5 neurocognitive, V7 ancillary and later endpoints belong to overlapping ARIC family. |
| Independence / overlap | Patient overlap unverified |
| Upstream family ID | Unknown |
| Upstream resource role | Unknown |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 2 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | Unknown |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | Fundus; later OCT/OCTA-related ancillary eye variables; brain MRI in a subset |
| Images / 图像数及口径 | Unknown |
| Participants / 参与者数及口径 | 10,358 retinal photography participants in early stroke study; 1,684 with MRI+retina in 1993–1995 study. These are distinct analytic denominators. |
| Eyes / 眼别 | Visit 3 single-eye protocol, later visits/ancillary forms distinguish eyes. |
| Device / 设备 | Unknown |
| Resolution / 分辨率 | Unknown |
| Quality / 质量控制 | Grading and ungradable/exclusion fields; later ancillary dictionary also distinguishes retina, GCC, ONH and macular/disc angio scans by eye. |
| Multiple visits / 多时点 | Yes; visit 3 and visit 5 CFP; MRI repeat subset and follow-up. Do not assume each participant has serial imaging. |
| Multiple modalities / 多模态 | Yes; CFP + brain MRI in overlapping participants. |
| Multiple centers / 多中心 | Yes; four US communities. |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Controlled access |
| Access or application route | [https://biolincc.nhlbi.nih.gov/studies/aric/](https://biolincc.nhlbi.nih.gov/studies/aric/) |
| Image files / 影像文件 | Uncertain for raw retinal/brain images via standard BioLINCC release. Public data dictionary documents study IDs, derived measures and flags, not distribution of image files. |
| Individual labels / 个体标签 | Confirmed application route for exam, annual follow-up, adjudicated event and ancillary variables; verify selected release/fields. |
| Data license / 数据许可 | BioLINCC Research Materials Distribution Agreement (RMDA); no open pixel licence verified. |
| Research use / 科研条件 | Register PI/submit study request and institution/ethics requirements per BioLINCC. BioLINCC/NIH controlled-access route prohibits covered access from institutions located in China (including Hong Kong/Macau) and the other listed countries under NOT-OD-25-083. A separate study collaboration is not a verified alternative route for covered data. |
| Commercial use / 商业用途 | Not permitted under the BioLINCC study data terms; the official Consent section prohibits commercial use. |
| Terms scope | Unknown |
| Terms evidence | Unknown |
| Upstream route review date | Unknown |
| Upstream acquisition support | Unknown |
| Upstream access friction | Unknown |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | Use cohort ID / visit-mapped scrambled ID supplied in approved release (visit-specific ID in ancillary dictionary); ascertain phenotype availability by visit. 1,684 actually had both retinal exam and brain MRI, not all 15,792 parent participants. |
| Strengths / 主要优点 | Direct correspondence among retinal signs, WML/infarcts, later clinical stroke, cognitive test trajectories and study-defined dementia. |
| Limitations / 关键缺陷 | Eye photos vs already derived grades, visit-specific laterality, censoring and late-visit survivor selection. Raw image package unconfirmed; check ancillary PI and linkage/consent. |
| Suggested experiments / 建议实验 | Compare baseline clinical model vs model adding retinal signs to predict first clinical stroke, quantify added calibration/discrimination at a fixed horizon and separately model MRI lesions; repeat cognition analyses accounting for attrition. |
| Retinal Aging suitability | A: Individual age and fundus photo/QC. \| Pixel gate: Uncertain for raw retinal/brain images via standard BioLINCC release. Public data dictionary documents study IDs, derived measures and flags, not distribution of image files. |
| Stroke / CSVD suitability | B: Adjudicated clinical ischemic stroke subtypes linked to retina. \| Pixel gate: Uncertain for raw retinal/brain images via standard BioLINCC release. Public data dictionary documents study IDs, derived measures and flags, not distribution of image files. \| C: 1,684 confirmed brain MRI and retinal participants (not all ARIC). \| Pixel gate: Uncertain for raw retinal/brain images via standard BioLINCC release. Public data dictionary documents study IDs, derived measures and flags, not distribution of image files. |
| AD / Dementia suitability | D: Normal/MCI/dementia at V5; longitudinal cognition from s6. \| Pixel gate: Uncertain for raw retinal/brain images via standard BioLINCC release. Public data dictionary documents study IDs, derived measures and flags, not distribution of image files. |
| Multicenter model suitability | G: Multiple communities; pixel acquisition for domain transfer requires separate confirmation. |
| Screening rationale / 筛查理由 | Individual age and fundus photo/QC. \| Pixel gate: Uncertain for raw retinal/brain images via standard BioLINCC release. Public data dictionary documents study IDs, derived measures and flags, not distribution of image files. \| Adjudicated clinical ischemic stroke subtypes linked to retina. \| Pixel gate: Uncertain for raw retinal/brain images via standard BioLINCC release. Public data dictionary documents study IDs, derived measures and flags, not distribution of image files. \| 1,684 confirmed brain MRI and retinal participants (not all ARIC). \| Pixel gate: Uncertain for raw retinal/brain images via standard BioLINCC release. Public data dictionary documents study IDs, derived measures and flags, not distribution of image files. \| Normal/MCI/dementia at V5; longitudinal cognition from s6. \| Pixel gate: Uncertain for raw retinal/brain images via standard BioLINCC release. Public data dictionary documents study IDs, derived measures and flags, not distribution of image files. \| Participant-level diabetes, BP and vascular risk factors in retinal study; broader event files s1. \| Pixel gate: Uncertain for raw retinal/brain images via standard BioLINCC release. Public data dictionary documents study IDs, derived measures and flags, not distribution of image files. \| Multiple communities; pixel acquisition for domain transfer requires separate confirmation. |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 2 | Tier 1 | Individual age and fundus photo/QC. \| Pixel gate: Uncertain for raw retinal/brain images via standard BioLINCC release. Public data dictionary documents study IDs, derived measures and flags, not distribution of image files. | [s2](#evidence-2) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Tier 2 | Tier 1 | Adjudicated clinical ischemic stroke subtypes linked to retina. \| Pixel gate: Uncertain for raw retinal/brain images via standard BioLINCC release. Public data dictionary documents study IDs, derived measures and flags, not distribution of image files. | [s8](#evidence-8) |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Tier 2 | Tier 1 | 1,684 confirmed brain MRI and retinal participants (not all ARIC). \| Pixel gate: Uncertain for raw retinal/brain images via standard BioLINCC release. Public data dictionary documents study IDs, derived measures and flags, not distribution of image files. | [s3](#evidence-3) |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Tier 2 | Tier 1 | Normal/MCI/dementia at V5; longitudinal cognition from s6. \| Pixel gate: Uncertain for raw retinal/brain images via standard BioLINCC release. Public data dictionary documents study IDs, derived measures and flags, not distribution of image files. | [s5](#evidence-5) |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Tier 2 | Tier 1 | Participant-level diabetes, BP and vascular risk factors in retinal study; broader event files s1. \| Pixel gate: Uncertain for raw retinal/brain images via standard BioLINCC release. Public data dictionary documents study IDs, derived measures and flags, not distribution of image files. | [s2](#evidence-2) |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Tier 3 | Tier 3 | Multiple communities; pixel acquisition for domain transfer requires separate confirmation. | [s2](#evidence-2) |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | Age recorded; early study range 51–72. | [s2](#evidence-2) |
| Sex / 性别 | Confirmed | Participant sex included. | [s2](#evidence-2) |
| Hypertension / 高血压 | Confirmed | BP/risk exposure. Distinguish BP vs derived hypertension definition. | [s2](#evidence-2) |
| Diabetes / 糖尿病 | Confirmed | Diabetes covariate in eye study. | [s2](#evidence-2) |
| Cardiovascular disease / 心血管病 | Confirmed | Available heart disease event follow-up, cross-match eye sample per release. | [s1](#evidence-1) |
| Stroke type / 卒中分型 | Confirmed | Adjudicated lacunar, nonlacunar thrombotic and cardioembolic stroke. | [s8](#evidence-8) |
| Stroke timing / 卒中事件时间 | Confirmed | Incident adjudication + follow-up. | [s2](#evidence-2) |
| Brain MRI / 脑 MRI | Confirmed | MRI–retina overlap. | [s3](#evidence-3) |
| CSVD / 脑小血管病 | Confirmed | White matter lesions and incident lacunar infarcts; not synonymous with clinical stroke. | [s4](#evidence-4) |
| Alzheimer’s disease / 阿尔茨海默病 | Uncertain | Source verifies syndrome; AD etiology/biomarker label not confirmed here. | [s5](#evidence-5) |
| Dementia / 痴呆 | Confirmed | Cognitive status adjudication V5. | [s5](#evidence-5) |
| Cognition / 认知功能 | Confirmed | Composite of three neuropsychological tests. | [s6](#evidence-6) |
| Parkinson’s disease / 帕金森病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Frailty / 衰弱 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Health status / 健康状态 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Mortality / 死亡结局 | Confirmed | Available follow-up for mortality in ARIC; eye-specific N must be determined. | [s1](#evidence-1) |
| Follow-up / 纵向随访 | Confirmed | Repeat MRI and events in subset. | [s4](#evidence-4) |

## Counting evidence

Unknown — 本快照没有单独的图像或参与者数量核验表，已知数量及其口径见 Imaging and cohort。

## Family and derivative ledger

Unknown — 未记录具体的资源关系边。患者或影像重叠情况仍见 Identity and provenance。

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Eye–Neurodegeneration — 随访认知及痴呆 | 2 / 85.0 | Not eligible / 58.75 | 4 / 3 / 3 / 1 / 3 | 神经分析独立分母未用于打分 | 四社区、阅读中心；独立像素交付未证。 |
| Eye–Stroke — 新发卒中、WMH 与腔隙 | 1 / 97.5 | Not eligible / 65.0 | 4 / 4 / 4 / 1 / 3 | 事件论文队列；另有 1684 影像 × MRI | 四社区、阅读中心；独立像素交付未证。 |
| Retinal Aging — 年龄、人群结局 | 1 / 97.5 | Not eligible / 65.0 | 4 / 4 / 4 / 1 / 3 | 卒中研究成像样本 | 四社区、阅读中心；独立像素交付未证。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://biolincc.nhlbi.nih.gov/studies/aric/)

## Sources

<a id="evidence-1"></a>

### s1

[Open original source](https://biolincc.nhlbi.nih.gov/studies/aric/)

Available data: exam cycles v1–v10, contacts years 2–35, events including death, heart disease and stroke to 2023. Study description, design and request process.

Recorded check date — 2026-11-03.

<a id="evidence-2"></a>

### s2

[Open original source](https://pubmed.ncbi.nlm.nih.gov/11597667/)

Methods; 10,358 people aged 51–72 from four communities had graded retina and record-adjudicated incident stroke; adjusts for sex, diabetes and BP.

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s3

[Open original source](https://pubmed.ncbi.nlm.nih.gov/12090864/)

Participants and outcome measures; 1,684 with same-visit retinal photographs and MRI, age 51–72, WMLs and subsequent clinical stroke.

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### s4

[Open original source](https://pubmed.ncbi.nlm.nih.gov/20519327/)

Methods/results; paired retinal microvascular lesions and new MRI brain/lacunar infarct or white matter lesions over median 10.5 years.

Recorded check date — 2026-11-03.

<a id="evidence-5"></a>

### s5

[Open original source](https://pubmed.ncbi.nlm.nih.gov/30706941/)

V5 ARIC-NCS cross-sectional retina and adjudicated normal cognition/MCI/dementia; this supports syndrome-level labels.

Recorded check date — 2026-11-03.

<a id="evidence-6"></a>

### s6

[Open original source](https://pmc.ncbi.nlm.nih.gov/articles/PMC5880633/)

Abstract and Methods; visit 3 fundus and cognitive battery at multiple time points (three tests, composite score). Flow/attrition may change effective N.

Recorded check date — 2026-11-03.

<a id="evidence-7"></a>

### s7

[Open original source](https://biolincc.nhlbi.nih.gov/media/studies/aric/Data%20Dictionary%20-%20Ancillary%20Studies.pdf)

as2014\_38\_v7\_err; scrambled cohort visit ID, eye-specific photograph/angiography exclusions ERR11A1–ERR11A6; no image payload indicated.

Recorded check date — 2026-11-03.

<a id="evidence-8"></a>

### s8

[Open original source](https://pmc.ncbi.nlm.nih.gov/articles/PMC2894269/)

Methods; retinal microvascular abnormalities followed for classified lacunar, nonlacunar thrombotic or cardioembolic stroke.

Recorded check date — 2026-11-03.

<a id="evidence-9"></a>

### s9

[Open original source](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/document.cgi?phd=4483&study_id=phs000280.v5.p1)

Visit 3 retinal photography manual; repeat same-eye photography in QC sample, systematic photograph grading and quality feedback.

Recorded check date — 2026-11-03.

<a id="evidence-10"></a>

### s10

[Open original source](https://biolincc.nhlbi.nih.gov/faq/)

PI registration, data requests and RMDA approval process.

Recorded check date — 2026-11-03.

<a id="evidence-11"></a>

### policy

[Open original source](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-083.html)

Official NIH implementation notice; as of April 4, 2025 institutions located in countries of concern including China (Hong Kong and Macau included) are prohibited from accessing NIH controlled-access repositories and associated data.

Recorded check date — 2026-11-03.

<a id="evidence-12"></a>

### biofaq

[Open original source](https://biolincc.nhlbi.nih.gov/faq/)

International requestors section explicitly applies NIH controlled-access restrictions. No general worldwide availability.

Recorded check date — 2026-11-03.

<a id="evidence-13"></a>

### consent\_20261106

[Open original source](https://biolincc.nhlbi.nih.gov/studies/aric/)

Targeted recheck 2026-11-06, Consent / Specific Consent Restrictions: study data cannot be used for commercial purposes. This recheck covers use restrictions, not all resource fields.

Recorded check date — 2026-11-06.
