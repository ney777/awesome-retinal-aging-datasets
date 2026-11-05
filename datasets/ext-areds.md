# Age-Related Eye Disease Study (AREDS)

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

有明确映射文件、双眼历次影像、随访卒中记录和死亡时间/病因。

当前核验的影像与模态范围 — Color stereoscopic fundus photography; lens/anterior-segment photography separately

Image availability — 受控申请可得原始眼底、晶状体等影像及 2014 ID 映射；不能加入 fundus reflex 前节照片作视网膜输入。

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | ext-areds |
| Name / 名称 | Age-Related Eye Disease Study (AREDS) |
| Acronym / 缩写 | AREDS |
| Official resource | [https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study\_id=phs000001.v3.p1](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000001.v3.p1) |
| Country or region / 国家地区 | United States |
| Institution / 机构 | National Eye Institute / US multicenter AREDS Research Group |
| Reported year / 年份口径 | 1999 (design); 2026 (dbGaP datasheet) |
| Publication date | Unknown |
| Date scope | Unknown |
| Date evidence | Unknown |
| Date reviewed | Unknown |
| Original citation | AREDS Research Group. Design Implications: AREDS Report No. 1. Control Clin Trials (1999). Prasad et al. Ophthalmol Sci (2026), 10.1016/j.xops.2026.101115 (release datasheet). |
| Publication DOI | [10.1016/s0197-2456(99)00031-8](https://doi.org/10.1016/s0197-2456%2899%2900031-8) |
| Dataset DOI | Unknown |
| Import origin | Extension |
| Original EyeDataHub ID | Unknown |
| Dataset family | AREDS program (partly overlapping cohorts) |
| Family or derivative relation | 独立试验编号 phs000001；AREDS2 的 WGS 子集有 488 名旧受试者。旧基因样本照片、2014 F2 批次、眼科数据衍生作品不可相加。 |
| Independence / overlap | Patient overlap unverified |
| Upstream family ID | Unknown |
| Upstream resource role | Unknown |
| Review depth | Source-reviewed |
| Best recorded topic tier | Tier 1 |
| Latest recorded source review | 2026-11-03 |
| Frozen upstream description | Unknown |

## Imaging and cohort

| Field | Recorded value |
| --- | --- |
| Modalities / 影像模态 | Color stereoscopic fundus photography; lens/anterior-segment photography separately |
| Images / 图像数及口径 | 2014 batch &gt;134,500 macular field F2 CFP (4,613 people); older &gt;72,000 mixed lens/fundus images (595); do not sum individuals or count all as CFP |
| Participants / 参与者数及口径 | 4,757 enrolled; 4,613 F2 batch; endpoint-specific overlap unknown |
| Eyes / 眼别 | Bilateral, field and stereopair identifiers |
| Device / 设备 | Standardized 30° stereoscopic retinal photography |
| Resolution / 分辨率 | Unknown |
| Quality / 质量控制 | Reading center grading; high-quality F2 images in 2014 batch |
| Multiple visits / 多时点 | Yes — baseline, years 2,4,6,8,10 and selected event/last photos; visit-dependent missingness |
| Multiple modalities / 多模态 | Fundus and lens photos; no brain imaging confirmed |
| Multiple centers / 多中心 | Yes — multi-center US trial |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Controlled access |
| Access or application route | [https://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?login=&amp;page=login](https://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?login=&page=login) |
| Image files / 影像文件 | 受控申请可得原始眼底、晶状体等影像及 2014 ID 映射；不能加入 fundus reflex 前节照片作视网膜输入。 |
| Individual labels / 个体标签 | 患者级人口学、基线史、随访新发卒中/心脏病记录和死亡表可申请；认知子研究原始测试数据申请路径未证实。 |
| Data license / 数据许可 | dbGaP Data Use Certification; applicable consent group and approved data use |
| Research use / 科研条件 | 合格机构 PI 经 dbGaP DAR/IRB、数据使用审查。NOT-OD-25-083 自 2025-04-04 起禁止位于中国（含香港/澳门）等所列地区的机构访问 NIH 受控库及相关数据。 |
| Commercial use / 商业用途 | Unknown — specific consent group, Data Use Certification and approved use govern |
| Terms scope | Unknown |
| Terms evidence | Unknown |
| Upstream route review date | Unknown |
| Upstream acquisition support | Unknown |
| Upstream access friction | Unknown |

## Research value and experimental design

| Field | Recorded value |
| --- | --- |
| Individual linkage / 个体配对依据 | v3 使用 ID2。旧照片文件编码 ID2、VISNO、眼别、拍摄视野；2014 图像目录由授权的 AREDS\_Image\_Mapping\_ImageDir\_ID2.txt 将 RC\_ID 映射至 ID2。按 ID2 + VISNO 连接 followup；死亡表为患者行。 |
| Strengths / 主要优点 | 有明确映射文件、双眼历次影像、随访卒中记录和死亡时间/病因。 |
| Limitations / 关键缺陷 | 高龄眼病试验，非一般人口；卒中由访视记录，精确发生日和亚型需额外确认；试验内 AMD 与视力损失可影响测试。 |
| Suggested experiments / 建议实验 | 基线 F2 照片与后续死亡做生存预测，时间零设为首张合格图；卒中只研究既往排除后的首次访视报告，按区间删失建模。 |
| Retinal Aging suitability | A: ID2 影像可连至基线人口学和历次访视。 |
| Stroke / CSVD suitability | B: followup 含新发卒中询问，属访视级记录。 |
| AD / Dementia suitability | D: 2,946 人认知子研究已发表；当前 13 张发布表未定位认知测试原始表。 |
| Multicenter model suitability | G: 多中心有统一拍摄流程；站点划分需核对可获得的字段。 |
| Screening rationale / 筛查理由 | ID2 影像可连至基线人口学和历次访视。 \| followup 含新发卒中询问，属访视级记录。 \| 2,946 人认知子研究已发表；当前 13 张发布表未定位认知测试原始表。 \| 死亡表的随访时长、ICD 死因、死因质量及心血管/糖尿病史。 \| 多中心有统一拍摄流程；站点划分需核对可获得的字段。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 1 | Tier 1 | ID2 影像可连至基线人口学和历次访视。 | [s2](#evidence-2) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Tier 1 | Tier 1 | followup 含新发卒中询问，属访视级记录。 | [s3](#evidence-3) |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Tier 2 | Tier 2 | 2,946 人认知子研究已发表；当前 13 张发布表未定位认知测试原始表。 | [s5](#evidence-5) |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Tier 1 | Tier 1 | 死亡表的随访时长、ICD 死因、死因质量及心血管/糖尿病史。 | [s4](#evidence-4) |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Tier 3 | Tier 3 | 多中心有统一拍摄流程；站点划分需核对可获得的字段。 | [s1](#evidence-1) |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | 人口学登记；影像年龄需纳入到相应访视之间的间隔。 | [s6](#evidence-6) |
| Sex / 性别 | Confirmed | 基线人口学表。 | [s6](#evidence-6) |
| Hypertension / 高血压 | Confirmed | 基线高血压存在与否。 | [s3](#evidence-3) |
| Diabetes / 糖尿病 | Confirmed | 基线及随访糖尿病状态。 | [s3](#evidence-3) |
| Cardiovascular disease / 心血管病 | Confirmed | 心绞痛病史/新发心脏病/外周血管病等。 | [s3](#evidence-3) |
| Stroke type / 卒中分型 | Uncertain | 随访表询问新诊卒中，已查文档未证实统一缺血/出血亚型。 | [s3](#evidence-3) |
| Stroke timing / 卒中事件时间 | Uncertain | 访视和区间可获得；精确卒中发生日未核验。 | [s4](#evidence-4) |
| Brain MRI / 脑 MRI | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| CSVD / 脑小血管病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Alzheimer’s disease / 阿尔茨海默病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Dementia / 痴呆 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Cognition / 认知功能 | Uncertain | 报告16有2,946人横断面认知电池；个人原始分数在v3的可得性未证实。 | [s5](#evidence-5) |
| Parkinson’s disease / 帕金森病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Frailty / 衰弱 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Health status / 健康状态 | Confirmed | 随访问卷与就医/健康状态变量；不等于虚弱指数。 | [s4](#evidence-4) |
| Mortality / 死亡结局 | Confirmed | 追踪至死亡的时间、ICD 死因、NDI 匹配可靠性。 | [s4](#evidence-4) |
| Follow-up / 纵向随访 | Confirmed | 不同拍摄时间和末次照片；定期随访。 | [s2](#evidence-2) |

## Counting evidence

Unknown — 本快照没有单独的图像或参与者数量核验表，已知数量及其口径见 Imaging and cohort。

## Family and derivative ledger

| Source resource | Relation | Target resource | Confidence | Scope | Evidence |
| --- | --- | --- | --- | --- | --- |
| [ext-areds2](ext-areds2.md) | cohort\_overlap | [ext-areds](ext-areds.md) | Confirmed | AREDS2 WGS 1363 人中的 488 人也参加过 AREDS；勿视为外部独立人群。 | [Relationship evidence](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs002015.v3.p1) |

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Eye–Neurodegeneration — 认知子研究 | 18 / 52.5 | Not eligible / 51.25 | 2 / 2 / 2 / 2 / 3 | 认知子研究原始资料待核 | 多中心试验、有正式受控眼图路径；地域适格性另审。 |
| Eye–Stroke — 新发卒中记录，亚型待核 | 16 / 68.75 | Not eligible / 61.25 | 3 / 3 / 2 / 2 / 3 | 临床事件 × 眼图分母未知 | 多中心试验、有正式受控眼图路径；地域适格性另审。 |
| Retinal Aging — 重复眼底及年龄 | 9 / 85.0 | Not eligible / 71.25 | 4 / 4 / 2 / 2 / 3 | F2 批次人数，非所有眼底字段交集 | 多中心试验、有正式受控眼图路径；地域适格性另审。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000001.v3.p1)

## Sources

<a id="evidence-1"></a>

### s1

[Open original source](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000001.v3.p1)

Study Description: 2014 F2 影像数（&gt;134,500，4,613 人）与较早含晶状体批次（&gt;72,000，595 人）。

Recorded check date — 2026-11-03.

<a id="evidence-2"></a>

### s2

[Open original source](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/document.cgi?phd=3307&study_id=phs000001.v3.p1)

Image File Naming Convention and 2014 addendum: ID2, VISNO，左右眼及 RC\_ID 与 ID2 的授权映射表。

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s3

[Open original source](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/GetListOfAllObjects.cgi?object_type=dataset&study_id=phs000001.v3.p1)

enrollment\_randomization (pht000373), followup (pht000374), mortality；v3 使用 ID2；列出卒中等疾病新诊与病史。

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### s4

[Open original source](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/GetPdf.cgi?id=phd001552.2)

User’s Guide pp. 5–6: 死亡追踪、ICD/NDI、访视时间单位及日期抑制。ID 部分以 v3 更新为准。

Recorded check date — 2026-11-03.

<a id="evidence-5"></a>

### s5

[Open original source](https://pubmed.ncbi.nlm.nih.gov/16606880/)

AREDS Report 16，2,946 人认知测试与 AMD/视力的横断关联；未提供受控表入口。

Recorded check date — 2026-11-03.

<a id="evidence-6"></a>

### s6

[Open original source](https://pubmed.ncbi.nlm.nih.gov/41858680/)

2026 release datasheet：4,757 人、年龄性别、图像和疾病/死亡等随访数据。

Recorded check date — 2026-11-03.

<a id="evidence-7"></a>

### s7

[Open original source](https://www.grants.nih.gov/grants/guide/notice-files/NOT-OD-25-083.html)

NIH NOT-OD-25-083 的机构地域限制。

Recorded check date — 2026-11-03.

<a id="evidence-8"></a>

### s8

[Open original source](https://pmc.ncbi.nlm.nih.gov/articles/PMC1473211/)

原始设计报告（1999）及拍摄计划。

Recorded check date — 2026-11-03.

<a id="evidence-9"></a>

### s9

[Open original source](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs002015.v3.p1)

4,203 名 AREDS2 受试者；1,363 人 WGS 子集内有 488 人参加原 AREDS。

Recorded check date — 2026-11-03.
