"""Read-only, offline release audit. Run from any directory with Python 3."""
import argparse
import csv
import hashlib
import json
import re
import sqlite3
import sys
import tarfile
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
INPUT, OUT = ROOT / "inputs", ROOT / "output"
BASE = INPUT / "v0.7.0"
FIELDS = "age sex hypertension diabetes cardiovascular stroke_type stroke_time brain_mri csvd ad dementia cognition parkinson frailty health mortality followup".split()
TRACKS = {"Age": "Retinal Aging", "Stroke": "Eye–Stroke", "Neuro": "Eye–Neurodegeneration"}
TARGET_FIELDS = {
    "Age": set("age sex diabetes hypertension cardiovascular mortality health followup".split()),
    "Stroke": set("stroke_type stroke_time brain_mri csvd age sex hypertension diabetes mortality followup".split()),
    "Neuro": set("ad dementia cognition parkinson brain_mri age sex followup".split()),
}
SCOPES = {"Study-linked participants", "Outcome-positive subset (lower bound)"}
REQUIRED = set("master topics phenotypes evidence relationships extensions_relationships rankings identity quantities access_audit excluded search_log pubmed_hits".split())
SEEDS = set("ext-uk-biobank ext-nhanes-2005-2008-retina brset odir2019 ext-areds ext-areds2".split())


def check(ok, message):
    if not ok:
        raise ValueError(message)


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def rows(path, delimiter=","):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream, delimiter=delimiter))


def keyed(items, keys):
    if isinstance(keys, str):
        result = {a[keys]: a for a in items}
    else:
        result = {tuple(a[k] for k in keys): a for a in items}
    check(len(result) == len(items), f"Duplicate key(s) {keys}")
    return result


def digest(data):
    return hashlib.sha256(data).hexdigest()


def snapshot(require_archive=False):
    m = read(BASE / "manifest.json")
    check((m["tag"], m["commit"], m["record_count"]) ==
          ("v0.7.0", "0ce7144459a41e8be255fed7fa62c30416613e6b", 451), "Incorrect pinned upstream release")
    tar = INPUT / "EyeDataHub-v0.7.0.tar.gz"
    check(m["archive_sha256"] == "66235c429b87bf90f4618480e92e39207f227ee38d234358cd8a4ce97a5227c7",
          "Original archive provenance changed")
    for name, expected in m["files"].items():
        check(digest((BASE / name).read_bytes()) == expected, f"Baseline manifest: {name}")
    check(not require_archive or tar.is_file(), "Original archive requested but not present (not bundled)")
    if tar.exists():
        check(digest(tar.read_bytes()) == m["archive_sha256"], "Archive SHA-256 mismatch")
        with tarfile.open(tar, "r:gz") as archive:
            members = {v.name.split("/", 1)[-1]: v for v in archive.getmembers() if v.isfile()}
            for name, expected in m["files"].items():
                check(name in members and digest(archive.extractfile(members[name]).read()) == expected,
                      f"Baseline archive: {name}")
    saved = read(BASE / "hub/catalog.json")
    catalog = saved["records"]
    original = rows(BASE / "hub/catalog.csv")
    check(len(original) == len(catalog) == saved["record_count"] == 451, "Baseline row count")
    check(saved["catalog_version"] == "0.7.0", "Wrong baseline catalog version")
    for a, b in zip(original, catalog):
        check(a.keys() == b.keys(), f"Baseline schema mismatch: {b['record_id']}")
        for k, v in b.items():
            actual = json.loads(a[k]) if isinstance(v, (list, dict)) else a[k]
            expected = v if isinstance(v, (list, dict)) else "" if v is None else str(v)
            check(actual == expected, f"Baseline CSV vs JSON: {b['record_id']}.{k}")
    side = read(INPUT / "supplement/manifest.json")
    check(digest((INPUT / "supplement" / side["file"]).read_bytes()) == side["sha256"], "Date supplement SHA-256")
    return keyed(catalog, "record_id")


def text(v):
    return "" if v is None else str(v)


def tables():
    paths = sorted(OUT.glob("*.csv"))
    check(REQUIRED <= {p.stem for p in paths}, "Missing expected CSV")
    data = {p.stem: rows(p) for p in paths}
    with sqlite3.connect((OUT / "resources.sqlite").as_uri() + "?mode=ro", uri=True) as db:
        check(db.execute("pragma integrity_check").fetchone() == ("ok",), "SQLite integrity error")
        names = {r[0] for r in db.execute("select name from sqlite_master where type='table'")}
        check(names == set(data), "CSV/SQLite table list differs")
        for name, items in data.items():
            check(bool(items), "Empty CSV: " + name)
            cur = db.execute('select * from "' + name.replace('"', '""') + '"')
            cols = list(items[0])
            check(cols == [col[0] for col in cur.description], "CSV/SQLite headers: " + name)
            def sql_value(col, val):
                if name == "rankings" and col in ("scientific_score", "practical_score"):
                    return float(val)
                return text(val)
            csv_values = Counter(tuple(sql_value(k, r[k]) for k in cols) for r in items)
            sql_values = Counter(tuple(sql_value(k, v) for k, v in zip(cols, r)) for r in cur)
            check(csv_values == sql_values, "CSV/SQLite data mismatch: " + name)
    return data


def graph(base, data, master):
    identity = keyed(data["identity"], "record_id")
    check(identity.keys() == base.keys(), "Baseline identity coverage")
    families = defaultdict(set)
    for i, b in base.items():
        fam = b["dataset_family_id"]
        families[fam].add(i)
        check(master[i]["upstream_family"] == identity[i]["dataset_family_id"] == fam,
              "Family mismatch: " + i)
    check(len(families) == 446, "Pinned upstream family count")
    edges = data["relationships"]
    check(len(edges) == 145, "Pinned upstream directed edge count")
    keyed(edges, ("source_record_id", "relationship_type", "target_record_id"))
    incoming, outgoing = defaultdict(set), defaultdict(set)
    for r in edges:
        src, dst = r["source_record_id"], r["target_record_id"]
        check(src in base and dst in base and r["evidence_url"], f"Invalid upstream edge {src}/{dst}")
        outgoing[src].add(dst)
        incoming[dst].add(src)
    for i, row in identity.items():
        members = set(row["dataset_family_members"].split("|"))
        check(members == families[row["dataset_family_id"]] and int(row["dataset_family_member_count"]) == len(members), "Family membership: " + i)
        for field, expected in (("outgoing_relationship_targets", outgoing[i]), ("incoming_relationship_sources", incoming[i])):
            check(set(filter(None, row[field].split("|"))) == expected, f"Identity graph mismatch: {i}.{field}")
    manual = data["extensions_relationships"]
    check(manual == read(INPUT / "relationships.json"), "Manual relationship ledger differs from inputs")
    keyed(manual, ("source_id", "relation", "target_id"))
    for r in manual:
        check({r["source_id"], r["target_id"]} <= master.keys() and bool(r["status"]) and
              urlsplit(r["evidence_url"]).scheme in ("http", "https"), f"Invalid manual edge {r}")
    for name, prefix in (("identity", "resource_identity_review"), ("relationships", "resource_relationship_edges"),
                         ("quantities", "resource_quantity_evidence"), ("access_audit", "access_verification_log")):
        source = next((BASE / "hub/audit").glob(prefix + "*.csv"))
        check(data[name] == rows(source), "Preserved audit differs from original: " + name)


def verify_refs(owner, packed, evidence, optional=False):
    if optional and packed == "Unknown":
        return
    for ref in packed.split(" | "):
        check(ref in evidence and evidence[ref]["id"] == owner, f"Unresolved/wrong-owner citation: {owner} -> {ref}")


def facts(data, master, gates):
    e = keyed(data["evidence"], "evidence_id")
    topic = keyed(data["topics"], ("id", "topic"))
    pheno = keyed(data["phenotypes"], ("id", "field"))
    check(all(v["id"] in master and key.startswith(v["id"]+"#") and v["locator"].strip() and
              urlsplit(v["url"]).scheme in ("http","https") for key, v in e.items()), "Invalid evidence ledger entry")
    check(set(topic) == {(i,k) for i in master for k in "ABCDEFG"}, "A–G matrix coverage")
    check({(i,k) for i in master for k in FIELDS} <= pheno.keys() and all(i in master for i,_ in pheno), "Phenotype matrix coverage")
    for (i,k), v in pheno.items():
        check(v["status"] in ("Confirmed","Uncertain","Not available") and bool(v["scope"]), f"Bad phenotype {i}/{k}")
        verify_refs(i, v["evidence_id"], e, optional=v["status"]=="Uncertain")
        if k in FIELDS:
            check(master[i][k] == v["status"], f"Master/long phenotype mismatch: {i}/{k}")
    for (i,k), v in topic.items():
        before = v["reviewed_tier_before_pixel_gate"]
        after = "Tier 2" if before=="Tier 1" and k in gates.get(i,{}).get("topics",[]) else before
        check(before in {"Unknown","Excluded","Tier 1","Tier 2","Tier 3"} and v["tier"] == after == master[i]["topic_"+k],
              f"Tier or pixel gate mismatch: {i}/{k}")
        verify_refs(i, v["evidence_id"], e, optional=after=="Unknown")
    for i, row in master.items():
        tiers = sorted(t["tier"] for k in "ABCDEFG" if (t:=topic[(i,k)])["tier"].startswith("Tier "))
        check(row["best_tier"] == (tiers[0] if tiers else "Excluded"), "Best tier: "+i)
    check(set(keyed(data["excluded"],"id")) == {i for i,r in master.items() if r["best_tier"]=="Excluded"}, "Exclusion list mismatch")
    return e, topic, pheno


def curated_facts(curated, evidence, topics, phenotypes):
    tier_labels=("Excluded","Tier 1","Tier 2","Tier 3")
    for i, review in curated.items():
        for key, (url, locator) in review["sources"].items():
            result=evidence[i+"#"+key]
            check((result["url"],result["locator"])==(url,locator), f"Changed curated evidence: {i}#{key}")
            if key in review.get("source_review_dates",{}):
                check(result["checked"]==review["source_review_dates"][key],
                      f"Lost targeted source review date: {i}#{key}")
        for collection, table in (("topics",topics),("phenotypes",phenotypes)):
            for key, (value, ref, note) in review[collection].items():
                result=table[i,key]
                raw_tokens=[ref] if ref in review["sources"] else re.split(r"[ ,;+/|]+",ref.strip())
                expected=" | ".join(i+"#"+t for t in raw_tokens)
                check(result["evidence_id"]==expected, f"Lost original evidence reference: {i}/{key}")
                if collection=="topics":
                    check(result["reviewed_tier_before_pixel_gate"]==tier_labels[value] and
                          (result["reason"]==note or result["reason"].startswith(note+" | Pixel gate: ")),
                          f"Lost topic curation: {i}/{key}")
                else:
                    check((result["status"],result["scope"])==(value,note),f"Lost phenotype curation: {i}/{key}")


def rankings(data, master, e, topic, pheno):
    targets = keyed(rows(INPUT / "score_targets.tsv", "\t"), ("id","track"))
    profiles = keyed(rows(INPUT / "score_profiles.tsv", "\t"), "id")
    omitted = read(INPUT / "score_label_omissions.json")
    ranking = keyed(data["rankings"], ("id","track"))
    check(set(ranking) == {(i,TRACKS[track]) for i,track in targets}, "Ranking ledger differs from target selection")
    for (i,tr), a in targets.items():
        row = ranking[(i,TRACKS[tr])]
        p = profiles[i]
        scope = a["n_scope"]
        n = int(a["n_supported"] or 0)
        supported = n if scope in SCOPES else 0
        check(i in master and bool(a["endpoint"]) and bool(a["n_basis"]) and scope in SCOPES|{"Unknown","Cohort or batch only"}, "Invalid target: "+i)
        check((row["reported_n"],row["n_supported"],row["n_scope"],row["paired_n_basis"],row["endpoint"]) ==
              (str(n) if n else "Unknown",str(supported) if supported else "Unknown",scope,a["n_basis"],a["endpoint"]), "Ranking n_scope / denominator mismatch: "+i)
        fields = sorted(k for k in TARGET_FIELDS[tr] if pheno[(i,k)]["status"]=="Confirmed" and k not in omitted.get(i,{}).get(tr,[]))
        rel, lab = int(a["relevance"]), min(4,(len(fields)+1)//2)
        task_followup = (pheno[(i,"followup")]["status"]=="Confirmed" and
                         "followup" not in omitted.get(i,{}).get(tr,[]))
        quality = min(4,int(p["population"])+int(p["qc"])+(supported>=100)+(supported>=1000)+task_followup)
        access, multi = int(p["access"]), int(p["multi"])
        check([int(row[k]) for k in ("R","L","Q","X","M")] == [rel,lab,quality,access,multi] and
              row["label_fields"]==(" | ".join(fields) or "None confirmed"), "Ranking dimensions: "+i)
        science=(40*rel+25*lab+25*quality+10*multi)/4
        practical=(25*rel+15*lab+10*quality+45*access+5*multi)/4
        check((float(row["scientific_score"]),float(row["practical_score"])) == (science,practical), "Ranking weights: "+i)
        tiers = {k:topic[(i,k)]["tier"] for k in a["topics"] if topic[(i,k)]["tier"]!="Unknown"}
        check(any(t in ("Tier 1","Tier 2") for t in tiers.values()), "Ranking requires Tier 1/2: "+i)
        rendered=" / ".join(k+" T"+("0" if t=="Excluded" else t.split()[-1]) for k,t in tiers.items())
        check(row["tier"]==rendered, "Ranking displayed tier differs from effective pixel tier: "+i)
        ready = tr in p["ready_tracks"].split(",") and "Tier 1" in tiers.values() and rel>=3 and access>=3
        check(row["near_term"]==("Yes" if ready else "No") and bool(row["practical_rank"])==ready, "Practical eligibility: "+i)
        verify_refs(i,row["evidence"],e)
    for tr in TRACKS.values():
        cohort = [r for r in data["rankings"] if r["track"]==tr]
        for kind in ("scientific","practical"):
            eligible = [r for r in cohort if kind=="scientific" or r["near_term"]=="Yes"]
            for r in eligible:
                expected = 1+sum(float(x[kind+"_score"])>float(r[kind+"_score"]) for x in eligible)
                check(int(r[kind+"_rank"])==expected, f"Competition rank or tie: {tr}/{r['id']}/{kind}")
    order=[(r["track"],int(r["scientific_rank"])) for r in data["rankings"]]
    check(order==sorted(order), "Ranking table order")


def searches(data):
    searches = data["search_log"]
    keyed(searches,"search_id")
    log = {(r["search_id"]):(r["source"],r["query"],r["result"],r["url"]) for r in searches}
    fixed = {f"{p.stem}-{n:03d}":tuple(x[k] for k in ("source","query","result","url"))
             for p in (INPUT/"search").glob("*.json") for n,x in enumerate(read(p),1)}
    check(log==fixed and all(all(entry) for entry in log.values()), "Search ledger differs from recorded inputs")
    footprint=" ".join(r["source"]+" "+r["url"] for r in searches).lower()
    for route in ("awesome ophthalmology","physionet","grand challenge","kaggle","hugging face","zenodo","figshare","dryad","pubmed","ncbi"):
        check(route in footprint,"Missing discovery route: "+route)
    check(any(any("\u4e00"<=ch<="\u9fff" for ch in r["query"]) for r in searches),"Missing Chinese-language query")
    hits = keyed(data["pubmed_hits"],"pmid")
    listed=defaultdict(set)
    for p in sorted((INPUT/"pubmed").glob("ageclock_pubmed_*.json")):
        snap=read(p)["esearchresult"]
        check(int(snap["count"])==len(snap["idlist"]), "Truncated PubMed snapshot: "+p.name)
        for pmid in snap["idlist"]:
            listed[pmid].add(p.stem.split("_")[-1])
    check(set(listed)==set(hits) and {q for qs in listed.values() for q in qs}=={"age","neuro","stroke","outcomes"}, "PubMed coverage")
    check(all(set(hits[i]["queries"].split(" | "))==qs for i,qs in listed.items()), "PubMed query membership")


class Reader(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
        self.payload=[]
        self.in_payload=False

    def handle_starttag(self, tag, attrs):
        attr=dict(attrs)
        if tag=="a" and "href" in attr:
            self.links.append(attr["href"])
        if tag=="script" and attr.get("id")=="payload":
            self.in_payload=True

    def handle_data(self, value):
        if self.in_payload:
            self.payload.append(value)

    def handle_endtag(self, tag):
        if tag=="script":
            self.in_payload=False


def reader(data, master, counts):
    html=Reader()
    html.feed((ROOT/"index.html").read_text())
    payload=json.loads("".join(html.payload))
    info = keyed([x["info"] for x in payload["items"]],"id")
    check(info.keys()==master.keys() and all(row=={k:v for k,v in master[i].items() if v not in ("","Unknown")} for i,row in info.items()),"Reader master JSON/CSV mismatch")
    check(payload["stats"]==counts,"Reader stats are stale")
    check(len(payload["rankings"])==len(data["rankings"]) and all({k:text(v) for k,v in x.items()}==y for x,y in zip(payload["rankings"],data["rankings"])),"Reader rankings differ from CSV")
    for table, bucket, keys, test in (
        ("topics","topics",("topic","tier","reason","evidence_id"),lambda r:r["tier"]!="Unknown"),
        ("phenotypes","clinical",("field","status","scope","evidence_id"),lambda r:r["evidence_id"]!="Unknown" or r["status"]!="Uncertain"),
        ("evidence","evidence",("evidence_id","url","locator","checked"),lambda r:True),
    ):
        expected=defaultdict(list)
        for r in data[table]:
            if test(r):
                expected[r["id"]].append([r[k] for k in keys])
        for item in payload["items"]:
            i=item["info"]["id"]
            check(item[bucket]==expected[i], f"Reader {bucket} differs from CSV: {i}")
    local=[unquote(urlsplit(x).path) for x in html.links if not urlsplit(x).scheme and urlsplit(x).path]
    check({"output/master.csv","output/resources.sqlite","RESEARCH_GUIDE.md"}<=set(local), "Reader required links")
    for path in local:
        check((ROOT/path).is_file(), "Broken local homepage link: "+path)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-archive", action="store_true",
                        help="Also require the original full archive, which is not redistributed")
    args=parser.parse_args()
    baseline=snapshot(args.require_archive)
    data=tables()
    master=keyed(data["master"],"id")
    curated={}
    for p in sorted((INPUT/"curation").glob("*.json")):
        part=keyed(read(p),"id")
        check(not (part.keys() & curated.keys()), "Duplicate curated ID across files: "+p.name)
        curated.update(part)
    check(master.keys()==baseline.keys()|curated.keys(), "Baseline/extensions coverage")
    check(SEEDS<=curated.keys() and all(master[i]["review_depth"]=="Source-reviewed" for i in SEEDS),"Missing required reviewed seed")
    check(all(master[i]["baseline_id"]==i for i in baseline),"An original ID was lost")
    check(all(i.startswith("ext-") for i in master.keys()-baseline.keys()),"New row with non-extension ID")
    graph(baseline,data,master)
    gates=read(INPUT/"pixel_gates.json")
    check(gates.keys()<=master.keys(), "Pixel gate references missing resource")
    e,topic,pheno=facts(data,master,gates)
    curated_facts(curated,e,topic,pheno)
    rankings(data,master,e,topic,pheno)
    searches(data)
    counts=read(OUT/"counts.json")
    expected=dict(baseline=len(baseline),upstream_families=446,relationships=len(data["relationships"]),
                  master=len(master),additional=len(master)-len(baseline),source_reviewed=len(curated),evidence=len(e),
                  unique_pubmed_hits=len(data["pubmed_hits"]),searches=len(data["search_log"]),overall_tiers=dict(Counter(r["best_tier"] for r in master.values())))
    check(all(counts.get(k)==v for k,v in expected.items()),"Release counts differ from ledgers")
    reader(data,master,counts)
    archive_status="present and verified" if (INPUT/"EyeDataHub-v0.7.0.tar.gz").exists() else "not bundled; selected metadata hashes verified"
    print(f"PASS: {len(master)} resources, {len(e)} evidence rows, {len(data['rankings'])} ranked track/resource pairs. Offline checks passed. Upstream archive: {archive_status}.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError, sqlite3.Error, tarfile.TarError) as exc:
        sys.exit("FAIL: "+str(exc))
