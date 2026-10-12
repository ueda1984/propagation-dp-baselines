"""Sparse/layered reference implementations for propagation-path DP.

The routines in this file mirror the layered finite-memory DP statements in the accompanying manuscript.
They deliberately use explicit sparse transition lists so the running time is
transparent in terms of |E_t| or |T_t| rather than dense M^2/M^3 arrays.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import inf
from typing import Iterable, List, Sequence, Tuple, Optional


@dataclass(frozen=True)
class Edge:
    src: int
    dst: int
    cost: float


@dataclass(frozen=True)
class TripleTransition:
    prev: int
    curr: int
    nxt: int
    cost: float


def pairwise_layered_dp(
    c_tx: Sequence[float],
    edge_layers: Sequence[Sequence[Edge]],
    c_rx: Sequence[float],
):
    """Exact single-best DP for a layer-dependent pairwise model.

    If there are R scattering objects, edge_layers has length R-1.
    Complexity is O(sum_t |E_t| + RM) for the transparent implementation;
    the transition work itself is O(sum_t |E_t|).
    """
    M = len(c_tx)
    if len(c_rx) != M:
        raise ValueError("c_tx and c_rx must have the same length")
    R = len(edge_layers) + 1

    prev = [float(x) for x in c_tx]
    parents: List[List[int]] = []

    for edges in edge_layers:
        curr = [inf] * M
        par = [-1] * M
        for e in edges:
            if not (0 <= e.src < M and 0 <= e.dst < M):
                raise IndexError("edge endpoint out of range")
            val = prev[e.src] + float(e.cost)
            if val < curr[e.dst]:
                curr[e.dst] = val
                par[e.dst] = e.src
        prev = curr
        parents.append(par)

    best_j = -1
    best = inf
    for j in range(M):
        val = prev[j] + float(c_rx[j])
        if val < best:
            best = val
            best_j = j
    if best_j < 0 or best == inf:
        return inf, None

    path = [best_j]
    j = best_j
    for par in reversed(parents):
        j = par[j]
        if j < 0:
            return inf, None
        path.append(j)
    path.reverse()
    assert len(path) == R
    return best, tuple(path)


def directional_layered_dp(
    M: int,
    initial_pairs: Sequence[Tuple[int, int, float]],
    triple_layers: Sequence[Sequence[TripleTransition]],
    end_cost,
):
    """Exact single-best ordered-pair DP for the direction-dependent model.

    initial_pairs contains allowed (i,j,c_init) states at the first two layers.
    Each subsequent triple layer contains allowed (i,j,k,cost) transitions from
    state (i,j) to state (j,k).  end_cost(i,j) is added at the receiver.

    Transition work is O(sum_t |T_t|).  State dictionaries store only reachable
    ordered pairs, so this implementation also exposes sparsity naturally.
    """
    if M < 1:
        raise ValueError("M must be positive")

    prev = {}
    for i, j, c in initial_pairs:
        if not (0 <= i < M and 0 <= j < M):
            raise IndexError("initial pair out of range")
        key = (i, j)
        c = float(c)
        if key not in prev or c < prev[key]:
            prev[key] = c

    parent_layers = []
    for transitions in triple_layers:
        curr = {}
        par = {}
        for tr in transitions:
            if not (0 <= tr.prev < M and 0 <= tr.curr < M and 0 <= tr.nxt < M):
                raise IndexError("triple endpoint out of range")
            old = (tr.prev, tr.curr)
            if old not in prev:
                continue
            new = (tr.curr, tr.nxt)
            val = prev[old] + float(tr.cost)
            if new not in curr or val < curr[new]:
                curr[new] = val
                par[new] = old
        prev = curr
        parent_layers.append(par)

    best_state = None
    best = inf
    for state, val0 in prev.items():
        val = val0 + float(end_cost(*state))
        if val < best:
            best = val
            best_state = state
    if best_state is None:
        return inf, None

    pairs = [best_state]
    st = best_state
    for par in reversed(parent_layers):
        st = par.get(st)
        if st is None:
            return inf, None
        pairs.append(st)
    pairs.reverse()

    # Convert overlapping pairs (v1,v2),(v2,v3),... into a vertex sequence.
    path = [pairs[0][0], pairs[0][1]]
    for a, b in pairs[1:]:
        if path[-1] != a:
            raise RuntimeError("inconsistent lifted-state reconstruction")
        path.append(b)
    return best, tuple(path)
