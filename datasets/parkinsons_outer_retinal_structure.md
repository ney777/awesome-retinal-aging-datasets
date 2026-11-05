# Parkinson outer retinal structure/function (Tran; individual OCT measurements)

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

可立即做 PD 个体派生表型复核；同日用药前后可区分。

当前核验的影像与模态范围 — OCT-derived thickness \| ERG \| psychophysics (no pixels)

Image availability — Not available in deposit: two measurement XLSX files only.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | parkinsons\_outer\_retinal\_structure |
| Name / 名称 | Parkinson outer retinal structure/function (Tran; individual OCT measurements) |
| Acronym / 缩写 | Unknown |
| Official resource | [https://doi.org/10.26188/24138420.v2](https://doi.org/10.26188/24138420.v2) |
| Country or region / 国家地区 | Australia |
| Institution / 机构 | University of Melbourne |
| Reported year / 年份口径 | 2023 |
| Publication date | 2023-09-14 |
| Date scope | initial\_public\_release |
| Date evidence | [https://api.figshare.com/v2/articles/24138420/versions/1](https://api.figshare.com/v2/articles/24138420/versions/1) |
| Date reviewed | 2026-09-11 |
| Original citation | Tran KKN et al. Altered Outer Retinal Structure, Electrophysiology and Visual Perception in Parkinson's Disease. J Parkinsons Dis. 2024. Dataset DOI 10.26188/24138420.v2. |
| Publication DOI | [10.3233/JPD-230293](https://doi.org/10.3233/JPD-230293) |
| Dataset DOI | [10.26188/24138420.v2](https://doi.org/10.26188/24138420.v2) |
| Import origin | EyeDataHub v0.7.0 |
| Original EyeDataHub ID | parkinsons\_outer\_retinal\_structure |
| Dataset family | Parkinson outer retinal structure (Melbourne, Tran) |
| Family or derivative relation | Two XLSX files are revisions; do not concatenate. Connection to directional OCT source unresolved. |
| Independence / overlap | Independence unverified |
| Upstream family ID | parkinsons\_outer\_retinal\_structure |
| Upstream resource role | current\_dataset |
| Review depth | Source-reviewed |
| Best recorded topic tier | Excluded |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | Retinal structure, electrophysiology, and visual-perception measurements from Parkinson disease and comparison participants. |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | OCT-derived thickness \| ERG \| psychophysics (no pixels) |
| Images / 图像数及口径 | Unknown |
| Participants / 参与者数及口径 | 16 PD, 21 age-matched controls enrolled; OCT worksheet is smaller than enrolled cohort. |
| Eyes / 眼别 | Tested eye is recorded. |
| Device / 设备 | Unknown |
| Resolution / 分辨率 | Unknown |
| Quality / 质量控制 | Unknown |
| Multiple visits / 多时点 | Two assessments in same visit, before/after L-DOPA or matched time. |
| Multiple modalities / 多模态 | Yes (measurements) |
| Multiple centers / 多中心 | Unknown |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Open download |
| Access or application route | [https://doi.org/10.26188/24138420.v2](https://doi.org/10.26188/24138420.v2) |
| Image files / 影像文件 | Not available in deposit: two measurement XLSX files only. |
| Individual labels / 个体标签 | Px ID + diagnostic-group sheet + demographic and OCT layers. Normalize whitespace in IDs across worksheets. |
| Data license / 数据许可 | CC BY 4.0 |
| Research use / 科研条件 | Attribution; use revised v2 workbook. |
| Commercial use / 商业用途 | CC BY 4.0 subject to attribution. |
| Terms scope | dataset\_files |
| Terms evidence | [https://doi.org/10.26188/24138420.v2](https://doi.org/10.26188/24138420.v2) |
| Upstream route review date | 2026-08-02 |
| Upstream acquisition support | standard\_platform\_supported |
| Upstream access friction | self\_service\_authenticated |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | Within XLSX, ID and eye join measured thickness to age, sex and PD group. Demographic vs OCT IDs contain spacing differences. No public OCT images. |
| Strengths / 主要优点 | 可立即做 PD 个体派生表型复核；同日用药前后可区分。 |
| Limitations / 关键缺陷 | 无像素，不纳入影像监督验证；同日重复不反映疾病进展。 |
| Suggested experiments / 建议实验 | 使用修订表按受试者 ID 和眼别关联层厚与诊断，进行协变量调整的探索性复现。 |
| Retinal Aging suitability | A: 年龄仅配派生测量，未提供眼底像素。 |
| Stroke / CSVD suitability | Unknown |
| AD / Dementia suitability | Unknown |
| Multicenter model suitability | Unknown |
| Screening rationale / 筛查理由 | 年龄仅配派生测量，未提供眼底像素。 \| 逐人 PD–OCT 派生层厚可分析；像素影像专题排除。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Excluded | Excluded | 年龄仅配派生测量，未提供眼底像素。 | [s2](#evidence-3) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Excluded | Excluded | 逐人 PD–OCT 派生层厚可分析；像素影像专题排除。 | [s2](#evidence-3) |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Unknown | Unknown | No topic-specific finding | Unknown |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | 逐人年龄（派生表） | [s2](#evidence-3) |
| Sex / 性别 | Confirmed | 逐人性别（派生表） | [s2](#evidence-3) |
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
| Parkinson’s disease / 帕金森病 | Confirmed | 逐人诊断/分组（派生表） | [s2](#evidence-3) |
| Frailty / 衰弱 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Health status / 健康状态 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Mortality / 死亡结局 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Follow-up / 纵向随访 | Not available | 仅同次就诊内重复，无长期随访 | [s1](#evidence-2) |

## Counting evidence

Unknown — 本快照没有单独的图像或参与者数量核验表，已知数量及其口径见 Imaging and cohort。

## Family and derivative ledger

Unknown — 未记录具体的资源关系边。患者或影像重叠情况仍见 Identity and provenance。

## Research priorities

Unknown — 本资源未进入当前三个科研方向的候选排名。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://doi.org/10.26188/24138420.v2)

## Sources

<a id="evidence-1"></a>

### base

[Open original source](https://doi.org/10.26188/24138420.v2)

EyeDataHub v0.7.0 → parkinsons\_outer\_retinal\_structure; catalog fields and dated source review, not a new clinical audit.

Recorded check date — 2026-08-02.

<a id="evidence-2"></a>

### s1

[Open original source](https://api.figshare.com/v2/articles/24138420/versions/2)

Figshare v2 description/files/license: PD n=16, controls n=21, age 41–85; two measurements in one visit; two Excel files.

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s2

[Open original source](https://ndownloader.figshare.com/files/43121452)

Inspected revised workbook: Ctrl/PD Demographic Data and OCT Data use Px ID, eye, Age, Sex, and pre/post layer thickness; no pixel objects.

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### s3

[Open original source](https://pubmed.ncbi.nlm.nih.gov/38189711/)

Original cross-sectional study methods; 16 PD and 21 controls.

Recorded check date — 2026-11-03.
