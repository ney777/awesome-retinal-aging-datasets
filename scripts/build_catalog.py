#!/usr/bin/env python3
"""Build evidence-linked Markdown resource pages from the library's exported CSVs.

Run from any directory. The default input is ../library/output. During development,
--library may point to retinal_resource_library instead. No network or dependencies.
"""
import argparse
import csv
import hashlib
import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

AS_OF = "2026-11-03"
UNKNOWN = "Unknown"
TOPICS = {
    "A": "Retinal aging / 眼底年龄与衰老",
    "B": "Stroke and cerebrovascular risk / 脑卒中与脑血管风险",
    "C": "Brain MRI and CSVD / 脑 MRI 与脑小血管病",
    "D": "Alzheimer’s, cognition and dementia / AD、认知与痴呆",
    "E": "Other neurological diseases / 其他神经系统疾病",
    "F": "Cardiovascular, metabolic and mortality outcomes / 心血管、代谢与死亡",
    "G": "Multicenter and foundation models / 多中心与基础模型",
}
CLINICAL = {
    "age": "Age / 年龄", "sex": "Sex / 性别", "hypertension": "Hypertension / 高血压",
    "diabetes": "Diabetes / 糖尿病", "cardiovascular": "Cardiovascular disease / 心血管病",
    "stroke_type": "Stroke type / 卒中分型", "stroke_time": "Stroke timing / 卒中事件时间",
    "brain_mri": "Brain MRI / 脑 MRI", "csvd": "CSVD / 脑小血管病",
    "ad": "Alzheimer’s disease / 阿尔茨海默病", "dementia": "Dementia / 痴呆",
    "cognition": "Cognition / 认知功能", "parkinson": "Parkinson’s disease / 帕金森病",
    "frailty": "Frailty / 衰弱", "health": "Health status / 健康状态",
    "mortality": "Mortality / 死亡结局", "followup": "Follow-up / 纵向随访",
}
GROUPS = [
    ("Identity and provenance", [
        ("id", "Stable resource ID"), ("name", "Name / 名称"), ("acronym", "Acronym / 缩写"),
        ("official_url", "Official resource"), ("country", "Country or region / 国家地区"),
        ("institution", "Institution / 机构"), ("year", "Reported year / 年份口径"),
        ("publication_date", "Publication date"), ("publication_date_scope", "Date scope"),
        ("publication_date_source_url", "Date evidence"), ("publication_date_reviewed_on", "Date reviewed"),
        ("citation", "Original citation"), ("doi", "Publication DOI"), ("dataset_doi", "Dataset DOI"),
        ("origin", "Import origin"), ("baseline_id", "Original EyeDataHub ID"),
        ("family", "Dataset family"), ("relation", "Family or derivative relation"),
        ("duplicate_status", "Independence / overlap"), ("upstream_family", "Upstream family ID"),
        ("upstream_role", "Upstream resource role"), ("review_depth", "Review depth"),
        ("best_tier", "Best recorded topic tier"),
        ("checked", "Latest recorded source review"),
        ("description", "Frozen upstream description"),
    ]),
    ("Imaging and cohort", [
        ("modalities", "Modalities / 影像模态"), ("images", "Images / 图像数及口径"),
        ("participants", "Participants / 参与者数及口径"), ("eyes", "Eyes / 眼别"),
        ("device", "Device / 设备"), ("resolution", "Resolution / 分辨率"),
        ("quality", "Quality / 质量控制"), ("multivisit", "Multiple visits / 多时点"),
        ("multimodal", "Multiple modalities / 多模态"), ("multicenter", "Multiple centers / 多中心"),
    ]),
    ("Access and reuse", [
        ("access", "Access category / 获取方式"), ("access_url", "Access or application route"),
        ("image_access", "Image files / 影像文件"), ("label_access", "Individual labels / 个体标签"),
        ("license", "Data license / 数据许可"), ("research_terms", "Research use / 科研条件"),
        ("commercial_terms", "Commercial use / 商业用途"), ("terms_scope", "Terms scope"),
        ("terms_evidence_url", "Terms evidence"), ("route_last_checked", "Upstream route review date"),
        ("acquisition_support", "Upstream acquisition support"), ("raw_access_friction", "Upstream access friction"),
    ]),
    ("Research value and experimental design", [
        ("pairing", "Individual linkage / 个体配对依据"), ("strengths", "Strengths / 主要优点"),
        ("limitations", "Limitations / 关键缺陷"), ("experiment", "Suggested experiments / 建议实验"),
        ("age_clock_fit", "Retinal Aging suitability"), ("stroke_csvd_fit", "Stroke / CSVD suitability"),
        ("ad_dementia_fit", "AD / Dementia suitability"), ("multicenter_model_fit", "Multicenter model suitability"),
        ("screen_reason", "Screening rationale / 筛查理由"),
    ]),
]
TIERS = {"Tier 1": 1, "Tier 2": 2, "Tier 3": 3, "Excluded": 4, UNKNOWN: 5}


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def text(value):
    """Escape content for Markdown prose and table cells while retaining Unknown."""
    value = str(value) if value not in (None, "") else UNKNOWN
    value = html.escape(value, quote=False)
    value = re.sub(r"([\\`*_{}\[\]<>|#])", r"\\\1", value)
    return value.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "<br>")


def target(value):
    # Preserve existing escapes and query delimiters while encoding Markdown delimiters.
    return quote(str(value), safe="/:?=&%+@!$,;~-._#")


def external(value, label="Source"):
    if value and urlsplit(str(value)).scheme.lower() in ("http", "https"):
        return "[" + text(label) + "](" + target(value) + ")"
    return text(value)


def local(value, label):
    return "[" + text(label) + "](" + target(value) + ")"


def field_value(key, value):
    if key.endswith("_url") or key == "official_url":
        return external(value, value)
    if key in ("doi", "dataset_doi") and str(value).startswith("10.") and " " not in value:
        return external("https://doi.org/" + value, value)
    return text(value)


def table(headers, rows):
    return "\n".join([
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
        *("| " + " | ".join(row) + " |" for row in rows),
    ])


def grouped(rows, key="id"):
    result = defaultdict(list)
    for row in rows:
        result[row[key]].append(row)
    return result


def evidence_refs(value, anchors):
    if not value or value == UNKNOWN:
        return UNKNOWN
    refs = []
    for key in value.split(" | "):
        if key not in anchors:
            raise ValueError("Unresolved evidence identifier " + key)
        refs.append(local("#" + anchors[key], key.rsplit("#", 1)[-1]))
    return ", ".join(refs)


def load_examples(repo, resource_ids):
    manifest = repo / "assets/examples/manifest.json"
    result = defaultdict(list)
    if not manifest.exists():
        return result
    data = json.loads(manifest.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = next((data[k] for k in ("assets", "examples", "images", "records") if k in data), [])
    if not isinstance(data, list):
        raise ValueError("Example manifest must contain a list")
    folder = (repo / "assets/examples").resolve()
    for row in data:
        resource_id = row.get("resource_id")
        if resource_id not in resource_ids:
            continue
        filename = row.get("path") or row.get("filename") or row.get("file")
        if not filename:
            continue
        path = Path(filename)
        if path.is_absolute():
            raise ValueError("Example paths must be repository relative")
        path = (repo / path if path.parts[:2] == ("assets", "examples") else folder / path).resolve()
        if not path.is_relative_to(folder) or not path.is_file():
            raise ValueError("Missing or unsafe local example " + str(filename))
        if row.get("sha256") and hashlib.sha256(path.read_bytes()).hexdigest() != row["sha256"]:
            raise ValueError("Example checksum mismatch " + str(filename))
        result[resource_id].append({**row, "relative_path": path.relative_to(repo).as_posix()})
    return result


def sample_section(row, examples, path_prefix="../"):
    if not examples:
        return ("本页尚无经过审核并收录到本仓库的本地影像样例。可在官方资源页查看作者提供的示例、"
                "预览或样例获取说明。样例可用性为 Unknown。\n\n" +
                external(row.get("official_url"), "Official resource / 官方示例入口"))
    parts = []
    for sample in examples:
        kind = sample.get("kind", UNKNOWN)
        caption = sample.get("caption") or sample.get("alt") or row["name"] + " — " + kind
        parts.append("![" + text(caption) + "](" + target(path_prefix + sample["relative_path"]) + ")")
        parts.append(text(sample.get("what_image_shows") or caption))
        parts.append(table(["Example metadata", "Value"], [
            ["Asset type", text(kind)],
            ["Modality", text(sample.get("modality"))],
            ["Source", external(sample.get("source_url") or sample.get("url"), "Official example source")],
            ["License", external(sample.get("license_url"), sample.get("license", UNKNOWN))],
            ["Attribution", text(sample.get("attribution"))],
            ["License evidence", external(sample.get("license_source_url"), "Source terms") + " — " + text(sample.get("license_evidence"))],
            ["Modification", text(sample.get("transform"))],
            ["Provider preprocessing evidence", external(sample.get("processing_source_url"), "Dataset descriptor")],
            ["Image verification date", text(sample.get("verified_date"))],
            ["Scope", text(sample.get("scope") or "Illustrative example. Clinical labels and representativeness require resource-specific evidence.")],
        ]))
    return "\n\n".join(parts)


def write_gallery(repo, examples, master):
    manifest = repo / "assets/examples/manifest.json"
    if not manifest.is_file():
        return []
    metadata = json.loads(manifest.read_text(encoding="utf-8"))
    metadata = metadata if isinstance(metadata, dict) else {}
    assets = [sample for samples in examples.values() for sample in samples]
    kinds = Counter(sample.get("kind", UNKNOWN) for sample in assets)
    resources = sum(bool(samples) for samples in examples.values())
    parts = [
        "# Image examples and source previews",
        local("../../catalog/README.md", "Dataset catalog") + " · " + local("manifest.json", "Image provenance manifest"),
        "Image metadata verified on " + text(metadata.get("verified_date")) + ". Dataset catalog snapshot — " + AS_OF + ".",
        "本画廊收录 " + str(resources) + " 个资源的 " + str(len(assets)) + " 张示例，包括 " +
        str(kinds["dataset_sample"]) + " 张 dataset_sample 和 " + str(kinds["published_figure"]) +
        " 张 published_figure。每项均附图像范围、原始来源、许可和署名。",
        "再利用时须保留对应作者署名和许可链接。每张图适用其原来源条款。",
    ]
    if metadata.get("public_provenance_note"):
        parts.append(text(metadata["public_provenance_note"]))
    for resource_id, samples in examples.items():
        if not samples:
            continue
        row = master[resource_id]
        parts.extend([
            "## " + text(samples[0].get("resource_name") or row["name"]),
            local("../../datasets/" + resource_id + ".md", "Resource details / 数据与临床关联说明"),
            sample_section(row, samples, "../../"),
        ])
    extra = metadata.get("additional_example_entries", [])
    parts.append("## Further official preview routes")
    parts.append(table(["Resource", "Official source", "Local display status", "Reason"], [
        [local("../../datasets/" + row["resource_id"] + ".md", row.get("name", row["resource_id"])),
         external(row.get("source_url"), "Official resource / 示例入口"), text(row.get("status")), text(row.get("reason"))]
        for row in extra
    ]) if extra else UNKNOWN)
    destination = repo / "assets/examples/README.md"
    destination.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    return [destination]


def relationship_rows(resource_id, relationships, master):
    result = []
    for edge in relationships:
        source = edge.get("source_record_id", edge.get("source_id"))
        dest = edge.get("target_record_id", edge.get("target_id"))
        if resource_id not in (source, dest):
            continue
        def ref(key):
            return local(key + ".md", key) if key in master else text(key)
        result.append([
            ref(source), text(edge.get("relationship_type", edge.get("relation"))), ref(dest),
            text(edge.get("confidence", edge.get("status"))),
            text(edge.get("evidence_summary", edge.get("note"))),
            external(edge.get("evidence_url"), "Relationship evidence"),
        ])
    return result


def resource_page(row, tables, master, examples):
    resource_id = row["id"]
    sources = tables["evidence"].get(resource_id, [])
    anchors = {r["evidence_id"]: "evidence-" + str(n) for n, r in enumerate(sources, 1)}
    review = row.get("review_depth", UNKNOWN)
    overview = text(row.get("description"))
    if review == "Source-reviewed":
        summary = next((row[key] for key in ("strengths", "screen_reason", "pairing")
                        if row.get(key) not in (None, "", UNKNOWN)), UNKNOWN)
        overview = (text(summary) + "\n\n当前核验的影像与模态范围 — " + text(row.get("modalities")) +
                    "\n\nImage availability — " + text(row.get("image_access")))
    note = ("Source-reviewed 表示已针对选题相关字段查阅原始来源；各字段仍按已确认、待确认和不提供分别记录。"
            if review == "Source-reviewed" else
            "Catalog screen 表示已完成 EyeDataHub 目录级筛查。该状态的临床配对、个体标签和数据内容仍需逐项核验。")
    sections = [
        "# " + text(row["name"]),
        local("../catalog/README.md", "All resources") + " · " + local("../catalog/reviewed.md", "Source-reviewed resources"),
        "Metadata as of " + AS_OF + " (base survey). Review depth — " + text(review) + ". " +
        "Later targeted corrections are dated in the evidence table and recorded in the " +
        local("../CHANGELOG.md", "changelog") + ".",
        note,
        "## Overview\n\n" + overview,
    ]
    covered = {"description", "best_tier", *CLINICAL, *("topic_" + t for t in TOPICS)}
    for title, fields in GROUPS:
        sections.append("## " + title + "\n\n" + table(["Field", "Recorded value"], [
            [text(label), field_value(key, row.get(key))] for key, label in fields
        ]))
        covered.update(key for key, _ in fields)
    topics = {r["topic"]: r for r in tables["topics"].get(resource_id, [])}
    sections.append("## Topic evidence\n\n" + table(
        ["Topic", "Image-specific tier", "Study tier before image-access review", "Rationale", "Evidence"], [
            [local("../catalog/topics/" + key + ".md", key + " · " + title), text(topics.get(key, {}).get("tier")),
             text(topics.get(key, {}).get("reviewed_tier_before_pixel_gate")), text(topics.get(key, {}).get("reason")),
             evidence_refs(topics.get(key, {}).get("evidence_id"), anchors)] for key, title in TOPICS.items()
        ]))
    clinical = {r["field"]: r for r in tables["phenotypes"].get(resource_id, [])}
    fields = list(CLINICAL) + sorted(clinical.keys() - CLINICAL.keys())
    sections.append("## Clinical phenotypes\n\n" + table(["Field", "Status", "Scope", "Evidence"], [
        [text(CLINICAL.get(key, key)), text(clinical.get(key, {}).get("status")),
         text(clinical.get(key, {}).get("scope")), evidence_refs(clinical.get(key, {}).get("evidence_id"), anchors)]
        for key in fields
    ]))
    quantities = tables["quantities"].get(resource_id, [])
    sections.append("## Counting evidence\n\n" + (table(
        ["Count", "Unit", "Scope", "Evidence basis", "Exactness", "Source"], [
            [text(q.get(k)) for k in ("count", "unit", "scope", "evidence_basis", "exactness")] +
            [external(q.get("evidence_url"), "Quantity source")] for q in quantities
        ]) if quantities else "Unknown — 本快照没有单独的图像或参与者数量核验表，已知数量及其口径见 Imaging and cohort。"))
    edges = relationship_rows(resource_id, tables["relationships"], master)
    sections.append("## Family and derivative ledger\n\n" + (table(
        ["Source resource", "Relation", "Target resource", "Confidence", "Scope", "Evidence"], edges
    ) if edges else "Unknown — 未记录具体的资源关系边。患者或影像重叠情况仍见 Identity and provenance。"))
    ranks = tables["rankings"].get(resource_id, [])
    sections.append("## Research priorities\n\n" + (table(
        ["Track / endpoint", "Science rank / score", "Near-term rank / score", "R / L / Q / X / M", "Denominator", "Rationale"], [
            [text(r["track"] + " — " + r["endpoint"]), text(r["scientific_rank"] + " / " + r["scientific_score"]),
             text((r["practical_rank"] or "Not eligible") + " / " + r["practical_score"]),
             text(" / ".join(r[k] for k in ("R", "L", "Q", "X", "M"))),
             text(r.get("paired_n_basis")), text(r.get("basis"))] for r in ranks
        ]) + "\n\nR 为研究适配，L 为标签丰富度，Q 为队列质量，X 为获取可行性，M 为多中心价值。分项范围 0–4。"
        if ranks else "Unknown — 本资源未进入当前三个科研方向的候选排名。"))
    sections.append("## Examples and previews\n\n" + sample_section(row, examples))
    remaining = sorted(row.keys() - covered)
    if remaining:
        sections.append("## Additional catalog fields\n\n" + table(
            ["Field", "Recorded value"], [[text(k), field_value(k, row[k])] for k in remaining]
        ))
    evidence = []
    for source in sources:
        evidence.append('<a id="' + anchors[source["evidence_id"]] + '"></a>\n\n' +
                        "### " + text(source["evidence_id"].rsplit("#", 1)[-1]) + "\n\n" +
                        external(source["url"], "Open original source") + "\n\n" +
                        text(source["locator"]) + "\n\nRecorded check date — " + text(source["checked"]) + ".")
    sections.append("## Sources\n\n" + ("\n\n".join(evidence) or UNKNOWN))
    return "\n\n".join(sections) + "\n"


def topic_badges(row):
    return "; ".join(key + " " + row.get("topic_" + key, UNKNOWN) for key in TOPICS
                     if row.get("topic_" + key, UNKNOWN).startswith("Tier")) or "Excluded"


def index_table(rows, prefix="../datasets/"):
    return table(["Resource", "Stable ID", "Modalities", "Topics", "Access", "Review depth"], [
        [local(prefix + row["id"] + ".md", row["name"]), text(row["id"]), text(row.get("modalities")),
         text(topic_badges(row)), text(row.get("access")), text(row.get("review_depth"))] for row in rows
    ])


def write_indexes(repo, rows, tables):
    catalog = repo / "catalog"
    (catalog / "topics").mkdir(parents=True, exist_ok=True)
    reviewed = [r for r in rows if r.get("review_depth") == "Source-reviewed"]
    baseline = sum(r.get("origin") == "EyeDataHub v0.7.0" for r in rows)
    banner = ("Metadata as of " + AS_OF + ". " + str(len(rows)) + " resource records, " + str(baseline) +
              " EyeDataHub v0.7.0 baseline records, " + str(len(reviewed)) + " source-reviewed records.\n\n"
              "资源记录保留原始 ID 和数据家族。独立参与者队列数为 Unknown，统计时应查阅每页的家族关系和重复说明。"
              "Catalog screen 记录仅完成目录级筛查，Source-reviewed 记录保留已核验字段及未确认项。")
    navigation = " · ".join(local("topics/" + key + ".md", key) for key in TOPICS)
    body = ["# Dataset catalog", banner, navigation + " · " + local("reviewed.md", "Source-reviewed") + " · " + local("excluded.md", "Excluded"),
            "## Alphabetical index", index_table(rows)]
    (catalog / "README.md").write_text("\n\n".join(body) + "\n", encoding="utf-8")
    (catalog / "reviewed.md").write_text("# Source-reviewed resources\n\n" + banner + "\n\n" +
                                         local("README.md", "Full catalog") + "\n\n" + index_table(reviewed) + "\n", encoding="utf-8")
    for key, title in TOPICS.items():
        judgments = {r["id"]: r for r in tables["topics_flat"] if r["topic"] == key}
        counts = Counter(judgments.get(r["id"], {}).get("tier", UNKNOWN) for r in rows)
        content = ["# " + key + " · " + title, "Metadata as of " + AS_OF + ".", local("../README.md", "Full catalog"),
                   "; ".join(text(tier) + " — " + str(counts[tier]) for tier in TIERS),
                   "未单独判定的资源保留为 Unknown，可通过完整目录和资源页查看。"]
        for tier in ("Tier 1", "Tier 2", "Tier 3", "Excluded"):
            found = [r for r in rows if judgments.get(r["id"], {}).get("tier") == tier]
            content.append("## " + tier)
            content.append(table(["Resource", "Modalities", "Access", "Review", "Rationale"], [
                [local("../../datasets/" + row["id"] + ".md", row["name"]), text(row.get("modalities")),
                 text(row.get("access")), text(row.get("review_depth")), text(judgments[row["id"]]["reason"])]
                for row in found
            ]) if found else "No resource currently assigned to this tier.")
        (catalog / "topics" / (key + ".md")).write_text("\n\n".join(content) + "\n", encoding="utf-8")
    excluded = [r for r in rows if r.get("best_tier") == "Excluded"]
    content = ["# Exclusion ledger", "Metadata as of " + AS_OF + ".", local("README.md", "Full catalog"),
               "## Resource-level exclusions", table(["Resource", "Review", "Recorded reason"], [
                   [local("../datasets/" + row["id"] + ".md", row["name"]), text(row.get("review_depth")),
                    text(row.get("screen_reason"))] for row in excluded
               ])]
    lookup = {r["id"]: r for r in rows}
    partial = [t for t in tables["topics_flat"] if t["tier"] == "Excluded" and lookup[t["id"]].get("best_tier") != "Excluded"]
    content += ["## Topic-specific exclusions", table(["Resource", "Topic", "Recorded reason"], [
        [local("../datasets/" + t["id"] + ".md", lookup[t["id"]]["name"]), text(t["topic"]), text(t["reason"])]
        for t in partial
    ]) if partial else "No additional topic-specific exclusions."]
    (catalog / "excluded.md").write_text("\n\n".join(content) + "\n", encoding="utf-8")


def check_links(paths, repo):
    """Check every generated local Markdown link, file, and explicit evidence anchor."""
    errors = []
    links = 0
    for path in paths:
        content = path.read_text(encoding="utf-8")
        for raw in re.findall(r"(?<!!)\]\(([^\n)]*)\)|!\[[^\n]*?\]\(([^\n)]*)\)", content):
            url = next(x for x in raw if x)
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc:
                continue
            links += 1
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path.resolve()
            if not dest.is_relative_to(repo.resolve()) or not dest.is_file():
                errors.append(str(path.relative_to(repo)) + " -> " + url)
                continue
            if parsed.fragment:
                anchor = unquote(parsed.fragment)
                if '<a id="' + anchor + '"></a>' not in dest.read_text(encoding="utf-8"):
                    errors.append(str(path.relative_to(repo)) + " -> missing anchor " + url)
    if errors:
        raise ValueError("Invalid generated local links\n" + "\n".join(errors[:30]))
    return links


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--library", type=Path, help="Library root containing output/*.csv")
    args = parser.parse_args()
    repo = args.repo.resolve()
    library = (args.library or repo / "library").resolve()
    output = library / "output"
    master_rows = read_csv(output / "master.csv")
    rows = sorted(master_rows, key=lambda row: (row["name"].casefold(), row["id"]))
    master = {row["id"]: row for row in rows}
    if len(master) != len(rows):
        raise ValueError("Duplicate resource IDs")
    for resource_id in master:
        if not re.fullmatch(r"[A-Za-z0-9_-]+", resource_id):
            raise ValueError("Unsafe resource ID " + resource_id)
    tables = {name: grouped(read_csv(output / (name + ".csv")))
              for name in ("topics", "phenotypes", "evidence", "rankings")}
    tables["topics_flat"] = read_csv(output / "topics.csv")
    tables["quantities"] = grouped(read_csv(output / "quantities.csv"), "record_id")
    tables["relationships"] = read_csv(output / "relationships.csv") + read_csv(output / "extensions_relationships.csv")
    examples = load_examples(repo, master)
    pages = repo / "datasets"
    pages.mkdir(parents=True, exist_ok=True)
    for row in rows:
        (pages / (row["id"] + ".md")).write_text(resource_page(row, tables, master, examples[row["id"]]), encoding="utf-8")
    write_indexes(repo, rows, tables)
    generated = [pages / (row["id"] + ".md") for row in rows] + list((repo / "catalog").rglob("*.md"))
    gallery = write_gallery(repo, examples, master)
    generated.extend(gallery)
    links = check_links(generated, repo)
    print(json.dumps({"resource_pages": len(rows), "catalog_pages": len(generated) - len(rows) - len(gallery),
                      "gallery_pages": len(gallery),
                      "local_links_checked": links, "example_resources": len([v for v in examples.values() if v]),
                      "metadata_as_of": AS_OF}, ensure_ascii=False))


if __name__ == "__main__":
    main()
