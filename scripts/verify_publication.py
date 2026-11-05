#!/usr/bin/env python3
"""Offline publication guard; findings contain paths/categories, never matched values.

Default: index blobs and tracked working-tree files. --all-history additionally
examines every Git blob reachable from local refs and HEAD, including tagged
blobs. This is a narrow release check, not a complete secret/privacy audit.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path, PurePosixPath


BLOCKED_ARCHIVE_SHA256 = {
    "66235c429b87bf90f4618480e92e39207f227ee38d234358cd8a4ce97a5227c7",
}
ARCHIVE_ENDINGS = (".tar", ".tar.gz", ".tgz", ".tar.bz2", ".tbz2", ".tar.xz", ".txz", ".zip", ".7z", ".rar")
BACKUP_DIRS = {"backup", "backups", ".backup", ".backups", ".local-only-retinal-backups", "local_backup", "local_backups", "local-backup", "local-backups", "private_backup", "private_backups", "private-backup", "private-backups"}
CREDENTIAL_DIRS = {".credentials", ".aws", ".azure", ".kaggle", ".ssh"}
CREDENTIAL_NAMES = {".netrc", "_netrc", ".git-credentials", ".npmrc", ".pypirc", "credentials", "credentials.json", "credentials.yml", "credentials.yaml", "credentials.ini", "credentials.txt", "token.json", "tokens.json", "kaggle.json", "application_default_credentials.json"}
KEY_NAMES = {"id_rsa", "id_dsa", "id_ecdsa", "id_ed25519", "identity"}
PATTERNS = {
    "private-key-material": re.compile(br"-----BEGIN (?:RSA |EC |DSA |OPENSSH |ENCRYPTED |PGP )?PRIVATE KEY(?: BLOCK)?-----"),
    "github-access-token": re.compile(br"(?<![A-Za-z0-9_])(?:gh[pousr]_[A-Za-z0-9]{36}|github_pat_[A-Za-z0-9_]{82})(?![A-Za-z0-9_])"),
    "aws-access-key-id": re.compile(br"(?<![A-Z0-9])(?:AKIA|ASIA)[A-Z0-9]{16}(?![A-Z0-9])"),
    "aws-secret-access-key": re.compile(br"(?i)\baws[_-]?secret[_-]?access[_-]?key\b[\"']?\s*[:=]\s*[\"']?([A-Za-z0-9/+=]{40})(?![A-Za-z0-9/+=])"),
    "aws-session-token": re.compile(br"(?i)\baws[_-]?session[_-]?token\b[\"']?\s*[:=]\s*[\"']?([A-Za-z0-9/+=]{40,2048})(?![A-Za-z0-9/+=])"),
}
CHUNK = 1024 * 1024
OVERLAP = 4096


def git(repo, *args, data=None, allow_failure=False):
    result = subprocess.run(["git", "-C", str(repo), *args], input=data, capture_output=True)
    if result.returncode and not allow_failure:
        raise RuntimeError("Git operation failed")
    return result.stdout if result.returncode == 0 else b""


def path_categories(path):
    p = PurePosixPath(path.lower())
    parts, name = p.parts, p.name
    found = set()
    archive = name.endswith(ARCHIVE_ENDINGS)
    if "eyedatahub" in name and archive:
        found.add("forbidden-upstream-archive")
    if name == ".env" or name.startswith(".env.") or name in CREDENTIAL_NAMES or any(x in CREDENTIAL_DIRS for x in parts) or any(parts[n:n+2] == (".config", "gcloud") for n in range(len(parts)-1)):
        found.add("forbidden-credential-file")
    if re.fullmatch(r"(?:client[_-]secret|service[_-]account)(?:[._-].*)?\.json", name):
        found.add("forbidden-credential-file")
    if name in KEY_NAMES or name.endswith((".pem", ".key", ".p12", ".pfx", ".jks")):
        found.add("forbidden-key-container")
    if any(x in BACKUP_DIRS for x in parts) or name.endswith((".bak", ".backup", ".orig", ".swp", ".swo", ".bundle", "~")) or (archive and re.search(r"(?:^|[._-])backups?(?:[._-]|$)", name)):
        found.add("forbidden-local-backup")
    return found


def scan_chunks(chunks):
    found, tail, digest = set(), b"", hashlib.sha256()
    for chunk in chunks:
        digest.update(chunk)
        window = tail + chunk
        found.update(category for category, pattern in PATTERNS.items() if pattern.search(window))
        tail = window[-OVERLAP:]
    if digest.hexdigest() in BLOCKED_ARCHIVE_SHA256:
        found.add("forbidden-upstream-archive")
    return found


def file_chunks(path):
    with path.open("rb") as stream:
        while True:
            chunk = stream.read(CHUNK)
            if not chunk:
                return
            yield chunk


class Blobs:
    """Stream Git objects without shell interpolation or credential access."""
    def __init__(self, repo):
        self.process = subprocess.Popen(["git", "-C", str(repo), "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

    def chunks(self, oid):
        self.process.stdin.write(oid.encode("ascii") + b"\n")
        self.process.stdin.flush()
        header = self.process.stdout.readline().split()
        if len(header) != 3 or header[1] != b"blob":
            raise RuntimeError("Expected a readable Git blob")
        remaining = int(header[2])
        while remaining:
            chunk = self.process.stdout.read(min(CHUNK, remaining))
            if not chunk:
                raise RuntimeError("Incomplete Git blob")
            remaining -= len(chunk)
            yield chunk
        if self.process.stdout.read(1) != b"\n":
            raise RuntimeError("Invalid Git object framing")

    def close(self):
        self.process.stdin.close()
        self.process.stdout.close()
        self.process.wait(timeout=10)


def index_entries(repo):
    entries = []
    for row in git(repo, "ls-files", "--stage", "-z").split(b"\0"):
        if row:
            meta, raw_path = row.split(b"\t", 1)
            mode, oid, stage = meta.decode("ascii").split()
            entries.append((mode, oid, stage, os.fsdecode(raw_path)))
    return entries


def historical_entries(repo):
    # List every reachable object, including tags aimed at blobs rather than commits.
    object_ids = git(repo, "rev-list", "--objects", "--all", "--no-object-names").splitlines()
    info = git(repo, "cat-file", "--batch-check=%(objectname) %(objecttype)", data=b"\n".join(object_ids) + b"\n") if object_ids else b""
    blobs = {line.split()[0].decode("ascii") for line in info.splitlines() if line.split()[1:2] == [b"blob"]}
    paths = defaultdict(set)
    roots = set(git(repo, "log", "--all", "--format=%T").splitlines()) if object_ids else set()
    # Include refs that point directly to a tree as well as ordinary commit trees.
    refs = git(repo, "for-each-ref", "--format=%(objectname)").splitlines()
    for ref in refs:
        tree = git(repo, "rev-parse", "--verify", ref.decode("ascii") + "^{tree}", allow_failure=True).strip()
        if tree:
            roots.add(tree)
    for tree in roots:
        for row in git(repo, "ls-tree", "-r", "-z", tree.decode("ascii")).split(b"\0"):
            if row:
                meta, raw_path = row.split(b"\t", 1)
                _, kind, oid = meta.decode("ascii").split()
                if kind == "blob":
                    paths[oid].add(os.fsdecode(raw_path))
    return blobs, paths


def audit(repo, all_history=False):
    repo = repo.resolve()
    findings, cache = set(), {}
    entries = index_entries(repo)
    reader = Blobs(repo)
    def record(path, categories):
        findings.update((path, category) for category in categories)
    def blob(oid, path):
        if oid not in cache:
            cache[oid] = scan_chunks(reader.chunks(oid))
        record(path, cache[oid] | path_categories(path))
    try:
        for mode, oid, stage, path in entries:
            record(path, path_categories(path))
            if stage != "0":
                record(path, {"unmerged-index-entry"})
            if mode == "160000":
                record(path, {"unreviewed-submodule"})
                continue
            blob(oid, path)
            target = repo / path
            if target.is_symlink():
                # Never follow a tracked link into a local credential or backup directory.
                record(path, scan_chunks([os.fsencode(os.readlink(target))]))
            elif not target.resolve().is_relative_to(repo):
                record(path, {"tracked-path-outside-repository"})
            elif target.is_file():
                record(path, scan_chunks(file_chunks(target)))
        historical_blobs = 0
        if all_history:
            oids, paths = historical_entries(repo)
            historical_blobs = len(oids)
            for oid in oids:
                for path in paths.get(oid, {"<reachable-blob:" + oid + ">"}):
                    blob(oid, path)
    finally:
        reader.close()
    return {"status": "FAIL" if findings else "PASS", "scope": "index + tracked working files + all local refs/HEAD reachable blobs" if all_history else "index + tracked working files; history not scanned", "tracked_paths": len({r[3] for r in entries}), "historical_blobs": historical_blobs, "findings": [{"path": p, "category": c} for p, c in sorted(findings)]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--all-history", action="store_true", help="Also scan all blobs reachable from local refs and HEAD; not reflogs, dangling objects, remote caches or other clones")
    args = parser.parse_args()
    try:
        repo = args.repo.resolve()
        top = git(repo, "rev-parse", "--show-toplevel").strip()
        if Path(os.fsdecode(top)).resolve() != repo:
            raise RuntimeError("Repository root required")
        result = audit(repo, args.all_history)
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError):
        # Do not leak process stderr, exception payloads, tokens or environment values.
        result = {"status": "FAIL", "findings": [{"path": "<repository>", "category": "publication-check-error"}]}
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 1 if result["status"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
