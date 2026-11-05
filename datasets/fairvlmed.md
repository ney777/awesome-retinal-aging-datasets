# Harvard-FairVLMed

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

一人一例、作者划分，足以比较不同人口学组的年龄误差，且允许图像-文本公平性研究。

当前核验的影像与模态范围 — Scanning laser ophthalmoscopy (SLO fundus) + notes + visual fields

Image availability — 作者 Hugging Face/项目说明提供 NPZ 图像。

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | fairvlmed |
| Name / 名称 | Harvard-FairVLMed |
| Acronym / 缩写 | Harvard-FairVLMed |
| Official resource | [https://huggingface.co/datasets/harvardairobotics/FairVLMed](https://huggingface.co/datasets/harvardairobotics/FairVLMed) |
| Country or region / 国家地区 | United States |
| Institution / 机构 | Department of Ophthalmology, Harvard Medical School / Massachusetts Eye and Ear |
| Reported year / 年份口径 | 2024 |
| Publication date | Unknown |
| Date scope | Unknown |
| Date evidence | Unknown |
| Date reviewed | Unknown |
| Original citation | Luo Y et al. FairCLIP: Harnessing Fairness in Vision-Language Learning. Proceedings of CVPR (2024), 12289–12301. |
| Publication DOI | [10.1109/CVPR52733.2024.01168](https://doi.org/10.1109/CVPR52733.2024.01168) |
| Dataset DOI | Unknown |
| Import origin | EyeDataHub v0.7.0 |
| Original EyeDataHub ID | fairvlmed |
| Dataset family | fairvlmed |
| Family or derivative relation | Harvard Ophthalmology AI 系列；与 Harvard-FairVision 等的患者重叠未经核准，不能自动作跨库独立测试。 |
| Independence / overlap | Independence unverified |
| Upstream family ID | fairvlmed |
| Upstream resource role | current\_dataset |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 1 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | 10,000 scanning-laser ophthalmoscopy fundus images paired with de-identified clinical notes, visual-field measurements, glaucoma labels, and demographic attributes. |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | Scanning laser ophthalmoscopy (SLO fundus) + notes + visual fields |
| Images / 图像数及口径 | 10,000 SLO fundus images |
| Participants / 参与者数及口径 | 10,000 subjects, one sample each |
| Eyes / 眼别 | One SLO per participant; bilateral pairing not available |
| Device / 设备 | Unknown |
| Resolution / 分辨率 | Unknown |
| Quality / 质量控制 | Unknown |
| Multiple visits / 多时点 | No — one released sample per subject |
| Multiple modalities / 多模态 | Yes — SLO + notes + visual field indices |
| Multiple centers / 多中心 | Unknown |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Open download |
| Access or application route | [https://huggingface.co/datasets/harvardairobotics/FairVLMed](https://huggingface.co/datasets/harvardairobotics/FairVLMed) |
| Image files / 影像文件 | 作者 Hugging Face/项目说明提供 NPZ 图像。 |
| Individual labels / 个体标签 | 相同 NPZ 和作者元数据字段有年龄/性别、青光眼，原始文本非独立系统疾病诊断。 |
| Data license / 数据许可 | CC BY-NC-ND 4.0 (dataset files) |
| Research use / 科研条件 | 仅非商业科研；禁止临床决策与患者诊疗用途。 |
| Commercial use / 商业用途 | 禁止商业使用。 |
| Terms scope | dataset\_files |
| Terms evidence | [https://huggingface.co/datasets/harvardairobotics/FairVLMed](https://huggingface.co/datasets/harvardairobotics/FairVLMed) |
| Upstream route review date | 2026-07-21 |
| Upstream acquisition support | standard\_platform\_supported |
| Upstream access friction | self\_service\_authenticated |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | 每名患者一个 data\_xxxxx.npz；slo\_fundus、age、gender、MD/TD、glaucoma、note 按同一文件键关联；原始文书或 note\_extra 可直接泄漏年龄。 |
| Strengths / 主要优点 | 一人一例、作者划分，足以比较不同人口学组的年龄误差，且允许图像-文本公平性研究。 |
| Limitations / 关键缺陷 | 若预测年龄需屏蔽文本和人口学输入；临床笔记中偶发神经疾病提及无系统结局判定。 |
| Suggested experiments / 建议实验 | 严格纯影像冻结年龄头，按患者预置 7000/1000/2000 分割报告分组校准；分别评估 SLO 相对 CFP 迁移。 |
| Retinal Aging suitability | A: 每名患者 SLO 样本内附年龄。 |
| Stroke / CSVD suitability | Unknown |
| AD / Dementia suitability | Unknown |
| Multicenter model suitability | G: SLO/视觉语言多模态与公平性基准。 |
| Screening rationale / 筛查理由 | 每名患者 SLO 样本内附年龄。 \| SLO/视觉语言多模态与公平性基准。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 1 | Tier 1 | 每名患者 SLO 样本内附年龄。 | [s1](#evidence-2) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Tier 3 | Tier 3 | SLO/视觉语言多模态与公平性基准。 | [s1](#evidence-2) |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | 每 NPZ 的 age。 | [s1](#evidence-2) |
| Sex / 性别 | Confirmed | 作者列为 gender 字段，非独立核实的生理性别。 | [s1](#evidence-2) |
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
| Follow-up / 纵向随访 | Not available | 每人一个样本。 | [s1](#evidence-2) |

## Counting evidence

| Count | Unit | Scope | Evidence basis | Exactness | Source |
| --- | --- | --- | --- | --- | --- |
| 10000 | images | Primary quantity reported in the reviewed catalog source | legacy\_catalog\_field | not\_assessed | [Quantity source](https://huggingface.co/datasets/harvardairobotics/FairVLMed) |

## Family and derivative ledger

| Source resource | Relation | Target resource | Confidence | Scope | Evidence |
| --- | --- | --- | --- | --- | --- |
| [fairvlmed](fairvlmed.md) | possible\_overlap | [harvard\_fairvision](harvard_fairvision.md) | Uncertain | 相关团队与临床来源，患者独立性未验证。 | [Relationship evidence](https://huggingface.co/datasets/harvardairobotics/FairVision) |

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Retinal Aging — 年龄、SLO 与临床文本 | 28 / 51.25 | 4 / 73.75 | 3 / 1 / 2 / 4 / 1 | 发布者每人一份 | 临床 SLO 单样本；科研条件，系列间重叠未证。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://huggingface.co/datasets/harvardairobotics/FairVLMed)

## Sources

<a id="evidence-1"></a>

### base

[Open original source](https://huggingface.co/datasets/harvardairobotics/FairVLMed)

EyeDataHub v0.7.0 → fairvlmed; catalog fields and dated source review, not a new clinical audit.

Recorded check date — 2026-07-21.

<a id="evidence-2"></a>

### s1

[Open original source](https://huggingface.co/datasets/harvardairobotics/FairVLMed)

Dataset Details / Data Fields / Uses: 每人1个NPZ、年龄/性别/文本等键，许可；数据浏览可见年龄区间约8.95–99.8。

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s2

[Open original source](https://github.com/Harvard-Ophthalmology-AI-Lab/FairCLIP)

Dataset: 10,000 独立受试者、7k/1k/2k 划分，CC BY-NC-ND；原始临床笔记与总结。

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### s3

[Open original source](https://openaccess.thecvf.com/content/CVPR2024/papers/Luo_FairCLIP_Harnessing_Fairness_in_Vision-Language_Learning_CVPR_2024_paper.pdf)

Original paper Table 1 / methodology：SLO 与临床笔记、VF及公平性。

Recorded check date — 2026-11-03.
