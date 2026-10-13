# Proposed license: BSD 3-Clause

**Status (October 2026): selected in principle by the lead author; NOT YET ACTIVATED.**

We intend to publish the reference Python implementations under the permissive BSD 3-Clause license (SPDX identifier `BSD-3-Clause`) after verifying authority to license the work. The private repository currently has **no effective root `LICENSE` file** and should not be described as open source yet.

Official terms: https://opensource.org/license/bsd-3-clause and https://spdx.org/licenses/BSD-3-Clause.html

## Confirmed purpose and remaining ownership question

On 2026-10-13 the corresponding author clarified that this code was developed **separately for numerical validation of the manuscript**, rather than as a deliverable under NEDO, SoftBank or other joint/commissioned research agreements. This supplements the 2026-10-12 statement that the reference code was prepared under Ueda's direction with AI assistance and without reusing existing corporate or RIKEN source.

This makes contract-deliverable and source-reuse questions less pertinent to this particular package, but does **not** establish who legally holds copyright or whether an academic employer's general policies apply. Do not infer institution-wide consent to public distribution. The provisional BSD-3-Clause choice is not operative until the actual rightsholder(s) authorize it.

## Scope and consequences

- Allows use, copying, modification, source/binary redistribution, and commercial use under three conditions: retaining source notices, reproducing notices for binary distributions, and no endorsement through use of author/contributor names without written permission.
- Does **not** require derivative software to be published or changes to be contributed back.
- Does **not** impose a legal obligation to cite the accompanying scientific paper. Give users a correct citation through `CITATION.cff` and the README, separate from license obligations.
- BSD-3-Clause contains **no express patent-license grant**. Review any overlapping employer, patent, confidentiality or consortium requirements. This repository's illustrative algorithmic implementations and synthetic test scripts must not be taken to confer rights to underlying third-party patented technologies.
- This is the proposed **software** license. The terms for generated validation data/records and the manuscript/arXiv paper must be considered separately. Do not apply a data license or an arXiv license merely by choosing BSD-3-Clause for software.

## Before adding an effective `LICENSE`

1. The corresponding author confirmed on 2026-10-12 that the Python code was newly developed under his direction with AI assistance, with no pre-existing SoftBank/RIKEN source reused. **This is a provenance statement, not an independent code audit or a copyright determination.** Determine the copyright owner(s) and whether University of Osaka/RIKEN/SoftBank employment, existing packages, collaboration agreements, funding conditions, or third-party rights impose approval requirements.
2. Ask each manuscript coauthor (Ueda, Seo, Tsukano, Miyakoshi) to review the public code/data package and disclose contributions, third-party material and confidentiality concerns. **Manuscript authorship does not imply software ownership.**
3. Identify the correct holder(s) for `Copyright (c) 2026, <verified copyright holder(s)>` and confirm that they authorize licensing under BSD-3-Clause.
4. Verify the package contains only self-generated synthetic examples/validation records, code intended for public release, and no confidential loss tables or unpublished proprietary inputs.
5. Finalize `CITATION.cff` with verified software authors and any public article citation; do not assume its provisional single-author entry establishes ownership.
6. After confirmation, place a copy of the **standard unmodified BSD-3-Clause text** in root `LICENSE`, with the approved holder notice, and remove/replace `LICENSE_DECISION_REQUIRED.md`.
7. Run the tests from a clean clone of the intended release commit, make the repository public, confirm anonymous access, create a fixed release tag or archive DOI, and then update the paper's Data Availability text.

The draft in `BSD_3_CLAUSE_LICENSE_DRAFT.txt` is not intended to function as an operative license; it is for review of wording only.
