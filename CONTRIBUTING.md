# Contributing

Please propose one resource addition or evidence correction per issue or pull request. Use official dataset releases, data dictionaries, provider access policies, or original research articles. Indexes and mirrors are discovery routes, not independent proof of a field or reuse permission.

## What a contribution needs

- A stable resource ID, original title and official source URL.
- The exact field or topic being added or corrected, with a source URL and a short locator/paraphrase.
- Separate image-file access, individual-label access, linkage evidence and permission scope.
- Counts with their units and population: people, eyes, visits, images, B-scans, volumes or files.
- Family, mirror, component, version and participant-overlap relationships, with uncertainty preserved.
- Dataset license distinct from publication, repository-code or mirror license.
- The date checked. Mark unresolved facts `Unknown` or `Uncertain`; do not infer them from an absent field.

## Edit inputs and regenerate

1. Read the pinned upstream [canonical guide](library/inputs/v0.7.0/CLAUDE.md). Keep the v0.7.0 inputs immutable.
2. Edit the appropriate file under `library/inputs/curation/`. Add source evidence and search records under `library/inputs/search/`. The structured format is illustrated by the existing entries. Scoring and image-access gates have separate input files.
3. Run `python3 library/src/build.py` and `python3 library/src/verify.py`.
4. Run `python3 scripts/build_catalog.py` and `python3 scripts/build_rankings.py`.
5. Run `python3 scripts/build_stats.py` in the plotting environment, then `python3 scripts/verify_repo.py`.
6. Review changed descriptions, counts, topic judgments and ranks. Update the two home pages, citation version and snapshot dates if the release scope changes. Check that graphics remain readable.

The Markdown cards, rankings, statistics and `library/output/` tables are generated outputs. Edit their source inputs or generators rather than silently changing one export.

## Publication guard

Before publishing, stage the intended files and run `python3 scripts/verify_publication.py`. CI runs this check before rebuilding. It scans Git index blobs and tracked working files, including binary bytes, and rejects full EyeDataHub archives, credential/environment files, key containers, local backups and high-confidence private-key/GitHub/AWS token patterns. A renamed copy of the removed baseline archive is also rejected by SHA-256. Ordinary public research contacts and paper URLs are not blocked. Findings report only relative paths and categories, never matching values; do not paste credentials into an issue to explain a failure.

The default check does **not** scan history or untracked files. `.gitignore` helps avoid accidental additions, but does not replace the guard and can be bypassed by a forced add. For release-history review, run `python3 scripts/verify_publication.py --all-history` in a complete local repository. This additionally checks blobs reachable from every local ref and HEAD; a shallow checkout cannot establish the state of missing history. Reflogs, dangling objects, remote cached objects and other clones are outside this check. CI intentionally uses the current-tree mode only.

Keep original source archives and private backups outside the publication repository. Do not add `.env` templates or key containers here; use a non-sensitive configuration example with a different filename if needed. Investigate any false positive from its source evidence rather than adding a broad ignore rule. These targeted checks do not certify absence of all secrets, resolve third-party redistribution rights, or certify medical-image anonymization.

## New EyeDataHub releases

Check the official tags and publication channel. Preserve the existing baseline, fetch the new stable release into a separate versioned directory, save its commit and SHA-256 manifest, and review added/removed/changed records before merging judgments. A newer development commit must not be presented as a stable release. See [library maintenance instructions](library/README.md#更新方法).

## Image examples

Only add a small, representative file when redistribution is documented. The manifest must specify resource ID, original source, license and license evidence, attribution, original filename, SHA-256, dimensions, whether it is a raw sample or a published figure, and any changes. Inspect the image and metadata. Keep its license separate from this repository's license. Controlled-access pixels, unavailable samples and unknown reuse terms should remain official-source links.

## Validation boundaries

Patient-level linkage needs an explicit key or documented approved linkage. Do not substitute row order, filename guesses, separate institutional datasets, or the existence of an association paper. Image-level evaluation, cross-dataset evaluation and simulated clients should not be described as independent patient validation or real federated deployment.

Local validation does not establish that an external URL is live today. Access checks should be dated, and failures distinguished from denied permission or unavailable data. No scheduled acquisition, agreement acceptance or patient-data download is performed by the repository checks.

For an explicit, bounded HTTP check of the landing URLs, run:

```bash
python3 scripts/check_links.py --as-of YYYY-MM-DD
```

This sends HEAD requests only and does not fetch medical-image bodies. A 2xx response confirms HTTP reachability only; it does not establish downloadable pixels, labels or permission. Authentication errors, timeouts and TLS failures remain unresolved. Even 404/410 responses require manual verification before changing a resource record; some platforms handle HEAD differently from a normal page visit. Preserve the original dated result when adding a follow-up interpretation.
