"""Extract read-only catalog inputs from a tagged upstream git export; compare future releases."""
import argparse
import csv
import hashlib
import io
import json
import re
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ("resource_identity_", "resource_relationship_", "resource_quantity_", "access_verification_log_",
         "superseded_and_alternate_records_", "download_load_verification_", "catalog_search_flow_")
def selected(path):
    return (path in {"CLAUDE.md", "LICENSE", "CITATION.cff", "RELEASE_POLICY.md", "CONTRIBUTING.md",
                     "hub/catalog.csv", "hub/catalog.json"} or
            (path.startswith("hub/audit/") and path.rsplit("/", 1)[-1].startswith(AUDIT)
             and path.endswith((".csv", ".json"))))

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("archive", type=Path)
    p.add_argument("tag")
    p.add_argument("commit", help="peeled Git commit, obtained via git rev-parse TAG^{commit}")
    p.add_argument("--verify-existing", action="store_true",
                   help="Compare selected metadata with a frozen snapshot without replacing its archive provenance")
    a = p.parse_args()
    if not re.fullmatch(r"v\d+\.\d+\.\d+", a.tag) or not re.fullmatch("[0-9a-f]{40}", a.commit):
        p.error("Supply a stable release tag and its 40-character commit.")
    folder = ROOT / "inputs" / a.tag
    entries = {}
    with tarfile.open(a.archive, "r:*") as tar:
        for member in tar.getmembers():
            path = member.name.split("/", 1)[-1]
            if member.isfile() and ".." not in Path(path).parts and selected(path):
                entries[path] = tar.extractfile(member).read()
    data = json.loads(entries["hub/catalog.json"])
    records = data["records"]
    ids = [r["record_id"] for r in records]
    csv_ids = [r["record_id"] for r in csv.DictReader(io.StringIO(entries["hub/catalog.csv"].decode("utf-8-sig")))]
    if ids != csv_ids or len(ids) != len(set(ids)) or len(ids) != data["record_count"]:
        raise ValueError("CSV/JSON ID mismatch or duplicated IDs")
    if data["catalog_version"] != a.tag[1:]:
        raise ValueError("Wrong release")
    if a.tag == "v0.7.0" and (a.commit != "0ce7144459a41e8be255fed7fa62c30416613e6b" or len(ids) != 451):
        raise ValueError("Baseline identity mismatch")
    sha = lambda b: hashlib.sha256(b).hexdigest()
    manifest = {"repository": "https://github.com/pooyakhosravi/EyeDataHub", "tag": a.tag, "commit": a.commit,
                "release_archive_doi": "10.5281/zenodo.21798623" if a.tag == "v0.7.0" else "Unknown",
                "archive_sha256": sha(a.archive.read_bytes()), "record_count": len(ids),
                "catalog_search_cutoff": data["catalog_search_cutoff"],
                "files": {k: sha(v) for k, v in sorted(entries.items())}}
    dest = folder / "manifest.json"
    if a.verify_existing:
        if not dest.exists():
            raise ValueError("No existing frozen snapshot to verify")
        saved=json.loads(dest.read_text())
        without_archive=lambda m:{k:v for k,v in m.items() if k!="archive_sha256"}
        if without_archive(saved)!=without_archive(manifest):
            raise ValueError("Selected metadata or source identity differs from frozen snapshot")
        print(json.dumps({"selected_metadata_verified":True,"files":len(entries),
                          "original_archive_bytes_match":saved["archive_sha256"]==manifest["archive_sha256"]}))
        return
    if dest.exists() and json.loads(dest.read_text()) != manifest:
        raise ValueError("Immutable snapshot differs. Use a new release tag.")
    for path, raw in entries.items():
        dst = folder / path
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(raw)
    dest.write_text(json.dumps(manifest, indent=2) + "\n")
    if a.tag != "v0.7.0":
        old = json.loads((ROOT/"inputs/v0.7.0/hub/catalog.json").read_text())["records"]
        prev = {r["record_id"]: r for r in old}
        now = {r["record_id"]: r for r in records}
        changes = {"added": sorted(now.keys() - prev.keys()), "removed": sorted(prev.keys() - now.keys()),
                   "changed_fields": {i: sorted(k for k in prev[i].keys()|now[i].keys() if prev[i].get(k)!=now[i].get(k))
                                      for i in sorted(prev.keys()&now.keys()) if prev[i]!=now[i]}}
        (folder/"diff_from_v0.7.0.json").write_text(json.dumps(changes, indent=2)+"\n")
    print(f"{a.tag} | {len(ids)} IDs | {len(entries)} preserved files")
if __name__ == "__main__":
    main()
