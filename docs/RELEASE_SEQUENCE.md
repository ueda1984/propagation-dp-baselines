# Release gates: private review to citable public code

**Current state: private; documentation/rights review in progress.**

1. **[x]** Create a private repository and upload source, tests, and validation records.
2. **[x]** Verify SHA-256 hashes and run smoke, 12 edge tests, and 200/100/30 synthetic correctness checks locally on the supplied code package. These are new runs, not historical-log recovery.
3. **[ ]** Review ownership, institutional obligations, patents and confidentiality; record source provenance and clear every contributor/rightsholder.
4. **[ ]** Approve BSD-3-Clause commercial-use implications, copyright holder notice, and package scope; decide if synthetic data records need a separate data license.
5. **[ ]** Finalize `CITATION.cff` (software author credits) and make a real root `LICENSE` (not the private draft).
6. **[ ]** Test the exact intended public commit from a clean clone; compare results with retained validation records, verify no secrets/sensitive inputs or inappropriate materials.
7. **[ ]** Change repository visibility to Public and verify anonymous reading.
8. **[ ]** Create a named immutable/archivable version (release tag, full commit, and optionally Zenodo DOI). Note that a branch name alone is not a fixed version.
9. **[ ]** Insert real release URL/revision into the paper's Data Availability section; regenerate publication source and proof.
10. **[ ]** Secure final approval of all paper authors and submit.

The manuscript's v0.32 scientific results, formulas and figures should not be modified as part of a license decision. The code repository is not public simply because GitHub is reachable by the owner.
