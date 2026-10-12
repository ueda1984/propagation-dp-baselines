"""Fast deterministic smoke tests for the public release package.

This does not replace the larger validation campaigns reported in the manuscript.
It is intended to catch packaging/API regressions after download or refactoring.
"""
from __future__ import annotations

from propagation_path_dp_reference import (
    brute_force_pairwise, dp_pairwise_kbest,
    brute_force_directional, dp_directional_kbest,
)
from propagation_qubo_equivalence import validate as validate_qubo
from synthetic_instances import make_pairwise_instance, make_directional_instance


def main():
    p = make_pairwise_instance(M=4, R=4, seed=1101)
    b = brute_force_pairwise(
        p["c_in"], p["c_edge"], p["c_out"], p["R"], p["allowed"], K=5
    )
    d = dp_pairwise_kbest(
        p["c_in"], p["c_edge"], p["c_out"], p["R"], p["allowed"], K=5
    )
    assert b == d, ("pairwise smoke mismatch", b, d)

    q = make_directional_instance(M=3, R=4, seed=2202)
    b = brute_force_directional(
        q["c_init"], q["c_triple"], q["c_end"], q["R"],
        q["allowed_pair"], q["allowed_triple"], K=5,
    )
    d = dp_directional_kbest(
        q["c_init"], q["c_triple"], q["c_end"], q["R"],
        q["allowed_pair"], q["allowed_triple"], K=5,
    )
    assert b == d, ("directional smoke mismatch", b, d)

    # One tiny instance exercises the all-degenerate-ground-state validator.
    assert validate_qubo(seed=3303, n=1) == 1

    print("release smoke tests: PASS")


if __name__ == "__main__":
    main()
