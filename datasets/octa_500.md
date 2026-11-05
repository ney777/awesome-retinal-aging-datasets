# OCTA-500: Large-scale OCTA Multi-task Benchmark

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

适合验证 OCT/OCTA 的年龄信息与血管特征。

当前核验的影像与模态范围 — OCT + OCTA volumes; 3 and 6 mm fields

Image availability — Paper points to IEEE DataPort; upstream access review records password request after login.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | octa\_500 |
| Name / 名称 | OCTA-500: Large-scale OCTA Multi-task Benchmark |
| Acronym / 缩写 | OCTA-500 |
| Official resource | [https://ieee-dataport.org/open-access/octa-500](https://ieee-dataport.org/open-access/octa-500) |
| Country or region / 国家地区 | China |
| Institution / 机构 | Nanjing University of Science and Technology / Nanjing Medical University |
| Reported year / 年份口径 | 2024 (descriptor) |
| Publication date | 2019-12-23 |
| Date scope | repository\_deposit |
| Date evidence | [https://ieee-dataport.org/open-access/octa-500](https://ieee-dataport.org/open-access/octa-500) |
| Date reviewed | 2026-09-11 |
| Original citation | Li M et al. OCTA-500: A retinal dataset for optical coherence tomography angiography study. Medical Image Analysis 93:103092. |
| Publication DOI | [10.1016/j.media.2024.103092](https://doi.org/10.1016/j.media.2024.103092) |
| Dataset DOI | Unknown |
| Import origin | EyeDataHub v0.7.0 |
| Original EyeDataHub ID | octa\_500 |
| Dataset family | octa\_500 |
| Family or derivative relation | current\_dataset |
| Independence / overlap | Potential reuse; see relationship ledger |
| Upstream family ID | octa\_500 |
| Upstream resource role | current\_dataset |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 1 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | 500 subjects with OCTA volumes, vessel segmentation, FAZ (foveal avascular zone) annotations, and layer segmentation. Largest public OCTA dataset. |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | OCT + OCTA volumes; 3 and 6 mm fields |
| Images / 图像数及口径 | 361,600 scans (paper; component B-scans, not subjects) |
| Participants / 参与者数及口径 | 500 subjects |
| Eyes / 眼别 | Eye label documented |
| Device / 设备 | Unknown |
| Resolution / 分辨率 | Unknown |
| Quality / 质量控制 | Unknown |
| Multiple visits / 多时点 | Unknown |
| Multiple modalities / 多模态 | Yes — OCT and OCTA |
| Multiple centers / 多中心 | Unknown |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Author contact |
| Access or application route | [https://ieee-dataport.org/open-access/octa-500](https://ieee-dataport.org/open-access/octa-500) |
| Image files / 影像文件 | Paper points to IEEE DataPort; upstream access review records password request after login. |
| Individual labels / 个体标签 | Age, gender, eye, disease per data subject; segmentation and projection derivatives. |
| Data license / 数据许可 | IEEE DataPort Open Access (research only) |
| Research use / 科研条件 | Source reports research-only use; inspect cited terms. |
| Commercial use / 商业用途 | Unknown |
| Terms scope | dataset\_files |
| Terms evidence | [https://ieee-dataport.org/open-access/octa-500](https://ieee-dataport.org/open-access/octa-500) |
| Upstream route review date | 2026-07-21 |
| Upstream acquisition support | manual\_access\_blocked |
| Upstream access friction | author\_contact |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | Subject-indexed OCT/OCTA set with text labels for age, gender, eye, disease. |
| Strengths / 主要优点 | 适合验证 OCT/OCTA 的年龄信息与血管特征。 |
| Limitations / 关键缺陷 | 眼病标签不能替代脑病终点；登记平台与解压条件须复查。 |
| Suggested experiments / 建议实验 | 按受试者和视野分层，检验年龄与血管密度的关联，避免同一体扫描切片泄漏。 |
| Retinal Aging suitability | A: 每位受试者的年龄和眼别标签。 |
| Stroke / CSVD suitability | Unknown |
| AD / Dementia suitability | Unknown |
| Multicenter model suitability | G: 双模态解剖和血管表征。 |
| Screening rationale / 筛查理由 | 每位受试者的年龄和眼别标签。 \| 双模态解剖和血管表征。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 1 | Tier 1 | 每位受试者的年龄和眼别标签。 | [p](#evidence-2) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Tier 3 | Tier 3 | 双模态解剖和血管表征。 | [p](#evidence-2) |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | text age | [p](#evidence-2) |
| Sex / 性别 | Confirmed | gender | [p](#evidence-2) |
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
| 500 | participants | Primary quantity reported in the reviewed catalog source | legacy\_catalog\_field | not\_assessed | [Quantity source](https://ieee-dataport.org/open-access/octa-500) |

## Family and derivative ledger

| Source resource | Relation | Target resource | Confidence | Scope | Evidence |
| --- | --- | --- | --- | --- | --- |
| [mm\_retinal\_reason](mm_retinal_reason.md) | derived\_from | [octa\_500](octa_500.md) | confirmed | The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. | [Relationship evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef) |

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Retinal Aging — 年龄及 OCTA 眼别 | 34 / 45.0 | Not eligible / 37.5 | 3 / 1 / 1 / 1 / 1 | 来源受试者数 | 具 OCT/OCTA；账号及作者密码流程。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://ieee-dataport.org/open-access/octa-500)

## Sources

<a id="evidence-1"></a>

### base

[Open original source](https://ieee-dataport.org/open-access/octa-500)

EyeDataHub v0.7.0 → octa\_500; catalog fields and dated source review, not a new clinical audit.

Recorded check date — 2026-07-21.

<a id="evidence-2"></a>

### p

[Open original source](https://pubmed.ncbi.nlm.nih.gov/38325155/)

Abstract and data statement: two modalities, four text labels, vessel masks and 500 subjects.

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### r

[Open original source](https://khosravipooya.com/EyeDataHub/datasets/octa_500/)

v0.7.0 access audit: IEEE login plus author-provided password; author\_contact.

Recorded check date — 2026-11-03.
