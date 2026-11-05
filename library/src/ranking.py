"""Task-specific prioritisation. All judgement inputs are public and editable."""
import csv
import json
from pathlib import Path

TRACKS = {"Age":"Retinal Aging","Stroke":"Eye–Stroke","Neuro":"Eye–Neurodegeneration"}
FEATURES = {
    "Age":{"age","sex","diabetes","hypertension","cardiovascular","mortality","health","followup"},
    "Stroke":{"stroke_type","stroke_time","brain_mri","csvd","age","sex","hypertension","diabetes","mortality","followup"},
    "Neuro":{"ad","dementia","cognition","parkinson","brain_mri","age","sex","followup"},
}
def rows(file):
    with Path(file).open() as f: return list(csv.DictReader(f,delimiter="\t"))
def rank(records,folder):
    profiles={r["id"]:r for r in rows(folder/"score_profiles.tsv")}
    omitted=json.loads((folder/"score_label_omissions.json").read_text())
    results=[]
    for a in rows(folder/"score_targets.tsv"):
        i=a["id"]; track=a["track"]; p=profiles[i]; raw=records[i]
        t=int(a["relevance"]); n=int(a["n_supported"] or 0)
        fields=sorted(k for k,v in raw["phenotypes"].items() if v[0]=="Confirmed" and k in FEATURES[track]
                      and k not in omitted.get(i,{}).get(track,[]))
        l=min(4,(len(fields)+1)//2)
        scored_n=n if a["n_scope"] in ("Study-linked participants","Outcome-positive subset (lower bound)") else 0
        # A cohort may have follow-up unrelated to the endpoint scored in this track.
        task_followup="followup" in fields
        q=min(4,int(scored_n>=100)+int(scored_n>=1000)+int(p["population"])+int(p["qc"])+int(task_followup))
        x=int(p["access"]); m=int(p["multi"])
        assert t in range(1,5) and x in range(5) and m in range(5)
        science=(40*t+25*l+25*q+10*m)/4
        practical=(25*t+15*l+10*q+5*m+45*x)/4
        keys=[k for k in a["topics"] if k in raw["topics"]]
        tiers=[raw["topics"][k][0] for k in keys]
        assert any(t in (1,2) for t in tiers), (i,track,tiers)
        ready=track in p["ready_tracks"].split(",") and min(v for v in tiers if v)>0 and 1 in tiers and t>=3 and x>=3
        ids=[i+"#"+k for k in raw["sources"] if k!="base"]
        results.append(dict(track=TRACKS[track],id=i,name=raw.get("name") or i,endpoint=a["endpoint"],
                            tier=" / ".join(k+" T"+str(raw["topics"][k][0]) for k in keys),R=t,L=l,Q=q,X=x,M=m,
                            scientific_score=round(science,2),practical_score=round(practical,2),
                            scientific_rank=0,practical_rank=None,near_term="Yes" if ready else "No",
                            paired_n_basis=a["n_basis"],n_scope=a["n_scope"],reported_n=n if n else "Unknown",
                            n_supported=scored_n if scored_n else "Unknown",label_fields=" | ".join(fields) or "None confirmed",
                            basis=p["basis"],evidence=" | ".join(ids),access=raw["access"],
                            image_access=raw.get("image_access","Unknown"),label_access=raw.get("label_access","Unknown")))
    for track in TRACKS.values():
        subset=[r for r in results if r["track"]==track]
        order=sorted(subset,key=lambda r:(-r["scientific_score"],-r["R"],r["id"]))
        for n,r in enumerate(order):
            r["scientific_rank"]=order[n-1]["scientific_rank"] if n and r["scientific_score"]==order[n-1]["scientific_score"] else n+1
        practical=sorted([r for r in subset if r["near_term"]=="Yes"],key=lambda r:(-r["practical_score"],-r["R"],r["id"]))
        for n,r in enumerate(practical):
            r["practical_rank"]=practical[n-1]["practical_rank"] if n and r["practical_score"]==practical[n-1]["practical_score"] else n+1
    return sorted(results,key=lambda r:(r["track"],r["scientific_rank"]))
