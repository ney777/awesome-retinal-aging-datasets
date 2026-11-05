#!/usr/bin/env python3
"""Build RANKINGS.md from library/output using only the Python standard library.

This renderer validates and preserves the library's judgments and ranks; it does
not invent endpoint eligibility, replace source evidence, or change scores.
"""

import argparse
import csv
import hashlib
import html
import re
from collections import Counter
from decimal import Decimal
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
TRACKS = {
    "Retinal Aging": "retinal-aging",
    "Eye–Stroke": "eye-stroke",
    "Eye–Neurodegeneration": "eye-neurodegeneration",
}
COMPONENTS = ("R", "L", "Q", "X", "M")
COUNTABLE_SCOPES = {"Study-linked participants", "Outcome-positive subset (lower bound)"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def text(value):
    value = html.escape(str(value), quote=False)
    value = re.sub(r"([\\`*_{}\[\]|])", r"\\\1", value)
    return value.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "<br>")


def link(row):
    target = quote(row["id"], safe="-_.~")
    return f"[{text(row['name'])}](datasets/{target}.md)"


def number(value):
    return format(Decimal(value).normalize(), "f")


def table(headers, rows):
    return "\n".join([
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
        *("| " + " | ".join(row) + " |" for row in rows),
    ])


def ordered(rows, score):
    return sorted(rows, key=lambda r: (-Decimal(r[score]), -int(r["R"]), r["id"]))


def check_ranks(rows, score, rank):
    previous_score = None
    expected = 0
    for position, row in enumerate(ordered(rows, score), 1):
        current = Decimal(row[score])
        if current != previous_score:
            expected = position
        require(row[rank] == str(expected),
                f"Incorrect competition rank: {row['track']} / {row['id']} / {rank}")
        previous_score = current


def load(input_dir):
    master_rows = read_csv(input_dir / "master.csv")
    master = {row["id"]: row for row in master_rows}
    require(len(master_rows) == len(master), "Duplicate master resource ID")
    rows = read_csv(input_dir / "rankings.csv")
    keys = {(r["track"], r["id"]) for r in rows}
    require(len(keys) == len(rows), "Duplicate dataset-track ranking pair")
    require(rows, "Empty rankings.csv")
    require(set(r["track"] for r in rows) == set(TRACKS), "Unexpected or missing ranking track")
    for row in rows:
        rid = row["id"]
        require(rid in master, f"Unknown ranked resource: {rid}")
        require(master[rid]["name"] == row["name"], f"Resource-name mismatch: {rid}")
        require(master[rid]["best_tier"] != "Excluded", f"Excluded ranked resource: {rid}")
        require((ROOT / "datasets" / (rid + ".md")).is_file(), f"Missing stable resource page: {rid}")
        values = {key: int(row[key]) for key in COMPONENTS}
        require(all(0 <= value <= 4 for value in values.values()), f"Invalid component score: {rid}")
        require(values["R"] >= 1, f"Invalid scientific-relevance score: {rid}")
        expected_science = Decimal(40 * values["R"] + 25 * values["L"] + 25 * values["Q"] + 10 * values["M"]) / 4
        expected_practical = Decimal(25 * values["R"] + 15 * values["L"] + 10 * values["Q"] + 5 * values["M"] + 45 * values["X"]) / 4
        require(Decimal(row["scientific_score"]) == expected_science, f"Scientific formula mismatch: {rid}")
        require(Decimal(row["practical_score"]) == expected_practical, f"Near-term formula mismatch: {rid}")
        require(row["near_term"] in {"Yes", "No"}, f"Unexpected near_term value: {rid}")
        if row["near_term"] == "Yes":
            require(row["practical_rank"] and values["R"] >= 3 and values["X"] >= 3
                    and re.search(r"(?:^| / )[A-G] T1(?: / |$)", row["tier"]),
                    f"Inconsistent near-term eligibility: {rid}")
        else:
            require(not row["practical_rank"], f"Ineligible resource has a near-term rank: {rid}")
        if row["n_supported"] != "Unknown":
            require(row["n_scope"] in COUNTABLE_SCOPES and int(row["n_supported"]) > 0,
                    f"Unsupported size denominator: {rid}")
    for track in TRACKS:
        selected = [row for row in rows if row["track"] == track]
        check_ranks(selected, "scientific_score", "scientific_rank")
        check_ranks([row for row in selected if row["near_term"] == "Yes"], "practical_score", "practical_rank")
    return rows, master


def scope(row):
    return text(row["n_scope"]) + ": " + text(row["paired_n_basis"])


def render(rows, master, input_dir):
    n_pairs = len(rows)
    unique_ids = {row["id"] for row in rows}
    n_ready = sum(row["near_term"] == "Yes" for row in rows)
    snapshot = max(master[rid]["checked"] for rid in unique_ids)
    parts = [
        "# Research priorities and rankings",
        "[Dataset catalog](catalog/README.md) · [Statistics](STATS.md) · "
        "[Machine-readable rankings](library/output/rankings.csv) · [Detailed scoring methods](library/METHODS.md)",
        f"This snapshot contains **{n_pairs} resource–task pairs across {len(unique_ids)} resource records**, "
        f"with **{n_ready} pairs eligible for the near-term list**. The latest resource-level review date among ranked "
        f"resources is {snapshot}. These are project-specific prioritization judgments, not independent "
        "cohort counts, clinical validation results, or a certification of data quality. "
        "Resource names link to stable pages containing evidence, access conditions and limitations.",
        "The scientific summaries below select **competition ranks 1–3, including all ties**. "
        "Equal scores receive the same rank and subsequent positions are skipped (for example, "
        "1, 1, 1, 1, 5). They do not select the first three distinct score bands or arbitrarily "
        "truncate a tied group. The near-term summaries show **every eligible pair**.",
        " · ".join(f"[{track}](#{anchor})" for track, anchor in TRACKS.items()) +
        " · [Five components and eligibility](#five-components-and-eligibility) · "
        "[All ranking rows](#all-ranking-rows) · [Reproduce](#reproduce)",
    ]
    for track, anchor in TRACKS.items():
        selected = [row for row in rows if row["track"] == track]
        top = [row for row in ordered(selected, "scientific_score") if int(row["scientific_rank"]) <= 3]
        ready = ordered([row for row in selected if row["near_term"] == "Yes"], "practical_score")
        parts.extend([f'<a id="{anchor}"></a>', f"## {track}",
                      f"{len(selected)} resource–task pairs are scored for this direction.",
                      "### Scientific priority: ranks 1–3, with ties",
                      f"<!-- scientific-top: {anchor} -->"])
        parts.append(table(["Science rank", "Resource", "Science / 100", "Topic tier", "Access route"],
                           [[r["scientific_rank"], link(r), number(r["scientific_score"]),
                             text(r["tier"]), text(r["access"])] for r in top]))
        parts.append(f"<!-- /scientific-top: {anchor} -->")
        top_ties = Counter(row["scientific_rank"] for row in top)
        tie_notes = [f"{count} resources share rank {rank}" for rank, count in top_ties.items() if count > 1]
        if tie_notes:
            parts.append("; ".join(tie_notes) + ". All are retained in this summary. "
                         "Scientific rank does not imply current access to the required images or labels.")
        parts.append(f"### Near-term implementation: all {len(ready)} eligible pairs")
        parts.append(f"<!-- near-term: {anchor} -->")
        if ready:
            parts.append(table(["Near-term rank", "Resource", "Near-term / 100", "Endpoint", "Size-score N and scope"],
                               [[r["practical_rank"], link(r), number(r["practical_score"]), text(r["endpoint"]),
                                 text(r["n_supported"]) + " — " + scope(r)] for r in ready]))
        else:
            parts.append("**No pair passes the current near-term gates in this direction.** "
                         "The scientific candidates still require resolution of image access, endpoint "
                         "availability, authorization or readiness. This empty list does not establish "
                         "that no suitable dataset exists elsewhere.")
        parts.append(f"<!-- /near-term: {anchor} -->")

    parts.extend([
        '<a id="five-components-and-eligibility"></a>', "## Five components and eligibility",
        "Each component is scored from 0 to 4 (ranked R values are 1–4). "
        "The five scores remain separate in the full tables; access feasibility is not folded into "
        "the scientific score. The source [judgment profiles](library/inputs/score_profiles.tsv), "
        "[endpoint and denominator inputs](library/inputs/score_targets.tsv), "
        "[label exceptions](library/inputs/score_label_omissions.json) and "
        "[ranking calculation](library/src/ranking.py) make the decisions auditable.",
        table(["Component", "Meaning", "Rule summary"], [
            ["R", "Scientific relevance", "Endpoint-specific relevance: 4 direct principal target; 3 direct age, clinical case–control, imaging or cognition; 2 proxy or restricted bridge; 1 weak match such as age bands."],
            ["L", "Label richness", "For k confirmed fields from the direction-specific field set: min(4, ceil(k/2)); recorded field exclusions apply."],
            ["Q", "Cohort quality", "One point each for supported endpoint-linked N ≥100 and ≥1000, population sampling, documented quality control, and confirmed follow-up; capped at 4."],
            ["X", "Access feasibility", "4 documented open image/label route; 3 explicit conditional or registration route; 2 formal image application or named secure project; 1 contact or unresolved pixel/authorization scope; 0 paused, prohibited or unverified route."],
            ["M", "Multicenter value", "0 unclear source; 1 one site or independent population/device domain; 2 device, population or recruitment heterogeneity; 3 documented multicenter/community project; 4 verifiable center keys plus regional/device distribution."],
        ]),
        "**Scientific score** = (40R + 25L + 25Q + 10M) / 4. "
        "**Near-term implementation score** = (25R + 15L + 10Q + 5M + 45X) / 4. Both use a 0–100 scale.",
        "A near-term rank is assigned only when the original curation marks the endpoint as ready, "
        "the relevant topic includes Tier 1, R ≥3 and X ≥3. A calculated implementation score "
        "does not bypass these gates. **Not eligible** means no near-term rank is assigned, even "
        "though the component-based score is retained. Eligibility is scoped to the stated endpoint "
        "and source review date; it does not establish permission for an individual applicant or "
        "sufficient sample size for a population model.",
        "**Denominator rule:** only study-linked participants and documented outcome-positive subsets "
        "can contribute scale points. A lower-bound case count is not a complete analysis cohort. "
        "A parent-cohort count, unmatched image count or unknown participant denominator does not "
        "receive scale points. `N for size score` is the original `n_supported`; `reported_n` is "
        "preserved separately below. Neither is a promise of currently deliverable training pairs.",
        "**Choose the endpoint before using a rank.** Incident stroke, contemporaneous small-vessel "
        "disease, self-reported stroke and carotid thickness are different targets. Short-term "
        "retest data, continuous-age prediction and biological-aging validation are also different "
        "experiments. The tables preserve the original endpoint and rationale wording instead of "
        "combining these targets into one implied clinical benchmark.",
        '<a id="all-ranking-rows"></a>', f"## All ranking rows: {n_pairs} resource–task pairs",
        "Each expandable section contains every row for that direction. The first table preserves "
        "all five components and both scores/ranks; the second preserves endpoint, denominator, "
        "access and scoring context. Equal-score rows are ordered by R and then stable resource ID "
        "for reproducible display; this does not break their shared rank.",
    ])
    for track, anchor in TRACKS.items():
        selected = ordered([row for row in rows if row["track"] == track], "scientific_score")
        parts.extend([
            "<details>", f"<summary>{text(track)} — all {len(selected)} ranking rows</summary>",
            "### Scores and ranks",
            f"<!-- all-scores: {anchor} -->",
            table(["Resource", "R", "L", "Q", "X", "M", "Science rank", "Science / 100", "Near-term rank", "Near-term / 100"],
                  [[link(r), *(r[k] for k in COMPONENTS), r["scientific_rank"], number(r["scientific_score"]),
                    r["practical_rank"] or "Not eligible", number(r["practical_score"])] for r in selected]),
            f"<!-- /all-scores: {anchor} -->",
            "### Endpoint and denominator context",
            table(["Resource", "Endpoint / tier", "N for size score", "Reported N", "Denominator scope", "Access route / judgment"],
                  [[link(r), text(r["endpoint"]) + "<br>" + text(r["tier"]), text(r["n_supported"]),
                    text(r["reported_n"]), scope(r), text(r["access"]) + "<br>" + text(r["basis"])] for r in selected]),
            "Image and individual-label availability are recorded separately on each linked resource page. "
            "An access category alone does not confirm those files or a right to link records.",
            "</details>",
        ])
    parts.extend([
        '<a id="reproduce"></a>', "## Reproduce",
        "The renderer uses **Python 3.9+ standard library only**. No plotting dependencies or network "
        "access are needed. From the repository root:",
        "```bash\npython scripts/build_rankings.py\n```",
        "To use another release while retaining the repository's stable resource pages:",
        "```bash\npython scripts/build_rankings.py --input-dir /path/to/library/output\n```",
        "The command reads `master.csv` and `rankings.csv`, checks unique pairs, resource names/pages, "
        "exclusion status, component formulas, rank ties/order, exported near-term gate conditions "
        "and sample-size scope, then overwrites only this page. It preserves the manually curated "
        "endpoint-readiness decision; it does not infer new readiness from the numeric score. "
        "Run the library's full verifier when changing the curation or ranking inputs.",
        "Plotting is separate and optional: "
        "[`requirements-stats.txt`](requirements-stats.txt) pins the matplotlib version used to "
        "build the [statistics figures](STATS.md). It is not required for this ranking page.",
        table(["Input CSV", "SHA-256"], [
            [f"[{name}](library/output/{name})", "`" + hashlib.sha256((input_dir / name).read_bytes()).hexdigest() + "`"]
            for name in ("master.csv", "rankings.csv")
        ]),
    ])
    return "\n\n".join(parts) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=ROOT / "library" / "output")
    args = parser.parse_args()
    rows, master = load(args.input_dir)
    result = render(rows, master, args.input_dir)
    (ROOT / "RANKINGS.md").write_text(result, encoding="utf-8")
    print(f"Wrote RANKINGS.md: {len(rows)} pairs, {len({r['id'] for r in rows})} resource records")
    for track in TRACKS:
        selected = [row for row in rows if row["track"] == track]
        top = [row for row in selected if int(row["scientific_rank"]) <= 3]
        near = [row for row in selected if row["near_term"] == "Yes"]
        print(f"  {track}: {len(selected)} total, {len(top)} scientific ranks 1–3 (including ties), {len(near)} near-term")


if __name__ == "__main__":
    main()
