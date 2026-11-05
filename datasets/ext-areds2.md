# Age-Related Eye Disease Study 2 (AREDS2)

[All resources](../catalog/README.md) · [Source-reviewed resources](../catalog/reviewed.md)

Metadata as of 2026-11-03 (base survey). Review depth — Source-reviewed. Later targeted corrections are dated in the evidence table and recorded in the [changelog](../CHANGELOG.md).

Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。

## Overview

受控原始眼影像、裁定卒中资料、认知电访、以随机化为原点的事件日数。

当前核验的影像与模态范围 — Color fundus photographs; FAF and SD-OCT in research subsets; lens reflex; raw OCT package coverage unknown

Image availability — v3 发布说明明确受控眼部 DICOM 可取。受控申请核对不同视野、原图与注释/迁移重复、FAF/OCT 子集。

## Identity and provenance

| Field | Recorded value |
| --- | --- |
| Stable resource ID | ext-areds2 |
| Name / 名称 | Age-Related Eye Disease Study 2 (AREDS2) |
| Acronym / 缩写 | AREDS2 |
| Official resource | [https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study\_id=phs002015.v3.p1](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs002015.v3.p1) |
| Country or region / 国家地区 | United States |
| Institution / 机构 | National Eye Institute / US multicenter AREDS Research Group |
| Reported year / 年份口径 | 2025 (datasheet); v3 release 2026 |
| Publication date | Unknown |
| Date scope | Unknown |
| Date evidence | Unknown |
| Date reviewed | Unknown |
| Original citation | Mukherjee S et al. A Datasheet for Age-Related Eye Disease Study 2 on the Database of Genotypes and Phenotypes. Ophthalmol Sci 6:100953 (online 2025). v3 release 9 Oct 2026. |
| Publication DOI | [10.1016/j.xops.2025.100953](https://doi.org/10.1016/j.xops.2025.100953) |
| Dataset DOI | Unknown |
| Import origin | Extension |
| Original EyeDataHub ID | Unknown |
| Dataset family | AREDS program (partly overlapping cohorts) |
| Family or derivative relation | phs002015；1,363 名 WGS 参与者之中 488 人也在 AREDS。病例跨代去重须经批准，不能以两库为默认独立外测。 |
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
| Modalities / 影像模态 | Color fundus photographs; FAF and SD-OCT in research subsets; lens reflex; raw OCT package coverage unknown |
| Images / 图像数及口径 | 512,713 unique ocular DICOM filenames in v3; includes annotated/migrated files; number of unique raw fundus views Unknown |
| Participants / 参与者数及口径 | 4,203 trial participants; 4,201 with v3 mapped ocular DICOM (1,814 male + 2,387 female); compliant image × endpoint overlap Unknown |
| Eyes / 眼别 | RCA/RCF gradings split by eye, participant, visit; DICOM mapping table has no eye field |
| Device / 设备 | Unknown |
| Resolution / 分辨率 | Unknown |
| Quality / 质量控制 | Reading center judged study eyes; longitudinal gradings with retake flag; DICOM header/visit field audit required |
| Multiple visits / 多时点 | Yes — annual visits for ~5 y; calls, yearly grading and cognitive protocol |
| Multiple modalities / 多模态 | Yes — CFP, subset FAF/OCT (cohort); v3 modality-specific raw volume availability not determined |
| Multiple centers / 多中心 | Yes — 82 US sites |

## Access and reuse

| Field | Recorded value |
| --- | --- |
| Access category / 获取方式 | Controlled access |
| Access or application route | [https://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?login=&amp;page=login](https://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?login=&page=login) |
| Image files / 影像文件 | v3 发布说明明确受控眼部 DICOM 可取。受控申请核对不同视野、原图与注释/迁移重复、FAF/OCT 子集。 |
| Individual labels / 个体标签 | v3 人口学、卒中裁定和认知测试字典已核实。c1 4,163 人 GRU-IRB-PUB，c2 40 人眼病用途 DS-ED-IRB-PUB；按具体用途判断可申请子集。 |
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
| Individual linkage / 个体配对依据 | v3 pht016356 通过 SUBJECT\_ID+FILENAME 映射眼部 DICOM；DEM、SAD、CTS 同为 SUBJECT\_ID。用 RCA/RCF 的眼别、访视与成像日期配准。映射中包含 Unknown\_Migrated / Annotated；已知汇总表不提供原始 CFP×认知/卒中交集人数。 CTI和CTS分别3,260与1,510人，不可相加（s12–s13）。 |
| Strengths / 主要优点 | 受控原始眼影像、裁定卒中资料、认知电访、以随机化为原点的事件日数。 |
| Limitations / 关键缺陷 | 研究对象为进展晚期 AMD 的高危患者；脑 MRI 仅查到卒中裁定中的结构化检查所见；认知测验不能替代 AD/痴呆诊断。两个人群同意范围不同。 卒中裁定137人175行，仅87行明确缺血、9行明确出血（s11）。 |
| Suggested experiments / 建议实验 | 先制备患者、眼别、访视、影像类型与终点相交矩阵。卒中以 CASEDATE 时间轴设计预测，认知以 TICS 纵向分数为终点，检查视力与听力/未完成状态。 |
| Retinal Aging suitability | A: DEM 的年龄与已发布的眼部 DICOM 同键。 |
| Stroke / CSVD suitability | B: SAD 有患者级卒中裁定及相对随机化时间。 \| C: 只支持卒中病例的 MRI 获取/梗死/出血结构化所见；不能作脑 MRI 像素或人群 CSVD 训练集。 |
| AD / Dementia suitability | D: TICS 等电话认知测试按患者和访视记录；AD 病理诊断未证实。 |
| Multicenter model suitability | G: 82 个中心；FAF/OCT 仅子集。 |
| Screening rationale / 筛查理由 | DEM 的年龄与已发布的眼部 DICOM 同键。 \| SAD 有患者级卒中裁定及相对随机化时间。 \| 只支持卒中病例的 MRI 获取/梗死/出血结构化所见；不能作脑 MRI 像素或人群 CSVD 训练集。 \| TICS 等电话认知测试按患者和访视记录；AD 病理诊断未证实。 \| 有心血管及死亡/不良事件的患者表。 \| 82 个中心；FAF/OCT 仅子集。 |

## Topic evidence

| Topic | Image-specific tier | Study tier before image-access review | Rationale | Evidence |
| --- | --- | --- | --- | --- |
| [A · Retinal aging / 眼底年龄与衰老](../catalog/topics/A.md) | Tier 1 | Tier 1 | DEM 的年龄与已发布的眼部 DICOM 同键。 | [s4](#evidence-4) |
| [B · Stroke and cerebrovascular risk / 脑卒中与脑血管风险](../catalog/topics/B.md) | Tier 1 | Tier 1 | SAD 有患者级卒中裁定及相对随机化时间。 | [s5](#evidence-5) |
| [C · Brain MRI and CSVD / 脑 MRI 与脑小血管病](../catalog/topics/C.md) | Tier 1 | Tier 1 | 只支持卒中病例的 MRI 获取/梗死/出血结构化所见；不能作脑 MRI 像素或人群 CSVD 训练集。 | [s5](#evidence-5) |
| [D · Alzheimer’s, cognition and dementia / AD、认知与痴呆](../catalog/topics/D.md) | Tier 1 | Tier 1 | TICS 等电话认知测试按患者和访视记录；AD 病理诊断未证实。 | [s6](#evidence-6) |
| [E · Other neurological diseases / 其他神经系统疾病](../catalog/topics/E.md) | Unknown | Unknown | No topic-specific finding | Unknown |
| [F · Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡](../catalog/topics/F.md) | Tier 1 | Tier 1 | 有心血管及死亡/不良事件的患者表。 | [s7](#evidence-7) |
| [G · Multicenter and foundation models / 多中心与基础模型](../catalog/topics/G.md) | Tier 3 | Tier 3 | 82 个中心；FAF/OCT 仅子集。 | [s1](#evidence-1) |

## Clinical phenotypes

| Field | Status | Scope | Evidence |
| --- | --- | --- | --- |
| Age / 年龄 | Confirmed | AGE at randomization, years | [s4](#evidence-4) |
| Sex / 性别 | Confirmed | GENDER | [s4](#evidence-4) |
| Hypertension / 高血压 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Diabetes / 糖尿病 | Confirmed | VIS 患者糖尿病史及新诊指标。 | [s7](#evidence-7) |
| Cardiovascular disease / 心血管病 | Confirmed | 心血管附属研究事件，包括 MI/卒中/死亡等。 | [s7](#evidence-7) |
| Stroke type / 卒中分型 | Confirmed | SADFINAD 最终裁定区分明确缺血性、出血性、蛛网膜下腔出血、TIA、未定型、非卒中等；TOASTCLA 为病因类别，含小血管闭塞。 | [s5](#evidence-5) |
| Stroke timing / 卒中事件时间 | Confirmed | CASEDATE：距随机化天数；SADFINDT 是最终裁定日，不能替代发生日。 | [s5](#evidence-5) |
| Brain MRI / 脑 MRI | Confirmed | SADMRI、MRIINFAR 等为卒中病例 MRI 检查状态/影像所见；原始脑 MRI 未证实。 | [s5](#evidence-5) |
| CSVD / 脑小血管病 | Uncertain | TOAST 小血管分类不能代替人群 WMH、腔隙、微出血等系统标注。 | [s5](#evidence-5) |
| Alzheimer’s disease / 阿尔茨海默病 | Uncertain | 认知评分不证明 AD 确诊。 | [s7](#evidence-7) |
| Dementia / 痴呆 | Uncertain | 未定位独立痴呆诊断字段。 | [s7](#evidence-7) |
| Cognition / 认知功能 | Confirmed | CTS 缩短版电访 TICS；Participant/segment/visit/date 与实施状态。 | [s6](#evidence-6) |
| Parkinson’s disease / 帕金森病 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Frailty / 衰弱 | Uncertain | Unknown — no field-specific evidence recorded for this resource/release. | Unknown |
| Health status / 健康状态 | Confirmed | VIS/ADV 一般健康、住院和不良事件。 | [s7](#evidence-7) |
| Mortality / 死亡结局 | Confirmed | ADV 死亡状态及心血管死亡裁定；全因死亡录入完整性待核。 | [s7](#evidence-7) |
| Follow-up / 纵向随访 | Confirmed | 年度影像检查，电话随访；平均约5年。 | [s1](#evidence-1) |

## Counting evidence

Unknown — 本快照没有单独的图像或参与者数量核验表，已知数量及其口径见 Imaging and cohort。

## Family and derivative ledger

| Source resource | Relation | Target resource | Confidence | Scope | Evidence |
| --- | --- | --- | --- | --- | --- |
| [ext-areds2](ext-areds2.md) | cohort\_overlap | [ext-areds](ext-areds.md) | Confirmed | AREDS2 WGS 1363 人中的 488 人也参加过 AREDS；勿视为外部独立人群。 | [Relationship evidence](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs002015.v3.p1) |

## Research priorities

| Track / endpoint | Science rank / score | Near-term rank / score | R / L / Q / X / M | Denominator | Rationale |
| --- | --- | --- | --- | --- | --- |
| Eye–Neurodegeneration — TICS 等，非 AD 诊断 | 14 / 68.75 | Not eligible / 61.25 | 3 / 3 / 2 / 2 / 3 | 认知文件与眼图交集未知 | 82 个中心，DICOM+ID 字典；dbGaP 资格限制。 |
| Eye–Stroke — 卒中裁定亚型与时间；病例 MRI 裁定摘要 | 12 / 85.0 | Not eligible / 71.25 | 4 / 4 / 2 / 2 / 3 | 137 个裁定对象与影像交集未知 | 82 个中心，DICOM+ID 字典；dbGaP 资格限制。 |
| Retinal Aging — 年龄、多时点眼图 | 9 / 85.0 | Not eligible / 71.25 | 4 / 4 / 2 / 2 / 3 | 有眼部 DICOM 人数，非每类视野完整 | 82 个中心，DICOM+ID 字典；dbGaP 资格限制。 |

R 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。

## Examples and previews

本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、预览或样例获取说明。样例可用性为 Unknown。

[Official resource / 官方示例入口](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs002015.v3.p1)

## Sources

<a id="evidence-1"></a>

### s1

[Open original source](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs002015.v3.p1)

Study Description：82 站点，4,203 人，50–85 岁；两次试验在 WGS 子集重叠 488 人。

Recorded check date — 2026-11-03.

<a id="evidence-2"></a>

### s2

[Open original source](https://ftp.ncbi.nlm.nih.gov/dbgap/studies/phs002015/phs002015.v3.p1/release_notes)

Release notes pp. 1–2：2026-10-09 v3 首次列明新影像与 AREDS2\_Subject\_Image；两个 consent group 及 DAR。

Recorded check date — 2026-11-03.

<a id="evidence-3"></a>

### s3

[Open original source](https://ftp.ncbi.nlm.nih.gov/dbgap/studies/phs002015/phs002015.v3.p1/pheno_variable_summaries/phs002015.v3.pht016356.v1.p1.AREDS2_Subject_Image.var_report.xml)

FILENAME 全组 distinct\_vals=512713，FILE\_TYPE=.dcm；SUBJECT\_ID 概要 1814 男 + 2387 女。例示 annotated、migrated、访问年未知；计数不可等同 CFP 数。

Recorded check date — 2026-11-03.

<a id="evidence-4"></a>

### s4

[Open original source](https://ftp.ncbi.nlm.nih.gov/dbgap/studies/phs002015/phs002015.v3.p1/pheno_variable_summaries/phs002015.v3.pht010376.v1.AREDS2_DEM.data_dict.xml)

DEM：SUBJECT\_ID, AGE (随机化时年龄), GENDER。

Recorded check date — 2026-11-03.

<a id="evidence-5"></a>

### s5

[Open original source](https://ftp.ncbi.nlm.nih.gov/dbgap/studies/phs002015/phs002015.v3.p1/pheno_variable_summaries/phs002015.v3.pht010393.v2.AREDS2_SAD.data_dict.xml)

SAD: SUBJECT\_ID、CASEDATE、SADFINDT、SADFINAD（缺血/出血/TIA/非卒中等），TOASTCLA（含小血管闭塞）和 MRI/CT 结构化所见；时间为随机化后天数。

Recorded check date — 2026-11-03.

<a id="evidence-6"></a>

### s6

[Open original source](https://ftp.ncbi.nlm.nih.gov/dbgap/studies/phs002015/phs002015.v3.p1/pheno_variable_summaries/phs002015.v3.pht010373.v1.AREDS2_CTS.data_dict.xml)

CTS: SUBJECT\_ID，PROTSEG，VISNO，CFMDATE，TICS、听力/CES-D 与是否实施。

Recorded check date — 2026-11-03.

<a id="evidence-7"></a>

### s7

[Open original source](https://pmc.ncbi.nlm.nih.gov/articles/PMC12731274/)

Table 2、Imaging、Cognitive Function：眼别和访视分级、摄影/FAF/OCT 范围、VIS 与 ADV 等；2025 版关于正在上传的描述被 v3 发布说明更新。

Recorded check date — 2026-11-03.

<a id="evidence-8"></a>

### s8

[Open original source](https://www.grants.nih.gov/grants/guide/notice-files/NOT-OD-25-083.html)

NIH NOT-OD-25-083 的机构地域限制。

Recorded check date — 2026-11-03.

<a id="evidence-9"></a>

### s9

[Open original source](https://ftp.ncbi.nlm.nih.gov/dbgap/studies/phs002015/phs002015.v3.p1/pheno_variable_summaries/phs002015.v3.pht016356.v1.AREDS2_Subject_Image.data_dict.xml)

v3 data dictionary: SUBJECT\_ID + FILENAME 复合键映射到 DICOM 眼影像。

Recorded check date — 2026-11-03.

<a id="evidence-10"></a>

### s10

[Open original source](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/GetPdf.cgi?id=phd008132.1)

AREDS2 MOP 裁定章节：病例定义含 TIA、缺血性/出血性卒中，主终点含心血管死亡与卒中。

Recorded check date — 2026-11-03.

<a id="evidence-11"></a>

### s11

[Open original source](https://ftp.ncbi.nlm.nih.gov/dbgap/studies/phs002015/phs002015.v3.p1/pheno_variable_summaries/phs002015.v3.pht010393.v2.p1.AREDS2_SAD.var_report.xml)

137人、175条裁定；缺血87行、明确出血9行、SAH 3行、非卒中31行。MRI Yes 98行，TOAST小血管闭塞12行；非独立患者数。

Recorded check date — 2026-11-03.

<a id="evidence-12"></a>

### s12

[Open original source](https://ftp.ncbi.nlm.nih.gov/dbgap/studies/phs002015/phs002015.v3.p1/pheno_variable_summaries/phs002015.v3.pht010373.v1.p1.AREDS2_CTS.var_report.xml)

CTS短访谈1,510人、2,849行，实际实施2,678行。

Recorded check date — 2026-11-03.

<a id="evidence-13"></a>

### s13

[Open original source](https://ftp.ncbi.nlm.nih.gov/dbgap/studies/phs002015/phs002015.v3.p1/pheno_variable_summaries/phs002015.v3.pht010372.v1.p1.AREDS2_CTI.var_report.xml)

CTI完整访谈3,260人、7,491行；与CTS的交集未知。

Recorded check date — 2026-11-03.
