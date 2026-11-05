"""Build all searchable outputs from pinned local metadata; Python 3 standard library."""
import csv
import hashlib
import json
import re
import sqlite3
import tempfile
from collections import Counter
from pathlib import Path
from ranking import rank
from browse import render

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "inputs"
OUT = ROOT / "output"
UNKNOWN = "Unknown"
TOPICS = "ABCDEFG"
CLINICAL = ("age sex hypertension diabetes cardiovascular stroke_type stroke_time brain_mri csvd ad "
            "dementia cognition parkinson frailty health mortality followup").split()
FIELDS = ("id name acronym official_url country institution year citation doi dataset_doi family relation duplicate_status "
          "modalities images participants eyes device resolution quality multivisit multimodal multicenter access "
            "image_access label_access license research_terms commercial_terms access_url pairing strengths limitations experiment").split()
FRICTION = {"anonymous_direct":"Open download", "self_service_authenticated":"Registration",
            "self_service_clickthrough":"Registration","controlled_or_manual":"Controlled access","author_contact":"Author contact"}
AUD = INPUT/"v0.7.0/hub/audit"
DATE = "2026-11-03"
def read(path):
    return json.loads(path.read_text())
def csvrows(path):
    with path.open(encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))
def audit(prefix):
    return csvrows(next(AUD.glob(prefix+"*.csv")))
def write_csv(name, rows):
    if not rows:
        raise ValueError(f"Empty table: {name}")
    with (OUT/(name+".csv")).open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
def string(v):
    if isinstance(v,(list,dict)):
        return json.dumps(v, ensure_ascii=False)
    return str(v) if v is not None and v != "" else UNKNOWN
def cleanurl(u):
    return isinstance(u,str) and u.startswith(("https://","http://"))
def from_baseline(r, ident, exceptions):
    i = r["record_id"]
    record = {k:UNKNOWN for k in FIELDS}
    record.update(id=i,name=r["canonical_name"],official_url=r["source_landing_page_url"],modalities=" | ".join(r["modalities"]),
                  access=FRICTION.get(r["access_friction"],UNKNOWN),access_url=r["preferred_route_url"],
                  license=r["source_terms"],citation=r["citation"],doi=r["associated_publication_doi"],dataset_doi=r["dataset_doi"],
                  family=r["dataset_family_id"],relation=r["resource_role"],resolution=string(r["image_size"]),
                  duplicate_status="Potential reuse; see relationship ledger" if (ident["incoming_relationship_sources"] or ident["outgoing_relationship_targets"]) else "Independence unverified")
    qs=r["reported_quantities"]
    for k,unit in (("images","images"),("participants","participants")):
        vals=[str(q["count"])+" "+q["unit"]+" ("+q["scope"]+")" for q in qs if q["unit"]==unit]
        if vals: record[k]=" | ".join(vals)
    source=r["source_landing_page_url"]
    if not cleanurl(source): source="https://github.com/pooyakhosravi/EyeDataHub/tree/v0.7.0/hub"
    record["sources"]={"base":[source,"EyeDataHub v0.7.0 → "+i+"; catalog fields and dated source review, not a new clinical audit."]}
    candidate=bool(set(r["modalities"]) & {"fundus","oct","octa","uwf_fundus","fundus_angiography","slo","adaptive_optics","infrared"})
    reason=exceptions.get(i)
    if reason: candidate=reason.startswith("Include:")
    record["screen_reason"]=reason or ("Catalog indicates posterior-segment imaging; auxiliary-use candidate only. Patient-level clinical linkage not established." if candidate else
                      "Catalog modalities / description do not identify human posterior-eye image pixels for this project.")
    record["topics"]={"G":[3 if candidate else 0,"base",record["screen_reason"]]}
    record["phenotypes"]={}
    record["origin"]="EyeDataHub v0.7.0"
    record["review_depth"]="Catalog screen"
    record["checked"]=r["source_check_date"] or UNKNOWN
    record["baseline_id"]=i
    record["upstream_family"]=r["dataset_family_id"]
    record["upstream_role"]=r["resource_role"]
    record["description"]=r["description"]
    record["terms_scope"]=r["terms_scope"]
    record["terms_evidence_url"]=r["terms_evidence_url"]
    record["route_last_checked"]=r["route_last_checked"]
    record["acquisition_support"]=r["acquisition_support"]
    record["raw_access_friction"]=r["access_friction"]
    if r["terms_scope"]=="dataset_files" and r["source_terms"]:
        terms=r["source_terms"].lower()
        if "noncommercial" in terms or "non-commercial" in terms or "-nc" in terms:
            record["commercial_terms"]="Source states a noncommercial restriction; see upstream terms evidence."
        if "research only" in terms or "research-only" in terms or "research purposes only" in terms:
            record["research_terms"]="Source reports research-only use; inspect cited terms."
    return record
def actual_key(k,sources):
    if k in sources:
        return [k]
    parts = [x for x in re.split(r'[ ,;+/|]+',k.strip()) if x]
    if parts and all(p in sources for p in parts):
        return parts
    raise ValueError(f"Unresolved evidence key {k!r}")
def apply_judgment(rec, manual):
    for i, review in manual.items():
        if not review["sources"]:
            raise ValueError(i+" lacks sources")
        if i not in rec:
            if not i.startswith("ext-"): raise ValueError(f"{i} is missing in baseline")
            rec[i] = {k:UNKNOWN for k in FIELDS}
            rec[i].update(origin="Extension",baseline_id=UNKNOWN, upstream_family=UNKNOWN,upstream_role=UNKNOWN,
                          description=UNKNOWN,terms_scope=UNKNOWN,terms_evidence_url=UNKNOWN,route_last_checked=UNKNOWN,
                          acquisition_support=UNKNOWN,raw_access_friction=UNKNOWN)
        row=rec[i]
        src={**row.get("sources",{}),**review["sources"]}
        row.update(review)
        row["sources"]=src
        row["checked"]=review.get("review_date", DATE)
        row["review_depth"]="Source-reviewed"
        row["screen_reason"]=" | ".join(str(a[2]) for a in row["topics"].values()) or row.get("limitations",UNKNOWN)
        if row["access_url"] in (None,"",UNKNOWN): row["access_url"]=row["official_url"]
        if row["family"] in (None,"",UNKNOWN): row["family"]=i
        if row["duplicate_status"]==UNKNOWN: row["duplicate_status"]="Patient overlap unverified"
        if i.startswith("ext-"): row["origin"]="Extension"
        for k in ("sources","topics","phenotypes"):
            if not isinstance(row[k],dict): raise ValueError((i,k))
        for k,v in row["sources"].items():
            if len(v)!=2 or not cleanurl(v[0]) or not v[1].strip(): raise ValueError((i,k,v))
        for k,date in row.get("source_review_dates",{}).items():
            if k not in row["sources"] or not re.fullmatch(r"\d{4}-\d{2}-\d{2}",date):
                raise ValueError((i,"invalid source-specific review date",k,date))
        for k,(tier,key,reason) in row["topics"].items():
            if k not in TOPICS or tier not in (0,1,2,3): raise ValueError((i,k,tier))
            actual_key(key,src)
        for k,(status,key,note) in row["phenotypes"].items():
            if status not in ("Confirmed","Uncertain","Not available"): raise ValueError((i,k,status))
            actual_key(key,src)
def literature():
    joined={}
    for p in sorted((INPUT/"pubmed").glob("ageclock_pubmed_*.json")):
        r=read(p)["esearchresult"]
        if len(r["idlist"]) != int(r["count"]): raise ValueError("Truncated PMID search")
        for i in r["idlist"]: joined.setdefault(i,[]).append(p.stem.split("_")[-1])
    items={}
    for p in sorted((INPUT/"pubmed").glob("summary*.json")):
        items.update({k:v for k,v in read(p)["result"].items() if k!="uids"})
    if set(joined)!=set(items): raise ValueError("Missing PubMed metadata")
    return [dict(pmid=i,queries=" | ".join(joined[i]),title=r["title"],year=r["pubdate"],journal=r["source"],
                 doi=next((a["value"] for a in r["articleids"] if a["idtype"]=="doi"),UNKNOWN),
                 url="https://pubmed.ncbi.nlm.nih.gov/"+i+"/") for i,r in sorted(items.items())]
def main():
    OUT.mkdir(exist_ok=True)
    snap=read(INPUT/"v0.7.0/manifest.json")
    for path,sha in snap["files"].items():
        if hashlib.sha256((INPUT/"v0.7.0"/path).read_bytes()).hexdigest()!=sha: raise ValueError("Baseline checksum: "+path)
    # Selected, hash-pinned metadata are sufficient for an offline rebuild.
    # The full upstream archive contains unrelated repository-search caches and
    # is deliberately not redistributed in the public-facing package.
    archive=INPUT/"EyeDataHub-v0.7.0.tar.gz"
    if archive.exists() and hashlib.sha256(archive.read_bytes()).hexdigest()!=snap["archive_sha256"]:
        raise ValueError("Release archive checksum")
    base=read(INPUT/"v0.7.0/hub/catalog.json")["records"]
    identity={r["record_id"]:r for r in audit("resource_identity_review")}
    edges=audit("resource_relationship_edges")
    exceptions=read(INPUT/"screening_exceptions.json")
    rec={r["record_id"]:from_baseline(r,identity[r["record_id"]],exceptions) for r in base}
    assert len(rec)==len(identity)==451 and set(rec)==set(identity) and len(edges)==145
    rev={}
    for path in sorted((INPUT/"curation").glob("*.json")):
        for row in read(path):
            if row["id"] in rev: raise ValueError("Duplicate review: "+row["id"])
            rev[row["id"]]=row
    apply_judgment(rec,rev)
    side=read(INPUT/"supplement/manifest.json")
    side_file=INPUT/"supplement"/side["file"]
    assert hashlib.sha256(side_file.read_bytes()).hexdigest()==side["sha256"]
    dates=read(side_file)["records"]
    assert set(dates)<=set(identity)
    for i,item in dates.items():
        rec[i]["date_record"]=item
        if rec[i]["year"] in (None,"",UNKNOWN):
            rec[i]["year"]=item["publication_date"][:4]+" ("+item["publication_date_scope"]+")"
    acronyms=read(INPUT/"acronyms.json")
    for i,acr in acronyms.items():
        assert i in rec
        rec[i]["acronym"]=acr
    # Clinical evidence can be direct in the study but only derived tables publicly accessible.
    # Keep the original topic evidence in the curation ledger; output the pixel-specific tier separately.
    original_tiers={i:{k:v[0] for k,v in r["topics"].items()} for i,r in rec.items()}
    gates=read(INPUT/"pixel_gates.json")
    for i,g in gates.items():
        if i not in rec: raise ValueError("Unknown gate "+i)
        for k in g["topics"]:
            val=rec[i]["topics"].get(k)
            if val and val[0]==1: rec[i]["topics"][k]=[2,val[1],val[2]+" | Pixel gate: "+g["reason"]]
        rec[i]["screen_reason"]=" | ".join(str(v[2]) for v in rec[i]["topics"].values())
    evidence=[]; pheno=[]; topic=[]; master=[]
    for i,r in sorted(rec.items()):
        for k,(url,loc) in r["sources"].items():
            checked=(r.get("source_review_dates",{}).get(k,r["checked"]) if k!="base" else
                     next(x["source_check_date"] for x in base if x["record_id"]==i))
            evidence.append(dict(evidence_id=i+"#"+k,id=i,url=url,locator=loc,checked=checked))
        for field in CLINICAL+sorted(r["phenotypes"].keys()-set(CLINICAL)):
            found=r["phenotypes"].get(field)
            if found:
                st,key,note=found
                refs=" | ".join(i+"#"+k for k in actual_key(key,r["sources"]))
            else: st,refs,note="Uncertain",UNKNOWN,"Unknown — no field-specific evidence recorded for this resource/release."
            pheno.append(dict(id=i,field=field,status=st,evidence_id=refs,scope=note))
        row={k:string(r.get(k)) for k in FIELDS}
        for k in ("origin","baseline_id","upstream_family","upstream_role","review_depth","checked","description","screen_reason",
                  "terms_scope","terms_evidence_url","route_last_checked","acquisition_support","raw_access_friction"):
            row[k]=string(r.get(k))
        labels=[]
        for k in TOPICS:
            v=r["topics"].get(k)
            tier=["Excluded","Tier 1","Tier 2","Tier 3"][v[0]] if v else "Unknown"
            note=v[2] if v else "No topic-specific finding"
            refs=" | ".join(i+"#"+key for key in actual_key(v[1],r["sources"])) if v else UNKNOWN
            source_tier=original_tiers[i].get(k)
            topic.append(dict(id=i,topic=k,tier=tier,reviewed_tier_before_pixel_gate=
                              ["Excluded","Tier 1","Tier 2","Tier 3"][source_tier] if source_tier is not None else UNKNOWN,
                              evidence_id=refs,reason=note))
            if v and v[0]>0:labels.append(v[0])
            row["topic_"+k]=tier
        row["best_tier"]=f"Tier {min(labels)}" if labels else "Excluded"
        for k in CLINICAL: row[k]=r["phenotypes"].get(k,["Uncertain"])[0]
        for col,keys in (("age_clock_fit","A"),("stroke_csvd_fit","BC"),("ad_dementia_fit","D"),("multicenter_model_fit","G")):
            row[col]=" | ".join(k+": "+r["topics"][k][2] for k in keys if k in r["topics"]) or UNKNOWN
        d=r.get("date_record",{})
        for key in ("publication_date","publication_date_scope","publication_date_source_url","publication_date_reviewed_on"):
            row[key]=string(d.get(key))
        master.append(row)
    searchlogs=[]
    for p in sorted((INPUT/"search").glob("*.json")):
        for j,r in enumerate(read(p),1):
            searchlogs.append(dict(search_id=p.stem+f"-{j:03d}",searched=DATE,source=r["source"],query=r["query"],
                                   result=r["result"],url=r["url"]))
    tables={"master":master,"phenotypes":pheno,"topics":topic,"evidence":evidence,"rankings":rank(rec,INPUT),
            "relationships":edges,"extensions_relationships":read(INPUT/"relationships.json"),"identity":list(identity.values()),
            "quantities":audit("resource_quantity_evidence"),"access_audit":audit("access_verification_log"),
            "excluded":[dict(id=r["id"],name=r["name"],reason=r["screen_reason"],review=r["review_depth"],source=r["official_url"]) for r in master if r["best_tier"]=="Excluded"],
            "search_log":searchlogs,"pubmed_hits":literature()}
    for name, rows in tables.items(): write_csv(name,rows)
    with tempfile.TemporaryDirectory(dir=OUT) as td:
        temp=Path(td)/"resources.sqlite"
        with sqlite3.connect(temp) as db:
            for name, rows in tables.items():
                keys=list(rows[0])
                db.execute(f'CREATE TABLE "{name}" ('+", ".join('"'+k+'" '+("NUMERIC" if name=="rankings" and k in ("scientific_rank","practical_rank","scientific_score","practical_score","R","L","Q","X","M") else "TEXT") for k in keys)+")")
                db.executemany(f'INSERT INTO "{name}" VALUES ('+",".join("?" for _ in keys)+")",[[r[k] for k in keys] for r in rows])
            db.execute("CREATE UNIQUE INDEX ix_master ON master(id)")
            db.execute("CREATE UNIQUE INDEX ix_pheno ON phenotypes(id,field)")
            db.execute("CREATE UNIQUE INDEX ix_topic ON topics(id,topic)")
            db.execute("CREATE UNIQUE INDEX ix_evidence ON evidence(evidence_id)")
            db.execute("CREATE INDEX ix_rank ON rankings(track,scientific_rank)")
            assert db.execute("PRAGMA integrity_check").fetchone()[0]=="ok"
        temp.replace(OUT/"resources.sqlite")
    stats={"baseline":len(base),"upstream_families":len({r["dataset_family_id"] for r in base}),"relationships":len(edges),
           "master":len(master),"additional":len(master)-len(base),"source_reviewed":len(rev),"evidence":len(evidence),
           "unique_pubmed_hits":len(tables["pubmed_hits"]),"searches":len(searchlogs),"overall_tiers":dict(Counter(r["best_tier"] for r in master))}
    (OUT/"counts.json").write_text(json.dumps(stats,ensure_ascii=False,indent=2)+"\n")
    render(ROOT,tables,stats)
    print(json.dumps(stats,ensure_ascii=False))
if __name__=="__main__": main()
