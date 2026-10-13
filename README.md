# Exact finite-memory DP for propagation-path models

Reference Python implementations accompanying the manuscript
*Exact classical baselines for QUBO-based multi-scattering radio-propagation path search*
(H. Ueda, S. Seo, S. Tsukano, and S. Miyakoshi; manuscript v0.32, October 2026).

**Software version:** 0.32.0. **License:** [BSD 3-Clause](LICENSE).
This reference code was prepared for independent numerical validation of the
manuscript under Hiroshi Ueda's direction, with AI assistance, rather than as
a deliverable from a NEDO or corporate joint/commissioned research project.
The software citation in [`CITATION.cff`](CITATION.cff) is distinct from the
four-author manuscript; it does not alter the paper's authorship.

## Scope

The code solves constrained discrete scattering-object sequence problems with
pairwise costs or direction-dependent three-object costs. It provides exact
single-best and ranked-path references and small-instance exhaustive enumerators.
It does **not** construct radio-propagation loss tables, validate geometrical
rays, reproduce any unpublished measurements, or demonstrate a quantum speedup.
Validation instances are synthetic examples of the mathematical model class,
not reconstructions of the original propagation studies.

## Files

| File | Purpose |
| --- | --- |
| `propagation_path_dp_reference.py` | Pairwise/directional single-best and K-best solvers; exhaustive references; random validation driver |
| `propagation_path_dp_layered.py` | Layer-dependent transitions and sparse-state interfaces |
| `propagation_qubo_equivalence.py` | Exact tiny penalty-QUBO enumeration, including degenerate ground states |
| `synthetic_instances.py` | Deterministic synthetic generators |
| `validate_release_smoke.py` | Packaging smoke checks |
| `tests/test_edge_cases.py` | Twelve additional regression tests |
| `run_validation.py` | Selectable smoke, edge, and full correctness suites (no timing benchmarks) |
| `validation_records/` | Historical-source checksums and clearly dated new validation records |
| `DATA_PROVENANCE.md` | Data origin, limitations, and validation-record distinctions |

The five inherited reference/source scripts were checked byte-for-byte against
recovered v0.22 reference sources. Some docstrings preserve their earlier
version names. Reference routines prioritize transparency over minimum memory:
for example, K-best implementations construct path tuples instead of realizing
the theoretical streaming-heap bound.

## Installation

Python and NumPy are required. Local validation of this preparation used
Python 3.13.5 and NumPy 2.3.5; see `requirements-tested.txt`. These are
recorded test conditions, **not** a claim of compatibility with every Python
version or operating system.

```bash
python -m pip install -r requirements.txt
```

## Reproduce the checks

```bash
python run_validation.py --mode smoke
python run_validation.py --mode edge
python run_validation.py --mode full
```

These commands write new machine-readable output into ignored `validation_output/`.
The full suite repeats 200 pairwise top-10, 100 direction-dependent top-10, and
30 tiny exact penalty-QUBO comparisons, using seed 20261006. A new full-suite
PASS record created on October 12, 2026 is retained at
`validation_records/v032_repository_full_20261012.json`. It is a new run,
**not** a reconstruction of historical individual-instance logs. Smoke and
edge checks passed independently; see the corresponding dated records.

Do not run `propagation_path_dp_reference.py` directly as a smoke test: its
`__main__` also launches timing benchmarks. Neither those timings nor the
structural counts in the paper constitute a quantum/classical speed comparison.

## Minimal example

```python
from synthetic_instances import make_pairwise_instance
from propagation_path_dp_reference import dp_pairwise_kbest

case = make_pairwise_instance(seed=20261006, M=4, R=4)
paths = dp_pairwise_kbest(
    case["c_in"], case["c_edge"], case["c_out"], case["R"],
    allowed=case["allowed"], K=5,
)
for cost, sequence in paths:
    print(cost, sequence)
```

Object labels are zero-based in the Python code and one-based in the paper.
Pairwise instances require R >= 1; directional instances require R >= 2.
The reference routines accept finite cost arrays and optional Boolean
feasibility masks. The paper's operation-count bounds assume explicit local
cost access; they exclude construction of the input tables, geometry checks,
and reconstruction storage.

## Data availability, citation and licensing

[`DATA_PROVENANCE.md`](DATA_PROVENANCE.md) identifies generated and unavailable
data. The full propagation-loss matrices for the published principal examples
were not available and are **not** included. These scripts reproduce correctness
checks for the specified mathematical model class, **not** complete
radio-propagation performance experiments.

All copyrightable original software, generated validation records, and
repository documentation are provided under the [BSD 3-Clause License](LICENSE)
as applicable. No license is granted for third-party source code or other
materials not included in this repository. The license imposes no requirement
to cite the associated scientific paper, but academic users are encouraged to
cite the manuscript and this software via [`CITATION.cff`](CITATION.cff).

For reproducible references, identify the **full Git commit SHA** of the
revision actually used: `git rev-parse HEAD`. A branch name by itself is not
an immutable software version. Do not add unpublished proprietary loss
matrices or annotated manuscript-review material.
