# 全球眼底影像、衰老与神经及全身疾病数据资源库

**2026-11-03 版。** 双击 [index.html](index.html) 打开离线目录，可按中文/英文关键词、专题、等级和访问方式检索、查看字段与证据。点击“排名”比较年龄、卒中与神经退行性疾病三个方向。文件本身不需要登录或本地服务器，访问原始来源链接时才需要联网。

- [科研选题与实验设计](RESEARCH_GUIDE.md) 从年龄重测、卒中/MRI 和认知转归三个实际问题出发。
- [调查口径与评分规则](METHODS.md) 解释分母、证据等级、像素获取和两种排名。
- [主表](output/master.csv)、[排名](output/rankings.csv) 和 [SQLite 数据库](output/resources.sqlite) 用于自己的查询。CSV 是带 BOM 的 UTF-8，保留多行说明。
- [冻结版本清单](inputs/v0.7.0/manifest.json) 和随库保留的原始 CSV、JSON、关系及访问核验元数据用于离线重建。完整上游仓库归档不随本库再分发，其提交与 SHA-256 仍保留在清单中。

## 文件与字段

| 文件 | 一行代表什么 | 应怎样使用 |
|---|---|---|
| output/master.csv | 一个资源，原始 ID 或稳定的扩展 ID | 人群/机构/出版信息、影像模态、图像和参与者分母、眼别/设备/QC、时点/模态/中心、配对依据、原始影像与标签获取、许可、专题、项目建议均在同一行。原索引保存在 inputs/v0.7.0/hub/catalog.json。 |
| output/topics.csv | 一个资源与 A–G 某专题的判断 | `tier` 是本调查用于像素课题的等级，`reviewed_tier_before_pixel_gate` 为应用统一像素规则前的等级。整体等级取最强的非排除专题。 |
| output/phenotypes.csv | 一个资源的一个临床字段 | `status` 与 `scope` 同读。从 `evidence_id` 回到证据表；未知字段不强行绑定“否定证据”。 |
| output/evidence.csv | 自然语言证据定位与 URL | 形如 `ext-areds2#s5`。每个 ID 含一个锚点，多个锚点之间用“竖线”分隔。以 `#base` 结尾的是冻结目录记录，其日期为上游检查日期。 |
| output/identity.csv、relationships.csv | 上游身份登记和有向关系边 | 查组件、派生、任务视图及重叠；一条有向边不代表可确定共同患者人数。 |
| output/extensions_relationships.csv | 本调查补充的项目间关系 | `status` 区分 confirmed 与 possible；包括 AREDS/AREDS2 的已证实重叠与 retina-age 上传的待核来源。 |
| output/quantities.csv、access_audit.csv | 原始数量加单位；上游访问核验 | 分开图像、参与者、眼、B-scan、体积、文件等单位。上游检查是历史检查，不证明今天可下载。 |
| output/rankings.csv | 一个资源对一个科研问题 | 五个分项、两个分数、科学排名、近期名次、人数口径和原始依据。没有满足条件者的近期榜保持为空。 |
| output/search_log.csv、pubmed_hits.csv、excluded.csv | 一次检索/查验、一篇 PMID、一条整库排除 | 可复查检索词和被拒资源；某资源在单个专题被排除但在其他专题可用时，应查 topics。 |
| inputs/curation/、inputs/search/ | 版本化的人工核验记录与检索输入 | 这里是维护时修改的地方。生成的 HTML/CSV/SQLite 不直接编辑。 |

`doi` 对应已核实的关联论文，`dataset_doi` 是数据发布 DOI。受控研究还可依官方链接、`relation` 和证据中的 study/table accession 定位。`year` 标明年度的语义；日期补充列保留来源 URL 和日期类型。`upstream_family`、`upstream_role`、`raw_access_friction`、`route_last_checked` 和 `acquisition_support` 保留基线层的历史信息。`official_url`、`access`、`image_access`、`label_access` 和 `research_terms` 是本项目决策时应优先看的列。`Open download` 可能只适用于发布表格；例如 NHANES 的原始眼图状态要看 `image_access`。

表型字典涵盖 `age`、`sex`、`hypertension`、`diabetes`、`cardiovascular`、`stroke_type`、`stroke_time`、`brain_mri`、`csvd`、`ad`、`dementia`、`cognition`、`parkinson`、`frailty`、`health`、`mortality`、`followup`。扩展字段如 CIMT 单独存放。看到 stroke_time=Confirmed 时要读 scope，可能是自报首次卒中年龄、首个临床编码日期、随机化后天数或真正的事件日。审阅现有表型时，取像素和个体标签的权限判断须同时满足。

## 离线复现

在本目录运行。Python 3.9 及以上版本即可，无需安装包。

```sh
python3 src/build.py
python3 src/verify.py
```

`build.py` 校验所选基线元数据的逐文件 SHA-256 和补充日期文件，然后依据可编辑的结构化输入生成全部表格、SQLite 与单文件浏览器。`verify.py` 独立核对 CSV/JSON 的全量 ID 和字段、家族/证据引用、主表与数据库、排名、浏览器与本地链接。如自行保留原始完整归档，程序还会检查其哈希；`python3 src/verify.py --require-archive` 可要求必须存在并核验该归档。默认离线复现不需要整仓库归档，也不会自动下载它。实时查询结果可能随提供方改变；离线重建以固定输入为准。

```sql
-- 哪些资源对“脑 MRI / CSVD”有直接像素科研证据？
SELECT m.id, m.name, m.image_access, t.reason, t.evidence_id
FROM master AS m JOIN topics AS t USING (id)
WHERE t.topic = 'C' AND t.tier = 'Tier 1';

-- 哪些可证实的 AD 字段有患者级来源？回看 scope 避免把 AD 编码当作病理金标准。
SELECT id, status, scope, evidence_id FROM phenotypes
WHERE field = 'ad' AND status = 'Confirmed';

-- 查近期可用队列及其与真正匹配的人数
SELECT track, practical_rank, name, endpoint, n_supported, n_scope
FROM rankings WHERE near_term = 'Yes' ORDER BY track, practical_rank;
```

例如用 `sqlite3 output/resources.sqlite` 后粘贴 SQL。没有 SQLite 命令的环境，也可用 Python 标准库 `sqlite3.connect("output/resources.sqlite")`。

## 更新方法

1. 到官方标签与包发布页确认是否出现新的稳定版本。先读新版本随附的 CLAUDE.md。核对标签与提交，下载元数据快照即可；不要下载医疗影像作为“检索”步骤。[Git 标签](https://github.com/pooyakhosravi/EyeDataHub/tags) · [PyPI](https://pypi.org/project/eyedatahub/)
2. 默认离线重建直接使用所选冻结元数据，不需要整仓库归档。若要独立从上游重新提取基线，以下命令会显式下载官方代码与审计资料；完整归档应保存在仓库之外，不重新上传。本库清单中的 `archive_sha256` 是当时原始归档的校验值，不是对任意工具版本重新压缩结果的哈希承诺；逐文件哈希才是元数据一致性的检查依据。未来稳定版本使用新的标签、准确的提交和另一个文件名；快照工具输出 `diff_from_v0.7.0.json`，列出新增、移除和字段变化。新版本不会自动替代本研究的冻结基线。

```sh
git clone --branch v0.7.0 --depth 1 https://github.com/pooyakhosravi/EyeDataHub /tmp/EyeDataHub-repro
git -C /tmp/EyeDataHub-repro rev-parse 'v0.7.0^{commit}'
git -C /tmp/EyeDataHub-repro archive --format=tar.gz --prefix=EyeDataHub-0.7.0/ -o /tmp/EyeDataHub-v0.7.0.tar.gz v0.7.0
python3 src/snapshot.py /tmp/EyeDataHub-v0.7.0.tar.gz v0.7.0 0ce7144459a41e8be255fed7fa62c30416613e6b --verify-existing
```

3. 以新的调查日期单独保存检索结果。运行 `python3 src/refresh_pubmed.py --as-of YYYY-MM-DD --plan` 可离线检查四组精确检索式；将 `--plan` 替换为 `--output /path/to/new-pubmed-snapshot` 可联网获取新的 ID 和题录。输出目录必须不存在，未完成的响应不会覆盖旧版本。PubMed 每个 ESearch 输入及原始返回现存于 inputs/search/additional.json 与 inputs/pubmed/；ESummary 以 PMID 再取标题/DOI。复查受控访问状态、数据版本、用途条款和以前未决的影像/标签交付。优先复查 UKB 新申请、BRSET/ODIR 版本、受控数据的机构适格性及新开放的眼脑原始影像。
4. 在新的版本目录中追加或修订 inputs/curation 的行。相同的数据产品沿用原 ID，更新核验日期、字段范围与带定位的来源；疑似镜像先加 relationships 和证据。新增记录使用 `ext-` ID；只有明确版本或产品关系才合并。新增判定必须带来源，撤回、不可用、改许可的历史信息保留在旧快照。新日期补充只能从固定提交导入并重新记录 SHA-256。
5. 修订 score_profiles/score_targets、像素门槛和搜索日志，再运行离线构建/核验并更新本指南使用的数字。查看新旧主表 ID、变化字段、证据及排名差异，发布新的带日期目录；上版可继续按原输入复现。

本库对 EyeDataHub 的元数据作了归类、关联、修订及打分。EyeDataHub 元数据采用 CC BY 4.0，软件 MIT；应引用 Pooya Khosravi 及相应版本，并分别引用实际使用的数据提供者和论文。第三方数据沿用各自条款。本次交付只包含元数据、文献索引和分析工具。[上游引用文件](inputs/v0.7.0/CITATION.cff) · [上游许可](inputs/v0.7.0/LICENSE)
