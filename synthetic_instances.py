"""Deterministic synthetic instances for the finite-memory propagation-path models.

These generators are intentionally model-level rather than geometry/ray-tracing
generators.  They create local costs and local feasibility masks for testing the
exact dynamic programs described in the accompanying manuscript.
"""
from __future__ import annotations

import numpy as np


def make_pairwise_instance(
    *, seed: int = 20261006, M: int = 5, R: int = 5,
    edge_density: float = 0.8, forbid_self: bool = True,
):
    """Return a deterministic synthetic pairwise finite-memory instance."""
    if M < 1 or R < 1:
        raise ValueError("M and R must be positive")
    rng = np.random.default_rng(seed)
    c_in = rng.integers(0, 1000, M, endpoint=False).astype(float)
    c_out = rng.integers(0, 1000, M, endpoint=False).astype(float)
    c_edge = rng.integers(0, 1000, (M, M), endpoint=False).astype(float)
    allowed = rng.random((M, M)) < edge_density
    if forbid_self:
        np.fill_diagonal(allowed, False)
    return {
        "M": M, "R": R, "c_in": c_in, "c_edge": c_edge,
        "c_out": c_out, "allowed": allowed, "seed": seed,
    }


def make_directional_instance(
    *, seed: int = 20261007, M: int = 4, R: int = 5,
    pair_density: float = 0.9, triple_density: float = 0.8,
    forbid_self: bool = True, forbid_backtrack: bool = True,
):
    """Return a deterministic synthetic ordered-pair/directional instance."""
    if M < 1 or R < 2:
        raise ValueError("directional instances require M >= 1 and R >= 2")
    rng = np.random.default_rng(seed)
    c_init = rng.integers(0, 1000, (M, M), endpoint=False).astype(float)
    c_end = rng.integers(0, 1000, (M, M), endpoint=False).astype(float)
    c_triple = rng.integers(0, 1000, (M, M, M), endpoint=False).astype(float)

    allowed_pair = rng.random((M, M)) < pair_density
    if forbid_self:
        np.fill_diagonal(allowed_pair, False)

    allowed_triple = rng.random((M, M, M)) < triple_density
    if forbid_backtrack:
        for i in range(M):
            for j in range(M):
                allowed_triple[i, j, i] = False

    return {
        "M": M, "R": R, "c_init": c_init, "c_triple": c_triple,
        "c_end": c_end, "allowed_pair": allowed_pair,
        "allowed_triple": allowed_triple, "seed": seed,
    }
