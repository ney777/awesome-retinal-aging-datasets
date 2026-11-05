# AlzEye

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

临床影像及住院诊断、死亡的链接已实现，英格兰长期监测。

当前核验的影像与模态范围 — Fundus \| OCT \| other ocular imaging

Image availability — Restricted to AlzEye team under cohort-specific contract; general INSIGHT SRE is not an external AlzEye dataset release.

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | ext-alzeye |
| Name / 名称 | AlzEye |
| Acronym / 缩写 | AlzEye |
| Official resource | [https://www.insight.hdrhub.org/alzeye](https://www.insight.hdrhub.org/alzeye) |
| Country or region / 国家地区 | United Kingdom |
| Institution / 机构 | Moorfields Eye Hospital / UCL / NHS Digital |
| Reported year / 年份口径 | 2022 |
| Publication date | Unknown |
| Date scope | Unknown |
| Date evidence | Unknown |
| Date reviewed | Unknown |
| Original citation | Wagner SK et al. AlzEye: longitudinal record-level linkage of ophthalmic imaging and hospital admissions of 353,157 patients in London, UK. BMJ Open. 2022. |
| Publication DOI | [10.1136/bmjopen-2021-058552](https://doi.org/10.1136/bmjopen-2021-058552) |
| Dataset DOI | Unknown |
| Import origin | Extension |
| Original EyeDataHub ID | Unknown |
| Dataset family | AlzEye |
| Family or derivative relation | Distinct from UK Biobank; PD paper used AlzEye and UKB separately. |
| Independence / overlap | Patient overlap unverified |
| Upstream family ID | Unknown |
| Upstream resource role | Unknown |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 2 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | Unknown |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | Fundus \| OCT \| other ocular imaging |
| Images / 图像数及口径 | 2022 cohort profile reported 1,874,175 retinal photographs and 1,567,358 OCT images; updated INSIGHT overview reports &gt;6M retinal images across project scope. |
| Participants / 参与者数及口径 | 353,157 cohort members; 186,651 linked with an admission; retinal imaging available for 154,830 in published PD analysis denominator. |
| Eyes / 眼别 | Unknown |
| Device / 设备 | Unknown |
| Resolution / 分辨率 | Unknown |
| Quality / 质量控制 | Unknown |
| Multiple visits / 多时点 | Yes; clinic visits and national admissions. |
| Multiple modalities / 多模态 | Yes |
| Multiple centers / 多中心 | One NHS trust, multiple locations; not independent hospital cohorts. |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Unavailable |
| Access or application route | [https://www.insight.hdrhub.org/alzeye](https://www.insight.hdrhub.org/alzeye) |
| Image files / 影像文件 | Restricted to AlzEye team under cohort-specific contract; general INSIGHT SRE is not an external AlzEye dataset release. |
| Individual labels / 个体标签 | Linked HES diagnoses and mortality held by team. PD study welcomes proposals to PI; no independent access. |
| Data license / 数据许可 | Unknown |
| Research use / 科研条件 | Collaborative enquiry via PI, not standard independent data request. Scope of source-specific contract controls. |
| Commercial use / 商业用途 | Unknown |
| Terms scope | Unknown |
| Terms evidence | Unknown |
| Upstream route review date | Unknown |
| Upstream acquisition support | Unknown |
| Upstream access friction | Unknown |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | Study team linked retinal images to HES via trusted third party using NHS identifiers. Counts of attendees, imaged participants and admitted patients differ. |
| Strengths / 主要优点 | 临床影像及住院诊断、死亡的链接已实现，英格兰长期监测。 |
| Limitations / 关键缺陷 | 住院编码漏诊，医院就诊样本有选择性；对外不可独立取得既有链接。 |
| Suggested experiments / 建议实验 | 仅作为合作价值推荐；经同意后研究 PD 或痴呆住院诊断的发生，按时间剔除基线患病者并区分死亡竞争风险。 |
| Retinal Aging suitability | A: 研究内按年龄配对；外部合同限制。 |
| Stroke / CSVD suitability | B: HES 编码及眼底已有研究链接，独立使用受限。 |
| AD / Dementia suitability | D: 已有同人 AD/痴呆链接；仅可讨论团队内合作。 |
| Multicenter model suitability | Unknown |
| Screening rationale / 筛查理由 | 研究内按年龄配对；外部合同限制。 \| HES 编码及眼底已有研究链接，独立使用受限。 \| 已有同人 AD/痴呆链接；仅可讨论团队内合作。 \| PD 与 OCT 研究可核，团队外访问受限。 \| 死亡资料已链接；外部审批未证实。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 2 | Tier 2 | 研究内按年龄配对；外部合同限制。 | [s1](#evidence-1) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Tier 2 | Tier 2 | HES 编码及眼底已有研究链接，独立使用受限。 | [s1](#evidence-1) |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Tier 2 | Tier 2 | 已有同人 AD/痴呆链接；仅可讨论团队内合作。 | [s2](#evidence-2) |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Tier 2 | Tier 2 | PD 与 OCT 研究可核，团队外访问受限。 | [s3](#evidence-3) |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Tier 2 | Tier 2 | 死亡资料已链接；外部审批未证实。 | [s1](#evidence-1) |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Unknown | Unknown | No topic-specific finding | Unknown |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | 40 岁以上，有年龄字段 | [s1](#evidence-1) |
| Sex / 性别 | Confirmed | 个体性别 | [s1](#evidence-1) |
| Hypertension / 高血压 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Diabetes / 糖尿病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Cardiovascular disease / 心血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Stroke type / 卒中分型 | Uncertain | HES 卒中/TIA 编码涉及漏捕；具体亚型供申请者使用未证实 | [s1](#evidence-1) |
| Stroke timing / 卒中事件时间 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Brain MRI / 脑 MRI | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| CSVD / 脑小血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Alzheimer’s disease / 阿尔茨海默病 | Confirmed | HES 诊断 | [s2](#evidence-2) |
| Dementia / 痴呆 | Confirmed | HES 诊断 | [s2](#evidence-2) |
| Cognition / 认知功能 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Parkinson’s disease / 帕金森病 | Confirmed | 既往/患病 PD；AlzEye 不等于 UKB 的前驱 PD 预测 | [s3](#evidence-3) |
| Frailty / 衰弱 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Health status / 健康状态 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Mortality / 死亡结局 | Confirmed | 原研究死亡资料；死因证书扩展见 s2 | [s1](#evidence-1) |
| Follow-up / 纵向随访 | Confirmed | 多年度诊疗及住院记录 | [s1](#evidence-1) |

## Counting evidence

Unknown — 本快照没有单独的图像或参与者数量核验表，已知数量及其口径见 Imaging and cohort。

## Family and derivative ledger

Unknown — 未记录具体的资源关系边。患者或影像重叠情况仍见 Identity and provenance。

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Eye–Neurodegeneration — 诊断编码 AD、痴呆、PD | 12 / 70.0 | Not eligible / 41.25 | 4 / 3 / 1 / 0 / 2 | 各病种有效交集需核 | 医院多个地点；限原团队分析个体系统疾病资料。 |
| Eye–Stroke — HES 脑血管事件，限原团队 | 18 / 53.75 | Not eligible / 31.25 | 3 / 2 / 1 / 0 / 2 | 本次未取得事件个案交集 | 医院多个地点；限原团队分析个体系统疾病资料。 |
| Retinal Aging — 年龄及纵向健康记录 | 23 / 63.75 | Not eligible / 37.5 | 4 / 2 / 1 / 0 / 2 | 不能使用整个 NHS 母库数作年龄共现数 | 医院多个地点；限原团队分析个体系统疾病资料。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://www.insight.hdrhub.org/alzeye)

## Sources

<a id="evidence-1"></a>

### s1

[Open original source](https://bmjopen.bmj.com/content/12/3/e058552)

Cohort profile: participants, imaging, individual NHS/HES linkage, mortality and stroke coding limitations; Data availability explicitly restricts to AlzEye research team.

Recorded check date — 2026-11-03.

<a id="evidence-2"></a>

### s2

[Open original source](https://www.insight.hdrhub.org/alzeye)

Project overview: dementia/AD linkage, update agreed in 2025 for HES through 2024 and death certificates; no external access commitment.

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s3

[Open original source](https://discovery.ucl.ac.uk/10175799/1/e1581.full.pdf)

Neurology PD study, Results and Data Availability: 700 with prevalent PD among 154,830 imaged; collaboration via PI, data unavailable outside AlzEye team.

Recorded check date — 2026-11-03.
