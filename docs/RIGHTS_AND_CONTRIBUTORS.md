# Rights, provenance and contributor clearance

**All cells marked 'pending' require human confirmation. Do not equate the four paper authors with the copyright holders of code.**

## Existing package provenance

| Material | What is currently known | Release check |
| --- | --- | --- |
| Five reference/source Python scripts | Recovered from previously prepared v0.22 code packages; unchanged in the private v0.32 repository. Ueda confirms these were newly prepared under his direction with AI assistance, without reuse of pre-existing SoftBank/RIKEN source code | Independent review for other third-party material, rights ownership, and institution obligations **Pending** |
| `run_validation.py` and twelve additional tests | Developed in the manuscript/release-preparation workflow under Ueda's direction with AI assistance (author-confirmed provenance) | Legal rights and institution obligations **Pending** |
| Synthetic local-cost generators | Model-level synthetic data; **not** published propagation-loss inputs | Any sensitive assumptions or external data? **Pending** |
| Dated JSON validation records | Outputs from explicitly documented synthetic correctness runs | Consent to publish records, and any desired separate data license **Pending** |
| Manuscript authors | Hiroshi Ueda, Shun Seo, Satoyuki Tsukano, Shohei Miyakoshi | Publication approval and credit for each person **Pending** |
| Employers/funders | University of Osaka, RIKEN R-CCS, SoftBank; NEDO noted in the paper | Any institutional, contract, funding, patent or disclosure approvals? **Pending** |

## Source-origin confirmation (corresponding author, 2026-10-12)

The corresponding author, Hiroshi Ueda, confirmed that the Python reference code was newly developed under his direction with AI assistance, **not by reusing existing SoftBank or RIKEN source code**. This statement is a description of provenance supplied by the corresponding author; it is not an independent line-by-line third-party code audit.

This narrows the outstanding provenance questions but **does not establish legal copyright ownership** or grant permission to release under BSD-3-Clause. Employment/commissioned-work rules, institutional policies, agreements, possible third-party material, AI-assisted-code considerations, attribution, and confidentiality still require applicable review.

No permission from any organization is inferred from the manuscript affiliation or from the creation of this private GitHub repository.

## Questions for code contributors and rights owners

- Did you author or adapt any part of the scripts? If so, which files and under which employment/institutional conditions?
- Does any file contain third-party code, restricted datasets, proprietary geometry/loss tables, unpublished industrial results, or material subject to a patent/confidentiality agreement?
- Are there required notices/attributions, a software export or disclosure process, or restrictions on royalty-free commercial redistribution?
- Can the confirmed rights holder(s) license the complete source package under BSD-3-Clause, including future commercial and closed-source downstream uses?
- Which people or organizations should be credited in the software metadata? Please give their preferred English names and spelling.
- For numerical validation JSON records, is a separate open-data dedication (e.g., CC0) desired? This is **not** decided here.
- Do the coauthors approve public availability of this exact code and record set, clearly described as synthetic model-level validation rather than reproduction of published propagation-loss matrices?

## Decision record (do not fill from inference)

| Item | Decision | Evidence (email/meeting/document) | Date |
| --- | --- | --- | --- |
| Code origin: AI-assisted new development directed by Ueda; no reused SoftBank/RIKEN existing source | **Confirmed by corresponding author (not independently audited)** | Direct confirmation in research conversation | 2026-10-12 |
| Confirmed software copyright holder(s) | **Pending** | | |
| Permission to license under BSD-3-Clause | **Pending** | | |
| Ueda author/publication sign-off | **Pending** | | |
| Seo author/publication sign-off | **Pending** | | |
| Tsukano author/publication sign-off | **Pending** | | |
| Miyakoshi author/publication sign-off | **Pending** | | |
| Institutional/company reviews, if required | **Pending** | | |
| Code third-party/confidentiality check | **Pending** | | |
| Software citation-author list | **Pending** | | |
| Synthetic validation-data license, if separate | **Pending** | | |

Only after the applicable items are approved should the placeholder in the license template be resolved and the root `LICENSE` file created.
