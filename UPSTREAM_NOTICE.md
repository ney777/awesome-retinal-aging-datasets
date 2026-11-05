# EyeDataHub attribution and metadata license

The baseline catalog in this repository is derived from:

**Pooya Khosravi, Parsa Riazi Esfehani, Andrew W. Browne and Xiaohui Xie (2026). _EyeDataHub: a command-line tool for finding and accessing ophthalmology datasets_, version 0.7.0.** [Upstream software DOI](https://doi.org/10.5281/zenodo.21798623) · [upstream repository](https://github.com/pooyakhosravi/EyeDataHub) · [fixed commit](https://github.com/pooyakhosravi/EyeDataHub/tree/0ce7144459a41e8be255fed7fa62c30416613e6b).

| Provenance item | Value |
| --- | --- |
| Stable baseline tag | `v0.7.0` |
| Stable baseline commit | `0ce7144459a41e8be255fed7fa62c30416613e6b` |
| Baseline resource records | 451; these are not 451 independent patient cohorts |
| Upstream metadata search cutoff | 2026-08-02 |
| Original source archive SHA-256 | `66235c429b87bf90f4618480e92e39207f227ee38d234358cd8a4ce97a5227c7` |
| Metadata file hashes | [Baseline manifest](library/inputs/v0.7.0/manifest.json) |
| Retained upstream citation | [CITATION.cff](library/inputs/v0.7.0/CITATION.cff) |
| Later date supplement | Commit `65104e4028a22e355f7d2cfc4d6919487fb4036b`; [separate manifest](library/inputs/supplement/manifest.json). This is not part of the stable v0.7.0 snapshot. |

The DOI is retained as the identifier supplied in the upstream citation. Its archival API returned HTTP 410 during the 2026-11-06 audit; the fixed Git commit and file hashes above identify the baseline without asserting that the DOI currently serves a downloadable archive. The archive hash records provenance, not a grant covering every file in that archive.

## Separate licenses for code and catalog metadata

The [README at the fixed commit, lines 190–195](https://github.com/pooyakhosravi/EyeDataHub/blob/0ce7144459a41e8be255fed7fa62c30416613e6b/README.md#L190-L195), states:

> EyeDataHub code is MIT licensed; the catalog metadata are CC BY 4.0.

This short excerpt was checked against the [raw v0.7.0 README](https://raw.githubusercontent.com/pooyakhosravi/EyeDataHub/v0.7.0/README.md) on 2026-11-06 and matched the original source archive. The [retained upstream LICENSE](library/inputs/v0.7.0/LICENSE) separately limits its MIT notice to the library code itself. The [upstream guide](library/inputs/v0.7.0/CLAUDE.md) also requires dataset, publication, website and code terms to remain distinct.

**The reused catalog metadata and this project's derived catalog are distributed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) ([legal code](https://creativecommons.org/licenses/by/4.0/legalcode.en)).** Copyright and attribution for upstream contributions remain with their original creators. Copyright (c) 2026 Qian Chen and contributors applies to this project's additions. Original software in this project is separately licensed under MIT; [LICENSE.md](LICENSE.md) defines the component scopes.

## What this project changed

- Imported the 451 baseline records and selected metadata audits, retaining original resource IDs, provenance, quantity units, family identities and relationship evidence.
- Added 28 resource records and research-specific source review. Added A–G topic judgments, clinical-field evidence status, image/label access scope, pairing limitations and suggested experiments.
- Added three research-direction scoring tables and endpoint-specific denominator decisions; these are this project's judgments, not EyeDataHub's rankings.
- Reorganized and normalized the metadata into CSV, SQLite, searchable presentation and per-resource Markdown pages; generated aggregate statistics and figures. Source-record descriptions and quoted source text remain attributable to their respective sources.
- Added publication-date metadata from the separately identified later upstream commit, without replacing the frozen v0.7.0 baseline.

The source-reviewed and catalog-screened records are distinguished in the release. These changes do not imply endorsement, permission for a particular dataset use, or scientific validation by EyeDataHub or the original data providers.

## Scope of the attribution

The CC BY attribution applies to the upstream catalog metadata and its derivatives, including the selected catalog and metadata-audit files, normalized record exports, resource pages and derived statistics. When sharing or adapting those materials, retain the upstream and project attribution, a link to CC BY 4.0, and an indication of modifications. The material is supplied as-is under the [license's warranty and liability provisions](https://creativecommons.org/licenses/by/4.0/legalcode.en#s5).

This notice does not grant rights to an entire upstream archive, crawler cache, third-party web page, source publication, underlying patient dataset or image file. The five displayed image examples have their own source grants and attribution in the [gallery](assets/examples/README.md) and [manifest](assets/examples/manifest.json). Provider descriptions and other third-party material retain any applicable source terms.
