# Software release notes: 0.32.0

Corresponding manuscript: *Exact classical baselines for QUBO-based
multi-scattering radio-propagation path search* (manuscript v0.32).

## Scope

- Exact pairwise and directional finite-memory path-selection reference routines.
- Exact enumeration comparisons, layered/sparse-state examples, and tiny penalty-QUBO checks.
- Deterministic synthetic local-cost generators and dated validation records.
- BSD 3-Clause license, software citation metadata, and GitHub Actions CI.

## Reproducibility checks

The release-validation campaign verifies 200 pairwise, 100 directional, and 30
tiny QUBO instances against exact enumeration. Packaging smoke and 12 edge-case
tests were also run. The numerical tests are synthetic and **do not** reproduce
unavailable full propagation-loss matrices, geometrical ray validation, or
quantum speedup claims.

Use the exact published Git commit identifier, not just `0.32.0`, when
citing a revision. No archive DOI is claimed until issued by an actual archive.
