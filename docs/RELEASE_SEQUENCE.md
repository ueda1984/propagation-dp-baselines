# Release gates: private review to citable public code

**Current state: private; documentation/rights review in progress.**

1. **[x]** Create a private repository and upload source, tests, and validation records.
2. **[x]** Verify SHA-256 hashes and run smoke, 12 edge tests, and 200/100/30 synthetic correctness checks locally on the supplied code package. These are new runs, not historical-log recovery.
2a. **[x]** Obtain corresponding author's statement that the code was newly developed under his direction using AI assistance and did not reuse existing SoftBank/RIKEN source. This does **not** finish the legal-rights or independent third-party-content checks.
2b. **[x]** Corresponding author confirms that the code was separately developed for numerical verification of this paper, not as an NEDO/SoftBank or other joint/commissioned-research deliverable (2026-10-13). Any applicable employment-policy or rights-holder question remains open.
2c. **[x]** Add GitHub Actions smoke, edge, full mathematical validation and manifest checks on Python 3.11 and 3.13. Both matrix jobs passed in private draft PR (run 38360411740); final release commit must still be checked.
3. **[ ]** Review ownership, institutional obligations, patents and confidentiality; record source provenance and clear every contributor/rightsholder.
4. **[ ]** Approve BSD-3-Clause commercial-use implications, copyright holder notice, and package scope; decide if synthetic data records need a separate data license.
5. **[ ]** Finalize `CITATION.cff` (software author credits) and make a real root `LICENSE` (not the private draft).
6. **[ ]** Test the exact intended public commit from a clean clone; compare results with retained validation records, verify no secrets/sensitive inputs or inappropriate materials.
7. **[ ]** Change repository visibility to Public and verify anonymous reading.
8. **[ ]** Create a named immutable/archivable version (release tag, full commit, and optionally Zenodo DOI). Note that a branch name alone is not a fixed version.
9. **[ ]** Insert the real release citation into both BibTeX and Data Availability per APS policy; regenerate the English manuscript and Japanese check proof.
10. **[ ]** Secure final approval of all paper authors and submit.

The manuscript's v0.32 scientific results, formulas and figures should not be modified as part of a license decision. The code repository is not public simply because GitHub is reachable by the owner.
