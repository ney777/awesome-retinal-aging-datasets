# Harvard-FairVision (30K)

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

实配的 SLO、OCT 与逐人年龄，支持相同人的跨模态年龄回归；作者允许非商业科研。

当前核验的影像与模态范围 — SLO fundus + paired volumetric OCT

Image availability — 作者发布提供 SLO 与 OCT B-scan NPZ；体积大，可先核对单组件可行性。

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | harvard\_fairvision |
| Name / 名称 | Harvard-FairVision (30K) |
| Acronym / 缩写 | Harvard-FairVision |
| Official resource | [https://huggingface.co/datasets/harvardairobotics/FairVision](https://huggingface.co/datasets/harvardairobotics/FairVision) |
| Country or region / 国家地区 | United States |
| Institution / 机构 | Department of Ophthalmology, Harvard Medical School / Massachusetts Eye and Ear |
| Reported year / 年份口径 | 2024 (author citation/preprint version) |
| Publication date | 2023-10-03 |
| Date scope | initial\_public\_release |
| Date evidence | [https://ophai.hms.harvard.edu/code/fairvision/](https://ophai.hms.harvard.edu/code/fairvision/) |
| Date reviewed | 2026-09-11 |
| Original citation | Luo Y et al. FairVision: Equitable Deep Learning for Eye Disease Screening via Fair Identity Scaling. arXiv:2310.02492 (author-cited 2024 version). |
| Publication DOI | [10.48550/arXiv.2310.02492](https://doi.org/10.48550/arXiv.2310.02492) |
| Dataset DOI | Unknown |
| Import origin | EyeDataHub v0.7.0 |
| Original EyeDataHub ID | harvard\_fairvision |
| Dataset family | harvard\_fairvision |
| Family or derivative relation | Harvard 3 个疾病子集；与 FairVLMed/其他 Harvard 版本的患者独立性未知；保留发布内官方划分。 |
| Independence / overlap | Independence unverified |
| Upstream family ID | harvard\_fairvision |
| Upstream resource role | current\_dataset |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 1 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | 30,000 subjects (10K each AMD, DR, glaucoma) with paired SLO fundus and OCT B-scans, demographic attributes (race, ethnicity, gender, language), for fairness analysis. |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | SLO fundus + paired volumetric OCT |
| Images / 图像数及口径 | 30,000 SLO and 30,000 paired OCT samples (one pair per source-reported subject); B-scans within volumes not new subjects |
| Participants / 参与者数及口径 | 30,000 source-reported subjects; 10,000 per AMD/DR/glaucoma subset |
| Eyes / 眼别 | One paired SLO/OCT sample per subject; DR study explicitly same eye/visit |
| Device / 设备 | Unknown |
| Resolution / 分辨率 | SLO 512×664 or 200×200 NPZ; OCT volume 200×200×200 glaucoma, 128×200×200 AMD/DR |
| Quality / 质量控制 | Unknown |
| Multiple visits / 多时点 | No — one paired sample per subject |
| Multiple modalities / 多模态 | Yes — paired SLO + volumetric OCT |
| Multiple centers / 多中心 | MEE clinical resource; no independent center split demonstrated |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Open download |
| Access or application route | [https://huggingface.co/datasets/harvardairobotics/FairVision](https://huggingface.co/datasets/harvardairobotics/FairVision) |
| Image files / 影像文件 | 作者发布提供 SLO 与 OCT B-scan NPZ；体积大，可先核对单组件可行性。 |
| Individual labels / 个体标签 | 作者数据卡逐疾病元数据含年龄等人口学，NPZ 含眼病分级；未证实系统疾病结局。 |
| Data license / 数据许可 | CC BY-NC-ND 4.0 (dataset files) |
| Research use / 科研条件 | 仅非商业科研；禁止临床决策与患者诊疗用途。 |
| Commercial use / 商业用途 | 禁止商业使用。 |
| Terms scope | dataset\_files |
| Terms evidence | [https://huggingface.co/datasets/harvardairobotics/FairVision](https://huggingface.co/datasets/harvardairobotics/FairVision) |
| Upstream route review date | 2026-07-21 |
| Upstream acquisition support | manual\_access\_blocked |
| Upstream access friction | controlled\_or\_manual |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | 按疾病目录和文件 ID 连接各 data\_summary\_\*.csv 的年龄与 NPZ 里的 slo\_fundus 和 oct\_bscans；同一编号在不同疾病目录不能当作同一患者键。 |
| Strengths / 主要优点 | 实配的 SLO、OCT 与逐人年龄，支持相同人的跨模态年龄回归；作者允许非商业科研。 |
| Limitations / 关键缺陷 | AMD/糖网病/青光眼子集反映临床就诊选择；同源人群泄漏须在外部验证前审计；DR 标签不可替代糖尿病病史。 |
| Suggested experiments / 建议实验 | 比较同一患者 SLO、OCT 和融合的年龄 MAE；按疾病子集和年龄层汇报校准；跨域测试采用外机构队列。 |
| Retinal Aging suitability | A: 每人年龄 + SLO/OCT 对。 |
| Stroke / CSVD suitability | Unknown |
| AD / Dementia suitability | Unknown |
| Multicenter model suitability | G: 多模态/公平性辅助训练和验证；不能冒称真实多中心。 |
| Screening rationale / 筛查理由 | 每人年龄 + SLO/OCT 对。 \| 多模态/公平性辅助训练和验证；不能冒称真实多中心。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 1 | Tier 1 | 每人年龄 + SLO/OCT 对。 | [s1](#evidence-2) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Tier 3 | Tier 3 | 多模态/公平性辅助训练和验证；不能冒称真实多中心。 | [s2](#evidence-3) |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | 每疾病 data\_summary 文件均载年龄。 | [s1](#evidence-2) |
| Sex / 性别 | Confirmed | 个体 gender/male 字段。 | [s1](#evidence-2) |
| Hypertension / 高血压 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Diabetes / 糖尿病 | Uncertain | 发布的是 DR 眼病分级；所有子集的系统糖尿病状态未核实。 | [s1](#evidence-2) |
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
| Follow-up / 纵向随访 | Not available | 作者声明每人一个 SLO 与一个 OCT 样本。 | [s2](#evidence-3) |

## Counting evidence

| Count | Unit | Scope | Evidence basis | Exactness | Source |
| --- | --- | --- | --- | --- | --- |
| 30000 | participants | Primary quantity reported in the reviewed catalog source | legacy\_catalog\_field | not\_assessed | [Quantity source](https://ophai.hms.harvard.edu/datasets/harvard-fairvision30k) |

## Family and derivative ledger

| Source resource | Relation | Target resource | Confidence | Scope | Evidence |
| --- | --- | --- | --- | --- | --- |
| [fairvlmed](fairvlmed.md) | possible\_overlap | [harvard\_fairvision](harvard_fairvision.md) | Uncertain | 相关团队与临床来源，患者独立性未验证。 | [Relationship evidence](https://huggingface.co/datasets/harvardairobotics/FairVision) |

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Retinal Aging — 配对 SLO+OCT 年龄 | 28 / 51.25 | 4 / 73.75 | 3 / 1 / 2 / 4 / 1 | 发布者总人数，年龄完备性需核 | 临床 SLO+OCT，公开文件；限非商业研究。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://huggingface.co/datasets/harvardairobotics/FairVision)

## Sources

<a id="evidence-1"></a>

### base

[Open original source](https://ophai.hms.harvard.edu/datasets/harvard-fairvision30k)

EyeDataHub v0.7.0 → harvard\_fairvision; catalog fields and dated source review, not a new clinical audit.

Recorded check date — 2026-07-21.

<a id="evidence-2"></a>

### s1

[Open original source](https://huggingface.co/datasets/harvardairobotics/FairVision)

Dataset Structure / Data Fields：三个疾病子集、按文件元数据年龄、SLO+OCT尺寸、许可及限制。

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s2

[Open original source](https://github.com/Harvard-Ophthalmology-AI-Lab/FairVision)

Dataset: one SLO + one OCT sample per person; 30K subjects, three disease subsets; non-commercial research only.

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### s3

[Open original source](https://pmc.ncbi.nlm.nih.gov/articles/PMC12227025/)

Harvard-FairVision30k subsection：DR analysis 的 MEE 子集 10,000 人，SLO 与 OCT 同一眼/访视。

Recorded check date — 2026-11-03.

<a id="evidence-5"></a>

### s4

[Open original source](https://arxiv.org/abs/2310.02492)

原始预印本，FairVision 队列和融合数据来源。

Recorded check date — 2026-11-03.
