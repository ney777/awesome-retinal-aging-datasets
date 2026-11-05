# TREND2 chronic-disease fundus study

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

可立即复核的黑山公共小样本；逐文件 AD、HTN、DM2 可查。

当前核验的影像与模态范围 — Fundus

Image availability — Anonymous ZIPs with TIFF originals and masks.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | trend2\_fundus |
| Name / 名称 | TREND2 chronic-disease fundus study |
| Acronym / 缩写 | TREND2 |
| Official resource | [https://zenodo.org/records/7678656](https://zenodo.org/records/7678656) |
| Country or region / 国家地区 | Montenegro |
| Institution / 机构 | Faculty of Medicine, University of Montenegro |
| Reported year / 年份口径 | 2023 |
| Publication date | 2023-02-26 |
| Date scope | initial\_public\_release |
| Date evidence | [https://zenodo.org/api/records/7678656](https://zenodo.org/api/records/7678656) |
| Date reviewed | 2026-09-11 |
| Original citation | Popovic N et al. Topological characterization of the retinal microvascular network visualized by portable fundus camera—effects of chronic disease (TREND2). Zenodo v1.1, 2023. |
| Publication DOI | Unknown |
| Dataset DOI | [10.5281/zenodo.7678656](https://doi.org/10.5281/zenodo.7678656) |
| Import origin | EyeDataHub v0.7.0 |
| Original EyeDataHub ID | trend2\_fundus |
| Dataset family | TREND / TREND2 |
| Family or derivative relation | Extension to TREND; participant overlap with TREND unverified. Masks are derivatives, not extra images. |
| Independence / overlap | Potential reuse; see relationship ledger |
| Upstream family ID | trend2\_fundus |
| Upstream resource role | extension\_dataset |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 1 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | Extension of TREND portable fundus imaging for chronic-disease and microvascular analysis. |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | Fundus |
| Images / 图像数及口径 | 28 original color photos, 28 corresponding masks. |
| Participants / 参与者数及口径 | 28 distinct ID-eye stems; number of independently verified people not stated by deposit. |
| Eyes / 眼别 | L/R suffix; 28 unique ID-eye stems matched to original TIFFs. |
| Device / 设备 | MiiS HORUS Scope DEC 200, 45° |
| Resolution / 分辨率 | 2560 × 1920 |
| Quality / 质量控制 | Manual retinal vessel masks; image exclusion criteria include bilateral media opacity. |
| Multiple visits / 多时点 | No repeat visits documented |
| Multiple modalities / 多模态 | Unknown |
| Multiple centers / 多中心 | Unknown |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Open download |
| Access or application route | [https://zenodo.org/records/7678656](https://zenodo.org/records/7678656) |
| Image files / 影像文件 | Anonymous ZIPs with TIFF originals and masks. |
| Individual labels / 个体标签 | 28/28 Excel ID\# stems matched to the two raw ZIPs’ TIFF filenames. Workbook includes HTN 18 positive, DM2 8 positive, AD 7 positive. |
| Data license / 数据许可 | CC BY 4.0 (EyeDataHub dataset terms) |
| Research use / 科研条件 | Cite and attribute dataset; catalog license applies to deposited material. |
| Commercial use / 商业用途 | CC BY 4.0 with attribution (scope: dataset files). |
| Terms scope | dataset\_files |
| Terms evidence | [https://zenodo.org/records/7678656](https://zenodo.org/records/7678656) |
| Upstream route review date | 2026-07-21 |
| Upstream acquisition support | standard\_platform\_supported |
| Upstream access friction | self\_service\_authenticated |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | ID\# = TIFF stem including L/R; all 28 rows mapped, 7 AD flags. Unique person count not inferred purely from eye suffix. All are age ≥56; workbook has no exact age. |
| Strengths / 主要优点 | 可立即复核的黑山公共小样本；逐文件 AD、HTN、DM2 可查。 |
| Limitations / 关键缺陷 | 仅 7 个 AD 阳性图像记录；疾病共存；不支持年龄回归、前瞻预测或临床筛查效能结论。 |
| Suggested experiments / 建议实验 | 探索同一图像的血管几何与 AD/HTN/DM2 共病关系，报告各标签共现和不确定性。 |
| Retinal Aging suitability | A: 只有全组年龄下限，没有逐人年龄列。 |
| Stroke / CSVD suitability | Unknown |
| AD / Dementia suitability | D: AD 二元列可逐 TIFF 连结。 |
| Multicenter model suitability | Unknown |
| Screening rationale / 筛查理由 | 只有全组年龄下限，没有逐人年龄列。 \| AD 二元列可逐 TIFF 连结。 \| HTN 与 DM2 二元列。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Excluded | Excluded | 只有全组年龄下限，没有逐人年龄列。 | [s2](#evidence-3) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Tier 1 | Tier 1 | AD 二元列可逐 TIFF 连结。 | [s2](#evidence-3) |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Tier 1 | Tier 1 | HTN 与 DM2 二元列。 | [s2](#evidence-3) |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Unknown | Unknown | No topic-specific finding | Unknown |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Not available | 工作簿无年龄字段；≥56 岁仅入组标准 | [s2](#evidence-3) |
| Sex / 性别 | Confirmed | Gender 编码；字典释义需确认后解释 0/1 | [s2](#evidence-3) |
| Hypertension / 高血压 | Confirmed | HTN 二元 | [s2](#evidence-3) |
| Diabetes / 糖尿病 | Confirmed | DM2 二元 | [s2](#evidence-3) |
| Cardiovascular disease / 心血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Stroke type / 卒中分型 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Stroke timing / 卒中事件时间 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Brain MRI / 脑 MRI | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| CSVD / 脑小血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Alzheimer’s disease / 阿尔茨海默病 | Confirmed | AD 二元；7 阳性 TIFF | [s2](#evidence-3) |
| Dementia / 痴呆 | Uncertain | 仅记录 AD 组；未提供独立的全因痴呆标签或严重程度。 | [s2](#evidence-3) |
| Cognition / 认知功能 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Parkinson’s disease / 帕金森病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Frailty / 衰弱 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Health status / 健康状态 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Mortality / 死亡结局 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Follow-up / 纵向随访 | Not available | 公开表无随访/时间列 | [s2](#evidence-3) |

## Counting evidence

| Count | Unit | Scope | Evidence basis | Exactness | Source |
| --- | --- | --- | --- | --- | --- |
| 28 | images | Primary color fundus images | official\_source\_description | exact | [Quantity source](https://zenodo.org/records/7678656) |

## Family and derivative ledger

| Source resource | Relation | Target resource | Confidence | Scope | Evidence |
| --- | --- | --- | --- | --- | --- |
| [trend2\_fundus](trend2_fundus.md) | extension\_of | [trend\_fundus](trend_fundus.md) | confirmed | TREND2 is described as an addition to the TREND portable-fundus resource. | [Relationship evidence](https://zenodo.org/records/7678656) |
| [trend2\_fundus](trend2_fundus.md) | extension\_of | [trend\_fundus](trend_fundus.md) | Confirmed extension; people overlap Unknown | TREND 扩展，不推断同人。 | [Relationship evidence](https://zenodo.org/records/7678656) |

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Eye–Neurodegeneration — AD 二元标记，7 阳性 ID-eye | 19 / 45.0 | 1 / 71.25 | 3 / 1 / 1 / 4 / 1 | 28 个 ID-eye，独立患者人数未知 | 公开病例列与 TIFF 名对应；仅 28 个 ID-eye，患者总数未证。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://zenodo.org/records/7678656)

## Sources

<a id="evidence-1"></a>

### base

[Open original source](https://zenodo.org/records/7678656)

EyeDataHub v0.7.0 → trend2\_fundus; catalog fields and dated source review, not a new clinical audit.

Recorded check date — 2026-07-21.

<a id="evidence-2"></a>

### s1

[Open original source](https://zenodo.org/records/7678656)

Description, Files and Inclusion Criteria: raw TIFFs 20+8, segmentations, device/resolution; ages ≥56; TREND extension.

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s2

[Open original source](https://zenodo.org/records/7678656/files/5_ASSOCIATED%20DATA.xlsx)

Inspected actual workbook Sheet 1, 28 rows; ID\#, Gender, Education, BMI, HTN, DM2, AD (last 3 binary). AD=1 in 7; no chronological age column; MD5 5ac6cdf910eb1421e7fc26b5682d9450.

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### s3

[Open original source](https://zenodo.org/records/7678656)

Raw ZIP central directories for files 1 and 3: 20+8 TIFF stems; compared both stem sets to ID\# in XLSX, 28 exact matches and 0 unmatched.

Recorded check date — 2026-11-03.

<a id="evidence-5"></a>

### s4

[Open original source](https://khosravipooya.com/EyeDataHub/datasets/trend2_fundus/)

At a glance → source-stated terms CC BY 4.0.

Recorded check date — 2026-11-03.
