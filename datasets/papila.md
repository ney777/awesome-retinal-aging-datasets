# PAPILA

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

公开文件、患者键、双眼完整配对，便于低成本检查年龄建模流程。

当前核验的影像与模态范围 — Color fundus photography

Image availability — 作者 Figshare v2 列出 PAPILA.zip

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | papila |
| Name / 名称 | PAPILA |
| Acronym / 缩写 | PAPILA |
| Official resource | [https://figshare.com/articles/dataset/PAPILA/14798004/2](https://figshare.com/articles/dataset/PAPILA/14798004/2) |
| Country or region / 国家地区 | Spain |
| Institution / 机构 | Hospital General Universitario Reina Sofía (Murcia); Universidad Politécnica de Cartagena |
| Reported year / 年份口径 | 2022 |
| Publication date | 2022-04-29 |
| Date scope | initial\_public\_release |
| Date evidence | [https://api.figshare.com/v2/articles/14798004/versions/1](https://api.figshare.com/v2/articles/14798004/versions/1) |
| Date reviewed | 2026-09-11 |
| Original citation | Kovalyk O et al. PAPILA: Dataset with fundus images and clinical data of both eyes of the same patient for glaucoma assessment. Scientific Data (2022). |
| Publication DOI | [10.1038/s41597-022-01388-1](https://doi.org/10.1038/s41597-022-01388-1) |
| Dataset DOI | [10.6084/m9.figshare.14798004.v2](https://doi.org/10.6084/m9.figshare.14798004.v2) |
| Import origin | EyeDataHub v0.7.0 |
| Original EyeDataHub ID | papila |
| Dataset family | papila |
| Family or derivative relation | 版本1/2、剪裁、叠加轮廓或镜像不是新增队列。原作者 Figshare v2 条款与索引 Zenodo/论文条款分开。 |
| Independence / overlap | Potential reuse; see relationship ledger |
| Upstream family ID | papila |
| Upstream resource role | current\_dataset |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 1 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | 488 fundus images from 244 patients (both eyes). Expert OD/OC segmentation, glaucoma stage, IOP, and clinical metadata. |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | Color fundus photography |
| Images / 图像数及口径 | 488 original CFP (segmentation overlays not new images) |
| Participants / 参与者数及口径 | 244 patients |
| Eyes / 眼别 | Each patient both eyes, OD and OS |
| Device / 设备 | Topcon TRC-NW400, 30° optic disc centered |
| Resolution / 分辨率 | 2576 × 1934 JPEG |
| Quality / 质量控制 | Two expert disc/cup segmentations; no independent image-quality scale verified |
| Multiple visits / 多时点 | No — one image per eye in the release |
| Multiple modalities / 多模态 | No other raw imaging; ocular clinical measurements plus segmentations |
| Multiple centers / 多中心 | Single acquisition hospital, Murcia |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Open download |
| Access or application route | [https://figshare.com/articles/dataset/PAPILA/14798004/2](https://figshare.com/articles/dataset/PAPILA/14798004/2) |
| Image files / 影像文件 | 作者 Figshare v2 列出 PAPILA.zip |
| Individual labels / 个体标签 | 同一包内左右眼各一个临床工作簿，有 ID 年龄性别等。 |
| Data license / 数据许可 | GPL 3.0+ (author Figshare v2 record for PAPILA.zip) |
| Research use / 科研条件 | 作者要求引用数据描述论文；遵从该数据版本的 GPL 3.0+ 声明。 |
| Commercial use / 商业用途 | 未见单独非商业条款；具体再分发遵从 Figshare 所列 GPL 3.0+。 |
| Terms scope | dataset\_files |
| Terms evidence | [https://api.figshare.com/v2/articles/14798004/versions/2](https://api.figshare.com/v2/articles/14798004/versions/2) |
| Upstream route review date | 2026-07-21 |
| Upstream acquisition support | guided\_instructions\_only |
| Upstream access friction | anonymous\_direct |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | ClinicalData/OD、OS 两张表的患者号和年龄与 FundusImages/RETnnnOD/OS.jpg 一一关联。 导入时识别双表头并排除非患者行；以 \#nnn（不是工作簿行号）连 RETnnnOD/OS.jpg。 |
| Strengths / 主要优点 | 公开文件、患者键、双眼完整配对，便于低成本检查年龄建模流程。 |
| Limitations / 关键缺陷 | 单中心、小规模、青光眼/可疑/健康样本，视盘中心构图；仅宜作小型独立域检查。 |
| Suggested experiments / 建议实验 | 冻结编码器，按患者预测年龄并报告 244 位患者的 bootstrap CI；比较单眼与双眼平均，不用于结局预测。 |
| Retinal Aging suitability | A: 每个患者年龄键配两张 CFP。 |
| Stroke / CSVD suitability | Unknown |
| AD / Dementia suitability | Unknown |
| Multicenter model suitability | G: 视盘中心/单中心与其他数据集的独立域比较。 |
| Screening rationale / 筛查理由 | 每个患者年龄键配两张 CFP。 \| 视盘中心/单中心与其他数据集的独立域比较。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 1 | Tier 1 | 每个患者年龄键配两张 CFP。 | [s1](#evidence-2) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Tier 3 | Tier 3 | 视盘中心/单中心与其他数据集的独立域比较。 | [s1](#evidence-2) |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | 在 OD 和 OS 表实检，244位ID年龄齐全、两表一致，15–90岁。 | [s4](#evidence-5) |
| Sex / 性别 | Confirmed | 性别代码 0 男 1 女。 | [s1](#evidence-2) |
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
| Mortality / 死亡结局 | Not available | 该发布列出完整临床列，不含死亡。 | [s1](#evidence-2) |
| Follow-up / 纵向随访 | Not available | 每眼一张 CFP；该包无纵向访视设计。 | [s1](#evidence-2) |

## Counting evidence

| Count | Unit | Scope | Evidence basis | Exactness | Source |
| --- | --- | --- | --- | --- | --- |
| 488 | images | Primary quantity reported in the reviewed catalog source | legacy\_catalog\_field | not\_assessed | [Quantity source](https://zenodo.org/records/6379970) |

## Family and derivative ledger

| Source resource | Relation | Target resource | Confidence | Scope | Evidence |
| --- | --- | --- | --- | --- | --- |
| [glaucoma\_expert\_cot\_refined](glaucoma_expert_cot_refined.md) | derived\_from | [papila](papila.md) | confirmed | The official dataset card identifies LAG and PAPILA as the source fundus resources paired with the refined glaucoma reasoning records. | [Relationship evidence](https://huggingface.co/datasets/yuzhench/glaucoma-expert-cot-refined-1077) |
| [mm\_retinal\_reason](mm_retinal_reason.md) | derived\_from | [papila](papila.md) | confirmed | The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. | [Relationship evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef) |
| [smdg](smdg.md) | derived\_from | [papila](papila.md) | confirmed | The official SMDG source table lists this catalog record among the 19 standardized source domains. | [Relationship evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset) |

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Retinal Aging — 逐眼实足年龄 | 34 / 45.0 | 6 / 71.25 | 3 / 1 / 1 / 4 / 1 | 逐眼表与影像匹配 | 单医院，公开原始影像和逐眼临床表。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://figshare.com/articles/dataset/PAPILA/14798004/2)

## Sources

<a id="evidence-1"></a>

### base

[Open original source](https://zenodo.org/records/6379970)

EyeDataHub v0.7.0 → papila; catalog fields and dated source review, not a new clinical audit.

Recorded check date — 2026-07-21.

<a id="evidence-2"></a>

### s1

[Open original source](https://www.nature.com/articles/s41597-022-01388-1)

Data Records / Composition: 244 名患者双眼、每眼年龄/性别及临床表、图像尺寸与文件命名。

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s2

[Open original source](https://api.figshare.com/v2/articles/14798004)

Figshare v2 file/rights API: PAPILA.zip，590857635 bytes；license.name=GPL 3.0+。

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### s3

[Open original source](https://portalinvestigacion.upct.es/documentos/668fc47cb9e7c03b01bdee3a)

作者机构馆藏：两版 DOI，v2 GPL 3.0+，要求优先引用数据描述论文。

Recorded check date — 2026-11-03.

<a id="evidence-5"></a>

### s4

[Open original source](https://ndownloader.figshare.com/files/35013982)

Figshare v2 ZIP 中央目录 + ClinicalData/patient\_data\_od.xlsx, patient\_data\_os.xlsx：每表244个唯一\#nnn，实足年龄15–90，两眼年龄逐人一致；两表共488个键全可对应 FundusImages/RETnnnOD/OS.jpg。

Recorded check date — 2026-11-03.
