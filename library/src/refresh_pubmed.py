"""Repeat the four PubMed searches into a NEW directory, without touching an existing survey."""
import argparse
import datetime
import json
import re
import tempfile
import time
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def fetch(endpoint, params):
    query = URL + endpoint + "?" + urlencode(dict(db="pubmed", retmode="json", **params))
    req = Request(query, headers={"User-Agent":"AgeClock-Resource-Survey/1"})
    for attempt in range(3):
        try:
            with urlopen(req, timeout=60) as response:
                data = json.load(response)
            if "error" in data: raise ValueError(data["error"])
            time.sleep(0.4)
            return data
        except OSError:
            if attempt == 2: raise
            time.sleep(2 ** (attempt+1))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of", type=datetime.date.fromisoformat, required=True)
    parser.add_argument("--output", type=Path, help="must not already exist")
    parser.add_argument("--plan", action="store_true", help="print exact translated search specification offline")
    args=parser.parse_args()
    plan={}
    for row in json.loads((ROOT/"inputs/search/additional.json").read_text()):
        if row["source"]!="PubMed ESearch + ESummary": continue
        name=re.search(r"ageclock_pubmed_(\w+)\.json",row["result"])[1]
        plan[name]=row["query"].replace('"2026/11/03"[PDAT]', '"'+args.as_of.strftime("%Y/%m/%d")+'"[PDAT]')
    if len(plan)!=4: raise ValueError("Expected four saved search strategies")
    if args.plan:
        print(json.dumps(plan, ensure_ascii=False, indent=2)); return
    if args.output is None or args.output.exists(): parser.error("Choose a new --output directory")
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(dir=args.output.parent) as temp:
        stage=Path(temp)/"snapshot"
        stage.mkdir()
        def write(name,value): (stage/name).write_text(json.dumps(value,ensure_ascii=False)+"\n")
        ids=set()
        for name,term in plan.items():
            data=fetch("esearch.fcgi",{"term":term,"retmax":9999,"sort":"relevance"})
            result=data["esearchresult"]
            if len(result["idlist"])!=int(result["count"]):
                raise ValueError("Search exceeds one complete PubMed page; split the strategy by date.")
            ids.update(result["idlist"]); write("ageclock_pubmed_"+name+".json",data)
        ordered=sorted(ids)
        for start in range(0,len(ordered),100):
            group=ordered[start:start+100]
            data=fetch("esummary.fcgi",{"id":",".join(group)})
            if set(data["result"]["uids"])!=set(group): raise ValueError("Incomplete PMID summary batch")
            write(f"summary_{start//100+1}.json",data)
        write("strategies.json",plan)
        if args.output.exists(): raise FileExistsError(args.output)
        stage.rename(args.output)
    print(f"{len(ordered)} unique PMIDs in {args.output}")
if __name__=="__main__": main()
