#!/usr/bin/env python3
"""HEAD-only landing-page audit; does not verify dataset download or permission.

Python standard library + curl. Redirects are followed one HEAD at a time so
every destination is screened for private addresses and embedded credentials.
No GET fallback, cookies, netrc, credentials, or response bodies are used.
"""
import argparse
import csv
import datetime as dt
import hashlib
import ipaddress
import io
import json
import os
import re
import socket
import subprocess
import threading
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit

REDIRECTS = {301, 302, 303, 307, 308}
PRIVATE_SUFFIXES = (".localhost", ".local", ".internal", ".lan", ".home", ".test", ".invalid")
SENSITIVE_QUERY = re.compile(r"(?i)(?:token|password|secret|signature|credential|authorization|session|(?:^|_)sig$|api.?key)")


def public_url(url):
    """Check syntax before any DNS or HTTP operation."""
    p = urlsplit(url)
    if p.scheme not in {"http", "https"} or not p.hostname:
        raise ValueError("Unsupported scheme or missing host")
    if p.username is not None or p.password is not None:
        raise ValueError("URL userinfo is prohibited")
    if any(ord(c) < 32 for c in url):
        raise ValueError("URL control character is prohibited")
    host = p.hostname.rstrip(".").lower()
    if host == "localhost" or host.endswith(PRIVATE_SUFFIXES) or "." not in host:
        raise ValueError("Local or non-public hostname is prohibited")
    port = p.port or (443 if p.scheme == "https" else 80)
    if port not in {80, 443}:
        raise ValueError("Non-web port is prohibited")
    try:
        addr = ipaddress.ip_address(host)
        if not addr.is_global:
            raise ValueError("Non-public IP address is prohibited")
    except ValueError as exc:
        if "prohibited" in str(exc):
            raise
    return p, host, port


def redact_url(url):
    p = urlsplit(url)
    netloc = p.hostname or ""
    if ":" in netloc:
        netloc = "[" + netloc + "]"
    if p.port:
        netloc += ":" + str(p.port)
    query = urlencode([(k, "[REDACTED]" if SENSITIVE_QUERY.search(k) else v)
                       for k, v in parse_qsl(p.query, keep_blank_values=True)])
    return urlunsplit((p.scheme, netloc, p.path, query, p.fragment))


def resolve_public(host, port, remaining):
    # A daemon bounds DNS wall time without creating an unbounded executor queue.
    box = {}
    def resolve():
        try:
            box["ips"] = list(dict.fromkeys(x[4][0] for x in socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)))
        except OSError:
            box["error"] = "DNS resolution failed"
    thread = threading.Thread(target=resolve, daemon=True)
    thread.start()
    thread.join(min(3.0, remaining))
    if thread.is_alive():
        raise TimeoutError("DNS timeout")
    if "error" in box or not box.get("ips"):
        raise OSError(box.get("error", "DNS resolution returned no addresses"))
    if any(not ipaddress.ip_address(ip).is_global for ip in box["ips"]):
        raise ValueError("DNS includes a non-public IP address; request blocked")
    return box["ips"]


def probe(url, deadline_seconds, max_redirects):
    start = time.monotonic()
    current, visited, chain = url, set(), []
    result = {"url": redact_url(url), "initial_host": urlsplit(url).hostname or "",
              "status": "Unresolved", "http_code": "", "final_url": redact_url(url),
              "redirect_count": 0, "content_type": "", "curl_exit": "", "reason": ""}
    try:
        while True:
            remaining = deadline_seconds - (time.monotonic() - start)
            if remaining <= 0:
                raise TimeoutError("Overall URL deadline exceeded")
            parsed, host, port = public_url(current)
            if current in visited:
                raise ValueError("Redirect loop")
            visited.add(current)
            ips = resolve_public(host, port, remaining)
            remaining = deadline_seconds - (time.monotonic() - start)
            if remaining <= 0:
                raise TimeoutError("Overall URL deadline exceeded after DNS")
            # Pin the screened DNS answers to prevent a second resolution from
            # changing the destination into a private address (DNS rebinding).
            resolve_arg = host + ":" + str(port) + ":" + ",".join("[" + ip + "]" if ":" in ip else ip for ip in ips)
            command = ["curl", "--disable", "--silent", "--show-error", "--head",
                       "--proto", "=http,https", "--noproxy", "*", "--max-time", f"{remaining:.3f}",
                       "--connect-timeout", f"{min(5.0, remaining):.3f}", "--resolve", resolve_arg,
                       "--user-agent", "RetinalResourceLandingAudit/1.0 (HEAD-only)",
                       "--output", os.devnull, "--dump-header", "-", "--url", current]
            call = subprocess.run(command, capture_output=True, timeout=remaining + 0.5)
            result["curl_exit"] = call.returncode
            raw = call.stdout.decode("iso-8859-1", "replace")
            blocks = [b for b in re.split(r"\r?\n\r?\n", raw) if b.startswith("HTTP/")]
            headers, code = {}, 0
            if blocks:
                lines = blocks[-1].splitlines()
                code = int(lines[0].split()[1])
                for line in lines[1:]:
                    if ":" in line:
                        key, value = line.split(":", 1)
                        headers[key.strip().lower()] = value.strip()
            result.update(http_code=code or "", final_url=redact_url(current),
                          content_type=headers.get("content-type", ""))
            chain.append({"url": redact_url(current), "http_code": code or "", "curl_exit": call.returncode})
            if call.returncode:
                reason = {6: "DNS resolution failed", 7: "Connection failed", 28: "Timeout",
                          35: "TLS handshake failed", 51: "TLS verification failed", 60: "TLS certificate verification failed"}.get(call.returncode, "curl transport error")
                result["reason"] = reason + "; does not establish a dead link"
                break
            if code in REDIRECTS:
                location = headers.get("location")
                if not location:
                    result["reason"] = "Redirect without Location"
                    break
                if result["redirect_count"] >= max_redirects:
                    result["reason"] = "Redirect limit exceeded"
                    break
                next_url = urljoin(current, location)
                public_url(next_url)
                current = next_url
                result["redirect_count"] += 1
                continue
            if 200 <= code < 300:
                result.update(status="HTTP reachable", reason="HEAD response only; image files, labels, permission and download access unverified")
            elif code in {404, 410}:
                result.update(status="Candidate missing", reason="404/410 candidate requires manual verification; no GET fallback performed")
            elif code in {401, 403, 405, 429}:
                result["reason"] = "Authentication, policy, rate limit or unsupported HEAD; not classified as dead"
            else:
                result["reason"] = "HTTP response does not resolve availability; manual review required"
            break
    except (ValueError, OSError, TimeoutError, subprocess.TimeoutExpired) as exc:
        result["reason"] = str(exc) if not isinstance(exc, subprocess.TimeoutExpired) else "Overall URL timeout"
    result["elapsed_seconds"] = round(time.monotonic() - start, 3)
    result["redirect_chain"] = json.dumps(chain, ensure_ascii=False, separators=(",", ":"))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of", required=True, help="Explicit audit date YYYY-MM-DD")
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=float, default=12.0, help="Total seconds per original URL, including all redirects")
    parser.add_argument("--max-redirects", type=int, default=5)
    parser.add_argument("--limit", type=int, help="Optional smoke check; marked incomplete in summary")
    args = parser.parse_args()
    dt.date.fromisoformat(args.as_of)
    if not 1 <= args.workers <= 8 or not 0 < args.timeout <= 12 or not 0 <= args.max_redirects <= 5:
        parser.error("Use at most 8 workers, 12 seconds and 5 redirects")
    repo = args.repo.resolve()
    input_path = repo / "library/output/master.csv"
    input_bytes = input_path.read_bytes()
    master = list(csv.DictReader(io.StringIO(input_bytes.decode("utf-8-sig"), newline="")))
    mapping = defaultdict(lambda: {"ids": set(), "fields": set()})
    for row in master:
        for field in ("official_url", "access_url"):
            url = row.get(field, "").strip()
            if url and url != "Unknown":
                mapping[url]["ids"].add(row["id"])
                mapping[url]["fields"].add(field)
    urls = sorted(mapping)
    total = len(urls)
    if args.limit is not None:
        urls = urls[:args.limit]
    locks = defaultdict(lambda: threading.Semaphore(2))
    def task(url):
        host = urlsplit(url).hostname or ""
        with locks[host]:
            row = probe(url, args.timeout, args.max_redirects)
        return {"as_of": args.as_of, **row, "resource_ids": " | ".join(sorted(mapping[url]["ids"])),
                "source_fields": " | ".join(sorted(mapping[url]["fields"])),
                "method": "HEAD", "body_downloaded": "No", "download_access_verified": "No"}
    rows = []
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        jobs = [executor.submit(task, url) for url in urls]
        for future in as_completed(jobs):
            rows.append(future.result())
            if len(rows) % 50 == 0:
                print(f"HEAD checked {len(rows)}/{len(urls)}", flush=True)
    output = repo / "audit" / args.as_of
    output.mkdir(parents=True, exist_ok=True)
    columns = ["as_of", "url", "resource_ids", "source_fields", "initial_host", "status", "http_code", "final_url", "redirect_count", "content_type", "curl_exit", "elapsed_seconds", "reason", "method", "body_downloaded", "download_access_verified", "redirect_chain"]
    with (output / "landing_links.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda r: r["url"]))
    summary = {"as_of": args.as_of, "started_utc": started, "finished_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
               "master_sha256": hashlib.sha256(input_bytes).hexdigest(), "resources": len(master),
               "unique_input_urls": total, "checked_urls": len(rows), "complete": len(rows) == total,
               "method": "HEAD only; guarded manual redirect following, maximum five hops; no GET fallback",
               "max_workers": args.workers, "per_initial_host_concurrency": 2, "url_deadline_seconds": args.timeout,
               "status_counts": dict(Counter(r["status"] for r in rows)),
               "http_code_counts": dict(Counter(str(r["http_code"]) for r in rows)),
               "candidate_missing": [{"url": r["url"], "http_code": r["http_code"], "resource_ids": r["resource_ids"]} for r in rows if r["status"] == "Candidate missing"],
               "download_access_verified": False,
               "limitations": ["2xx establishes only a HEAD HTTP response, not image/label download or permission.",
                               "401/403/405/429, DNS/TLS/transport failures and timeouts remain Unresolved, not dead.",
                               "404/410 remain candidates for manual verification; some sites reject HEAD.",
                               "The total 12-second budget includes redirects; no page text or medical data was fetched.",
                               "Every destination is checked for userinfo, local names, private IPs and DNS answers; DNS answers are pinned for curl.",
                               "Sensitive redirect query values are redacted; response headers/cookies are not archived."]}
    (output / "link_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(output), "checked_urls": len(rows), "status_counts": summary["status_counts"]}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
