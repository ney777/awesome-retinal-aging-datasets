# Changelog

## 0.1.2 — 2026-11-06 (publication safety)

- Minimized sample provenance metadata: omitted source member names containing study/patient codes or precise acquisition timestamps while retaining provider releases, licenses and image SHA-256 hashes. No image pixels were modified.
- Added a publication guard against tracked credentials, local backups, full upstream archives and high-confidence secret patterns. Pattern checks do not certify clinical anonymization.
- Replaced main in the existing repository with a clean root and retained an intentional local private backup. A subsequent authenticated probe showed that GitHub still serves the old commit and sample manifest. Remote execution and server-retention checks are recorded in [publication safety](audit/2026-11-06/PUBLICATION_SAFETY.md); this entry does not claim that all GitHub caches have been purged.

## 0.1.1 — 2026-11-06 (public-release review)

- Corrected CHS and AGES neurodegeneration relevance from 4 to 3 because the scored cognitive/dementia evidence is cross-sectional. Task-specific follow-up exclusions now affect both label richness and the follow-up quality point. Neuro scientific scores change from 91.25 to 81.25 (CHS) and 92.5 to 76.25 (AGES); all rankings were regenerated.
- Added ARIC's commercial-use restriction and CHS's consent-dependent commercial/research-area conditions with source-specific review dates, preserving the original resource-level review dates.
- Clarified code MIT versus catalog/documentation CC BY 4.0 licensing, upstream attribution, and the individual image licenses. CIMT image descriptions now distinguish unchanged release bytes from publisher preprocessing.
- Removed the full 44,717,463-byte upstream archive from the publication tree because it includes unrelated repository-search caches. Kept all selected metadata, original IDs, file hashes and provenance; rebuilding no longer requires the archive. Historical commits require separate cleanup before making the existing repository public.
- Added a bounded HEAD-only landing-link audit. HTTP reachability does not establish data access, licensing or downloadable image availability.
- No dataset added or removed: 479 resource records, 235 included, 244 excluded and 49 source-reviewed. The base survey remains 2026-11-03; this is a targeted correction release.

## 0.1.0 — 2026-11-04

- Initial GitHub edition with English and Chinese home pages, 479 individual resource cards, seven topic directories, reviewed and exclusion indexes.
- Preserved the 451-record EyeDataHub v0.7.0 baseline and 28 supplementary resources; 49 priority records source-reviewed as of 2026-11-03.
- Added a five-source image gallery with per-file provenance, licensing, attribution and checksums: China-Fundus-CIMT, FDR26, MCFI, OCTDL and a complete GRAPE publication figure.
- Added topic-tier, access-route and clinical-phenotype statistics with explicit denominators and source CSV hashes.
- Published three research rankings with separate scientific and near-term feasibility scores, ties and access gates.
- Included the offline searchable viewer, CSV and SQLite exports, original curation/search inputs, frozen upstream archive and reproducible build/validation scripts.
- Configured a read-only GitHub Actions check for metadata, generated Markdown and local asset integrity. No scheduled data acquisition or dataset agreement acceptance.
