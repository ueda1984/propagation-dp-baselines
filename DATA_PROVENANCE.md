# Data provenance and limits

The reported numerical validation tests are **synthetic**, not reconstructed
radio-propagation benchmark instances.  The published principal examples' full
loss matrices were not available to the authors, and none are included here.

- `synthetic_instances.py` supplies deterministic example-instance generators.
- `run_validation.py --mode full` reruns the correctness campaigns for the
  mathematical model class (pairwise top-10: 200 tests; directional top-10:
  100 tests; tiny penalty-QUBO: 30 tests) using seed `20261006`.  This creates
  a **new** run log, not an authenticated recovery of the historical log.
- `run_validation.py --mode smoke` and `--mode edge` exercise packaging and
  boundary cases without running the full correctness campaign or benchmarks.
- `validation_records/` contains historical provenance and preparation-time
  records.  Consult the JSON `note`, timestamps, and source hashes; do not
  combine counts from distinct campaigns.
- A new full-suite verification log for this repository preparation is stored as `validation_records/v032_repository_full_20261012.json` (200 pairwise, 100 directional, 30 QUBO checks; all passed). It is not the missing historical per-instance log.
- Table III in the manuscript reports exact combinatorial/transition counts
  computed from specified expressions, not execution times.

No third-party publication PDFs, unpublished corporate data, real propagation
loss tables, or annotated review manuscripts are included.  Publication of
this repository, the software license, and contributor/citation metadata require
approval of the relevant owners and authors.
