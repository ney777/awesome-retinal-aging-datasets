# Research priorities and rankings

[Dataset catalog](catalog/README.md) · [Statistics](STATS.md) · [Machine-readable rankings](library/output/rankings.csv) · [Detailed scoring methods](library/METHODS.md)

This snapshot contains **83 resource–task pairs across 42 resource records**, with **9 pairs eligible for the near-term list**. The latest resource-level review date among ranked resources is 2026-11-03. These are project-specific prioritization judgments, not independent cohort counts, clinical validation results, or a certification of data quality. Resource names link to stable pages containing evidence, access conditions and limitations.

The scientific summaries below select **competition ranks 1–3, including all ties**. Equal scores receive the same rank and subsequent positions are skipped (for example, 1, 1, 1, 1, 5). They do not select the first three distinct score bands or arbitrarily truncate a tied group. The near-term summaries show **every eligible pair**.

[Retinal Aging](#retinal-aging) · [Eye–Stroke](#eye-stroke) · [Eye–Neurodegeneration](#eye-neurodegeneration) · [Five components and eligibility](#five-components-and-eligibility) · [All ranking rows](#all-ranking-rows) · [Reproduce](#reproduce)

<a id="retinal-aging"></a>

## Retinal Aging

40 resource–task pairs are scored for this direction.

### Scientific priority: ranks 1–3, with ties

<!-- scientific-top: retinal-aging -->

| Science rank | Resource | Science / 100 | Topic tier | Access route |
| --- | --- | --- | --- | --- |
| 1 | [Atherosclerosis Risk in Communities (ARIC) retinal ancillary studies](datasets/ext-aric.md) | 97.5 | A T2 | Controlled access |
| 1 | [Cardiovascular Health Study (CHS) retinal examination](datasets/ext-chs.md) | 97.5 | A T2 | Controlled access |
| 1 | [Scottish Collaborative Optometry-Ophthalmology Network e-research (SCONe)](datasets/ext-scone-scotland.md) | 97.5 | A T1 | Controlled access |
| 1 | [UK Biobank Eye and Vision / UK Biobank Repeat Imaging](datasets/ext-uk-biobank.md) | 97.5 | A T1 | Controlled access |

<!-- /scientific-top: retinal-aging -->

4 resources share rank 1. All are retained in this summary. Scientific rank does not imply current access to the required images or labels.

### Near-term implementation: all 7 eligible pairs

<!-- near-term: retinal-aging -->

| Near-term rank | Resource | Near-term / 100 | Endpoint | Size-score N and scope |
| --- | --- | --- | --- | --- |
| 1 | [Glaucoma Real-world Appraisal Progression Ensemble (GRAPE)](datasets/grape.md) | 87.5 | 年龄、多访视青光眼 | 144 — Study-linked participants: 整队列患者，非全部多次 CFP 人数 |
| 2 | [China-Fundus-CIMT](datasets/china_fundus_cimt.md) | 76.25 | 年龄与同期 CIMT | 2903 — Study-linked participants: 人级双眼真实年龄 |
| 3 | [MCFI: A Multi-Session Colored Fundus Image Dataset](datasets/ext-mcfi.md) | 75 | 同眼短期重测；长期衰老速率样本不足 | 37 — Study-linked participants: 37 人都有同眼跨日影像，11 人跨度至少180天 |
| 4 | [Harvard-FairVLMed](datasets/fairvlmed.md) | 73.75 | 年龄、SLO 与临床文本 | 10000 — Study-linked participants: 发布者每人一份 |
| 4 | [Harvard-FairVision (30K)](datasets/harvard_fairvision.md) | 73.75 | 配对 SLO+OCT 年龄 | 30000 — Study-linked participants: 发布者总人数，年龄完备性需核 |
| 6 | [PAPILA](datasets/papila.md) | 71.25 | 逐眼实足年龄 | 244 — Study-linked participants: 逐眼表与影像匹配 |
| 7 | [Johns Hopkins OCT MS and Healthy Controls](datasets/oct_ms_jhu.md) | 60 | 可唯一匹配的 OCT 年龄 | 26 — Study-linked participants: 仅 26 个唯一 ID 能匹配个体年龄 |

<!-- /near-term: retinal-aging -->

<a id="eye-stroke"></a>

## Eye–Stroke

22 resource–task pairs are scored for this direction.

### Scientific priority: ranks 1–3, with ties

<!-- scientific-top: eye-stroke -->

| Science rank | Resource | Science / 100 | Topic tier | Access route |
| --- | --- | --- | --- | --- |
| 1 | [Atherosclerosis Risk in Communities (ARIC) retinal ancillary studies](datasets/ext-aric.md) | 97.5 | B T2 / C T2 | Controlled access |
| 1 | [Cardiovascular Health Study (CHS) retinal examination](datasets/ext-chs.md) | 97.5 | B T2 / C T2 | Controlled access |
| 1 | [Multi-Ethnic Study of Atherosclerosis (MESA Eye / cognitive–MRI ancillaries)](datasets/ext-mesa.md) | 97.5 | B T2 / C T2 | Controlled access |
| 1 | [UK Biobank Eye and Vision / UK Biobank Repeat Imaging](datasets/ext-uk-biobank.md) | 97.5 | B T1 / C T1 | Controlled access |

<!-- /scientific-top: eye-stroke -->

4 resources share rank 1. All are retained in this summary. Scientific rank does not imply current access to the required images or labels.

### Near-term implementation: all 0 eligible pairs

<!-- near-term: eye-stroke -->

**No pair passes the current near-term gates in this direction.** The scientific candidates still require resolution of image access, endpoint availability, authorization or readiness. This empty list does not establish that no suitable dataset exists elsewhere.

<!-- /near-term: eye-stroke -->

<a id="eye-neurodegeneration"></a>

## Eye–Neurodegeneration

21 resource–task pairs are scored for this direction.

### Scientific priority: ranks 1–3, with ties

<!-- scientific-top: eye-neurodegeneration -->

| Science rank | Resource | Science / 100 | Topic tier | Access route |
| --- | --- | --- | --- | --- |
| 1 | [UK Biobank Eye and Vision / UK Biobank Repeat Imaging](datasets/ext-uk-biobank.md) | 97.5 | D T1 / E T1 | Controlled access |
| 2 | [Atherosclerosis Risk in Communities (ARIC) retinal ancillary studies](datasets/ext-aric.md) | 85 | D T2 | Controlled access |
| 3 | [Cardiovascular Health Study (CHS) retinal examination](datasets/ext-chs.md) | 81.25 | D T2 | Controlled access |
| 3 | [Scottish Collaborative Optometry-Ophthalmology Network e-research (SCONe)](datasets/ext-scone-scotland.md) | 81.25 | D T1 / E T1 | Controlled access |

<!-- /scientific-top: eye-neurodegeneration -->

2 resources share rank 3. All are retained in this summary. Scientific rank does not imply current access to the required images or labels.

### Near-term implementation: all 2 eligible pairs

<!-- near-term: eye-neurodegeneration -->

| Near-term rank | Resource | Near-term / 100 | Endpoint | Size-score N and scope |
| --- | --- | --- | --- | --- |
| 1 | [TREND2 chronic-disease fundus study](datasets/trend2_fundus.md) | 71.25 | AD 二元标记，7 阳性 ID-eye | Unknown — Unknown: 28 个 ID-eye，独立患者人数未知 |
| 2 | [Functional OCT Retinal Response Dataset (Bissig)](datasets/dryad_functional_oct_alzheimer.md) | 60 | 功能 OCT、早发 AD 病例对照 | 28 — Study-linked participants: 14 EOAD ＋ 14 年龄匹配对照 |

<!-- /near-term: eye-neurodegeneration -->

<a id="five-components-and-eligibility"></a>

## Five components and eligibility

Each component is scored from 0 to 4 (ranked R values are 1–4). The five scores remain separate in the full tables; access feasibility is not folded into the scientific score. The source [judgment profiles](library/inputs/score_profiles.tsv), [endpoint and denominator inputs](library/inputs/score_targets.tsv), [label exceptions](library/inputs/score_label_omissions.json) and [ranking calculation](library/src/ranking.py) make the decisions auditable.

| Component | Meaning | Rule summary |
| --- | --- | --- |
| R | Scientific relevance | Endpoint-specific relevance: 4 direct principal target; 3 direct age, clinical case–control, imaging or cognition; 2 proxy or restricted bridge; 1 weak match such as age bands. |
| L | Label richness | For k confirmed fields from the direction-specific field set: min(4, ceil(k/2)); recorded field exclusions apply. |
| Q | Cohort quality | One point each for supported endpoint-linked N ≥100 and ≥1000, population sampling, documented quality control, and confirmed follow-up; capped at 4. |
| X | Access feasibility | 4 documented open image/label route; 3 explicit conditional or registration route; 2 formal image application or named secure project; 1 contact or unresolved pixel/authorization scope; 0 paused, prohibited or unverified route. |
| M | Multicenter value | 0 unclear source; 1 one site or independent population/device domain; 2 device, population or recruitment heterogeneity; 3 documented multicenter/community project; 4 verifiable center keys plus regional/device distribution. |

**Scientific score** = (40R + 25L + 25Q + 10M) / 4. **Near-term implementation score** = (25R + 15L + 10Q + 5M + 45X) / 4. Both use a 0–100 scale.

A near-term rank is assigned only when the original curation marks the endpoint as ready, the relevant topic includes Tier 1, R ≥3 and X ≥3. A calculated implementation score does not bypass these gates. **Not eligible** means no near-term rank is assigned, even though the component-based score is retained. Eligibility is scoped to the stated endpoint and source review date; it does not establish permission for an individual applicant or sufficient sample size for a population model.

**Denominator rule:** only study-linked participants and documented outcome-positive subsets can contribute scale points. A lower-bound case count is not a complete analysis cohort. A parent-cohort count, unmatched image count or unknown participant denominator does not receive scale points. `N for size score` is the original `n_supported`; `reported_n` is preserved separately below. Neither is a promise of currently deliverable training pairs.

**Choose the endpoint before using a rank.** Incident stroke, contemporaneous small-vessel disease, self-reported stroke and carotid thickness are different targets. Short-term retest data, continuous-age prediction and biological-aging validation are also different experiments. The tables preserve the original endpoint and rationale wording instead of combining these targets into one implied clinical benchmark.

<a id="all-ranking-rows"></a>

## All ranking rows: 83 resource–task pairs

Each expandable section contains every row for that direction. The first table preserves all five components and both scores/ranks; the second preserves endpoint, denominator, access and scoring context. Equal-score rows are ordered by R and then stable resource ID for reproducible display; this does not break their shared rank.

<details>

<summary>Retinal Aging — all 40 ranking rows</summary>

### Scores and ranks

<!-- all-scores: retinal-aging -->

| Resource | R | L | Q | X | M | Science rank | Science / 100 | Near-term rank | Near-term / 100 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Atherosclerosis Risk in Communities (ARIC) retinal ancillary studies](datasets/ext-aric.md) | 4 | 4 | 4 | 1 | 3 | 1 | 97.5 | Not eligible | 65 |
| [Cardiovascular Health Study (CHS) retinal examination](datasets/ext-chs.md) | 4 | 4 | 4 | 1 | 3 | 1 | 97.5 | Not eligible | 65 |
| [Scottish Collaborative Optometry-Ophthalmology Network e-research (SCONe)](datasets/ext-scone-scotland.md) | 4 | 4 | 4 | 2 | 3 | 1 | 97.5 | Not eligible | 76.25 |
| [UK Biobank Eye and Vision / UK Biobank Repeat Imaging](datasets/ext-uk-biobank.md) | 4 | 4 | 4 | 0 | 3 | 1 | 97.5 | Not eligible | 53.75 |
| [Age, Gene/Environment Susceptibility–Reykjavik Study (AGES-RS)](datasets/ext-ages-reykjavik.md) | 4 | 4 | 4 | 1 | 1 | 5 | 92.5 | Not eligible | 62.5 |
| [Blue Mountains Eye Study (BMES)](datasets/ext-bmes.md) | 4 | 4 | 4 | 1 | 1 | 5 | 92.5 | Not eligible | 62.5 |
| [Multi-Ethnic Study of Atherosclerosis (MESA Eye / cognitive–MRI ancillaries)](datasets/ext-mesa.md) | 4 | 3 | 4 | 1 | 3 | 7 | 91.25 | Not eligible | 61.25 |
| [Northern Ireland Cohort for the Longitudinal Study of Ageing (NICOLA)](datasets/ext-nicola.md) | 4 | 3 | 4 | 1 | 1 | 8 | 86.25 | Not eligible | 58.75 |
| [Age-Related Eye Disease Study (AREDS)](datasets/ext-areds.md) | 4 | 4 | 2 | 2 | 3 | 9 | 85 | Not eligible | 71.25 |
| [Age-Related Eye Disease Study 2 (AREDS2)](datasets/ext-areds2.md) | 4 | 4 | 2 | 2 | 3 | 9 | 85 | Not eligible | 71.25 |
| [NHANES 2005–2008 Ophthalmology – Retinal Imaging (OPXRET\_D / OPXRET\_E)](datasets/ext-nhanes-2005-2008-retina.md) | 3 | 4 | 4 | 0 | 2 | 9 | 85 | Not eligible | 46.25 |
| [NHANES III (1988–1994) fundus grading and NDI linkage](datasets/ext-nhanes-iii-retina.md) | 3 | 4 | 4 | 0 | 2 | 9 | 85 | Not eligible | 46.25 |
| [Shanghai Diabetes Prevention Program (SDPP; DeepRETStroke subsets)](datasets/ext-shanghai-sdpp.md) | 4 | 2 | 4 | 1 | 1 | 13 | 80 | Not eligible | 55 |
| [Singapore two-site memory clinic retinal vessel cohort](datasets/ext-singapore-memory-clinics.md) | 4 | 3 | 2 | 1 | 2 | 14 | 76.25 | Not eligible | 55 |
| [Glaucoma Real-world Appraisal Progression Ensemble (GRAPE)](datasets/grape.md) | 4 | 2 | 3 | 4 | 2 | 14 | 76.25 | 1 | 87.5 |
| [EyePACS full research cohort used for eyeAge](datasets/ext-eyepacs-eyeage.md) | 4 | 1 | 4 | 1 | 1 | 16 | 73.75 | Not eligible | 51.25 |
| [Rotterdam Study / Rotterdam Scan Study (ERGO)](datasets/ext-rotterdam-study.md) | 4 | 1 | 4 | 1 | 1 | 16 | 73.75 | Not eligible | 51.25 |
| [Singapore Epidemiology of Eye Diseases (SEED), including SCES → EDIS retinal subcohort](datasets/ext-seed-edis.md) | 4 | 2 | 2 | 2 | 2 | 18 | 70 | Not eligible | 62.5 |
| [Beijing Eye Study 2011 retinal / stroke and cognition substudies](datasets/ext-beijing-eye-study.md) | 3 | 3 | 3 | 1 | 1 | 18 | 70 | Not eligible | 50 |
| [Rhineland Study / Rheinland Studie](datasets/ext-rhineland-study.md) | 3 | 2 | 4 | 2 | 1 | 18 | 70 | Not eligible | 60 |
| [Mobile Brazilian Retinal Dataset (mBRSET)](datasets/mbrset.md) | 3 | 3 | 3 | 2 | 1 | 18 | 70 | Not eligible | 61.25 |
| [Lothian Birth Cohort 1936 (LBC1936) retinal and brain imaging](datasets/ext-lothian-birth-cohort-1936.md) | 2 | 3 | 4 | 1 | 1 | 22 | 66.25 | Not eligible | 46.25 |
| [AlzEye](datasets/ext-alzeye.md) | 4 | 2 | 1 | 0 | 2 | 23 | 63.75 | Not eligible | 37.5 |
| [The Maastricht Study](datasets/ext-maastricht-study.md) | 3 | 2 | 3 | 1 | 1 | 23 | 63.75 | Not eligible | 46.25 |
| [China-Fundus-CIMT](datasets/china_fundus_cimt.md) | 3 | 1 | 3 | 4 | 1 | 25 | 57.5 | 2 | 76.25 |
| [Brazilian Multilabel Ophthalmological Dataset (BRSET)](datasets/brset.md) | 3 | 2 | 1 | 2 | 3 | 26 | 56.25 | Not eligible | 55 |
| [Framingham Eye Study (FES I/II), Original Framingham Heart Study cohort](datasets/ext-framingham-original-eye.md) | 2 | 2 | 3 | 1 | 1 | 27 | 53.75 | Not eligible | 40 |
| [FDR26 (Morocco)](datasets/ext-fdr26.md) | 3 | 2 | 1 | 3 | 1 | 28 | 51.25 | Not eligible | 63.75 |
| [MCFI: A Multi-Session Colored Fundus Image Dataset](datasets/ext-mcfi.md) | 3 | 2 | 1 | 4 | 1 | 28 | 51.25 | 3 | 75 |
| [Harvard-FairVLMed](datasets/fairvlmed.md) | 3 | 1 | 2 | 4 | 1 | 28 | 51.25 | 4 | 73.75 |
| [Harvard-FairVision (30K)](datasets/harvard_fairvision.md) | 3 | 1 | 2 | 4 | 1 | 28 | 51.25 | 4 | 73.75 |
| [Ocular Disease Intelligent Recognition (ODIR-5K / ODIR-2019)](datasets/odir2019.md) | 3 | 1 | 1 | 1 | 3 | 32 | 50 | Not eligible | 40 |
| [Ontario Neurodegenerative Disease Research Initiative (ONDRI), Foundational Study release 2.0](datasets/ext-ondri.md) | 2 | 1 | 2 | 1 | 3 | 33 | 46.25 | Not eligible | 36.25 |
| [Johns Hopkins OCT MS and Healthy Controls](datasets/oct_ms_jhu.md) | 3 | 1 | 1 | 3 | 1 | 34 | 45 | 7 | 60 |
| [OCTA-500: Large-scale OCTA Multi-task Benchmark](datasets/octa_500.md) | 3 | 1 | 1 | 1 | 1 | 34 | 45 | Not eligible | 37.5 |
| [PAPILA](datasets/papila.md) | 3 | 1 | 1 | 4 | 1 | 34 | 45 | 6 | 71.25 |
| [JOIR / JSAIO fifth competition health-check subset](datasets/ext-joir-japanese-checkup.md) | 3 | 1 | 0 | 1 | 1 | 37 | 38.75 | Not eligible | 35 |
| [Retina Age Analysis (Hugging Face upload)](datasets/retina_age_analysis.md) | 2 | 1 | 0 | 0 | 0 | 38 | 26.25 | Not eligible | 16.25 |
| [Functional OCT Retinal Response Dataset (Bissig)](datasets/dryad_functional_oct_alzheimer.md) | 1 | 1 | 1 | 3 | 1 | 39 | 25 | Not eligible | 47.5 |
| [OculoScope: Fairer AI in Ophthalmology Dataset](datasets/oculoscope.md) | 2 | 0 | 0 | 1 | 1 | 40 | 22.5 | Not eligible | 25 |

<!-- /all-scores: retinal-aging -->

### Endpoint and denominator context

| Resource | Endpoint / tier | N for size score | Reported N | Denominator scope | Access route / judgment |
| --- | --- | --- | --- | --- | --- |
| [Atherosclerosis Risk in Communities (ARIC) retinal ancillary studies](datasets/ext-aric.md) | 年龄、人群结局<br>A T2 | 10358 | 10358 | Study-linked participants: 卒中研究成像样本 | Controlled access<br>四社区、阅读中心；独立像素交付未证。 |
| [Cardiovascular Health Study (CHS) retinal examination](datasets/ext-chs.md) | 年龄、后续风险<br>A T2 | 1717 | 1717 | Study-linked participants: 眼底和脑影像的历史人群子集 | Controlled access<br>多地社区、有不可分级照片；像素供给未证。 |
| [Scottish Collaborative Optometry-Ophthalmology Network e-research (SCONe)](datasets/ext-scone-scotland.md) | 年龄、多次采集及编码结局<br>A T1 | 36000 | 36000 | Study-linked participants: 早期描述超过36000名匹配患者，取保守下界 | Controlled access<br>社区验光多门店多设备；须项目团队合作在苏格兰安全环境内运行。 |
| [UK Biobank Eye and Vision / UK Biobank Repeat Imaging](datasets/ext-uk-biobank.md) | 年龄、死亡与重复评估<br>A T1 | 64367 | 64367 | Study-linked participants: 可分级 CFP 基线人数（不是 repeat × outcome 全部交集） | Controlled access<br>多评估中心，受控 RAP；新申请暂停。 |
| [Age, Gene/Environment Susceptibility–Reykjavik Study (AGES-RS)](datasets/ext-ages-reykjavik.md) | 年龄及随访<br>A T2 | 3906 | 3906 | Study-linked participants: 眼底、认知和 MRI 分析 | Author contact<br>同一雷克雅未克人群；合作范围待核。 |
| [Blue Mountains Eye Study (BMES)](datasets/ext-bmes.md) | 年龄、重复影像和死亡<br>A T2 | 3654 | 3654 | Study-linked participants: 基线眼底人群 | Application<br>单地区、标准化分级，原始影像交付待核。 |
| [Multi-Ethnic Study of Atherosclerosis (MESA Eye / cognitive–MRI ancillaries)](datasets/ext-mesa.md) | 年龄及事件<br>A T2 | 4849 | 4849 | Study-linked participants: 眼底卒中分析队列 | Controlled access<br>六社区，MRI 子集集中于北卡；像素须另审。 |
| [Northern Ireland Cohort for the Longitudinal Study of Ageing (NICOLA)](datasets/ext-nicola.md) | 年龄、健康随访<br>A T2 | 1431 | 1431 | Study-linked participants: 认知眼底分析样本 | Controlled access<br>地区老年人群、掩蔽分级；安全环境内像素供给待核。 |
| [Age-Related Eye Disease Study (AREDS)](datasets/ext-areds.md) | 重复眼底及年龄<br>A T1 | Unknown | 4613 | Cohort or batch only: F2 批次人数，非所有眼底字段交集 | Controlled access<br>多中心试验、有正式受控眼图路径；地域适格性另审。 |
| [Age-Related Eye Disease Study 2 (AREDS2)](datasets/ext-areds2.md) | 年龄、多时点眼图<br>A T1 | Unknown | 4201 | Cohort or batch only: 有眼部 DICOM 人数，非每类视野完整 | Controlled access<br>82 个中心，DICOM+ID 字典；dbGaP 资格限制。 |
| [NHANES 2005–2008 Ophthalmology – Retinal Imaging (OPXRET\_D / OPXRET\_E)](datasets/ext-nhanes-2005-2008-retina.md) | 公开分级、人口学与死亡<br>A T2 | 5371 | 5371 | Study-linked participants: 可分级子集；原始像素未核实 | Open download<br>概率抽样与分级质控；公开 XPT 无像素。 |
| [NHANES III (1988–1994) fundus grading and NDI linkage](datasets/ext-nhanes-iii-retina.md) | 分级及死亡，像素未知<br>A T2 | 7640 | 7640 | Study-linked participants: 死亡/分级研究分析样本 | Open download<br>历史概率样本；公开阅读分级。 |
| [Shanghai Diabetes Prevention Program (SDPP; DeepRETStroke subsets)](datasets/ext-shanghai-sdpp.md) | 年龄与未来卒中<br>A T1 | 29160 | 29160 | Study-linked participants: 非 MRI 卒中队列 | Author contact<br>非营利定向申请；MRI 子集与事件子集分别计。 |
| [Singapore two-site memory clinic retinal vessel cohort](datasets/ext-singapore-memory-clinics.md) | 年龄及纵向认知状态<br>A T2 | 491 | 491 | Study-linked participants: 认知分析样本 | Author contact<br>双门诊，个体资料共享受限。 |
| [Glaucoma Real-world Appraisal Progression Ensemble (GRAPE)](datasets/grape.md) | 年龄、多访视青光眼<br>A T1 | 144 | 144 | Study-linked participants: 整队列患者，非全部多次 CFP 人数 | Open download<br>单中心三种相机，开放真实访视与眼别。 |
| [EyePACS full research cohort used for eyeAge](datasets/ext-eyepacs-eyeage.md) | 重复访视年龄<br>A T1 | 100692 | 100692 | Study-linked participants: 训练人数；调参另有 25238 | Author contact<br>论文多个访视；与竞赛包有重叠，需联系 EyePACS。 |
| [Rotterdam Study / Rotterdam Scan Study (ERGO)](datasets/ext-rotterdam-study.md) | 年龄与随访风险<br>A T2 | 5540 | 5540 | Study-linked participants: 卒中眼底分析队列 | Application<br>单地区人群；管理团队受理；像素需确认。 |
| [Singapore Epidemiology of Eye Diseases (SEED), including SCES → EDIS retinal subcohort](datasets/ext-seed-edis.md) | 年龄与随访<br>A T1 | Unknown | Unknown | Unknown: 各族群/波次眼图分母未合并 | Application<br>多族群，影像项目申请；EDIS 另需许可。 |
| [Beijing Eye Study 2011 retinal / stroke and cognition substudies](datasets/ext-beijing-eye-study.md) | 年龄<br>A T2 | 3205 | 3205 | Study-linked participants: 有卒中问卷眼科分析分母 | Author contact<br>地域人群，研究申请到像素映射待核。 |
| [Rhineland Study / Rheinland Studie](datasets/ext-rhineland-study.md) | 年龄<br>A T1 | 2872 | 2872 | Study-linked participants: 质控后 OCT 与 MRI 样本 | Application<br>社区研究、MRI/OCT 质控；DUAC 受理影像申请。 |
| [Mobile Brazilian Retinal Dataset (mBRSET)](datasets/mbrset.md) | 实足年龄<br>A T1 | 1291 | 1291 | Study-linked participants: 原始患者规模 | Controlled access<br>单次地区活动手机设备，须认证。 |
| [Lothian Birth Cohort 1936 (LBC1936) retinal and brain imaging](datasets/ext-lothian-birth-cohort-1936.md) | 近单年龄外测<br>A T2 | 603 | 603 | Study-linked participants: 窄年龄出生队列，脑眼分析子集 | Application<br>苏格兰单地区出生队列，年龄窄，影像授权待核。 |
| [AlzEye](datasets/ext-alzeye.md) | 年龄及纵向健康记录<br>A T2 | Unknown | Unknown | Unknown: 不能使用整个 NHS 母库数作年龄共现数 | Unavailable<br>医院多个地点；限原团队分析个体系统疾病资料。 |
| [The Maastricht Study](datasets/ext-maastricht-study.md) | 年龄<br>A T2 | 3436 | 3436 | Study-linked participants: OCT与认知分母 | Application<br>地区人群及糖尿病富集；申请需指明影像格式。 |
| [China-Fundus-CIMT](datasets/china_fundus_cimt.md) | 年龄与同期 CIMT<br>A T1 | 2903 | 2903 | Study-linked participants: 人级双眼真实年龄 | Open download<br>单中心住院人群；公开双眼、ID与真年龄；CIMT 仅替代终点。 |
| [Brazilian Multilabel Ophthalmological Dataset (BRSET)](datasets/brset.md) | 实足年龄<br>A T1 | Unknown | 8524 | Cohort or batch only: 患者规模，去除缺年龄后数量未核 | Controlled access<br>三门诊两种相机，PhysioNet 认证与 DUA。 |
| [Framingham Eye Study (FES I/II), Original Framingham Heart Study cohort](datasets/ext-framingham-original-eye.md) | 年龄、历史胶片路径待核<br>A T2 | Unknown | 2631 | Cohort or batch only: 既往眼科检查人数非像素交集 | Controlled access<br>单社区历史胶片及分级，数字化待核。 |
| [FDR26 (Morocco)](datasets/ext-fdr26.md) | 整数年龄，外部北非人群<br>A T1 | Unknown | 1918 | Cohort or batch only: 论文患者数，ID 前缀分组待作者确认 | Open download<br>开放北非单中心资源，逐图年龄已核实；没有已认证患者键，独立验证暂待分组核准。 |
| [MCFI: A Multi-Session Colored Fundus Image Dataset](datasets/ext-mcfi.md) | 同眼短期重测；长期衰老速率样本不足<br>A T1 | 37 | 37 | Study-linked participants: 37 人都有同眼跨日影像，11 人跨度至少180天 | Open download<br>单中心多间隔，患者/会话/眼别文件映射已核。 |
| [Harvard-FairVLMed](datasets/fairvlmed.md) | 年龄、SLO 与临床文本<br>A T1 | 10000 | 10000 | Study-linked participants: 发布者每人一份 | Open download<br>临床 SLO 单样本；科研条件，系列间重叠未证。 |
| [Harvard-FairVision (30K)](datasets/harvard_fairvision.md) | 配对 SLO+OCT 年龄<br>A T1 | 30000 | 30000 | Study-linked participants: 发布者总人数，年龄完备性需核 | Open download<br>临床 SLO+OCT，公开文件；限非商业研究。 |
| [Ocular Disease Intelligent Recognition (ODIR-5K / ODIR-2019)](datasets/odir2019.md) | 年龄、双眼<br>A T1 | Unknown | 5000 | Cohort or batch only: 组织者患者数；按实际可用分区复核 | Open download<br>多医院/设备；官方科研复用范围未确立，暂缓实际使用。 |
| [Ontario Neurodegenerative Disease Research Initiative (ONDRI), Foundational Study release 2.0](datasets/ext-ondri.md) | 年龄与派生 OCT<br>A T2 | Unknown | Unknown | Unknown: 只确定眼表型、影像获取范围未明 | Controlled access<br>跨安大略中心；影像表型存在，原始眼图未知。 |
| [Johns Hopkins OCT MS and Healthy Controls](datasets/oct_ms_jhu.md) | 可唯一匹配的 OCT 年龄<br>A T1 | 26 | 26 | Study-linked participants: 仅 26 个唯一 ID 能匹配个体年龄 | Open download<br>原 ZIP 标识核验；仅 26 个唯一年龄匹配。 |
| [OCTA-500: Large-scale OCTA Multi-task Benchmark](datasets/octa_500.md) | 年龄及 OCTA 眼别<br>A T1 | 500 | 500 | Study-linked participants: 来源受试者数 | Author contact<br>具 OCT/OCTA；账号及作者密码流程。 |
| [PAPILA](datasets/papila.md) | 逐眼实足年龄<br>A T1 | 244 | 244 | Study-linked participants: 逐眼表与影像匹配 | Open download<br>单医院，公开原始影像和逐眼临床表。 |
| [JOIR / JSAIO fifth competition health-check subset](datasets/ext-joir-japanese-checkup.md) | 年龄、代谢综合征<br>A T1 | Unknown | Unknown | Unknown: 5000 是照片数 | Author contact<br>日本男性体检子集；须项目方批准。 |
| [Retina Age Analysis (Hugging Face upload)](datasets/retina_age_analysis.md) | 年龄，来源隔离<br>A T2 | Unknown | 5393 | Cohort or batch only: 卡片声称人数；归属、重用权待核 | Open download<br>来源/授权链及 BRSET 潜在重叠未证。 |
| [Functional OCT Retinal Response Dataset (Bissig)](datasets/dryad_functional_oct_alzheimer.md) | 年龄段，非连续回归<br>A T1 | 28 | 28 | Study-linked participants: AD 比较子集；年龄为区间 | Registration<br>数据包与病例映射明确；按平台流程获取，机制样本很小。 |
| [OculoScope: Fairer AI in Ophthalmology Dataset](datasets/oculoscope.md) | 年龄分组公平性<br>A T2 | Unknown | Unknown | Unknown: 年龄字段与患者键未知 | Controlled access<br>UWF 源档受控；年龄连续值与个体键未知。 |

Image and individual-label availability are recorded separately on each linked resource page. An access category alone does not confirm those files or a right to link records.

</details>

<details>

<summary>Eye–Stroke — all 22 ranking rows</summary>

### Scores and ranks

<!-- all-scores: eye-stroke -->

| Resource | R | L | Q | X | M | Science rank | Science / 100 | Near-term rank | Near-term / 100 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Atherosclerosis Risk in Communities (ARIC) retinal ancillary studies](datasets/ext-aric.md) | 4 | 4 | 4 | 1 | 3 | 1 | 97.5 | Not eligible | 65 |
| [Cardiovascular Health Study (CHS) retinal examination](datasets/ext-chs.md) | 4 | 4 | 4 | 1 | 3 | 1 | 97.5 | Not eligible | 65 |
| [Multi-Ethnic Study of Atherosclerosis (MESA Eye / cognitive–MRI ancillaries)](datasets/ext-mesa.md) | 4 | 4 | 4 | 1 | 3 | 1 | 97.5 | Not eligible | 65 |
| [UK Biobank Eye and Vision / UK Biobank Repeat Imaging](datasets/ext-uk-biobank.md) | 4 | 4 | 4 | 0 | 3 | 1 | 97.5 | Not eligible | 53.75 |
| [Age, Gene/Environment Susceptibility–Reykjavik Study (AGES-RS)](datasets/ext-ages-reykjavik.md) | 4 | 4 | 4 | 1 | 1 | 5 | 92.5 | Not eligible | 62.5 |
| [Lothian Birth Cohort 1936 (LBC1936) retinal and brain imaging](datasets/ext-lothian-birth-cohort-1936.md) | 4 | 4 | 4 | 1 | 1 | 5 | 92.5 | Not eligible | 62.5 |
| [Singapore Epidemiology of Eye Diseases (SEED), including SCES → EDIS retinal subcohort](datasets/ext-seed-edis.md) | 4 | 4 | 3 | 2 | 2 | 7 | 88.75 | Not eligible | 72.5 |
| [Scottish Collaborative Optometry-Ophthalmology Network e-research (SCONe)](datasets/ext-scone-scotland.md) | 3 | 4 | 4 | 2 | 3 | 8 | 87.5 | Not eligible | 70 |
| [Blue Mountains Eye Study (BMES)](datasets/ext-bmes.md) | 4 | 3 | 4 | 1 | 1 | 9 | 86.25 | Not eligible | 58.75 |
| [Rotterdam Study / Rotterdam Scan Study (ERGO)](datasets/ext-rotterdam-study.md) | 4 | 3 | 4 | 1 | 1 | 9 | 86.25 | Not eligible | 58.75 |
| [Shanghai Diabetes Prevention Program (SDPP; DeepRETStroke subsets)](datasets/ext-shanghai-sdpp.md) | 4 | 3 | 4 | 1 | 1 | 9 | 86.25 | Not eligible | 58.75 |
| [Age-Related Eye Disease Study 2 (AREDS2)](datasets/ext-areds2.md) | 4 | 4 | 2 | 2 | 3 | 12 | 85 | Not eligible | 71.25 |
| [Northern Ireland Cohort for the Longitudinal Study of Ageing (NICOLA)](datasets/ext-nicola.md) | 4 | 3 | 3 | 1 | 1 | 13 | 80 | Not eligible | 56.25 |
| [Rhineland Study / Rheinland Studie](datasets/ext-rhineland-study.md) | 3 | 3 | 4 | 2 | 1 | 14 | 76.25 | Not eligible | 63.75 |
| [NHANES 2005–2008 Ophthalmology – Retinal Imaging (OPXRET\_D / OPXRET\_E)](datasets/ext-nhanes-2005-2008-retina.md) | 2 | 4 | 4 | 0 | 2 | 15 | 75 | Not eligible | 40 |
| [Age-Related Eye Disease Study (AREDS)](datasets/ext-areds.md) | 3 | 3 | 2 | 2 | 3 | 16 | 68.75 | Not eligible | 61.25 |
| [Beijing Eye Study 2011 retinal / stroke and cognition substudies](datasets/ext-beijing-eye-study.md) | 2 | 3 | 3 | 1 | 1 | 17 | 60 | Not eligible | 43.75 |
| [AlzEye](datasets/ext-alzeye.md) | 3 | 2 | 1 | 0 | 2 | 18 | 53.75 | Not eligible | 31.25 |
| [Framingham Eye Study (FES I/II), Original Framingham Heart Study cohort](datasets/ext-framingham-original-eye.md) | 2 | 2 | 3 | 1 | 1 | 18 | 53.75 | Not eligible | 40 |
| [Ontario Neurodegenerative Disease Research Initiative (ONDRI), Foundational Study release 2.0](datasets/ext-ondri.md) | 2 | 2 | 2 | 1 | 3 | 20 | 52.5 | Not eligible | 40 |
| [The Maastricht Study](datasets/ext-maastricht-study.md) | 3 | 2 | 1 | 1 | 1 | 21 | 51.25 | Not eligible | 41.25 |
| [China-Fundus-CIMT](datasets/china_fundus_cimt.md) | 2 | 1 | 3 | 4 | 1 | 22 | 47.5 | Not eligible | 70 |

<!-- /all-scores: eye-stroke -->

### Endpoint and denominator context

| Resource | Endpoint / tier | N for size score | Reported N | Denominator scope | Access route / judgment |
| --- | --- | --- | --- | --- | --- |
| [Atherosclerosis Risk in Communities (ARIC) retinal ancillary studies](datasets/ext-aric.md) | 新发卒中、WMH 与腔隙<br>B T2 / C T2 | 10358 | 10358 | Study-linked participants: 事件论文队列；另有 1684 影像 × MRI | Controlled access<br>四社区、阅读中心；独立像素交付未证。 |
| [Cardiovascular Health Study (CHS) retinal examination](datasets/ext-chs.md) | 脑 MRI 微血管表型及卒中<br>B T2 / C T2 | 1717 | 1717 | Study-linked participants: 眼底和脑 MRI | Controlled access<br>多地社区、有不可分级照片；像素供给未证。 |
| [Multi-Ethnic Study of Atherosclerosis (MESA Eye / cognitive–MRI ancillaries)](datasets/ext-mesa.md) | 新发卒中、MRI 子集<br>B T2 / C T2 | 4849 | 4849 | Study-linked participants: 卒中队列；MRI 子集另计 | Controlled access<br>六社区，MRI 子集集中于北卡；像素须另审。 |
| [UK Biobank Eye and Vision / UK Biobank Repeat Imaging](datasets/ext-uk-biobank.md) | 新发卒中；另有脑 MRI 指标<br>B T1 / C T1 | 35304 | 35304 | Study-linked participants: 既往无卒中、论文可评估者；MRI 交集另计 | Controlled access<br>多评估中心，受控 RAP；新申请暂停。 |
| [Age, Gene/Environment Susceptibility–Reykjavik Study (AGES-RS)](datasets/ext-ages-reykjavik.md) | 脑微出血进展<br>B T2 / C T2 | 2502 | 2502 | Study-linked participants: 基线眼底与两期 MRI | Author contact<br>同一雷克雅未克人群；合作范围待核。 |
| [Lothian Birth Cohort 1936 (LBC1936) retinal and brain imaging](datasets/ext-lothian-birth-cohort-1936.md) | MRI 定量 CSVD；另有既往史<br>B T2 / C T2 | 603 | 603 | Study-linked participants: 双眼映射与 MRI 分析子集 | Application<br>苏格兰单地区出生队列，年龄窄，影像授权待核。 |
| [Singapore Epidemiology of Eye Diseases (SEED), including SCES → EDIS retinal subcohort](datasets/ext-seed-edis.md) | 卒中，EDIS 微出血<br>B T1 / C T2 | 300 | 300 | Study-linked participants: EDIS 同人脑眼子集；新发卒中系列另计 | Application<br>多族群，影像项目申请；EDIS 另需许可。 |
| [Scottish Collaborative Optometry-Ophthalmology Network e-research (SCONe)](datasets/ext-scone-scotland.md) | 首次医学编码日期，非裁定发病日<br>B T1 | 2495 | 2495 | Outcome-positive subset (lower bound): 描述论文 stroke 代码阳性人数，非全部随访交集 | Controlled access<br>社区验光多门店多设备；须项目团队合作在苏格兰安全环境内运行。 |
| [Blue Mountains Eye Study (BMES)](datasets/ext-bmes.md) | 卒中、TIA、脑血管死亡分别报告<br>B T2 | 3654 | 3654 | Study-linked participants: 原始基线，随访完整人群另计 | Application<br>单地区、标准化分级，原始影像交付待核。 |
| [Rotterdam Study / Rotterdam Scan Study (ERGO)](datasets/ext-rotterdam-study.md) | 首次卒中与 CSVD 子集<br>B T2 / C T2 | 5540 | 5540 | Study-linked participants: 卒中队列；CSVD 配对 490 另计 | Application<br>单地区人群；管理团队受理；像素需确认。 |
| [Shanghai Diabetes Prevention Program (SDPP; DeepRETStroke subsets)](datasets/ext-shanghai-sdpp.md) | 新发卒中与 MRI 静默梗死<br>B T1 / C T1 | 29160 | 29160 | Study-linked participants: 卒中子集；静默梗死 MRI 子集782，分开 | Author contact<br>非营利定向申请；MRI 子集与事件子集分别计。 |
| [Age-Related Eye Disease Study 2 (AREDS2)](datasets/ext-areds2.md) | 卒中裁定亚型与时间；病例 MRI 裁定摘要<br>B T1 / C T1 | Unknown | Unknown | Unknown: 137 个裁定对象与影像交集未知 | Controlled access<br>82 个中心，DICOM+ID 字典；dbGaP 资格限制。 |
| [Northern Ireland Cohort for the Longitudinal Study of Ageing (NICOLA)](datasets/ext-nicola.md) | 随访卒中<br>B T2 | Unknown | Unknown | Unknown: 卒中分析分母独立 | Controlled access<br>地区老年人群、掩蔽分级；安全环境内像素供给待核。 |
| [Rhineland Study / Rheinland Studie](datasets/ext-rhineland-study.md) | 结构与扩散 MRI；特定 CSVD 病灶未确立<br>C T1 | 2872 | 2872 | Study-linked participants: 协议和质控后 MRI 交集 | Application<br>社区研究、MRI/OCT 质控；DUAC 受理影像申请。 |
| [NHANES 2005–2008 Ophthalmology – Retinal Imaging (OPXRET\_D / OPXRET\_E)](datasets/ext-nhanes-2005-2008-retina.md) | 既往自报卒中，非新发事件<br>B T2 | 4570 | 4570 | Study-linked participants: 卒中问卷＋分级 | Open download<br>概率抽样与分级质控；公开 XPT 无像素。 |
| [Age-Related Eye Disease Study (AREDS)](datasets/ext-areds.md) | 新发卒中记录，亚型待核<br>B T1 | Unknown | Unknown | Unknown: 临床事件 × 眼图分母未知 | Controlled access<br>多中心试验、有正式受控眼图路径；地域适格性另审。 |
| [Beijing Eye Study 2011 retinal / stroke and cognition substudies](datasets/ext-beijing-eye-study.md) | 既往自报卒中<br>B T2 | 3205 | 3205 | Study-linked participants: 卒中问卷样本 | Author contact<br>地域人群，研究申请到像素映射待核。 |
| [AlzEye](datasets/ext-alzeye.md) | HES 脑血管事件，限原团队<br>B T2 | Unknown | Unknown | Unknown: 本次未取得事件个案交集 | Unavailable<br>医院多个地点；限原团队分析个体系统疾病资料。 |
| [Framingham Eye Study (FES I/II), Original Framingham Heart Study cohort](datasets/ext-framingham-original-eye.md) | 历史眼科研究与父队列临床记录<br>B T2 / C T2 | Unknown | Unknown | Unknown: 眼底 × 事件或脑 MRI 交集未证 | Controlled access<br>单社区历史胶片及分级，数字化待核。 |
| [Ontario Neurodegenerative Disease Research Initiative (ONDRI), Foundational Study release 2.0](datasets/ext-ondri.md) | 卒中史及 MRI 范围待核<br>B T2 / C T2 | Unknown | Unknown | Unknown: 原眼图与 MRI 共现分母未知 | Controlled access<br>跨安大略中心；影像表型存在，原始眼图未知。 |
| [The Maastricht Study](datasets/ext-maastricht-study.md) | 白质脑影像关联<br>C T2 | Unknown | Unknown | Unknown: MRI 子集与可分级双眼分母待重算 | Application<br>地区人群及糖尿病富集；申请需指明影像格式。 |
| [China-Fundus-CIMT](datasets/china_fundus_cimt.md) | 仅颈动脉壁厚替代指标，无脑卒中事件<br>B T1 | 2903 | 2903 | Study-linked participants: 眼底 × 超声 CIMT | Open download<br>单中心住院人群；公开双眼、ID与真年龄；CIMT 仅替代终点。 |

Image and individual-label availability are recorded separately on each linked resource page. An access category alone does not confirm those files or a right to link records.

</details>

<details>

<summary>Eye–Neurodegeneration — all 21 ranking rows</summary>

### Scores and ranks

<!-- all-scores: eye-neurodegeneration -->

| Resource | R | L | Q | X | M | Science rank | Science / 100 | Near-term rank | Near-term / 100 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [UK Biobank Eye and Vision / UK Biobank Repeat Imaging](datasets/ext-uk-biobank.md) | 4 | 4 | 4 | 0 | 3 | 1 | 97.5 | Not eligible | 53.75 |
| [Atherosclerosis Risk in Communities (ARIC) retinal ancillary studies](datasets/ext-aric.md) | 4 | 3 | 3 | 1 | 3 | 2 | 85 | Not eligible | 58.75 |
| [Cardiovascular Health Study (CHS) retinal examination](datasets/ext-chs.md) | 3 | 3 | 4 | 1 | 3 | 3 | 81.25 | Not eligible | 55 |
| [Scottish Collaborative Optometry-Ophthalmology Network e-research (SCONe)](datasets/ext-scone-scotland.md) | 3 | 3 | 4 | 2 | 3 | 3 | 81.25 | Not eligible | 66.25 |
| [Singapore two-site memory clinic retinal vessel cohort](datasets/ext-singapore-memory-clinics.md) | 4 | 3 | 2 | 1 | 2 | 5 | 76.25 | Not eligible | 55 |
| [Age, Gene/Environment Susceptibility–Reykjavik Study (AGES-RS)](datasets/ext-ages-reykjavik.md) | 3 | 3 | 4 | 1 | 1 | 5 | 76.25 | Not eligible | 52.5 |
| [Lothian Birth Cohort 1936 (LBC1936) retinal and brain imaging](datasets/ext-lothian-birth-cohort-1936.md) | 3 | 3 | 4 | 1 | 1 | 5 | 76.25 | Not eligible | 52.5 |
| [Multi-Ethnic Study of Atherosclerosis (MESA Eye / cognitive–MRI ancillaries)](datasets/ext-mesa.md) | 3 | 3 | 3 | 1 | 3 | 8 | 75 | Not eligible | 52.5 |
| [Ontario Neurodegenerative Disease Research Initiative (ONDRI), Foundational Study release 2.0](datasets/ext-ondri.md) | 3 | 4 | 2 | 1 | 3 | 8 | 75 | Not eligible | 53.75 |
| [Rotterdam Study / Rotterdam Scan Study (ERGO)](datasets/ext-rotterdam-study.md) | 4 | 3 | 2 | 1 | 1 | 10 | 73.75 | Not eligible | 53.75 |
| [Singapore Epidemiology of Eye Diseases (SEED), including SCES → EDIS retinal subcohort](datasets/ext-seed-edis.md) | 3 | 3 | 3 | 2 | 2 | 11 | 72.5 | Not eligible | 62.5 |
| [AlzEye](datasets/ext-alzeye.md) | 4 | 3 | 1 | 0 | 2 | 12 | 70 | Not eligible | 41.25 |
| [Northern Ireland Cohort for the Longitudinal Study of Ageing (NICOLA)](datasets/ext-nicola.md) | 3 | 2 | 4 | 1 | 1 | 12 | 70 | Not eligible | 48.75 |
| [Age-Related Eye Disease Study 2 (AREDS2)](datasets/ext-areds2.md) | 3 | 3 | 2 | 2 | 3 | 14 | 68.75 | Not eligible | 61.25 |
| [Beijing Eye Study 2011 retinal / stroke and cognition substudies](datasets/ext-beijing-eye-study.md) | 3 | 2 | 3 | 1 | 1 | 15 | 63.75 | Not eligible | 46.25 |
| [The Maastricht Study](datasets/ext-maastricht-study.md) | 3 | 2 | 3 | 1 | 1 | 15 | 63.75 | Not eligible | 46.25 |
| [Framingham Eye Study (FES I/II), Original Framingham Heart Study cohort](datasets/ext-framingham-original-eye.md) | 2 | 2 | 3 | 1 | 1 | 17 | 53.75 | Not eligible | 40 |
| [Age-Related Eye Disease Study (AREDS)](datasets/ext-areds.md) | 2 | 2 | 2 | 2 | 3 | 18 | 52.5 | Not eligible | 51.25 |
| [Functional OCT Retinal Response Dataset (Bissig)](datasets/dryad_functional_oct_alzheimer.md) | 3 | 1 | 1 | 3 | 1 | 19 | 45 | 2 | 60 |
| [TREND2 chronic-disease fundus study](datasets/trend2_fundus.md) | 3 | 1 | 1 | 4 | 1 | 19 | 45 | 1 | 71.25 |
| [ROSE: Retinal OCT-Angiography Vessel Segmentation (ROSE-1 and ROSE-2)](datasets/rose.md) | 2 | 0 | 1 | 1 | 2 | 21 | 31.25 | Not eligible | 28.75 |

<!-- /all-scores: eye-neurodegeneration -->

### Endpoint and denominator context

| Resource | Endpoint / tier | N for size score | Reported N | Denominator scope | Access route / judgment |
| --- | --- | --- | --- | --- | --- |
| [UK Biobank Eye and Vision / UK Biobank Repeat Imaging](datasets/ext-uk-biobank.md) | 新发 AD、痴呆及 PD<br>D T1 / E T1 | 30573 | 30573 | Study-linked participants: OCT 与痴呆队列，PD 分析另外计 | Controlled access<br>多评估中心，受控 RAP；新申请暂停。 |
| [Atherosclerosis Risk in Communities (ARIC) retinal ancillary studies](datasets/ext-aric.md) | 随访认知及痴呆<br>D T2 | Unknown | Unknown | Unknown: 神经分析独立分母未用于打分 | Controlled access<br>四社区、阅读中心；独立像素交付未证。 |
| [Cardiovascular Health Study (CHS) retinal examination](datasets/ext-chs.md) | 横断面认知及痴呆<br>D T2 | 2211 | 2211 | Study-linked participants: 发表横断面认知分析；未证实该终点的前瞻随访 | Controlled access<br>多地社区、有不可分级照片；像素供给未证。 |
| [Scottish Collaborative Optometry-Ophthalmology Network e-research (SCONe)](datasets/ext-scone-scotland.md) | 痴呆、AD、PD 代码<br>D T1 / E T1 | 1630 | 1630 | Outcome-positive subset (lower bound): 痴呆代码人数；AD、PD 另计，不相加 | Controlled access<br>社区验光多门店多设备；须项目团队合作在苏格兰安全环境内运行。 |
| [Singapore two-site memory clinic retinal vessel cohort](datasets/ext-singapore-memory-clinics.md) | 新发痴呆及认知下降<br>D T2 | 212 | 212 | Study-linked participants: 新发痴呆风险集；491 用于认知下降 | Author contact<br>双门诊，个体资料共享受限。 |
| [Age, Gene/Environment Susceptibility–Reykjavik Study (AGES-RS)](datasets/ext-ages-reykjavik.md) | 横断面认知、痴呆及 AD<br>D T2 | 3906 | 3906 | Study-linked participants: 横断面眼底和认知分析；痴呆子集另计 | Author contact<br>同一雷克雅未克人群；合作范围待核。 |
| [Lothian Birth Cohort 1936 (LBC1936) retinal and brain imaging](datasets/ext-lothian-birth-cohort-1936.md) | 纵向认知功能<br>D T2 | 683 | 683 | Study-linked participants: 另一个纵向认知分析队列 | Application<br>苏格兰单地区出生队列，年龄窄，影像授权待核。 |
| [Multi-Ethnic Study of Atherosclerosis (MESA Eye / cognitive–MRI ancillaries)](datasets/ext-mesa.md) | 认知评分<br>D T2 | Unknown | Unknown | Unknown: 认知数依分析子集 | Controlled access<br>六社区，MRI 子集集中于北卡；像素须另审。 |
| [Ontario Neurodegenerative Disease Research Initiative (ONDRI), Foundational Study release 2.0](datasets/ext-ondri.md) | 研究内 AD、PD及认知分型<br>D T2 / E T2 | Unknown | Unknown | Unknown: 可用眼图与个体病种交集未知 | Controlled access<br>跨安大略中心；影像表型存在，原始眼图未知。 |
| [Rotterdam Study / Rotterdam Scan Study (ERGO)](datasets/ext-rotterdam-study.md) | 随访 AD 或血管性痴呆<br>D T2 | Unknown | Unknown | Unknown: 另一个痴呆分析样本；不沿用卒中人数 | Application<br>单地区人群；管理团队受理；像素需确认。 |
| [Singapore Epidemiology of Eye Diseases (SEED), including SCES → EDIS retinal subcohort](datasets/ext-seed-edis.md) | 认知<br>D T2 | 300 | 300 | Study-linked participants: EDIS 同人神经心理测量 | Application<br>多族群，影像项目申请；EDIS 另需许可。 |
| [AlzEye](datasets/ext-alzeye.md) | 诊断编码 AD、痴呆、PD<br>D T2 / E T2 | Unknown | Unknown | Unknown: 各病种有效交集需核 | Unavailable<br>医院多个地点；限原团队分析个体系统疾病资料。 |
| [Northern Ireland Cohort for the Longitudinal Study of Ageing (NICOLA)](datasets/ext-nicola.md) | 操作性定义 MCI，不等同 AD<br>D T2 | 1431 | 1431 | Study-linked participants: 认知眼底分析样本 | Controlled access<br>地区老年人群、掩蔽分级；安全环境内像素供给待核。 |
| [Age-Related Eye Disease Study 2 (AREDS2)](datasets/ext-areds2.md) | TICS 等，非 AD 诊断<br>D T1 | Unknown | Unknown | Unknown: 认知文件与眼图交集未知 | Controlled access<br>82 个中心，DICOM+ID 字典；dbGaP 资格限制。 |
| [Beijing Eye Study 2011 retinal / stroke and cognition substudies](datasets/ext-beijing-eye-study.md) | 同期 MMSE<br>D T2 | 3127 | 3127 | Study-linked participants: 认知论文分析分母 | Author contact<br>地域人群，研究申请到像素映射待核。 |
| [The Maastricht Study](datasets/ext-maastricht-study.md) | 域认知评分<br>D T2 | 3436 | 3436 | Study-linked participants: OCT与认知分母 | Application<br>地区人群及糖尿病富集；申请需指明影像格式。 |
| [Framingham Eye Study (FES I/II), Original Framingham Heart Study cohort](datasets/ext-framingham-original-eye.md) | 父队列认知数据，配对待核<br>D T2 | Unknown | Unknown | Unknown: 眼底与痴呆交集未证 | Controlled access<br>单社区历史胶片及分级，数字化待核。 |
| [Age-Related Eye Disease Study (AREDS)](datasets/ext-areds.md) | 认知子研究<br>D T2 | Unknown | Unknown | Unknown: 认知子研究原始资料待核 | Controlled access<br>多中心试验、有正式受控眼图路径；地域适格性另审。 |
| [Functional OCT Retinal Response Dataset (Bissig)](datasets/dryad_functional_oct_alzheimer.md) | 功能 OCT、早发 AD 病例对照<br>D T1 | 28 | 28 | Study-linked participants: 14 EOAD ＋ 14 年龄匹配对照 | Registration<br>数据包与病例映射明确；按平台流程获取，机制样本很小。 |
| [TREND2 chronic-disease fundus study](datasets/trend2_fundus.md) | AD 二元标记，7 阳性 ID-eye<br>D T1 | Unknown | Unknown | Unknown: 28 个 ID-eye，独立患者人数未知 | Open download<br>公开病例列与 TIFF 名对应；仅 28 个 ID-eye，患者总数未证。 |
| [ROSE: Retinal OCT-Angiography Vessel Segmentation (ROSE-1 and ROSE-2)](datasets/rose.md) | 论文记录有 AD，发布标签待证<br>D T2 | Unknown | 39 | Cohort or batch only: ROSE-1 受试者；外部逐图诊断未知 | Controlled access<br>两个设备/子集，病例映射与准入未证。 |

Image and individual-label availability are recorded separately on each linked resource page. An access category alone does not confirm those files or a right to link records.

</details>

<a id="reproduce"></a>

## Reproduce

The renderer uses **Python 3.9+ standard library only**. No plotting dependencies or network access are needed. From the repository root:

```bash
python scripts/build_rankings.py
```

To use another release while retaining the repository's stable resource pages:

```bash
python scripts/build_rankings.py --input-dir /path/to/library/output
```

The command reads `master.csv` and `rankings.csv`, checks unique pairs, resource names/pages, exclusion status, component formulas, rank ties/order, exported near-term gate conditions and sample-size scope, then overwrites only this page. It preserves the manually curated endpoint-readiness decision; it does not infer new readiness from the numeric score. Run the library's full verifier when changing the curation or ranking inputs.

Plotting is separate and optional: [`requirements-stats.txt`](requirements-stats.txt) pins the matplotlib version used to build the [statistics figures](STATS.md). It is not required for this ranking page.

| Input CSV | SHA-256 |
| --- | --- |
| [master.csv](library/output/master.csv) | `a5bfbd02d32f16839ed42e0a2f8f384598750e19f7f70ebae4ec494f40fe9f4d` |
| [rankings.csv](library/output/rankings.csv) | `6e5586da94a604b21fabc2e139c37401508d3021fc629a5e7029a925d7f6d480` |
