<p align="center">
  <img src="assets/banner.svg" width="100%" alt="Awesome Retinal Aging and Oculomics Datasets — evidence-linked resources for retinal aging, eye–brain research and generalizable AI">
</p>

<p align="center">
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="catalog/README.md">Browse all resources</a> ·
  <a href="assets/examples/README.md">Image gallery</a> ·
  <a href="STATS.md">Statistics</a> ·
  <a href="library/RESEARCH_GUIDE.md">Research guide</a>
</p>

# Awesome Retinal Aging & Oculomics Datasets

A curated, evidence-linked catalog of retinal imaging resources for **aging clocks, cerebrovascular disease, neurodegeneration, systemic health, and transferable ophthalmic AI**. Every resource has a dedicated page with its description, imaging scope, clinical labels, access route, source evidence, limitations, and suggested experiments.

Coverage includes open-download, registration-based and controlled-access resources; access scopes are stated separately.

**Base survey:** 3 November 2026 · **Public-release review:** 6 November 2026 · **Baseline:** [EyeDataHub v0.7.0](https://github.com/pooyakhosravi/EyeDataHub/tree/v0.7.0). Targeted corrections are documented in the [changelog](CHANGELOG.md); this is not a new source review of all 479 records.

| 479 resource records | 235 included resources | 49 source-reviewed records | 7 research topics |
|:---:|:---:|:---:|:---:|
| 451 baseline + 28 additions | 23 Tier 1 · 19 Tier 2 · 193 Tier 3 | 43 included · 6 excluded | Multi-label classification |

**Records are not independent patient cohorts.** Mirrors, annotation sets and derivative releases may overlap. The other 244 records are retained in an [exclusion ledger](catalog/excluded.md). The 430 catalog-screened records have not undergone the same source review as the 49 priority records. Unknown fields remain explicit.

## Start here

- **Find a dataset:** [A–Z catalog](catalog/README.md) · [49 source-reviewed records](catalog/reviewed.md) · [topic directories](#research-topics).
- **Choose an experiment:** [scientific priorities and near-term options](#choose-a-research-direction) · [detailed research guide](library/RESEARCH_GUIDE.md).
- **Inspect real images:** [five-source image gallery](assets/examples/README.md), with original-file hashes, licenses and attribution.
- **Query the evidence:** [master CSV](library/output/master.csv) · [phenotypes](library/output/phenotypes.csv) · [evidence](library/output/evidence.csv) · [SQLite](library/output/resources.sqlite).
- **Review publication readiness:** [Scientific and licensing audit](audit/2026-11-06/REPORT.md) and [publication safety checks](audit/2026-11-06/PUBLICATION_SAFETY.md), including sample-metadata minimization, history cleanup and server-side verification limits.
- **Search locally:** download or clone this repository, then open [`library/index.html`](library/index.html). It is a self-contained bilingual search interface. GitHub shows the HTML source; open the downloaded file in a browser to use the interface.

## Image examples

These are source images, with no generated retina examples. Four gallery assets are unmodified dataset files; the GRAPE asset is a complete published figure. The samples illustrate image format and appearance, not diagnostic accuracy or dataset-wide image quality. “Unmodified” refers to the files in this repository: providers may already have processed them. For example, the [China-Fundus-CIMT descriptor](https://www.nature.com/articles/s41597-025-04930-z) reports cropping and restoration of some images; restoration of the particular sample shown here is Unknown.

| China-Fundus-CIMT · fundus | MCFI · fundus | FDR26 · fundus |
|:---:|:---:|:---:|
| <img src="assets/examples/china-fundus-cimt-original.png" width="230" alt="Distributed left-eye fundus sample from China-Fundus-CIMT"> | <img src="assets/examples/mcfi-original.jpg" width="230" alt="Distributed right-eye fundus sample from MCFI"> | <img src="assets/examples/fdr26-original.jpg" width="230" alt="Distributed fundus sample from the FDR26 classification archive"> |
| [Dataset card](datasets/china_fundus_cimt.md) · [Official source](https://doi.org/10.6084/m9.figshare.27907056.v1) | [Dataset card](datasets/ext-mcfi.md) · [Official source](https://data.mendeley.com/datasets/stskv6zjt9/1) | [Dataset card](datasets/ext-fdr26.md) · [Official source](https://zenodo.org/records/23101200) |
| Guo Na et al., 2025 · [CC0](https://creativecommons.org/publicdomain/zero/1.0/) | Sangeeta Biswas et al., 2026 · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Sanae Lamti et al., 2026 · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

<p align="center"><img src="assets/examples/octdl-original.jpg" width="700" alt="Distributed retinal OCT B-scan from the OCTDL Normal source category"></p>

**OCTDL — distributed OCT B-scan.** Mikhail Kulyabin et al., 2024; [official source](https://zenodo.org/records/10839556), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The category comes from the source directory. [Dataset card](datasets/octdl.md) · [full image credits and provenance](assets/examples/README.md) · [machine-readable manifest](assets/examples/manifest.json).

Every dataset page provides an official example/source entry. **Local image examples currently cover five resources**, not all 479; controlled or unresolved sources remain links rather than redistributed images.

## Research topics

| Topic | Browse | What the evidence needs to establish |
|---|---|---|
| **A · Retinal aging** | [Age / aging resources](catalog/topics/A.md) | Images linked to individual age; repeat visits and health outcomes assessed separately |
| **B · Eye–stroke** | [Stroke / cerebrovascular risk](catalog/topics/B.md) | Stroke definition, subtype and timing; distinguish incident stroke from vascular risk surrogates |
| **C · Eye–brain MRI** | [MRI / cerebral small-vessel disease](catalog/topics/C.md) | Same-person linkage to MRI, WMH or other CSVD measures |
| **D · Neurodegeneration** | [AD / cognition / dementia](catalog/topics/D.md) | Accessible diagnoses or cognitive measures linked to individual images |
| **E · Other neurology** | [Other neurological diseases](catalog/topics/E.md) | Disease-specific evidence, including MS and peripheral neuropathy |
| **F · Systemic health** | [Cardiometabolic disease / mortality](catalog/topics/F.md) | Individual clinical measures, events or follow-up outcomes |
| **G · Generalizable AI** | [Multicenter / multimodal resources](catalog/topics/G.md) | Useful imaging representations and domain variation; federation requires additional governance |

**Tier 1** = direct individual-level linkage evidence with an established image-access route. **Tier 2** = potentially valuable linkage with unresolved pixels, permissions or pairing. **Tier 3** = auxiliary imaging resources. Tiers are topic-specific and do not replace access approval. A published association alone does not establish that the raw images can be obtained.

## Choose a research direction

The two recommendation tracks answer different questions. **Scientific priority** favors relevant phenotypes, follow-up and cohort quality. **Near-term feasibility** adds explicit image/label access gates. Scores are transparent curatorial decision aids, not measures of model performance.

| Direction | Scientific priorities under the documented rubric | Feasible starting points in this snapshot |
|---|---|---|
| **Retinal Aging** | [UK Biobank](datasets/ext-uk-biobank.md), [ARIC](datasets/ext-aric.md), [CHS](datasets/ext-chs.md), [SCONe](datasets/ext-scone-scotland.md): tied scientific rank 1 | [GRAPE](datasets/grape.md), [China-Fundus-CIMT](datasets/china_fundus_cimt.md), [MCFI](datasets/ext-mcfi.md); see the [full near-term list](RANKINGS.md) |
| **Eye–Stroke** | [UK Biobank](datasets/ext-uk-biobank.md), [ARIC](datasets/ext-aric.md), [MESA](datasets/ext-mesa.md), [CHS](datasets/ext-chs.md): tied scientific rank 1 | **No resource passed all near-term gates for the image-linked stroke endpoint.** CIMT can support vascular-surrogate work, not stroke-outcome validation. |
| **Eye–Neurodegeneration** | [UK Biobank](datasets/ext-uk-biobank.md) ranks 1st, [ARIC](datasets/ext-aric.md) 2nd; [CHS](datasets/ext-chs.md) and [SCONe](datasets/ext-scone-scotland.md) tie at 3rd. The ranking distinguishes cross-sectional cognition from documented longitudinal endpoints. | [TREND2](datasets/trend2_fundus.md) and [functional OCT / AD](datasets/dryad_functional_oct_alzheimer.md) support small exploratory experiments; their labels, sample sizes and age information constrain validation. |

[All three rankings and five component scores](RANKINGS.md) · [scoring methods](library/METHODS.md) · [rankings CSV](library/output/rankings.csv).

### A few useful dataset cards

| Resource | What makes it useful | Read before designing the experiment |
|---|---|---|
| [GRAPE](datasets/grape.md) | 144 glaucoma participants, 263 eyes, 1,115 visits; 631 original fundus photographs and clinical information | Not every visit has a photograph. OCT-derived RNFL measurements are not raw OCT volumes. |
| [China-Fundus-CIMT](datasets/china_fundus_cimt.md) | 2,903 participants and 5,806 bilateral fundus images with individual age/CIMT metadata | Endocrinology inpatient cohort; CIMT is not a stroke event label. |
| [MCFI](datasets/ext-mcfi.md) | 37 people, 84 sessions and 442 JPEG images; useful for repeatability and visit-aware splits | Too small for broad population claims; a single image is not a longitudinal sequence. |
| [BRSET](datasets/brset.md) | 16,266 images from 8,524 patients, with age and systemic metadata | Credentialed PhysioNet access and DUA; age missingness needs handling. |
| [NHANES 2005–2008](datasets/ext-nhanes-2005-2008-retina.md) | Population survey with retinal grades, demographics and mortality linkage | Public grading tables do not establish public access to the original retinal photographs. |
| [AREDS2](datasets/ext-areds2.md) | Longitudinal trial images, clinical events and ancillary cognition resources | Apply the documented mapping and participant denominators; archive file counts are not counts of independent fundus photographs. |
| [SCONe](datasets/ext-scone-scotland.md) | Real-world optometry imaging with linked health records in Scotland | Secure project partnership and approved-team access; parent collection and linked subset have different denominators. |
| [ODIR](datasets/odir2019.md) | Bilateral fundus images and age/sex metadata from multiple collection sites | Verify organizer terms and patient grouping; a mirror's license cannot establish the original data license. |

For time-sensitive application routes and regional restrictions, open the current official policy linked in each resource card. The catalog records what was evidenced at the snapshot date.

## What the catalog contains

![Evidence tiers by topic, among 235 included resource records](assets/stats/topic_tiers.png)

Multi-label counts among **235 included resource records**; excluded records do not enter this figure. Topic G includes auxiliary resources and does not imply that all of them are multicenter cohorts. [Exact tables, access distribution and clinical-label coverage](STATS.md).

| Layer | Files | Purpose |
|---|---|---|
| GitHub reading | [`datasets/`](datasets), [`catalog/`](catalog/README.md), [gallery](assets/examples/README.md) | One resource per page, topic navigation, genuine examples |
| Queryable exports | [`library/output/`](library/output) | CSV, SQLite, topic judgments, phenotype states, evidence and relationships |
| Curation inputs | [`library/inputs/curation/`](library/inputs/curation), [`library/inputs/search/`](library/inputs/search) | Source-linked decisions and reproducible search log |
| Frozen baseline | [v0.7.0 manifest](library/inputs/v0.7.0/manifest.json), [original catalog](library/inputs/v0.7.0/hub/catalog.json) | All 451 original records with preserved IDs and SHA-256 checks |
| Rebuild tools | [`scripts/`](scripts), [`library/src/`](library/src) | Deterministic catalog generation and independent validation |

## Reproduce and update

Python 3.9+ rebuilds the metadata and Markdown without third-party packages:

```bash
python3 library/src/build.py
python3 library/src/verify.py
python3 scripts/build_catalog.py
python3 scripts/build_rankings.py
python3 scripts/verify_repo.py
```

Recreate the statistical figures with the pinned plotting dependencies:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-stats.txt
.venv/bin/python scripts/build_stats.py
```

The selected upstream metadata are preserved byte-for-byte with their manifest, source commit and individual SHA-256 hashes. The full upstream source archive, which also contains unrelated repository-search caches, is not bundled; it is not required for a rebuild. The repository includes only the five explicitly documented gallery assets as illustrative image examples. The offline search page and SQLite database need no server. See [maintenance instructions](CONTRIBUTING.md) and the [full survey methods](library/METHODS.md) for updating the snapshot without overwriting the baseline.

## Contribute and cite

Contributions should provide an official source, field-level evidence, access/permission scope and overlap information. [Suggest a resource or correction](https://github.com/ney777/awesome-retinal-aging-datasets/issues/new/choose) · [contribution guide](CONTRIBUTING.md).

When using a dataset, cite **its original publication and dataset release**, follow its terms, and acknowledge its creators. This catalog is a discovery aid and does not grant access to indexed datasets. [Citation metadata](CITATION.cff) · [license and third-party notices](LICENSE.md).

Built on [EyeDataHub](https://github.com/pooyakhosravi/EyeDataHub), with additional source review of population cohorts, aging, stroke, MRI, neurodegeneration and systemic outcomes. All uncertainty and exclusion decisions remain available for inspection.
