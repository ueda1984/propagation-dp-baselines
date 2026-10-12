# Exact finite-memory DP for propagation-path models

Private staging repository for reference code accompanying *Exact classical baselines for QUBO-based multi-scattering radio-propagation path search* (manuscript v0.32).

The implementation, synthetic test generators, regression tests, and provenance records have been prepared and locally checked; **they have not yet all been committed here**. The GitHub repository remains private pending agreement on software authorship, license, and public release.

## Local validation commands

Once files have been committed, install NumPy and run:

```bash
python -m pip install -r requirements.txt
python run_validation.py --mode smoke
python run_validation.py --mode edge
python run_validation.py --mode full
```

The first two validation modes passed locally before upload (smoke and 12 edge-case tests). The full mode is an optional new run of the published correctness campaigns, not a recovery of historical logs. The code does not generate published propagation-loss matrices and makes no quantum speedup claims.

## Release steps

Populate the repository from the prepared v0.32 code package, verify the files and tests in a clean clone, confirm contributor approval and software license, then publish a fixed commit or release. The journal Data Availability statement should be updated only after these steps.
