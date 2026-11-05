# ROSE: Retinal OCT-Angiography Vessel Segmentation (ROSE-1 and ROSE-2)

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

不同设备 OCTA 分割；可核查跨设备误差。

当前核验的影像与模态范围 — OCTA

Image availability — Zenodo metadata public, files restricted with request-access form; override v0.7.0 automated/open assumption.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | rose |
| Name / 名称 | ROSE: Retinal OCT-Angiography Vessel Segmentation (ROSE-1 and ROSE-2) |
| Acronym / 缩写 | ROSE |
| Official resource | [https://zenodo.org/records/12775880](https://zenodo.org/records/12775880) |
| Country or region / 国家地区 | China / other study sites |
| Institution / 机构 | iMED, Ningbo Institute of Materials Technology and Engineering and collaborators |
| Reported year / 年份口径 | 2021 |
| Publication date | 2021-03-02 |
| Date scope | associated\_publication |
| Date evidence | [https://pubmed.ncbi.nlm.nih.gov/33284751/](https://pubmed.ncbi.nlm.nih.gov/33284751/) |
| Date reviewed | 2026-09-11 |
| Original citation | Ma Y et al. ROSE: A Retinal OCT-Angiography Vessel Segmentation Dataset and New Model. IEEE TMI 2021. Zenodo 10.5281/zenodo.12775880. |
| Publication DOI | [10.1109/TMI.2020.3042802](https://doi.org/10.1109/TMI.2020.3042802) |
| Dataset DOI | [10.5281/zenodo.12775880](https://doi.org/10.5281/zenodo.12775880) |
| Import origin | EyeDataHub v0.7.0 |
| Original EyeDataHub ID | rose |
| Dataset family | ROSE |
| Family or derivative relation | ROSE-1 and ROSE-2 scanner-specific subsets; ROSE-O annotation product described on current landing page, not additional people by default. |
| Independence / overlap | Independence unverified |
| Upstream family ID | rose |
| Upstream resource role | current\_dataset |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 2 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | 229 OCTA images (ROSE-1 + ROSE-2) with pixel-level retinal vessel segmentation ground truth. |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | OCTA |
| Images / 图像数及口径 | 117 ROSE-1 + 112 ROSE-2 = 229 en face images in original segmentation data; not 229 participants. |
| Participants / 参与者数及口径 | 39 ROSE-1; ROSE-2 112 eyes, number of independent people unverified. |
| Eyes / 眼别 | Unknown |
| Device / 设备 | Optovue RTVue XR Avanti (ROSE-1); Heidelberg OCT2 (ROSE-2). |
| Resolution / 分辨率 | 304×304 vs 840×840, 3×3 mm. |
| Quality / 质量控制 | Centerline/pixel vessel masks; expert consensus. |
| Multiple visits / 多时点 | Unknown |
| Multiple modalities / 多模态 | Unknown |
| Multiple centers / 多中心 | Unknown |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Controlled access |
| Access or application route | [https://zenodo.org/records/12775880](https://zenodo.org/records/12775880) |
| Image files / 影像文件 | Zenodo metadata public, files restricted with request-access form; override v0.7.0 automated/open assumption. |
| Individual labels / 个体标签 | Vessel annotations documented. ROSE-1 contains AD/controls in paper; no confirmed per-image diagnostic crosswalk supplied by official accession. |
| Data license / 数据许可 | EyeDataHub records CC BY 4.0 for mirror; iMED states academic research only. Confirm exact use with custodian. |
| Research use / 科研条件 | Origin site specifies academic research; official Zenodo files require permission. |
| Commercial use / 商业用途 | Origin site limits academic use; verify terms directly before any other use. |
| Terms scope | dataset\_files |
| Terms evidence | [https://zenodo.org/doi/10.5281/zenodo.12775880](https://zenodo.org/doi/10.5281/zenodo.12775880) |
| Upstream route review date | 2026-07-21 |
| Upstream acquisition support | manual\_access\_blocked |
| Upstream access friction | controlled\_or\_manual |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | Three slabs per ROSE-1 subject; deposit describes 26 diseased vs 13 controls; obtain subject groups from custodian before disease prediction. |
| Strengths / 主要优点 | 不同设备 OCTA 分割；可核查跨设备误差。 |
| Limitations / 关键缺陷 | 队列中包含 AD 不证明发布逐图诊断；实际 Zenodo 下载受限；禁止将匿名分割图硬赋 AD 标签。 |
| Suggested experiments / 建议实验 | 经申请后以设备/受试者分组评估血管分割；AD 仅在确证映射后探索。 |
| Retinal Aging suitability | Unknown |
| Stroke / CSVD suitability | Unknown |
| AD / Dementia suitability | D: 研究中有 AD 患者；逐图诊断字典与权限待核。 |
| Multicenter model suitability | G: OCTA 分割、多设备外测。 |
| Screening rationale / 筛查理由 | 研究中有 AD 患者；逐图诊断字典与权限待核。 \| OCTA 分割、多设备外测。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Tier 2 | Tier 2 | 研究中有 AD 患者；逐图诊断字典与权限待核。 | [s3](#evidence-4) |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Tier 3 | Tier 3 | OCTA 分割、多设备外测。 | [s2](#evidence-3) |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Sex / 性别 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Hypertension / 高血压 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Diabetes / 糖尿病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Cardiovascular disease / 心血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Stroke type / 卒中分型 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Stroke timing / 卒中事件时间 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Brain MRI / 脑 MRI | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| CSVD / 脑小血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Alzheimer’s disease / 阿尔茨海默病 | Uncertain | 病种入组确认，官方目录未给逐图诊断映射 | [s3](#evidence-4) |
| Dementia / 痴呆 | Uncertain | 只知队列包含 AD，不可生成逐人标签 | [s3](#evidence-4) |
| Cognition / 认知功能 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Parkinson’s disease / 帕金森病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Frailty / 衰弱 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Health status / 健康状态 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Mortality / 死亡结局 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Follow-up / 纵向随访 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |

## Counting evidence

| Count | Unit | Scope | Evidence basis | Exactness | Source |
| --- | --- | --- | --- | --- | --- |
| 229 | images | Primary quantity reported in the reviewed catalog source | legacy\_catalog\_field | not\_assessed | [Quantity source](https://zenodo.org/doi/10.5281/zenodo.12775880) |

## Family and derivative ledger

Unknown — 未记录具体的资源关系边。患者或影像重叠情况仍见 Identity and provenance。

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Eye–Neurodegeneration — 论文记录有 AD，发布标签待证 | 21 / 31.25 | Not eligible / 28.75 | 2 / 0 / 1 / 1 / 2 | ROSE-1 受试者；外部逐图诊断未知 | 两个设备/子集，病例映射与准入未证。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://zenodo.org/records/12775880)

## Sources

<a id="evidence-1"></a>

### base

[Open original source](https://zenodo.org/doi/10.5281/zenodo.12775880)

EyeDataHub v0.7.0 → rose; catalog fields and dated source review, not a new clinical audit.

Recorded check date — 2026-07-21.

<a id="evidence-2"></a>

### s1

[Open original source](https://zenodo.org/records/12775880)

Current Zenodo v2: file access restricted, request form. Modality/device/counts; public description lacks subject-to-diagnosis manifest.

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s2

[Open original source](https://imed.nimte.ac.cn/dataofrose.html)

Dataset Description; academic research only; device/resolution; two distinct study subsets.

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### s3

[Open original source](https://arxiv.org/abs/2007.05201)

Original paper, ROSE-1 subjects include AD cases and controls; determine whether diagnosis map is distributed separately.

Recorded check date — 2026-11-03.

<a id="evidence-5"></a>

### s4

[Open original source](https://khosravipooya.com/EyeDataHub/datasets/rose/)

v0.7.0 terms/automatic route conflicts with current restricted provider status.

Recorded check date — 2026-11-03.
