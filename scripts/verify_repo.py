#!/usr/bin/env python3
"""Read-only, offline acceptance audit of the GitHub release (Python 3.9+).

This checks the exported package against its CSVs, rather than regenerating it.
It also runs library/src/verify.py, which independently audits the frozen inputs,
database, evidence, eligibility, and scoring. No network or third-party packages.
Frozen upstream Markdown under library/inputs is intentionally not link-audited.
"""
import argparse
import csv
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from decimal import Decimal
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

RELEASE = {"resources": 479, "baseline": 451, "ranked_pairs": 83,
           "metadata_as_of": "2026-11-03"}
CLINICAL = "age sex hypertension diabetes cardiovascular stroke_type stroke_time brain_mri csvd ad dementia cognition parkinson frailty health mortality followup".split()
TIERS = ("Tier 1", "Tier 2", "Tier 3", "Unknown", "Excluded")
STATUSES = ("Confirmed", "Uncertain", "Not available")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def unfence(source):
    """Remove code blocks, preserving line numbers for useful diagnostics."""
    lines, fence = [], None
    for line in source.splitlines(keepends=True):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            lines.append("\n" if line.endswith("\n") else "")
        elif fence is None:
            lines.append(line)
        else:
            lines.append("\n" if line.endswith("\n") else "")
    return "".join(lines)


def plain(value):
    value = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"<[^>]*>", "", value)
    value = re.sub(r"\\([\\`*_{}\[\]()<>|#!])", r"\1", value)
    return html.unescape(value.replace("**", "").replace("`", "")).strip()


class HTMLReferences(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links, self.anchors = [], set()

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if value is None:
                continue
            if key == "id" or (tag == "a" and key == "name"):
                self.anchors.add(value)
            if key in ("src", "href"):
                self.links.append((value, self.getpos()[0]))

    handle_startendtag = handle_starttag


def destination(value):
    """Read a Markdown destination, including balanced parentheses or <...>."""
    value = value.lstrip()
    if value.startswith("<"):
        end = value.find(">")
        return value[1:end] if end >= 0 else None
    chars, depth, escaped = [], 0, False
    for char in value:
        if escaped:
            chars.append(char)
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == "(" :
            depth += 1
            chars.append(char)
        elif char == ")":
            if depth == 0:
                break
            depth -= 1
            chars.append(char)
        elif char.isspace() and depth == 0:
            break
        else:
            chars.append(char)
    return "".join(chars)


def references(source, markdown=True):
    body = unfence(source) if markdown else source
    # Inline code is not a live hyperlink. Keep heading code text separately below.
    link_body = re.sub(r"(`+)([^`\n]*?)\1", "", body) if markdown else body
    parser = HTMLReferences()
    parser.feed(link_body)
    links = list(parser.links)
    if markdown:
        for match in re.finditer(r"(?<!\\)\]\(", link_body):
            target = destination(link_body[match.end():])
            if target is not None:
                links.append((target, link_body.count("\n", 0, match.start()) + 1))
        definitions = {}
        for match in re.finditer(r"(?m)^\s{0,3}\[([^\]]+)\]:\s*(.+)$", link_body):
            target = destination(match.group(2))
            if target is not None:
                definitions[match.group(1).casefold()] = target
                links.append((target, link_body.count("\n", 0, match.start()) + 1))
        for match in re.finditer(r"(?<!\\)\[([^\]\n]+)\]\[([^\]\n]*)\]", link_body):
            key = (match.group(2) or match.group(1)).casefold()
            require(key in definitions, "Undefined Markdown reference: " + key)
    anchors = set(parser.anchors)
    if markdown:
        used = Counter()
        headings = []
        lines = body.splitlines()
        for i, line in enumerate(lines):
            atx = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
            if atx:
                headings.append(atx.group(1))
            elif i and re.fullmatch(r"\s{0,3}(?:=+|-+)\s*", line) and lines[i - 1].strip():
                headings.append(lines[i - 1])
        for heading in headings:
            value = plain(heading).lower().replace("*", "")
            # GitHub heading slugs preserve Unicode letters/numbers, '_' and '-'.
            slug = "".join(c for c in value if c in "_- " or unicodedata.category(c)[0] in "LNM").replace(" ", "-")
            base = slug
            if used[base]:
                slug += "-" + str(used[base])
            used[base] += 1
            anchors.add(slug)
    return links, anchors


def check_local_links(repo, paths):
    checked, external, github_routes = 0, 0, 0
    anchor_cache, errors = {}, []
    for path in paths:
        try:
            links, anchors = references(path.read_text(encoding="utf-8"), path.suffix == ".md")
        except ValueError as exc:
            errors.append(str(path.relative_to(repo)) + ": " + str(exc))
            continue
        anchor_cache[path] = anchors
        for target, line in links:
            target = html.unescape(target)
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                external += 1
                continue
            route = unquote(parsed.path)
            # These routes exist on GitHub, rather than in a downloaded repository.
            if re.fullmatch(r"/?(?:\.\./)*issues(?:/(?:new|new/choose|[0-9]+))?/?", route):
                github_routes += 1
                continue
            dest = (repo / route.lstrip("/") if route.startswith("/") else path.parent / route).resolve() if route else path
            checked += 1
            label = str(path.relative_to(repo)) + ":" + str(line) + " -> " + target
            if not dest.is_relative_to(repo) or not dest.exists():
                errors.append(label + " (missing/outside repository)")
                continue
            if parsed.fragment:
                if dest.is_dir():
                    dest = dest / "README.md"
                if dest.suffix not in (".md", ".html", ".svg"):
                    continue  # PDF/media fragments do not use Markdown heading IDs.
                if dest not in anchor_cache:
                    _, anchor_cache[dest] = references(dest.read_text(encoding="utf-8"), dest.suffix == ".md")
                fragment = html.unescape(unquote(parsed.fragment))
                # GitHub prepends user-content- to authored IDs in rendered Markdown.
                alternatives = {fragment}
                if fragment.startswith("user-content-"):
                    alternatives.add(fragment[len("user-content-"):])
                if not alternatives & anchor_cache[dest]:
                    errors.append(label + " (missing anchor)")
    require(not errors, "Local link errors:\n" + "\n".join(errors[:40]))
    return {"authored_documents": len(paths), "local_links_checked": checked,
            "external_links_not_fetched": external, "github_issue_routes_skipped": github_routes}


def resource_links(source):
    return re.findall(r"\]\((?:\.\./)*datasets/([A-Za-z0-9_-]+)\.md(?:#[^)]*)?\)", source)


def section(source, heading):
    found = re.search(r"(?m)^## " + re.escape(heading) + r"\s*$", source)
    require(found is not None, "Missing section: " + heading)
    tail = source[found.end():]
    return re.split(r"(?m)^## ", tail, maxsplit=1)[0]


def check_pages(repo, master, topics):
    ids = {r["id"] for r in master}
    pages = {p.stem for p in (repo / "datasets").glob("*.md")}
    require(pages == ids, "Dataset page/CSV ID mismatch: " + str(sorted(pages ^ ids)))
    for row in master:
        source = (repo / "datasets" / (row["id"] + ".md")).read_text(encoding="utf-8")
        normalized = plain(source)
        require("Metadata as of " + RELEASE["metadata_as_of"] in source, row["id"] + ": missing snapshot date")
        require("| Stable resource ID | " + row["id"] + " |" in normalized, row["id"] + ": incorrect page ID")
        require("| Review depth | " + row["review_depth"] + " |" in normalized, row["id"] + ": review-depth mismatch")
        if row["review_depth"] == "Source-reviewed":
            overview = plain(section(source, "Overview"))
            require(row["modalities"] in overview and row["image_access"] in overview,
                    row["id"] + ": reviewed overview omits current image scope")
    index = (repo / "catalog/README.md").read_text(encoding="utf-8")
    ordered = resource_links(index)
    require(len(ordered) == len(ids) and set(ordered) == ids, "A–Z index must link each resource once")
    expected = [r["id"] for r in sorted(master, key=lambda r: (r["name"].casefold(), r["id"]))]
    require(ordered == expected, "A–Z index is not alphabetical")
    reviewed = resource_links((repo / "catalog/reviewed.md").read_text(encoding="utf-8"))
    require(Counter(reviewed) == Counter(r["id"] for r in master if r["review_depth"] == "Source-reviewed"), "Reviewed index differs from CSV")
    excluded = section((repo / "catalog/excluded.md").read_text(encoding="utf-8"), "Resource-level exclusions")
    require(Counter(resource_links(excluded)) == Counter(r["id"] for r in master if r["best_tier"] == "Excluded"), "Exclusion index differs from CSV")
    for topic in "ABCDEFG":
        source = (repo / "catalog/topics" / (topic + ".md")).read_text(encoding="utf-8")
        for tier in TIERS:
            expected = [r["id"] for r in topics if r["topic"] == topic and r["tier"] == tier]
            require(tier + " — " + str(len(expected)) in source, topic + ": wrong topic count " + tier)
            if tier != "Unknown":
                require(Counter(resource_links(section(source, tier))) == Counter(expected), topic + ": incorrect membership for " + tier)


def check_statistics(repo, master, topics, phenotypes):
    stats = json.loads((repo / "assets/stats/data.json").read_text(encoding="utf-8"))
    included = {r["id"] for r in master if r["best_tier"] != "Excluded"}
    reviewed = {r["id"] for r in master if r["review_depth"] == "Source-reviewed"}
    clinical = included & reviewed
    counts = {
        "all_resource_records": len(master),
        "baseline_records": sum(r["origin"] == "EyeDataHub v0.7.0" for r in master),
        "extension_records": sum(r["origin"] != "EyeDataHub v0.7.0" for r in master),
        "included_resource_records": len(included),
        "excluded_resource_records": len(master) - len(included),
        "source_reviewed_all": len(reviewed), "source_reviewed_included": len(clinical),
        "source_reviewed_excluded": len(reviewed - included),
        "catalog_screen_included": len(included - reviewed),
    }
    require(stats["counts"] == counts, "Statistics headline counts differ from master.csv")
    for key, expected in (("included_resource_ids", included), ("clinical_denominator_ids", clinical)):
        require(len(stats[key]) == len(expected) and set(stats[key]) == expected, "Incorrect statistics denominator: " + key)
    require(stats["latest_resource_check_date"] == max(r["checked"] for r in master), "Statistics date stale")
    for name in ("master.csv", "topics.csv", "phenotypes.csv"):
        digest = hashlib.sha256((repo / "library/output" / name).read_bytes()).hexdigest()
        require(stats["source_sha256"][name] == digest, "Statistics input SHA256 stale: " + name)
    tiers = Counter(r["best_tier"] for r in master if r["id"] in included)
    require(stats["included_best_tier"] == dict(tiers), "Statistics best-tier counts disagree")
    require({r["topic"] for r in stats["topic_tiers"]} == set("ABCDEFG"), "Missing statistics topic")
    for row in stats["topic_tiers"]:
        observed = Counter(r["tier"] for r in topics if r["id"] in included and r["topic"] == row["topic"])
        require(all(row[t] == observed[t] for t in TIERS) and sum(row[t] for t in TIERS) == len(included), "Topic statistics/denominator mismatch: " + row["topic"])
    observed = Counter(r["access"] for r in master if r["id"] in included)
    require({r["access"]: r["count"] for r in stats["access_routes"]} == dict(observed), "Access statistics differ")
    for row in stats["access_routes"]:
        require(row["percent"] == round(row["count"] * 100 / len(included), 1), "Access percentage denominator mismatch")
    require({r["field"] for r in stats["clinical_statuses"]} == set(CLINICAL), "Clinical statistics field coverage differs")
    for row in stats["clinical_statuses"]:
        observed = Counter(r["status"] for r in phenotypes if r["id"] in clinical and r["field"] == row["field"])
        require(all(row[s] == observed[s] for s in STATUSES) and sum(row[s] for s in STATUSES) == len(clinical), "Clinical statistics/denominator mismatch: " + row["field"])
    expected_exclusions = reviewed - included
    require({r["id"] for r in stats["source_reviewed_exclusions"]} == expected_exclusions, "Reviewed exclusions differ")
    for item in stats.get("geometric_checks", []):
        require(not any(item[key] for key in ("text_overlaps", "out_of_bounds_text", "text_spine_overlaps")), "Reported figure geometry issue: " + item["name"])
    for name in ("topic_tiers", "access_routes", "clinical_statuses"):
        for ext in ("png", "svg"):
            require((repo / "assets/stats" / (name + "." + ext)).stat().st_size > 100, "Missing/empty statistical figure")
    return counts, tiers, stats


def check_text_counts(repo, counts, tiers, stats):
    # Check labeled assertions rather than the mere presence of a numeral elsewhere.
    english = (repo / "README.md").read_text(encoding="utf-8")
    assertions = [
        (r"(\d+) resource records", counts["all_resource_records"]),
        (r"(\d+) included resources", counts["included_resource_records"]),
        (r"(\d+) source-reviewed records", counts["source_reviewed_all"]),
        (r"(\d+) baseline \+", counts["baseline_records"]),
        (r"\+ (\d+) additions", counts["extension_records"]),
        (r"(\d+) included ·", counts["source_reviewed_included"]),
        (r"· (\d+) excluded", counts["source_reviewed_excluded"]),
        (r"other (\d+) records", counts["excluded_resource_records"]),
        (r"(\d+) catalog-screened records", counts["all_resource_records"] - counts["source_reviewed_all"]),
        (r"(\d+) research topics", 7),
    ] + [(r"(\d+) " + re.escape(tier) + r"\b", count) for tier, count in tiers.items()]
    for pattern, expected in assertions:
        matches = re.findall(pattern, english)
        require(matches and all(int(x) == expected for x in matches), "README numeric claim differs: " + pattern)
    chinese = (repo / "README.zh-CN.md").read_text(encoding="utf-8")
    assertions = [
        (r"全部资源记录 \| (\d+)", counts["all_resource_records"]),
        (r"的\s*(\d+)条原始记录", counts["baseline_records"]),
        (r"\+ (\d+)条补充", counts["extension_records"]),
        (r"纳入研究范围 \| (\d+)", counts["included_resource_records"]),
        (r"排除记录 \| (\d+)", counts["excluded_resource_records"]),
        (r"来源深度核验 \| (\d+)", counts["source_reviewed_all"]),
        (r"其中(\d+)条纳入", counts["source_reviewed_included"]),
        (r"、(\d+)条排除", counts["source_reviewed_excluded"]),
        (r"其余(\d+)条为目录筛查", counts["all_resource_records"] - counts["source_reviewed_all"]),
    ] + [(re.escape(tier) + r"为(\d+)", count) for tier, count in tiers.items()]
    for pattern, expected in assertions:
        matches = re.findall(pattern, chinese)
        require(matches and all(int(x) == expected for x in matches), "Chinese README numeric claim differs: " + pattern)
    source = (repo / "STATS.md").read_text(encoding="utf-8")
    cells = [list(map(plain, re.split(r"(?<!\\)\|", line)[1:-1])) for line in source.splitlines() if line.startswith("|")]
    table = {row[0]: row[1:] for row in cells if row}
    labels = {"All catalog records": "all_resource_records", "EyeDataHub v0.7.0 baseline records": "baseline_records",
              "Additional records": "extension_records", "Included (best_tier != Excluded)": "included_resource_records",
              "Separate exclusion records": "excluded_resource_records", "Source-reviewed, all records": "source_reviewed_all",
              "Source-reviewed and included": "source_reviewed_included", "Source-reviewed and excluded": "source_reviewed_excluded",
              "Catalog-screened and included": "catalog_screen_included"}
    for label, field in labels.items():
        require(table.get(label) == [str(counts[field])], "STATS scope table differs: " + label)
    for tier, count in tiers.items():
        require(table.get(tier) == [str(count)], "STATS best-tier table differs")
    for row in stats["topic_tiers"]:
        require(table.get(row["topic"] + ": " + row["label"]) == [str(row[t]) for t in TIERS], "STATS topic table differs")
    for row in stats["access_routes"]:
        require(table.get(row["access"]) == [str(row["count"]), str(row["percent"]) + "%"], "STATS access table differs")
    for row in stats["clinical_statuses"]:
        require(table.get(row["label"]) == [str(row[s]) for s in STATUSES], "STATS clinical table differs")


def check_images(repo, ids):
    manifest = json.loads((repo / "assets/examples/manifest.json").read_text(encoding="utf-8"))
    gallery = (repo / "assets/examples/README.md").read_text(encoding="utf-8")
    assets = manifest["assets"]
    paths, resource_ids = set(), set()
    for item in assets:
        require(item["resource_id"] in ids, "Example has unknown resource ID")
        path = (repo / item["path"]).resolve()
        require(path.is_relative_to(repo / "assets/examples") and path.is_file(), "Unsafe/missing example path")
        require(path not in paths, "Duplicate example asset path")
        paths.add(path)
        resource_ids.add(item["resource_id"])
        payload = path.read_bytes()
        require(hashlib.sha256(payload).hexdigest() == item["sha256"], "Example SHA256 mismatch: " + item["path"])
        require(len(payload) == item["bytes"], "Example byte count mismatch: " + item["path"])
        card = (repo / "datasets" / (item["resource_id"] + ".md")).read_text(encoding="utf-8")
        for document, title in ((gallery, "gallery"), (card, item["resource_id"])):
            rendered = plain(document)
            for key in ("attribution", "what_image_shows", "kind"):
                require(item[key] in rendered, title + ": missing example " + key)
            require(item["license_url"] in document and path.name in document, title + ": missing sample/license link")
    for item in manifest.get("additional_example_entries", []):
        require(item["resource_id"] in ids and item["source_url"] in gallery, "Additional example entry missing/unknown")
    unlisted = {p.resolve() for p in (repo / "assets/examples").iterdir() if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".tif", ".tiff", ".webp")} - paths
    require(not unlisted, "Local image files absent from attribution manifest: " + str(unlisted))
    return {"image_assets_hashed": len(paths), "resources_with_local_examples": len(resource_ids)}


def check_rankings(repo, rankings):
    require(len(rankings) == RELEASE["ranked_pairs"], "Ranked-pair count changed; review this release contract")
    pairs = {(r["track"], r["id"]) for r in rankings}
    require(len(pairs) == len(rankings), "Duplicate ranked track/resource pair")
    tracks = {"Retinal Aging": "retinal-aging", "Eye–Stroke": "eye-stroke", "Eye–Neurodegeneration": "eye-neurodegeneration"}
    require({r["track"] for r in rankings} == set(tracks), "Unexpected ranking tracks")
    source = (repo / "RANKINGS.md").read_text(encoding="utf-8")
    require(set(resource_links(source)) == {r["id"] for r in rankings}, "Ranking page resource set differs from CSV")
    for track, slug in tracks.items():
        rows = {r["id"]: r for r in rankings if r["track"] == track}
        for kind in ("all-scores", "scientific-top", "near-term"):
            match = re.search(r"<!-- " + kind + ": " + slug + r" -->(.*?)<!-- /" + kind + ": " + slug + r" -->", source, re.S)
            require(match is not None, "Missing ranking block: " + kind + "/" + track)
            block = match.group(1)
            expected = set(rows) if kind == "all-scores" else {rid for rid, r in rows.items() if (int(r["scientific_rank"]) <= 3 if kind == "scientific-top" else r["near_term"] == "Yes")}
            require(Counter(resource_links(block)) == Counter(expected), "Ranking membership/ties differ: " + kind + "/" + track)
            if not expected:
                require("No pair passes the current near-term gates" in block, "Empty ranking needs an explicit scope statement")
            for line in block.splitlines():
                linked = resource_links(line)
                if not linked:
                    continue
                require(len(linked) == 1, "Ambiguous ranking table row")
                row = rows[linked[0]]
                cells = [plain(x) for x in re.split(r"(?<!\\)\|", line)[1:-1]]
                if kind == "all-scores":
                    expected_numbers = [row[key] for key in ("R", "L", "Q", "X", "M", "scientific_rank", "scientific_score")]
                    require(len(cells) == 10 and all(Decimal(actual) == Decimal(wanted) for actual, wanted in zip(cells[1:8], expected_numbers)), "Ranking components/scores changed: " + linked[0])
                    require(cells[8] == (row["practical_rank"] or "Not eligible") and Decimal(cells[9]) == Decimal(row["practical_score"]), "Ranking near-term rank/score changed: " + linked[0])
                else:
                    prefix = "scientific" if kind == "scientific-top" else "practical"
                    require(cells[0] == row[prefix + "_rank"] and Decimal(cells[2]) == Decimal(row[prefix + "_score"]), "Ranking summary rank/score changed: " + linked[0])
    # The library verifier separately audits eligibility, exact component scores,
    # independent weighted arithmetic, ties, and the near-term filter.
    return {"ranked_track_resource_pairs": len(pairs),
            "near_term_by_track": dict(Counter(r["track"] for r in rankings if r["near_term"] == "Yes"))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--skip-library", action="store_true", help="Only when library/src/verify.py has been run separately")
    args = parser.parse_args()
    repo = args.repo.resolve()
    out = repo / "library/output"
    master, topics, phenotypes, rankings = [read_csv(out / (name + ".csv")) for name in ("master", "topics", "phenotypes", "rankings")]
    ids = {r["id"] for r in master}
    require(len(ids) == len(master) == RELEASE["resources"], "Resource count/uniqueness changed; review release contract")
    require(sum(r["origin"] == "EyeDataHub v0.7.0" for r in master) == RELEASE["baseline"], "Baseline count changed")
    check_pages(repo, master, topics)
    counts, tiers, stats = check_statistics(repo, master, topics, phenotypes)
    check_text_counts(repo, counts, tiers, stats)
    image_report = check_images(repo, ids)
    ranking_report = check_rankings(repo, rankings)
    paths = sorted(p for p in repo.rglob("*.md") if not p.is_relative_to(repo / "library/inputs") and ".git" not in p.relative_to(repo).parts)
    paths += sorted(p for p in repo.rglob("*.html") if not p.is_relative_to(repo / "library/inputs") and ".git" not in p.relative_to(repo).parts)
    link_report = check_local_links(repo, paths)
    if not args.skip_library:
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        result = subprocess.run([sys.executable, str(repo / "library/src/verify.py")], cwd=repo, env=env, text=True, capture_output=True)
        require(result.returncode == 0, "Library audit failed:\n" + result.stdout + result.stderr)
        print(result.stdout.strip())
    print(json.dumps({"status": "PASS", "offline": True, "metadata_as_of": RELEASE["metadata_as_of"],
                      "resource_pages": len(ids), "counts": counts, **ranking_report, **image_report,
                      **link_report, "library_audit": "skipped by explicit option" if args.skip_library else "passed"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as error:
        print("FAIL: " + str(error), file=sys.stderr)
        sys.exit(1)
