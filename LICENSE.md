# Licenses and third-party material

This repository contains separately licensed components. The licenses below apply to their stated scopes; they are not interchangeable alternatives for the whole repository.

| Component | License and scope |
| --- | --- |
| Original software in `scripts/` and `library/src/` | MIT, as reproduced below; any separately identified third-party code retains its own notice. |
| EyeDataHub catalog metadata and this project's derived catalog, original research documentation, tables and statistical figures | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), with upstream attribution and modification history in [UPSTREAM_NOTICE.md](UPSTREAM_NOTICE.md). This includes the catalog metadata under `library/inputs/v0.7.0/hub/`, the date-metadata supplement, curated metadata and exported catalog records, `catalog/`, `datasets/`, `RANKINGS.md` and `STATS.md`. |
| Third-party image examples | Their individual CC0 or CC BY 4.0 terms, listed below and in the [image manifest](assets/examples/manifest.json). |
| Indexed datasets, source publications, provider text and other third-party materials | Their own source-specific terms; neither this repository's MIT grant nor its CC BY grant expands rights in those materials. |

## Original software: MIT

MIT License

Copyright (c) 2026 Qian Chen and contributors

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Catalog and original research documentation: CC BY 4.0

The catalog metadata, original research documentation, derived tables and statistical figures contributed by this project are licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) ([legal code](https://creativecommons.org/licenses/by/4.0/legalcode.en)). Copyright (c) 2026 Qian Chen and contributors for our contributions. This grant excludes separately identified third-party materials and the software licensed above.

The 451-record baseline is adapted from **EyeDataHub v0.7.0**, by **Pooya Khosravi, Parsa Riazi Esfehani, Andrew W. Browne and Xiaohui Xie**. EyeDataHub's [fixed-version README, “Citation and licences”](https://github.com/pooyakhosravi/EyeDataHub/blob/0ce7144459a41e8be255fed7fa62c30416613e6b/README.md#L190-L195) licenses its catalog metadata under CC BY 4.0. Its [retained MIT notice](library/inputs/v0.7.0/LICENSE), copyright 2026 EyeDataHub Contributors, expressly concerns the library code itself. The software DOI supplied by upstream is [10.5281/zenodo.21798623](https://doi.org/10.5281/zenodo.21798623); the fixed Git commit remains the reproducible source reference.

This project imports and reorganizes the baseline, adds research-specific evidence and records, and generates topic tiers, rankings, tables and resource pages. Retain the upstream and project attribution, license link, and indication of these changes when sharing or adapting the catalog. The exact upstream reference, selected source components and modification history are in [UPSTREAM_NOTICE.md](UPSTREAM_NOTICE.md). No endorsement by the upstream creators or dataset providers is implied.

This metadata license does not blanket-license an upstream repository archive, crawler cache, downloaded web page, publication, or every file referenced by a catalog record. Any such material requires its own stated scope and applicable terms. The catalog and documentation are provided as-is, without warranties; see the [CC BY 4.0 warranty and liability provisions](https://creativecommons.org/licenses/by/4.0/legalcode.en#s5).

## Image examples and indexed datasets

Gallery images are third-party materials, **excluded from the repository's own MIT and CC BY grants**. China-Fundus-CIMT's included sample is CC0; FDR26, MCFI, OCTDL and the included GRAPE publication figure are CC BY 4.0 under their respective source grants. Full attribution, version, license URL, evidence and file hashes are in the [gallery](assets/examples/README.md) and [manifest](assets/examples/manifest.json).

The license on this repository grants no additional rights over the indexed datasets, publications, clinical records or controlled-access collections. Follow the specific provider's current conditions and cite the original creators. A code license, article license or mirror label is not automatically the original dataset's license.
