# CI and synthetic validation

The workflow file `.github/workflows/validation.yml` runs with read-only `contents` permission and with no credentials passed to project tests. It is currently staged in private draft PR #2; merging/publication is subject to release review.

## Verified October 13, 2026

- [GitHub Actions pull-request run 38360411740](https://github.com/ueda1984/propagation-dp-baselines/actions/runs/38360411740): **success**.
- Matrix jobs: **Python 3.11 PASS; Python 3.13 PASS**.
- Each job: NumPy dependency installation, `sha256sum -c SHA256SUMS.txt`, Python syntax compilation, packaging smoke test, 12 edge-condition tests, and full correctness check (200 pairwise, 100 directional, and 30 tiny penalty-QUBO instances).
- An independent push-triggered run 38360410547 also completed successfully.

Passing these suites establishes correspondence against exact enumeration for **synthetic instances of the stated finite-memory models only**. It is not validation of actual electromagnetic attenuation data or ray tracing, and not a quantum/classical performance comparison.

The manifest `SHA256SUMS.txt` covers the 22 original source/metadata/record files; the CI workflow and release-review documents are not covered by that original manifest. A final archived release should regenerate and verify a full manifest **after** copyright/attribution metadata and license files are finalized.

## Final public-release checks (pending)

- [ ] Review correct attribution and license.
- [ ] Approve all final code/data files for public release.
- [ ] Merge any approved changes and rerun CI on the **actual release commit**.
- [ ] Confirm anonymous reading, fixed commit/tag, DOI if generated, and matching APS code citation.
