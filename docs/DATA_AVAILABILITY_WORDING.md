# Manuscript Data Availability and code citation (review draft)

**Status: private prepublication review. Neither a public code release nor software DOI exists yet.**

APS author policy: https://journals.aps.org/authors/data-availability-statements

APS requires a Data Availability Statement for Physical Review papers and explicitly asks for public data/software cited both **in the reference list and in the statement**. An anonymous-access URL, fixed revision, and actual bibliographic entry are needed once this repository becomes public.

## Private-repository version (for internal manuscript review only)

> The reference code, synthetic-instance generators, validation scripts, and machine-readable records are held in a private GitHub repository. They are available from the corresponding author upon reasonable request while release permission is finalized. A citable fixed revision will be added after public release. The structural counts are in Table III. The tests use synthetic local costs; complete propagation-loss matrices for the published examples were unavailable and were not used.

This is a draft; it must not be represented as an unconditional permission to redistribute. Use it in an APS submission only if the corresponding author can actually provide the indicated code and data to editors, reviewers, and readers upon reasonable request. The v0.32 original manuscript/source remains unchanged.

## After a public code release has been verified

> The Python reference implementations, deterministic synthetic-instance generators, and numerical validation scripts and records are publicly available in the archived code release, Ref. [CODE CITATION]. The tests use synthetic local-cost instances rather than reconstructions of the complete propagation-loss matrices from the principal published examples, which were unavailable for this work. The structural operation counts follow directly from the expressions in Table III.

**In the final LaTeX file:** replace `Ref. [CODE CITATION]` with an actual citation such as `Ref.~\\cite{PropagationDPCode2026}` and add the verified software-release record to the English (and Japanese check) BibTeX databases; regenerate the `.bbl` and PDF. Confirm journal style for arXiv and accepted manuscript.

## BibTeX entry skeleton — NOT A REAL RELEASE CITATION

The following is deliberately not directly valid without replacing the placeholders.

```bibtex
@misc{PropagationDPCode2026,
  author       = {<APPROVED SOFTWARE AUTHOR(S)>},
  title        = {Exact finite-memory dynamic programming for propagation-path models},
  year         = {2026},
  howpublished = {Code repository and reproducibility materials},
  url          = {https://github.com/ueda1984/propagation-dp-baselines/tree/<FULL-RELEASE-COMMIT>},
  note         = {Version <APPROVED VERSION>; accessed <DATE>}
}
```

If a Zenodo archive DOI is minted, cite the **actual** corresponding version DOI instead (and its authors/metadata) and give the URL in the Data Availability statement as appropriate. Do not invent a tag, DOI or software author list. A mere `main` branch is not a fixed release.

## Publication gates

- Confirm root BSD-3-Clause `LICENSE` and copyright notice with the authorized rights holder(s).
- Confirm coauthors' approval and any actual institutional restrictions.
- Confirm CI and manual QA on the intended public release revision.
- Verify the repository is accessible without GitHub login.
- Fix a commit or release version; optionally archive to Zenodo; update `CITATION.cff`.
- Insert the matching bibliographic reference and final Data Availability in the manuscript and submission metadata.
