# NHANES 2005–2008 Ophthalmology – Retinal Imaging (OPXRET\_D / OPXRET\_E)

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

Independently reproducible participant-level analysis using open retinal grades and mortality/medical questionnaires; probability sampling.

当前核验的影像与模态范围 — Fundus

Image availability — Unknown for raw TIFFs; official open OPXRET files are derived XPT tables, not images. Acquisition manual describes historical TIFF creation only.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | ext-nhanes-2005-2008-retina |
| Name / 名称 | NHANES 2005–2008 Ophthalmology – Retinal Imaging (OPXRET\_D / OPXRET\_E) |
| Acronym / 缩写 | NHANES |
| Official resource | [https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/OPXRET\_D.htm](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/OPXRET_D.htm) |
| Country or region / 国家地区 | United States |
| Institution / 机构 | CDC, NCHS; University of Wisconsin reading centre |
| Reported year / 年份口径 | 2008 (first release of 2005–2006 codebook); next independent 2007–2008 cycle also included. |
| Publication date | Unknown |
| Date scope | Unknown |
| Date evidence | Unknown |
| Date reviewed | Unknown |
| Original citation | CDC/NCHS. NHANES 2005–2006 and 2007–2008, Ophthalmology – Retinal Imaging, OPXRET\_D/E codebooks. |
| Publication DOI | Unknown |
| Dataset DOI | Unknown |
| Import origin | Extension |
| Original EyeDataHub ID | Unknown |
| Dataset family | NHANES |
| Family or derivative relation | Two independent continuous-NHANES cycles grouped as one resource; not NHANES III or the derived myopia/metal exposure entry. |
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
| Modalities / 影像模态 | Fundus |
| Images / 图像数及口径 | Unknown |
| Participants / 参与者数及口径 | 5,371 had gradable retinal photographs across the two cycles in a published stroke analysis; 4,570 had its required stroke and eye variables. Not total recruited. |
| Eyes / 眼别 | Protocol two 45° fields per eye, both eyes. |
| Device / 设备 | Canon CR6-45NM with Canon 10D back. |
| Resolution / 分辨率 | 6.3 MP image capture (not necessarily released pixel dimensions). |
| Quality / 质量控制 | Reading-centre graders; per-eye gradability fields; analytic sample excludes ungradable cases. |
| Multiple visits / 多时点 | Two independent survey cross-sections; mortality linkage extends follow-up. No repeated retinal imaging documented for the same respondents. |
| Multiple modalities / 多模态 | Fundus + clinical questionnaires/exams |
| Multiple centers / 多中心 | National clustered multistage sampling; mobile exam locations do not imply released centre IDs. |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Open download |
| Access or application route | [https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Examination&amp;Cycle=2005-2006](https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Examination&Cycle=2005-2006) |
| Image files / 影像文件 | Unknown for raw TIFFs; official open OPXRET files are derived XPT tables, not images. Acquisition manual describes historical TIFF creation only. |
| Individual labels / 个体标签 | Confirmed open respondent-level grading, demographic and questionnaire variables; public-use NDI-linked mortality restricted in detail. |
| Data license / 数据许可 | Unknown |
| Research use / 科研条件 | Use public-use documentation, design/weights, codebooks and cycle-specific rules; raw pixel access separately unverified. |
| Commercial use / 商业用途 | Unknown |
| Terms scope | Unknown |
| Terms evidence | Unknown |
| Upstream route review date | Unknown |
| Upstream acquisition support | Unknown |
| Upstream access friction | Unknown |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | SEQN keys within corresponding OPXRET\_D/E, DEMO\_D/E, MCQ\_D/E and public LMF files. Sampling weights and design variables mandatory. MCQ160F is self-reported stroke history, MCQ180F age first told. Public mortality includes limited fields and disclosure protection; no incident non-fatal stroke demonstrated. |
| Strengths / 主要优点 | Independently reproducible participant-level analysis using open retinal grades and mortality/medical questionnaires; probability sampling. |
| Limitations / 关键缺陷 | No confirmed public raw image route. No verified brain MRI or contemporaneous standard dementia battery in the retinal cycles. Cross-cycle cognition data cannot be joined by respondent. |
| Suggested experiments / 建议实验 | Use public OPXRET grades as exposures for survey-weighted prevalent self-reported stroke and time-to-death. Restrict to eligible adults, combine cycles correctly, estimate total eligible-to-complete attrition; pixel-level age model requires separately verified images. |
| Retinal Aging suitability | A: Age + grade linkage verified via SEQN (s9); pixel access unresolved. \| Pixel gate: Unknown for raw TIFFs; official open OPXRET files are derived XPT tables, not images. Acquisition manual describes historical TIFF creation only. |
| Stroke / CSVD suitability | B: Matched retinal grades + prevalent self-reported stroke; no incident stroke endpoint. \| Pixel gate: Unknown for raw TIFFs; official open OPXRET files are derived XPT tables, not images. Acquisition manual describes historical TIFF creation only. |
| AD / Dementia suitability | D: Excluded from direct cognitive-battery studies across later independent survey cycles; hidden/linked dementia phenotype not confirmed. |
| Multicenter model suitability | G: Acquisition protocol useful; pixel dataset and commercial licence unresolved. |
| Screening rationale / 筛查理由 | Age + grade linkage verified via SEQN (s9); pixel access unresolved. \| Pixel gate: Unknown for raw TIFFs; official open OPXRET files are derived XPT tables, not images. Acquisition manual describes historical TIFF creation only. \| Matched retinal grades + prevalent self-reported stroke; no incident stroke endpoint. \| Pixel gate: Unknown for raw TIFFs; official open OPXRET files are derived XPT tables, not images. Acquisition manual describes historical TIFF creation only. \| Excluded from direct cognitive-battery studies across later independent survey cycles; hidden/linked dementia phenotype not confirmed. \| Same participants' retinal grades/NDI mortality. \| Pixel gate: Unknown for raw TIFFs; official open OPXRET files are derived XPT tables, not images. Acquisition manual describes historical TIFF creation only. \| Acquisition protocol useful; pixel dataset and commercial licence unresolved. |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 2 | Tier 1 | Age + grade linkage verified via SEQN (s9); pixel access unresolved. \| Pixel gate: Unknown for raw TIFFs; official open OPXRET files are derived XPT tables, not images. Acquisition manual describes historical TIFF creation only. | [s1](#evidence-1) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Tier 2 | Tier 1 | Matched retinal grades + prevalent self-reported stroke; no incident stroke endpoint. \| Pixel gate: Unknown for raw TIFFs; official open OPXRET files are derived XPT tables, not images. Acquisition manual describes historical TIFF creation only. | [s6](#evidence-6) |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Excluded | Excluded | Excluded from direct cognitive-battery studies across later independent survey cycles; hidden/linked dementia phenotype not confirmed. | [s10](#evidence-10) |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Tier 2 | Tier 1 | Same participants' retinal grades/NDI mortality. \| Pixel gate: Unknown for raw TIFFs; official open OPXRET files are derived XPT tables, not images. Acquisition manual describes historical TIFF creation only. | [s7](#evidence-7) |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Tier 3 | Tier 3 | Acquisition protocol useful; pixel dataset and commercial licence unresolved. | [s8](#evidence-8) |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | Age in years, top-coded per cycle; ≥40 eligible. | [s9](#evidence-9) |
| Sex / 性别 | Confirmed | RIAGENDR. | [s9](#evidence-9) |
| Hypertension / 高血压 | Confirmed | BPQ020 self-report; BPX adds exam-based measures. | [s9](#evidence-9) |
| Diabetes / 糖尿病 | Confirmed | DIQ010 clinician-diagnosed diabetes, self-report. | [s9](#evidence-9) |
| Cardiovascular disease / 心血管病 | Confirmed | Self-reported coronary heart disease/MI, separate from adjudicated CVD. | [s3](#evidence-3) |
| Stroke type / 卒中分型 | Not available | MCQ160F/180F supply any stroke with no type. | [s4](#evidence-4) |
| Stroke timing / 卒中事件时间 | Confirmed | Age first told; not calendar event date or verified age of onset. | [s4](#evidence-4) |
| Brain MRI / 脑 MRI | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| CSVD / 脑小血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Alzheimer’s disease / 阿尔茨海默病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Dementia / 痴呆 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Cognition / 认知功能 | Uncertain | Do not borrow later cognitive batteries; same-cycle standardized cognitive test not confirmed. | [s10](#evidence-10) |
| Parkinson’s disease / 帕金森病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Frailty / 衰弱 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Health status / 健康状态 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Mortality / 死亡结局 | Confirmed | All-cause and limited cause-specific linkage. | [s7](#evidence-7) |
| Follow-up / 纵向随访 | Confirmed | National Death Index linkage, not repeated eye visits. | [s5](#evidence-5) |

## Counting evidence

Unknown — 本快照没有单独的图像或参与者数量核验表，已知数量及其口径见 Imaging and cohort。

## Family and derivative ledger

| Source resource | Relation | Target resource | Confidence | Scope | Evidence |
| --- | --- | --- | --- | --- | --- |
| [ext-nhanes-iii-retina](ext-nhanes-iii-retina.md) | different\_survey\_wave | [ext-nhanes-2005-2008-retina](ext-nhanes-2005-2008-retina.md) | Confirmed survey distinction | 不同抽样波次，不是同一批人随访。 | [Relationship evidence](https://www.cdc.gov/nchs/nhanes/about/) |

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Eye–Stroke — 既往自报卒中，非新发事件 | 15 / 75.0 | Not eligible / 40.0 | 2 / 4 / 4 / 0 / 2 | 卒中问卷＋分级 | 概率抽样与分级质控；公开 XPT 无像素。 |
| Retinal Aging — 公开分级、人口学与死亡 | 9 / 85.0 | Not eligible / 46.25 | 3 / 4 / 4 / 0 / 2 | 可分级子集；原始像素未核实 | 概率抽样与分级质控；公开 XPT 无像素。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/OPXRET_D.htm)

## Sources

<a id="evidence-1"></a>

### s1

[Open original source](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/OPXRET_D.htm)

Component/eligibility, protocol, analytic notes and SEQN codebook. Eligible ≥40 years, two images/eye, Canon camera, per-eye grading; file type XPT.

Recorded check date — 2026-11-03.

<a id="evidence-2"></a>

### s2

[Open original source](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2007/DataFiles/OPXRET_E.htm)

Component Description, Quality Control and codebook; SEQN-keyed 2007–2008 grades.

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s3

[Open original source](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/MCQ_D.htm)

MCQ160F and MCQ180F; respondent-level history and age at first diagnosis; CVD/coronary disease items included.

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### s4

[Open original source](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2007/DataFiles/MCQ_E.htm)

Variable labels: self-reported stroke history and age first told, no event date or stroke subtype in these fields.

Recorded check date — 2026-11-03.

<a id="evidence-5"></a>

### s5

[Open original source](https://www.cdc.gov/nchs/linked-data/mortality-files/)

Public-use NDI-linked files, NHANES eligibility, limited released mortality variables; some variables receive synthetic values.

Recorded check date — 2026-11-03.

<a id="evidence-6"></a>

### s6

[Open original source](https://pmc.ncbi.nlm.nih.gov/articles/PMC10275905/)

Study population/flow; paired retinal-grade and stroke records across 2005–2008: 5,371 graded, 4,570 complete for analysis.

Recorded check date — 2026-11-03.

<a id="evidence-7"></a>

### s7

[Open original source](https://pubmed.ncbi.nlm.nih.gov/37680275/)

Methods; jointly analysed 2005–2008 grades and NDI-linked follow-up through 2019.

Recorded check date — 2026-11-03.

<a id="evidence-8"></a>

### s8

[Open original source](https://wwwn.cdc.gov/nchs/data/nhanes/public/2007/manuals/manual_op.pdf)

Sec. 3.4.1; acquisition system made participant/eye-coded TIFFs. Does not describe public distribution.

Recorded check date — 2026-11-03.

<a id="evidence-9"></a>

### s9

[Open original source](https://wwwn.cdc.gov/nchs/nhanes/search/variablelist.aspx?Cycle=2005-2006)

RIDAGEYR, RIAGENDR, BPQ020, DIQ010 and corresponding file names. Check each cycle for top-coding.

Recorded check date — 2026-11-03.

<a id="evidence-10"></a>

### s10

[Open original source](https://www.cdc.gov/healthy-aging-data/nhanes/index.html)

CDC cognitive performance page lists selected later adult cycles, distinct from these retinal imaging cycles.

Recorded check date — 2026-11-03.

<a id="evidence-11"></a>

### s11

[Open original source](https://ftp.cdc.gov/pub/health_statistics/nchs/datalinkage/linked_mortality/)

Official public-use file listing includes separate NHANES 2005–06/2007–08 \_MORT\_2019\_PUBLIC.dat.

Recorded check date — 2026-11-03.
