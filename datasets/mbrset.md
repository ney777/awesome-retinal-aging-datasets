# Mobile Brazilian Retinal Dataset (mBRSET)

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

手机相机；有同期临床问卷，也标注图像质量。

当前核验的影像与模态范围 — Color fundus photography (handheld)

Image availability — 凭项目资质可获取眼底照片；未登录下载。

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | mbrset |
| Name / 名称 | Mobile Brazilian Retinal Dataset (mBRSET) |
| Acronym / 缩写 | mBRSET |
| Official resource | [https://physionet.org/content/mbrset/1.0/](https://physionet.org/content/mbrset/1.0/) |
| Country or region / 国家地区 | Brazil |
| Institution / 机构 | Itabuna Diabetes Campaign, Bahia; mBRSET investigators |
| Reported year / 年份口径 | 2025 (descriptor); 2024 PhysioNet v1.0 |
| Publication date | 2024-06-26 |
| Date scope | initial\_public\_release |
| Date evidence | [https://physionet.org/content/mbrset/1.0/](https://physionet.org/content/mbrset/1.0/) |
| Date reviewed | 2026-09-11 |
| Original citation | Wu C et al. A portable retina fundus photos dataset for clinical, demographic, and diabetic retinopathy prediction. Scientific Data 12:323 (2025). |
| Publication DOI | [10.1038/s41597-025-04627-3](https://doi.org/10.1038/s41597-025-04627-3) |
| Dataset DOI | [10.13026/qxpd-1y65](https://doi.org/10.13026/qxpd-1y65) |
| Import origin | EyeDataHub v0.7.0 |
| Original EyeDataHub ID | mbrset |
| Dataset family | mbrset |
| Family or derivative relation | Itabuna 糖尿病筛查活动与 BRSET 的 São Paulo 门诊来源不同；两库生成人工智能 embeddings，衍生向量不增加患者。 PhysioNet 项目页还反向引用 BRSET v1.0.0 为父项目；项目衍生关系不等于患者重叠证明。 |
| Independence / overlap | Potential reuse; see relationship ledger |
| Upstream family ID | mbrset |
| Upstream resource role | current\_dataset |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 1 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | 5,164 fundus images from 1,291 patients captured with the Phelcom Eyer handheld smartphone-based fundus camera. Labels for DR grading + clinical/demographic prediction. |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | Color fundus photography (handheld) |
| Images / 图像数及口径 | 5,164 CFP |
| Participants / 参与者数及口径 | 1,291 patients with diabetes |
| Eyes / 眼别 | laterality；右/左视盘或黄斑视野。 |
| Device / 设备 | Phelcom Eyer, Samsung Galaxy S10, 45° |
| Resolution / 分辨率 | 1600 × 1600 |
| Quality / 质量控制 | final\_artifacts / final\_quality，部分图像无 ICDR 标签。 |
| Multiple visits / 多时点 | No — one cross-sectional campaign |
| Multiple modalities / 多模态 | No additional image modality in this release |
| Multiple centers / 多中心 | Single campaign in Itabuna (November 2022) |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Controlled access |
| Access or application route | [https://physionet.org/content/mbrset/1.0/](https://physionet.org/content/mbrset/1.0/) |
| Image files / 影像文件 | 凭项目资质可获取眼底照片；未登录下载。 |
| Individual labels / 个体标签 | 凭项目资质可获取逐图/患者级 CSV；未取得个人数据。 |
| Data license / 数据许可 | PhysioNet Credentialed Health Data License 1.5.0 + DUA |
| Research use / 科研条件 | 个人完成资质认证、CITI 培训并签署 DUA；仅限合法科研，禁止与未获批者共享。PhysioNet 对部分数据有地区/机构限制，巴西数据两项的项目级适用情况未核准。 |
| Commercial use / 商业用途 | DUA 限科研目的；无一般商业再利用授权。 |
| Terms scope | dataset\_files |
| Terms evidence | [https://physionet.org/content/mbrset/1.0/](https://physionet.org/content/mbrset/1.0/) |
| Upstream route review date | 2026-07-21 |
| Upstream acquisition support | manual\_access\_blocked |
| Upstream access friction | controlled\_or\_manual |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | labels\_mbrset.csv 中 file→patient；含年龄、眼别、同期问卷及质量。标签公开描述中自报既往 MI 阳性 98、神经病变 55、系统性高血压 914；分母随缺失变。 |
| Strengths / 主要优点 | 手机相机；有同期临床问卷，也标注图像质量。 |
| Limitations / 关键缺陷 | 入组人群均有糖尿病，不能以此评估区分有无糖尿病的判别力；并发症多为既往自报，不能作新发卒中/AD结局。 |
| Suggested experiments / 建议实验 | 作为便携设备域验证实足年龄回归；自报高血压或既往 MI 仅做横断面表型试验。 |
| Retinal Aging suitability | A: 患者年龄可关联。 |
| Stroke / CSVD suitability | Unknown |
| AD / Dementia suitability | Unknown |
| Multicenter model suitability | G: 手机相机的外部域。 |
| Screening rationale / 筛查理由 | 患者年龄可关联。 \| 自报糖尿病相关周围神经病变；无 AD/PD 的确认。 \| 既往 MI、高血压及糖尿病血管并发症均有患者字段。 \| 手机相机的外部域。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 1 | Tier 1 | 患者年龄可关联。 | [s1](#evidence-2) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Tier 1 | Tier 1 | 自报糖尿病相关周围神经病变；无 AD/PD 的确认。 | [s1](#evidence-2) |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Tier 1 | Tier 1 | 既往 MI、高血压及糖尿病血管并发症均有患者字段。 | [s1](#evidence-2) |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Tier 3 | Tier 3 | 手机相机的外部域。 | [s1](#evidence-2) |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | age，1291 人年龄无缺失（汇总表）。 | [s1](#evidence-2) |
| Sex / 性别 | Confirmed | sex，0 女，1 男。 | [s1](#evidence-2) |
| Hypertension / 高血压 | Confirmed | systemic\_hypertension 既往自报。 | [s1](#evidence-2) |
| Diabetes / 糖尿病 | Confirmed | 所有入组者患糖尿病；有病程和用药。 | [s1](#evidence-2) |
| Cardiovascular disease / 心血管病 | Confirmed | 自报既往急性心梗/糖尿病相关血管病。 | [s1](#evidence-2) |
| Stroke type / 卒中分型 | Not available | 发布字段无卒中亚型。 | [s1](#evidence-2) |
| Stroke timing / 卒中事件时间 | Not available | 发布字段无卒中日期。 | [s1](#evidence-2) |
| Brain MRI / 脑 MRI | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| CSVD / 脑小血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Alzheimer’s disease / 阿尔茨海默病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Dementia / 痴呆 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Cognition / 认知功能 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Parkinson’s disease / 帕金森病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Frailty / 衰弱 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Health status / 健康状态 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Mortality / 死亡结局 | Not available | 已公布字典无死亡终点。 | [s1](#evidence-2) |
| Follow-up / 纵向随访 | Not available | 2022年11月筛查，问卷既往史。 | [s1](#evidence-2) |

## Counting evidence

| Count | Unit | Scope | Evidence basis | Exactness | Source |
| --- | --- | --- | --- | --- | --- |
| 5164 | images | Primary quantity reported in the reviewed catalog source | legacy\_catalog\_field | not\_assessed | [Quantity source](https://physionet.org/content/mbrset/1.0/) |

## Family and derivative ledger

| Source resource | Relation | Target resource | Confidence | Scope | Evidence |
| --- | --- | --- | --- | --- | --- |
| [brset\_mbrset\_embeddings](brset_mbrset_embeddings.md) | derived\_from | [mbrset](mbrset.md) | confirmed | The PhysioNet record supplies precomputed representations for mBRSET images. | [Relationship evidence](https://physionet.org/content/embedding-brset-mbrset/1.0.0/) |

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Retinal Aging — 实足年龄 | 18 / 70.0 | Not eligible / 61.25 | 3 / 3 / 3 / 2 / 1 | 原始患者规模 | 单次地区活动手机设备，须认证。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://physionet.org/content/mbrset/1.0/)

## Sources

<a id="evidence-1"></a>

### base

[Open original source](https://physionet.org/content/mbrset/1.0/)

EyeDataHub v0.7.0 → mbrset; catalog fields and dated source review, not a new clinical audit.

Recorded check date — 2026-07-21.

<a id="evidence-2"></a>

### s1

[Open original source](https://physionet.org/content/mbrset/1.0/)

Methods / Data Description / Tables 1–3 / Access：采集活动、患者与眼别键、自报系统并发症、设备、质量、样本量。

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s2

[Open original source](https://www.nature.com/articles/s41597-025-04627-3)

Methods/Data Records，便携相机 1600×1600，结构化人口学和自报临床资料。

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### s3

[Open original source](https://physionet.org/content/embedding-brset-mbrset/1.0.0/)

Methods：两队列产生相应的二次 embedding。

Recorded check date — 2026-11-03.

<a id="evidence-5"></a>

### s4

[Open original source](https://github.com/MIT-LCP/license-and-dua/blob/main/DataUseAgreement-v1.5.0.md)

DUA v1.5 科研使用及禁止共享条款。

Recorded check date — 2026-11-03.

<a id="evidence-6"></a>

### s5

[Open original source](https://physionet.org/news/post/data-security-program-1/)

平台仅称某些数据集受国别限制，本文未代表项目判定适用性。

Recorded check date — 2026-11-03.
