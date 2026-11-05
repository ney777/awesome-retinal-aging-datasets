# UK Biobank Eye and Vision / UK Biobank Repeat Imaging

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

Published same-participant outcomes across age, stroke, OCT–MRI, dementia and PD; separated eye fields and repeat instances.

当前核验的影像与模态范围 — Fundus; OCT; brain MRI in a subset

Image availability — Confirmed bulk CFP/OCT data fields under approved UKB-RAP project; new applications paused on cited page.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | ext-uk-biobank |
| Name / 名称 | UK Biobank Eye and Vision / UK Biobank Repeat Imaging |
| Acronym / 缩写 | UKB |
| Official resource | [https://www.ukbiobank.ac.uk/about-our-data/types-of-data/imaging-data/](https://www.ukbiobank.ac.uk/about-our-data/types-of-data/imaging-data/) |
| Country or region / 国家地区 | United Kingdom |
| Institution / 机构 | UK Biobank; UK Biobank Eye and Vision Consortium |
| Reported year / 年份口径 | 2022 (online publication of retinal grading report; print 2023) |
| Publication date | Unknown |
| Date scope | Unknown |
| Date evidence | Unknown |
| Date reviewed | Unknown |
| Original citation | Warwick AN et al. UK Biobank retinal imaging grading: methodology, baseline characteristics and findings for common ocular diseases. Eye. Online 2022; print 2023 (PubMed 36329166; correction 36604558). |
| Publication DOI | [10.1038/s41433-022-02298-7](https://doi.org/10.1038/s41433-022-02298-7) |
| Dataset DOI | Unknown |
| Import origin | Extension |
| Original EyeDataHub ID | Unknown |
| Dataset family | UK Biobank |
| Family or derivative relation | Cohort family; eye, brain, repeat assessment, outcome subsets and secondary papers are overlapping facets. |
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
| Modalities / 影像模态 | Fundus; OCT; brain MRI in a subset |
| Images / 图像数及口径 | Aug 2025 Showcase, 102,971 left-eye field items and 104,504 right-eye field items across instances; counts include repeats. Historical 2009–2010 grading paper reports 121,260 gradable eyes. |
| Participants / 参与者数及口径 | 2009–2010: 68,514 attended, 68,504 had ≥1 CFP; 64,367 had ≥1 gradable CFP. Not the all-instances union. |
| Eyes / 眼别 | Left/right coded separately; unilateral missingness possible. |
| Device / 设备 | Topcon 3D OCT-1000 Mark II; single-field 45° CFP (baseline reported protocol). |
| Resolution / 分辨率 | Unknown |
| Quality / 质量控制 | Separate grades; gradeable denominators differ by eye and endpoint. |
| Multiple visits / 多时点 | Yes; Showcase instances per eye. Repeated observations apply only to a subset. |
| Multiple modalities / 多模态 | Yes; OCT + CFP, brain MRI in an overlapping subset. |
| Multiple centers / 多中心 | Yes; recruitment/assessment centres, imaging availability varies by centre and instance. |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Controlled access |
| Access or application route | [https://www.ukbiobank.ac.uk/use-our-data/apply-for-access/](https://www.ukbiobank.ac.uk/use-our-data/apply-for-access/) |
| Image files / 影像文件 | Confirmed bulk CFP/OCT data fields under approved UKB-RAP project; new applications paused on cited page. |
| Individual labels / 个体标签 | Confirmed controlled participant-level linkage, depending on approved tier/fields and consent. |
| Data license / 数据许可 | UK Biobank project agreement; not an open image licence. |
| Research use / 科研条件 | Eligible researchers, public-interest health research, approved project, institutional agreement and fees; RAP compute/storage costs additional. |
| Commercial use / 商业用途 | Eligible scientific researchers in commercial organisations can apply on the public-interest health-research terms; no general commercial reuse right. |
| Terms scope | Unknown |
| Terms evidence | Unknown |
| Upstream route review date | Unknown |
| Upstream acquisition support | Unknown |
| Upstream access friction | Unknown |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | Approved project participant ID + assessment instance + laterality for retinal bulk fields. Define imaging index date and match hospital/death follow-up or MRI instance explicitly. 46,969 people passed QC in a historical age/stroke study (35,917 held out after healthy age-training group); not the whole UKB or the eye–MRI intersection. |
| Strengths / 主要优点 | Published same-participant outcomes across age, stroke, OCT–MRI, dementia and PD; separated eye fields and repeat instances. |
| Limitations / 关键缺陷 | New application intake shown as paused at 2026-11-03 (planned late-2026 opening is not confirmation); selection by imaging/QC/healthy volunteer and different exam dates. Age gap is a prediction residual; individual biological age is not ground truth. |
| Suggested experiments / 建议实验 | Train a patient-split chronological-age model in the disease-free baseline subset. Estimate independent age-bias correction; compare a clinical stroke-risk baseline against baseline+age gap under time-to-event analysis with an external cohort. Audit MRI temporal offsets, withdrawals and follow-up. |
| Retinal Aging suitability | A: Chronological age with CFP and mortality follow-up in same individuals. |
| Stroke / CSVD suitability | B: Subsequent stroke ascertained from linked hospital/death records. \| C: Same individuals with OCT morphology and brain MRI; see s11 for WMH field. |
| AD / Dementia suitability | D: Baseline OCT linked to incident AD/FTD diagnoses; s10 also supports cognition/dementia. |
| Multicenter model suitability | G: Bilateral multimodal source for pretraining/transfer; independent external centres still needed. |
| Screening rationale / 筛查理由 | Chronological age with CFP and mortality follow-up in same individuals. \| Subsequent stroke ascertained from linked hospital/death records. \| Same individuals with OCT morphology and brain MRI; see s11 for WMH field. \| Baseline OCT linked to incident AD/FTD diagnoses; s10 also supports cognition/dementia. \| Person-level PD ICD record linked to acquisition dates. \| Incident CVD and mortality were evaluated in eye-imaged participants. \| Bilateral multimodal source for pretraining/transfer; independent external centres still needed. |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 1 | Tier 1 | Chronological age with CFP and mortality follow-up in same individuals. | [s6](#evidence-6) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Tier 1 | Tier 1 | Subsequent stroke ascertained from linked hospital/death records. | [s5](#evidence-5) |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Tier 1 | Tier 1 | Same individuals with OCT morphology and brain MRI; see s11 for WMH field. | [s7](#evidence-7) |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Tier 1 | Tier 1 | Baseline OCT linked to incident AD/FTD diagnoses; s10 also supports cognition/dementia. | [s8](#evidence-8) |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Tier 1 | Tier 1 | Person-level PD ICD record linked to acquisition dates. | [s9](#evidence-9) |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Tier 1 | Tier 1 | Incident CVD and mortality were evaluated in eye-imaged participants. | [s10](#evidence-10) |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Tier 3 | Tier 3 | Bilateral multimodal source for pretraining/transfer; independent external centres still needed. | [s2](#evidence-2) |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | Chronological age, not a biological-age label. | [s6](#evidence-6) |
| Sex / 性别 | Confirmed | Sex-stratified eye analyses. | [s10](#evidence-10) |
| Hypertension / 高血压 | Confirmed | Hypertension covariate, algorithm and measurement to reproduce from original study. | [s5](#evidence-5) |
| Diabetes / 糖尿病 | Confirmed | Diabetes covariate in retinal-stroke models. | [s5](#evidence-5) |
| Cardiovascular disease / 心血管病 | Confirmed | Incident CVD. | [s10](#evidence-10) |
| Stroke type / 卒中分型 | Confirmed | ICD I60/I61/I63/I64 identify coded categories incl. unspecified; not all clinically adjudicated subtypes. | [s5](#evidence-5) |
| Stroke timing / 卒中事件时间 | Confirmed | First recorded stroke after baseline; hospital/death linkage. | [s5](#evidence-5) |
| Brain MRI / 脑 MRI | Confirmed | Direct overlapping eye + brain MRI subset. | [s7](#evidence-7) |
| CSVD / 脑小血管病 | Confirmed | WMH volume exists at person/instance level; compute paired usable N after approval. | [s11](#evidence-11) |
| Alzheimer’s disease / 阿尔茨海默病 | Confirmed | Incident clinical AD diagnosis, not biomarker-confirmed in every case. | [s8](#evidence-8) |
| Dementia / 痴呆 | Confirmed | Incident dementia. | [s10](#evidence-10) |
| Cognition / 认知功能 | Confirmed | Cognitive performance. | [s10](#evidence-10) |
| Parkinson’s disease / 帕金森病 | Confirmed | ICD-coded prevalent/incident PD; attrition severe after QC. | [s9](#evidence-9) |
| Frailty / 衰弱 | Confirmed | Research-derived FI, not a clinician-assigned gold standard. | [s14](#evidence-14) |
| Health status / 健康状态 | Confirmed | Healthy reference subset by study-specific disease exclusion. | [s5](#evidence-5) |
| Mortality / 死亡结局 | Confirmed | All-cause registry follow-up. | [s6](#evidence-6) |
| Follow-up / 纵向随访 | Confirmed | Time to first recorded stroke/end of observation. | [s5](#evidence-5) |

## Counting evidence

Unknown — 本快照没有单独的图像或参与者数量核验表，已知数量及其口径见 Imaging and cohort。

## Family and derivative ledger

Unknown — 未记录具体的资源关系边。患者或影像重叠情况仍见 Identity and provenance。

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Eye–Neurodegeneration — 新发 AD、痴呆及 PD | 1 / 97.5 | Not eligible / 53.75 | 4 / 4 / 4 / 0 / 3 | OCT 与痴呆队列，PD 分析另外计 | 多评估中心，受控 RAP；新申请暂停。 |
| Eye–Stroke — 新发卒中；另有脑 MRI 指标 | 1 / 97.5 | Not eligible / 53.75 | 4 / 4 / 4 / 0 / 3 | 既往无卒中、论文可评估者；MRI 交集另计 | 多评估中心，受控 RAP；新申请暂停。 |
| Retinal Aging — 年龄、死亡与重复评估 | 1 / 97.5 | Not eligible / 53.75 | 4 / 4 / 4 / 0 / 3 | 可分级 CFP 基线人数（不是 repeat × outcome 全部交集） | 多评估中心，受控 RAP；新申请暂停。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://www.ukbiobank.ac.uk/about-our-data/types-of-data/imaging-data/)

## Sources

<a id="evidence-1"></a>

### s1

[Open original source](https://pubmed.ncbi.nlm.nih.gov/36329166/)

Warwick et al., abstract, Results; baseline attendance, at least one photograph, graded photographs and gradeable eyes. See linked correction before using full tables.

Recorded check date — 2026-11-03.

<a id="evidence-2"></a>

### s2

[Open original source](https://biobank.ndph.ox.ac.uk/ukb/label.cgi?id=725)

Category 725, bulk fields 21015/21016 bilateral CFP and 21017/21018 OCT slices; 21011–21014 native OCT.

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s3

[Open original source](https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=21015)

Aug 2025 item count and assessment instances for left-eye field.

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### s4

[Open original source](https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=21016)

Aug 2025 item count and assessment instances for right-eye field.

Recorded check date — 2026-11-03.

<a id="evidence-5"></a>

### s5

[Open original source](https://pmc.ncbi.nlm.nih.gov/articles/PMC9710167/)

Methods, stroke ascertainment and statistical analysis; imaging cohort, healthy age training subset, linkage to hospital admission/death, first stroke timing, ICD codes I60/I61/I63/I64.

Recorded check date — 2026-11-03.

<a id="evidence-6"></a>

### s6

[Open original source](https://pubmed.ncbi.nlm.nih.gov/35042683/)

Methods; 80,169 selected CFP from 46,969 participants with chronological age and subsequent death follow-up.

Recorded check date — 2026-11-03.

<a id="evidence-7"></a>

### s7

[Open original source](https://pubmed.ncbi.nlm.nih.gov/33369822/)

Methods and Results; same-person macular OCT layers and brain MRI regional volumes; MRI subset independent of larger CFP counts.

Recorded check date — 2026-11-03.

<a id="evidence-8"></a>

### s8

[Open original source](https://pubmed.ncbi.nlm.nih.gov/39868381/)

Methods and Results; baseline UKB retinal OCT was followed for clinical AD and FTD diagnoses.

Recorded check date — 2026-11-03.

<a id="evidence-9"></a>

### s9

[Open original source](https://doi.org/10.1038/s41598-024-54251-1)

Methods/data flow; PD derived from linked clinical records with status relative to fundus date; 296 people before image QC, 84 PD cases retained in matched analysis.

Recorded check date — 2026-11-03.

<a id="evidence-10"></a>

### s10

[Open original source](https://www.ukbiobank.ac.uk/publications/deep-learning-aging-marker-from-retinal-images-unveils-sex-specific-clinical-and-genetic-signatures/)

Abstract; chronological age/sex, cognitive performance, incident dementia/CVD and all-cause mortality in UKB retinal image analysis.

Recorded check date — 2026-11-03.

<a id="evidence-11"></a>

### s11

[Open original source](https://biobank.ndph.ox.ac.uk/ukb/field.cgi?id=25781)

Total WMH volume in mm³ from T1/T2 FLAIR. Field existence confirmed; intersection with fundus after QC not enumerated here.

Recorded check date — 2026-11-03.

<a id="evidence-12"></a>

### s12

[Open original source](https://www.ukbiobank.ac.uk/use-our-data/apply-for-access/)

Apply for access notice: new applications paused for platform changes; late 2026 intended reopening. Scientific researchers including commercial organisations, public interest requirement.

Recorded check date — 2026-11-03.

<a id="evidence-13"></a>

### s13

[Open original source](https://www.ukbiobank.ac.uk/use-our-data/fees/)

Fees section: approved tier and UKB-RAP compute/storage charges.

Recorded check date — 2026-11-03.

<a id="evidence-14"></a>

### s14

[Open original source](https://pubmed.ncbi.nlm.nih.gov/42837054/)

Methods; image-based retinal parameters paired with constructed frailty index and systemic aging indices in 45,542 UKB participants.

Recorded check date — 2026-11-03.

<a id="evidence-15"></a>

### s15

[Open original source](https://pmc.ncbi.nlm.nih.gov/articles/PMC8261460/)

Participants/methods; baseline was collected at 22 centres; OCT/brain MRI analysis.

Recorded check date — 2026-11-03.

<a id="evidence-16"></a>

### s16

[Open original source](https://doi.org/10.1038/s41467-026-77102-1)

Methods, fundus photography acquisition; Topcon 3D OCT-1000 Mark II and field of view.

Recorded check date — 2026-11-03.

<a id="evidence-17"></a>

### s17

[Open original source](https://www.ukbiobank.ac.uk/about-us/how-we-work/access-to-uk-biobank-data/)

Access checks, legal agreement and controlled research platform.

Recorded check date — 2026-11-03.

<a id="evidence-18"></a>

### adfull

[Open original source](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2024.1513302/full)

Discussion and cohort methods: 30,573 UK Biobank participants with baseline OCT for incident dementia analyses, separate MRI subset.

Recorded check date — 2026-11-03.
