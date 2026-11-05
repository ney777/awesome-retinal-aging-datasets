# Brazilian Multilabel Ophthalmological Dataset (BRSET)

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

多设备、多中心；逐图质量和患者键。

当前核验的影像与模态范围 — Color fundus photography

Image availability — 凭项目资质可获取眼底照片；未登录下载。

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | brset |
| Name / 名称 | Brazilian Multilabel Ophthalmological Dataset (BRSET) |
| Acronym / 缩写 | BRSET |
| Official resource | [https://physionet.org/content/brazilian-ophthalmological/1.0.2/](https://physionet.org/content/brazilian-ophthalmological/1.0.2/) |
| Country or region / 国家地区 | Brazil |
| Institution / 机构 | São Paulo 三家眼科门诊；BRSET 研究组 |
| Reported year / 年份口径 | 2024 (descriptor); 2023 first deposit; v1.0.2 2026 |
| Publication date | 2023-03-08 |
| Date scope | initial\_public\_release |
| Date evidence | [https://physionet.org/content/brazilian-ophthalmological/1.0.0/](https://physionet.org/content/brazilian-ophthalmological/1.0.0/) |
| Date reviewed | 2026-09-11 |
| Original citation | Nakayama LF et al. BRSET: A Brazilian Multilabel Ophthalmological Dataset of Retina Fundus Photos. PLOS Digital Health 3:e0000454 (2024). |
| Publication DOI | [10.1371/journal.pdig.0000454](https://doi.org/10.1371/journal.pdig.0000454) |
| Dataset DOI | [10.13026/mysn-8b26](https://doi.org/10.13026/mysn-8b26) |
| Import origin | EyeDataHub v0.7.0 |
| Original EyeDataHub ID | brset |
| Dataset family | brset |
| Family or derivative relation | PhysioNet v1.0.2 将 mBRSET 列为 Parent Project；两者的采集地点/设备和目标人群不同。无跨库患者键，不能假定独立；embedding 记录是衍生物。 |
| Independence / overlap | Potential reuse; see relationship ledger |
| Upstream family ID | brset |
| Upstream resource role | current\_dataset |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 1 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | 16,266 color fundus images from 8,524 Brazilian patients with 14 disease labels (DR, AMD, glaucoma, drusen, others), image quality flags, and demographic attributes. |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | Color fundus photography |
| Images / 图像数及口径 | 16,266 CFP |
| Participants / 参与者数及口径 | 8,524 patients |
| Eyes / 眼别 | exam\_eye 字段标明左右；不可将照片数当人数。 |
| Device / 设备 | Canon CR 系列，Nikon NF5050 |
| Resolution / 分辨率 | Unknown |
| Quality / 质量控制 | focus、illumination、image\_field、artifacts |
| Multiple visits / 多时点 | Unknown — no visit time in published label schema |
| Multiple modalities / 多模态 | No additional image modality documented in this release |
| Multiple centers / 多中心 | Yes — 3 São Paulo outpatient centers; center ID not established |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Controlled access |
| Access or application route | [https://physionet.org/content/brazilian-ophthalmological/1.0.2/](https://physionet.org/content/brazilian-ophthalmological/1.0.2/) |
| Image files / 影像文件 | 凭项目资质可获取眼底照片；未登录下载。 |
| Individual labels / 个体标签 | 凭项目资质可获取逐图/患者级 CSV；未取得个人数据。 |
| Data license / 数据许可 | PhysioNet Credentialed Health Data License 1.5.0 + DUA |
| Research use / 科研条件 | 个人完成资质认证、CITI 培训并签署 DUA；仅限合法科研，禁止与未获批者共享。PhysioNet 对部分数据有地区/机构限制，巴西数据两项的项目级适用情况未核准。 |
| Commercial use / 商业用途 | DUA 限科研目的；无一般商业再利用授权。 |
| Terms scope | dataset\_files |
| Terms evidence | [https://physionet.org/content/brazilian-ophthalmological/1.0.2/](https://physionet.org/content/brazilian-ophthalmological/1.0.2/) |
| Upstream route review date | 2026-07-21 |
| Upstream acquisition support | manual\_access\_blocked |
| Upstream access friction | controlled\_or\_manual |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | labels.csv: image\_id → patient\_id, patient\_age (years), patient\_sex, exam\_eye, camera, diabetes。配对年龄完整人数需在获批后复核。 |
| Strengths / 主要优点 | 多设备、多中心；逐图质量和患者键。 |
| Limitations / 关键缺陷 | 年龄有缺失；横断面门诊选择偏倚。高血压视网膜病变是眼科标签；自由文本不能直接作为卒中/全身高血压结局。 |
| Suggested experiments / 建议实验 | 患者划分、按相机和图像质量分层验证实足年龄 MAE；按患者重采样置信区间。 |
| Retinal Aging suitability | A: 逐图年龄与 patient\_id 可配对。 |
| Stroke / CSVD suitability | Unknown |
| AD / Dementia suitability | Unknown |
| Multicenter model suitability | G: 跨门诊/相机辅助评测；逐图中心键未知。 |
| Screening rationale / 筛查理由 | 逐图年龄与 patient\_id 可配对。 \| 糖尿病诊断/用药，限同期；无事件时间。 \| 跨门诊/相机辅助评测；逐图中心键未知。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 1 | Tier 1 | 逐图年龄与 patient\_id 可配对。 | [s1](#evidence-2) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Tier 1 | Tier 1 | 糖尿病诊断/用药，限同期；无事件时间。 | [s1](#evidence-2) |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Tier 3 | Tier 3 | 跨门诊/相机辅助评测；逐图中心键未知。 | [s2](#evidence-3) |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | patient\_age；存在缺失。 | [s1](#evidence-2) |
| Sex / 性别 | Confirmed | patient\_sex | [s1](#evidence-2) |
| Hypertension / 高血压 | Uncertain | 只有自报共病自由文本及眼底高血压病变，结构化全身高血压病史未证实。 | [s1](#evidence-2) |
| Diabetes / 糖尿病 | Confirmed | diabetes，另有 diabetes\_time 与 insulin\_use。 | [s1](#evidence-2) |
| Cardiovascular disease / 心血管病 | Uncertain | comorbidities 为自报自由文本。 | [s1](#evidence-2) |
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
| Mortality / 死亡结局 | Not available | 已列发布表无死亡字段。 | [s1](#evidence-2) |
| Follow-up / 纵向随访 | Not available | 发布字段表不含随访时间或事件表。 | [s1](#evidence-2) |

## Counting evidence

| Count | Unit | Scope | Evidence basis | Exactness | Source |
| --- | --- | --- | --- | --- | --- |
| 16266 | images | Primary quantity reported in the reviewed catalog source | legacy\_catalog\_field | not\_assessed | [Quantity source](https://physionet.org/content/brazilian-ophthalmological/1.0.1/) |

## Family and derivative ledger

| Source resource | Relation | Target resource | Confidence | Scope | Evidence |
| --- | --- | --- | --- | --- | --- |
| [brset\_mbrset\_embeddings](brset_mbrset_embeddings.md) | derived\_from | [brset](brset.md) | confirmed | The PhysioNet record supplies precomputed representations for BRSET images. | [Relationship evidence](https://physionet.org/content/embedding-brset-mbrset/1.0.0/) |
| [retina\_age\_analysis](retina_age_analysis.md) | possible\_overlap | [brset](brset.md) | Uncertain | 字段、文件名模式提示应查来源；未确认重用或许可，不合并人数。 | [Relationship evidence](https://huggingface.co/datasets/ramankamran/retina-age-analysis) |

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Retinal Aging — 实足年龄 | 26 / 56.25 | Not eligible / 55.0 | 3 / 2 / 1 / 2 / 3 | 患者规模，去除缺年龄后数量未核 | 三门诊两种相机，PhysioNet 认证与 DUA。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://physionet.org/content/brazilian-ophthalmological/1.0.2/)

## Sources

<a id="evidence-1"></a>

### base

[Open original source](https://physionet.org/content/brazilian-ophthalmological/1.0.1/)

EyeDataHub v0.7.0 → brset; catalog fields and dated source review, not a new clinical audit.

Recorded check date — 2026-07-21.

<a id="evidence-2"></a>

### s1

[Open original source](https://physionet.org/content/brazilian-ophthalmological/1.0.2/)

Data Description / Access / Releases：v1.0.2；fundus\_photos 和 labels.csv 的 ID、年龄、性别、眼别、糖尿病、质量字段和控制访问条件。

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s2

[Open original source](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000454)

Methods / Data Quality Assessment：São Paulo 三家门诊及两种相机；年龄列有缺失。

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### s3

[Open original source](https://physionet.org/content/embedding-brset-mbrset/1.0.0/)

Methods：BRSET 与 mBRSET 不同采集方案以及按来源影像 ID 的衍生向量。

Recorded check date — 2026-11-03.

<a id="evidence-5"></a>

### s4

[Open original source](https://github.com/MIT-LCP/license-and-dua/blob/main/DataUseAgreement-v1.5.0.md)

DUA v1.5 §3, §6：不得共享访问，仅限合法科学研究。

Recorded check date — 2026-11-03.

<a id="evidence-6"></a>

### s5

[Open original source](https://physionet.org/news/post/data-security-program-1/)

Access Restrictions：针对某些受控数据集的地区/机构/IP 限制，项目适用性未列清。

Recorded check date — 2026-11-03.
