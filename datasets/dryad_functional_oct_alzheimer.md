# Functional OCT Retinal Response Dataset (Bissig)

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

有逐人诊断分组、实验条件和可解析的影像。

当前核验的影像与模态范围 — SD-OCT

Image availability — Repository lists 2020 RAR with processed/raw-stage ANALYZE images; Dryad authenticated transfer route recorded by EyeDataHub.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | dryad\_functional\_oct\_alzheimer |
| Name / 名称 | Functional OCT Retinal Response Dataset (Bissig) |
| Acronym / 缩写 | Unknown |
| Official resource | [https://datadryad.org/dataset/doi:10.5061/dryad.msbcc2ftc](https://datadryad.org/dataset/doi:10.5061/dryad.msbcc2ftc) |
| Country or region / 国家地区 | United States |
| Institution / 机构 | Oregon Health &amp; Science University (deposit affiliation) |
| Reported year / 年份口径 | 2019 |
| Publication date | 2019-11-18 |
| Date scope | initial\_public\_release |
| Date evidence | [https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.msbcc2ftc/versions](https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.msbcc2ftc/versions) |
| Date reviewed | 2026-09-11 |
| Original citation | Bissig D, Zhou CG, Le V, Bernard JT. Optical coherence tomography reveals light-dependent retinal responses in Alzheimer’s disease. NeuroImage. 2020. Dataset DOI 10.5061/dryad.msbcc2ftc. |
| Publication DOI | [10.1016/j.neuroimage.2020.117022](https://doi.org/10.1016/j.neuroimage.2020.117022) |
| Dataset DOI | [10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc) |
| Import origin | EyeDataHub v0.7.0 |
| Original EyeDataHub ID | dryad\_functional\_oct\_alzheimer |
| Dataset family | dryad\_functional\_oct\_alzheimer |
| Family or derivative relation | Zenodo record 4935639 mirrors Dryad; repeated/processed image objects and release versions are not new cohorts. |
| Independence / overlap | Independence unverified |
| Upstream family ID | dryad\_functional\_oct\_alzheimer |
| Upstream resource role | current\_dataset |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 1 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | Repeated light/dark SD-OCT acquisitions and retinal reflectivity profiles from healthy, neuromyelitis-optica, and Alzheimer groups. |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | SD-OCT |
| Images / 图像数及口径 | 432 .img files reported in EyeDataHub's deposit audit, include derived copies; not 432 independent acquisitions. |
| Participants / 参与者数及口径 | 40 unique IDs in repository profile tables across experiments; AD experiment compares 14 early-onset AD and 14 age-matched controls. |
| Eyes / 眼别 | Experiment 4 targets one retinal slice per participant; laterality across entire release unverified. |
| Device / 设备 | Heidelberg SPECTRALIS SD-OCT |
| Resolution / 分辨率 | 3.89 μm isometric resampled pixels; 30° slice for experiments 1,3,4. |
| Quality / 质量控制 | Usage notes give per-experiment exclusions and manual processing. |
| Multiple visits / 多时点 | Repeated conditions within visit; long-term follow-up not documented. |
| Multiple modalities / 多模态 | Unknown |
| Multiple centers / 多中心 | Unknown |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Registration |
| Access or application route | [https://datadryad.org/dataset/doi:10.5061/dryad.msbcc2ftc](https://datadryad.org/dataset/doi:10.5061/dryad.msbcc2ftc) |
| Image files / 影像文件 | Repository lists 2020 RAR with processed/raw-stage ANALYZE images; Dryad authenticated transfer route recorded by EyeDataHub. |
| Individual labels / 个体标签 | SubjectID folders + profile tables link experimental cohorts and age ranges. Not exact ages. |
| Data license / 数据许可 | CC0 1.0 (dataset) |
| Research use / 科研条件 | Cite dataset; extract v6 archive; Dryad API token for automated retrieval. |
| Commercial use / 商业用途 | CC0 for dataset files; no separate commercial restriction identified. |
| Terms scope | dataset\_files |
| Terms evidence | [https://doi.org/10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc) |
| Upstream route review date | 2026-07-21 |
| Upstream acquisition support | end\_to\_end\_tested |
| Upstream access friction | self\_service\_authenticated |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | SubjectID with light/dark condition; AD experiment n=14+14, AQP4 sample n=3. Image derivatives and acquisitions from one subject must stay in same split. |
| Strengths / 主要优点 | 有逐人诊断分组、实验条件和可解析的影像。 |
| Limitations / 关键缺陷 | AD 病例仅 14 人；年龄按区间；刺激周期非长期随访；不同实验部分人重叠。 |
| Suggested experiments / 建议实验 | 逐人留一分析光暗反射差值，区分 AD 与同龄对照，报告每位受试者权重及区间。 |
| Retinal Aging suitability | A: 按受试者可对应年龄段；不支持连续年龄回归。 |
| Stroke / CSVD suitability | Unknown |
| AD / Dementia suitability | D: 早发 AD 病例和匹配对照，SubjectID 与像素配对。 |
| Multicenter model suitability | Unknown |
| Screening rationale / 筛查理由 | 按受试者可对应年龄段；不支持连续年龄回归。 \| 早发 AD 病例和匹配对照，SubjectID 与像素配对。 \| AQP4 抗体神经疾病机制样本 3 人。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 1 | Tier 1 | 按受试者可对应年龄段；不支持连续年龄回归。 | [s1](#evidence-2) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Tier 1 | Tier 1 | 早发 AD 病例和匹配对照，SubjectID 与像素配对。 | [s1](#evidence-2) |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Tier 1 | Tier 1 | AQP4 抗体神经疾病机制样本 3 人。 | [s1](#evidence-2) |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Unknown | Unknown | No topic-specific finding | Unknown |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | 年龄区间，个体精确年龄无 | [s1](#evidence-2) |
| Sex / 性别 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Hypertension / 高血压 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Diabetes / 糖尿病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Cardiovascular disease / 心血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Stroke type / 卒中分型 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Stroke timing / 卒中事件时间 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Brain MRI / 脑 MRI | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| CSVD / 脑小血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Alzheimer’s disease / 阿尔茨海默病 | Confirmed | 早发 AD 14；分组诊断 | [s1](#evidence-2) |
| Dementia / 痴呆 | Uncertain | 仅记录 AD 组；未提供独立的全因痴呆标签或严重程度。 | [s1](#evidence-2) |
| Cognition / 认知功能 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Parkinson’s disease / 帕金森病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Frailty / 衰弱 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Health status / 健康状态 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Mortality / 死亡结局 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Follow-up / 纵向随访 | Not available | 本发布是同次检查光暗刺激条件重复，不含长期结局 | [s1](#evidence-2) |

## Counting evidence

| Count | Unit | Scope | Evidence basis | Exactness | Source |
| --- | --- | --- | --- | --- | --- |
| 40 | participants | Unique participant identifiers across the two deposited profile tables in Dryad version 6 | current\_deposit\_table | exact | [Quantity source](https://doi.org/10.5061/dryad.msbcc2ftc) |
| 1370 | rows | Processed retinal-reflectivity profile rows across the two deposited tables | current\_deposit\_table | exact | [Quantity source](https://doi.org/10.5061/dryad.msbcc2ftc) |
| 432 | images | ANALYZE-format .img objects in the Dryad version 6 archive | current\_deposit\_file\_listing | exact | [Quantity source](https://doi.org/10.5061/dryad.msbcc2ftc) |
| 1 | deposited\_files | RAR archive in Dryad version 6 | current\_deposit\_file\_listing | exact | [Quantity source](https://doi.org/10.5061/dryad.msbcc2ftc) |
| 8 | group\_enrollments | Healthy young-adult experiment | official\_source\_description | exact | [Quantity source](https://doi.org/10.5061/dryad.msbcc2ftc) |
| 3 | group\_enrollments | Aquaporin-4 antibody experiment | official\_source\_description | exact | [Quantity source](https://doi.org/10.5061/dryad.msbcc2ftc) |
| 14 | group\_enrollments | Early-onset Alzheimer group | official\_source\_description | exact | [Quantity source](https://doi.org/10.5061/dryad.msbcc2ftc) |
| 14 | group\_enrollments | Age-matched control group | official\_source\_description | exact | [Quantity source](https://doi.org/10.5061/dryad.msbcc2ftc) |

## Family and derivative ledger

Unknown — 未记录具体的资源关系边。患者或影像重叠情况仍见 Identity and provenance。

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Eye–Neurodegeneration — 功能 OCT、早发 AD 病例对照 | 19 / 45.0 | 2 / 60.0 | 3 / 1 / 1 / 3 / 1 | 14 EOAD ＋ 14 年龄匹配对照 | 数据包与病例映射明确；按平台流程获取，机制样本很小。 |
| Retinal Aging — 年龄段，非连续回归 | 39 / 25.0 | Not eligible / 47.5 | 1 / 1 / 1 / 3 / 1 | AD 比较子集；年龄为区间 | 数据包与病例映射明确；按平台流程获取，机制样本很小。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://datadryad.org/dataset/doi:10.5061/dryad.msbcc2ftc)

## Sources

<a id="evidence-1"></a>

### base

[Open original source](https://doi.org/10.5061/dryad.msbcc2ftc)

EyeDataHub v0.7.0 → dryad\_functional\_oct\_alzheimer; catalog fields and dated source review, not a new clinical audit.

Recorded check date — 2026-07-21.

<a id="evidence-2"></a>

### s1

[Open original source](https://datadryad.org/dataset/doi:10.5061/dryad.msbcc2ftc)

Abstract, Methods and Usage notes: IDs in filenames, 14 AD + 14 controls, 3 AQP4 subjects, SD-OCT acquisition and QC; PROFILE\_DATA\_for\_Dryad lists age ranges.

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s2

[Open original source](https://khosravipooya.com/EyeDataHub/datasets/dryad_functional_oct_alzheimer/)

Reported quantities/transfer audit: 40 unique IDs, 432 derivative-inclusive ANALYZE objects, authenticated route, dataset CC0.

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### s3

[Open original source](https://zenodo.org/records/4935639)

Mirror cites same Dryad DOI, source dataset and experiments.

Recorded check date — 2026-11-03.

<a id="evidence-5"></a>

### s4

[Open original source](https://pubmed.ncbi.nlm.nih.gov/32512126/)

Peer-reviewed linked NeuroImage article; its title differs from the Dryad deposit title.

Recorded check date — 2026-11-03.
