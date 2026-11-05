#!/usr/bin/env python3
"""Build repository statistics from release CSVs, without fetching remote data.

Requires Python >=3.9 and matplotlib. Run from any working directory:
    python scripts/build_stats.py
    python scripts/build_stats.py --input-dir /path/to/library/output

All reported counts are computed from CSV rows. Resource records are not
independent patient cohorts. Excluded records never enter plotted summaries.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import tempfile
from collections import Counter
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "retinal-stats-mpl"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.text import Text
from matplotlib.ticker import MaxNLocator


ROOT = Path(__file__).resolve().parents[1]
TIERS = ("Tier 1", "Tier 2", "Tier 3")
STATUSES = ("Confirmed", "Uncertain", "Not available")
TOPICS = {
    "A": "Age / aging",
    "B": "Stroke / cerebrovascular risk",
    "C": "Brain MRI / small-vessel disease",
    "D": "Alzheimer disease / cognition / dementia",
    "E": "Other neurological conditions",
    "F": "Cardiometabolic / mortality",
    "G": "Multicenter / multimodal model resources",
}
TOPIC_LABELS = {
    "A": "A · Age / aging",
    "B": "B · Stroke / cerebrovascular risk",
    "C": "C · Brain MRI /\nsmall-vessel disease",
    "D": "D · Alzheimer disease /\ncognition / dementia",
    "E": "E · Other neurological conditions",
    "F": "F · Cardiometabolic / mortality",
    "G": "G · Multicenter / multimodal\nmodel resources",
}
FIELDS = {
    "age": "Age",
    "sex": "Sex",
    "hypertension": "Hypertension",
    "diabetes": "Diabetes",
    "cardiovascular": "Cardiovascular disease",
    "stroke_type": "Stroke subtype",
    "stroke_time": "Stroke time",
    "brain_mri": "Brain MRI",
    "csvd": "Cerebral small-vessel disease",
    "ad": "Alzheimer disease",
    "dementia": "Dementia",
    "cognition": "Cognition",
    "parkinson": "Parkinson disease",
    "frailty": "Frailty",
    "health": "Health status",
    "mortality": "Mortality",
    "followup": "Follow-up",
}
ACCESS = (
    "Open download", "Registration", "Controlled access", "Application",
    "Author contact", "Unavailable",
)


def apply_figure_style():
    """Portable style settings following the Apache-2.0 figure-style skill.

    The helper is embedded so reproducing repository assets does not require a
    machine-local Codex skill installation. Sizes are enlarged for GitHub.
    """
    matplotlib.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 14,
        "axes.labelsize": 14, "axes.titlesize": 14,
        "legend.fontsize": 12, "xtick.labelsize": 11, "ytick.labelsize": 11,
        "axes.linewidth": 0.6, "xtick.direction": "out", "ytick.direction": "out",
        "xtick.major.size": 3, "ytick.major.size": 3,
        "xtick.major.width": 0.6, "ytick.major.width": 0.6,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": False, "legend.frameon": False,
        "figure.dpi": 120, "savefig.dpi": 300,
        "axes.titleweight": "normal", "axes.titlelocation": "left",
        "axes.labelweight": "normal", "lines.linewidth": 1.2,
        "patch.linewidth": 0.6, "pdf.fonttype": 42, "ps.fonttype": 42,
        "svg.fonttype": "none", "svg.hashsalt": "retinal-resource-stats-v1",
    })


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def collect(input_dir):
    files = ("master.csv", "topics.csv", "phenotypes.csv")
    rows = {name: read_csv(input_dir / name) for name in files}
    master = rows["master.csv"]
    ids = {r["id"] for r in master}
    require(len(ids) == len(master), "Duplicate resource ID in master.csv")
    require(master, "Empty master.csv")
    require(all(r["best_tier"] in (*TIERS, "Excluded") for r in master),
            "Unexpected best_tier; update the statistics inclusion rule")
    included = [r for r in master if r["best_tier"] != "Excluded"]
    excluded = [r for r in master if r["best_tier"] == "Excluded"]
    retained_ids = {r["id"] for r in included}
    reviewed = [r for r in master if r["review_depth"] == "Source-reviewed"]
    reviewed_in = [r for r in included if r["review_depth"] == "Source-reviewed"]
    reviewed_out = [r for r in excluded if r["review_depth"] == "Source-reviewed"]
    reviewed_ids = {r["id"] for r in reviewed_in}
    require(included and reviewed_in, "No included/source-reviewed rows to plot")
    require(all(r["access"] in ACCESS for r in included), "Unknown access category")

    topic_index = {}
    for row in rows["topics.csv"]:
        key = row["id"], row["topic"]
        require(key not in topic_index, f"Duplicate topic row: {key}")
        require(row["id"] in ids and row["topic"] in TOPICS, f"Unknown topic key: {key}")
        require(row["tier"] in (*TIERS, "Unknown", "Excluded"), f"Unknown tier: {key}")
        topic_index[key] = row
    require(set(topic_index) == {(rid, topic) for rid in ids for topic in TOPICS},
            "Incomplete topic coverage")
    topic_table = []
    for code, label in TOPICS.items():
        counts = Counter(topic_index[rid, code]["tier"] for rid in retained_ids)
        topic_table.append({"topic": code, "label": label,
                            **{tier: counts[tier] for tier in (*TIERS, "Unknown", "Excluded")}})
        require(sum(counts.values()) == len(included), f"Wrong topic denominator: {code}")

    phenotype_index = {}
    for row in rows["phenotypes.csv"]:
        key = row["id"], row["field"]
        require(key not in phenotype_index, f"Duplicate phenotype row: {key}")
        require(row["id"] in ids, f"Unknown phenotype resource: {key}")
        require(row["status"] in STATUSES, f"Unknown phenotype status: {key}")
        phenotype_index[key] = row
    core_phenotype_keys = {(rid, field) for rid in ids for field in FIELDS}
    require(core_phenotype_keys <= set(phenotype_index), "Incomplete core phenotype coverage")
    phenotype_table = []
    for field, label in FIELDS.items():
        counts = Counter(phenotype_index[rid, field]["status"] for rid in reviewed_ids)
        phenotype_table.append({"field": field, "label": label,
                                **{status: counts[status] for status in STATUSES}})
        require(sum(counts.values()) == len(reviewed_in), f"Wrong clinical denominator: {field}")
    # Confirm the normalized tables match the master representation being released.
    for row in master:
        for topic in TOPICS:
            require(row[f"topic_{topic}"] == topic_index[row["id"], topic]["tier"],
                    f"Master/topic mismatch: {row['id']} / {topic}")
        for field in FIELDS:
            require(row[field] == phenotype_index[row["id"], field]["status"],
                    f"Master/phenotype mismatch: {row['id']} / {field}")

    access_counts = Counter(r["access"] for r in included)
    access_table = [{"access": name, "count": count,
                     "percent": round(100 * count / len(included), 1)}
                    for name, count in sorted(access_counts.items(), key=lambda x: (-x[1], x[0]))]
    require(sum(r["count"] for r in access_table) == len(included), "Wrong access denominator")
    return {
        "schema_version": 1,
        "source_sha256": {name: hashlib.sha256((input_dir / name).read_bytes()).hexdigest()
                          for name in files},
        "latest_resource_check_date": max(r["checked"] for r in master),
        "unit": "resource record, not an independent patient cohort",
        "definitions": {
            "included": "master.csv: best_tier != Excluded",
            "excluded": "master.csv: best_tier == Excluded; retained as exclusion records only",
            "source_reviewed": "master.csv: review_depth == Source-reviewed; depth of review, not universal field confirmation",
            "topics": "Effective topics.csv tier after the pixel-availability gate; multi-label; count once per resource per topic",
            "clinical_denominator": "Included AND Source-reviewed resource records only",
            "access": "One recorded access route per included resource; does not establish raw-image/label access",
            "clinical_status": "Scoped source evidence; Uncertain includes unverified fields and does not mean absent",
        },
        "counts": {
            "all_resource_records": len(master),
            "baseline_records": sum(r["origin"] == "EyeDataHub v0.7.0" for r in master),
            "extension_records": sum(r["origin"] != "EyeDataHub v0.7.0" for r in master),
            "included_resource_records": len(included),
            "excluded_resource_records": len(excluded),
            "source_reviewed_all": len(reviewed),
            "source_reviewed_included": len(reviewed_in),
            "source_reviewed_excluded": len(reviewed_out),
            "catalog_screen_included": sum(r["review_depth"] == "Catalog screen" for r in included),
        },
        "included_best_tier": {tier: sum(r["best_tier"] == tier for r in included) for tier in TIERS},
        "topic_tiers": topic_table,
        "access_routes": access_table,
        "clinical_statuses": phenotype_table,
        "additional_phenotype_fields_not_plotted": sorted({field for _, field in phenotype_index} - set(FIELDS)),
        "included_resource_ids": sorted(retained_ids),
        "clinical_denominator_ids": sorted(reviewed_ids),
        "source_reviewed_exclusions": [{"id": r["id"], "name": r["name"]}
                                        for r in sorted(reviewed_out, key=lambda r: r["id"])],
    }


def contrasting_text(rgba):
    rgb = [channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4
           for channel in rgba[:3]]
    luminance = sum(weight * channel for weight, channel in zip((0.2126, 0.7152, 0.0722), rgb))
    return "#111111" if (luminance + .05) / .055 >= 4.5 else "white"


def matrix(fig, ax, values, row_labels, column_labels, vmax, cbar_position):
    cmap = matplotlib.colormaps["Blues"]
    norm = Normalize(0, vmax)
    im = ax.imshow(values, cmap=cmap, norm=norm, aspect="auto")
    ax.set_xticks(range(len(column_labels)), column_labels)
    ax.set_yticks(range(len(row_labels)), row_labels)
    ax.xaxis.tick_top()
    ax.tick_params(axis="x", length=0, pad=12)
    ax.tick_params(axis="y", length=0, pad=12)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks([x - .5 for x in range(len(column_labels) + 1)], minor=True)
    ax.set_yticks([y - .5 for y in range(len(row_labels) + 1)], minor=True)
    ax.grid(which="minor", color="white", linewidth=1.5)
    ax.tick_params(which="minor", length=0)
    for y, row in enumerate(values):
        for x, value in enumerate(row):
            ax.text(x, y, str(value), ha="center", va="center", fontsize=12,
                    color=contrasting_text(cmap(norm(value))))
    cax = fig.add_axes(cbar_position)
    cb = fig.colorbar(im, cax=cax)
    cb.set_ticks([tick for tick in MaxNLocator(nbins=5, integer=True).tick_values(0, vmax)
                  if 0 <= tick <= vmax])
    cb.outline.set_visible(False)
    cb.ax.set_title("Records", fontsize=11, pad=12)
    cb.ax.tick_params(labelsize=11)


def check_geometry(fig, name):
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    texts = [(text, text.get_window_extent(renderer)) for text in fig.findobj(Text)
             if text.get_visible() and text.get_text().strip()]
    errors = []
    canvas = fig.bbox
    for text, box in texts:
        if not (canvas.x0 - 1 <= box.x0 <= box.x1 <= canvas.x1 + 1
                and canvas.y0 - 1 <= box.y0 <= box.y1 <= canvas.y1 + 1):
            errors.append(f"Outside canvas: {text.get_text()!r}")
    for i, (first, a) in enumerate(texts):
        for second, b in texts[i + 1:]:
            if a.overlaps(b):
                errors.append(f"Text overlap: {first.get_text()!r} / {second.get_text()!r}")
    for ax in fig.axes:
        ticks = set(ax.get_xticklabels(which="both") + ax.get_yticklabels(which="both"))
        for spine in ax.spines.values():
            if spine.get_visible():
                box = spine.get_window_extent(renderer)
                for text, text_box in texts:
                    if text not in ticks and text_box.overlaps(box):
                        errors.append(f"Text/spine overlap: {text.get_text()!r}")
    require(not errors, f"{name}: " + "; ".join(errors))
    return {"name": name, "visible_text_items": len(texts),
            "text_overlaps": 0, "out_of_bounds_text": 0, "text_spine_overlaps": 0}


def save_figure(fig, output, name, alt):
    fig.savefig(output / f"{name}.png", dpi=300, facecolor="white")
    fig.savefig(output / f"{name}.svg", facecolor="white",
                metadata={"Date": None, "Title": alt, "Description": alt})
    qa = check_geometry(fig, name)
    plt.close(fig)
    return qa


def plot_all(data, output):
    apply_figure_style()
    counts = data["counts"]
    n = counts["included_resource_records"]
    nr = counts["source_reviewed_included"]
    qa = []

    fig = plt.figure(figsize=(11, 6.3))
    fig.text(.045, .95, "Topic evidence tiers", ha="left", va="top", fontsize=14)
    fig.text(.045, .89, f"{n} included resource records · multi-label topics", fontsize=12)
    ax = fig.add_axes((.39, .22, .44, .58))
    values = [[row[tier] for tier in TIERS] for row in data["topic_tiers"]]
    matrix(fig, ax, values, list(TOPIC_LABELS.values()), TIERS,
           max(max(row) for row in values), (.90, .22, .018, .58))
    fig.text(.045, .115, "Effective tiers after the raw-pixel gate. Unknown and topic-excluded cells are not plotted.", fontsize=11)
    fig.text(.045, .065, "Topic counts overlap; they must not be added to estimate independent cohorts. Shading uses a linear count scale.", fontsize=11)
    qa.append(save_figure(fig, output, "topic_tiers",
                          f"Evidence-tier counts by topic among {n} included resource records; topics overlap."))

    fig = plt.figure(figsize=(11, 5.7))
    fig.text(.045, .95, "Reported access routes", ha="left", va="top", fontsize=14)
    fig.text(.045, .88, f"{n} included resource records · one recorded category per resource", fontsize=12)
    ax = fig.add_axes((.255, .22, .67, .57))
    routes = data["access_routes"]
    for y, row in enumerate(routes):
        ax.plot((0, row["count"]), (y, y), color="#b9c5ce", linewidth=1.2)
        ax.plot(row["count"], y, "o", color="#225e91", markersize=7)
        ax.annotate(f"{row['count']} ({row['percent']:.1f}%)", (row["count"], y),
                    xytext=(9, 0), textcoords="offset points", va="center", fontsize=12)
    ax.set_yticks(range(len(routes)), [r["access"] for r in routes])
    ax.tick_params(axis="y", length=0, pad=12)
    ax.set_ylim(len(routes) - .55, -.55)
    ax.set_xlim(-2, max(r["count"] for r in routes) * 1.25)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("Resource records", labelpad=10)
    fig.text(.045, .07, "Access route does not guarantee access to raw images or individual labels. Excluded records are omitted.", fontsize=11)
    qa.append(save_figure(fig, output, "access_routes",
                          f"Access-route distribution among {n} included resource records; this is not raw-image availability."))

    fig = plt.figure(figsize=(11, 9.6))
    fig.text(.045, .96, "Clinical-field evidence status", ha="left", va="top", fontsize=14)
    fig.text(.045, .915, f"{nr} included, source-reviewed resource records · each row sums to {nr}", fontsize=12)
    ax = fig.add_axes((.34, .15, .49, .70))
    values = [[row[status] for status in STATUSES] for row in data["clinical_statuses"]]
    matrix(fig, ax, values, list(FIELDS.values()), STATUSES, nr, (.90, .15, .018, .70))
    fig.text(.045, .085, "Confirmed refers to the recorded evidence scope; it does not guarantee raw-image or label access.", fontsize=11)
    fig.text(.045, .05, "Uncertain includes unverified fields. Excluded records and catalog-only screens are omitted.", fontsize=11)
    qa.append(save_figure(fig, output, "clinical_statuses",
                          f"Clinical-field evidence status for {nr} included source-reviewed resource records; unverified does not mean absent."))
    return qa


def markdown(data):
    c = data["counts"]
    n, nr = c["included_resource_records"], c["source_reviewed_included"]
    lines = [
        "# Repository statistics", "",
        "Generated from the release CSVs by [`scripts/build_stats.py`](scripts/build_stats.py). "
        "These are **resource-record counts, not independent patient-cohort counts**. "
        "Mirrors, annotations, releases and derived resources can belong to the same family. "
        "No patient total is inferred from these counts.", "",
        f"Latest `checked` date in the input: **{data['latest_resource_check_date']}**. "
        "This is a snapshot date, not a claim that every record or access route was checked on that date.", "",
        "## Scope and denominators", "",
        "| Scope | Records |", "| --- | ---: |",
        f"| All catalog records | {c['all_resource_records']} |",
        f"| EyeDataHub v0.7.0 baseline records | {c['baseline_records']} |",
        f"| Additional records | {c['extension_records']} |",
        f"| Included (`best_tier != Excluded`) | {n} |",
        f"| Separate exclusion records | {c['excluded_resource_records']} |",
        f"| Source-reviewed, all records | {c['source_reviewed_all']} |",
        f"| Source-reviewed and included | {nr} |",
        f"| Source-reviewed and excluded | {c['source_reviewed_excluded']} |",
        f"| Catalog-screened and included | {c['catalog_screen_included']} |", "",
        f"The {c['excluded_resource_records']} exclusion records are retained to document decisions; "
        "they enter none of the three plotted summaries. "
        f"**Source-reviewed ({c['source_reviewed_all']}) describes review depth, not confirmation of every field.** "
        f"The clinical-status figure uses only the {nr} included source-reviewed records.", "",
        "| Best tier among included resources | Records |", "| --- | ---: |",
    ]
    lines += [f"| {tier} | {data['included_best_tier'][tier]} |" for tier in TIERS]
    lines += ["", "## Topic evidence tiers", "",
              f"![Topic-tier matrix for {n} included resource records](assets/stats/topic_tiers.png)", "",
              "[SVG](assets/stats/topic_tiers.svg). **Multi-label**: a record may contribute to several topics. "
              "The table uses the effective `tier` in `topics.csv` after the raw-pixel availability gate, "
              "not `reviewed_tier_before_pixel_gate`. Each row, including Unknown and topic-excluded, "
              f"sums to {n}; topic totals must not be added to obtain a cohort count.", "",
              "Tier 1 indicates direct individual-level linkage evidence; Tier 2 indicates unresolved "
              "access, linkage or necessary permissions; Tier 3 indicates an auxiliary imaging resource. "
              "A Tier 3 entry in G does not independently establish multicenter acquisition or readiness for federated learning.", "",
              "| Topic | Tier 1 | Tier 2 | Tier 3 | Unknown | Topic-excluded |",
              "| --- | ---: | ---: | ---: | ---: | ---: |"]
    lines += [f"| {r['topic']}: {r['label']} | {r['Tier 1']} | {r['Tier 2']} | {r['Tier 3']} | {r['Unknown']} | {r['Excluded']} |"
              for r in data["topic_tiers"]]
    lines += ["", "## Reported access routes", "",
              f"![Access-route distribution for {n} included resource records](assets/stats/access_routes.png)", "",
              "[SVG](assets/stats/access_routes.svg). Access categories are mutually exclusive per resource record. "
              f"Percentages use {n} included records and are rounded to one decimal place. "
              "This field describes the recorded route to a resource; it does **not** guarantee raw image "
              "files, individual-level clinical labels, permission to link data, or current eligibility. "
              "Consult `image_access`, `label_access`, access conditions and supporting evidence before planning an experiment.", "",
              "| Access route | Records | Percent of included records |", "| --- | ---: | ---: |"]
    lines += [f"| {r['access']} | {r['count']} | {r['percent']:.1f}% |" for r in data["access_routes"]]
    lines += ["", "## Clinical-field evidence status", "",
              f"![Clinical-field status matrix for {nr} included source-reviewed records](assets/stats/clinical_statuses.png)", "",
              "[SVG](assets/stats/clinical_statuses.svg). The denominator is the intersection of "
              f"`best_tier != Excluded` and `review_depth == Source-reviewed` ({nr} records). "
              "Statuses come from `phenotypes.csv`, without imputing unknown fields. Confirmed is scoped "
              "to the cited evidence, which may describe only a subcohort, visit, derived measurement or "
              "restricted variable. It is not a guarantee of image-label access. Uncertain includes unverified "
              "fields and does not establish absence. Not available follows the recorded evidence scope; "
              "these counts are not patient disease prevalences. The figure covers the 17 standard clinical "
              "fields; any additional fields are listed in `data.json` and are not plotted.", "",
              "| Clinical field | Confirmed | Uncertain | Not available |",
              "| --- | ---: | ---: | ---: |"]
    lines += [f"| {r['label']} | {r['Confirmed']} | {r['Uncertain']} | {r['Not available']} |"
              for r in data["clinical_statuses"]]
    lines += ["", "### Source-reviewed exclusions (outside all plotted denominators)", "",
              "| Resource ID | Resource |", "| --- | --- |"]
    lines += [f"| `{r['id']}` | {r['name']} |" for r in data["source_reviewed_exclusions"]]
    lines += ["", "## Reproduce and audit", "",
              "From the repository root, using Python 3.9 or later:", "",
              "```bash", "python -m venv .venv", "source .venv/bin/activate",
              "python -m pip install matplotlib==3.9.4", "python scripts/build_stats.py", "```", "",
              "The default input is `library/output/`. To use another release:", "", "```bash",
              "python scripts/build_stats.py --input-dir /path/to/library/output", "```", "",
              "The script overwrites only `assets/stats/{topic_tiers,access_routes,clinical_statuses}.{png,svg}`, "
              "`assets/stats/data.json` and this generated page. It checks row identity, category coverage, "
              "master/normalized-table agreement and denominators, then renders all figures and checks text "
              "overlaps and canvas bounds. A visual inspection of the PNGs is still needed after data or layout changes.", "",
              "[`data.json`](assets/stats/data.json) contains all plotted tables, denominator IDs, methods, "
              "input SHA-256 digests and geometric checks. Counts and tables are deterministic for the "
              "same CSV bytes; image bytes can vary with font and rendering-library versions.", "",
              "| Source CSV | SHA-256 |", "| --- | --- |"]
    lines += [f"| [`{name}`](library/output/{name}) | `{digest}` |"
              for name, digest in data["source_sha256"].items()]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=ROOT / "library" / "output")
    args = parser.parse_args()
    data = collect(args.input_dir)
    output = ROOT / "assets" / "stats"
    output.mkdir(parents=True, exist_ok=True)
    data["geometric_checks"] = plot_all(data, output)
    (output / "data.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "STATS.md").write_text(markdown(data), encoding="utf-8")
    print(json.dumps({"counts": data["counts"], "figures": 3,
                      "geometric_checks": data["geometric_checks"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
