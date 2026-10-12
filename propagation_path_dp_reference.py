
from __future__ import annotations
import itertools
import time
import numpy as np


def _topk_unique(candidates, k):
    best = {}
    for c, p in candidates:
        p = tuple(p)
        c = float(c)
        if p not in best or c < best[p]:
            best[p] = c
    return sorted(((c, p) for p, c in best.items()), key=lambda x: (x[0], x[1]))[:k]


def brute_force_pairwise(c_in, c_edge, c_out, R, allowed=None, K=1):
    c_in = np.asarray(c_in, dtype=float)
    c_edge = np.asarray(c_edge, dtype=float)
    c_out = np.asarray(c_out, dtype=float)
    M = len(c_in)
    allowed = np.ones((M, M), dtype=bool) if allowed is None else np.asarray(allowed, dtype=bool)

    cand = []
    for p in itertools.product(range(M), repeat=R):
        if not all(allowed[p[t], p[t+1]] for t in range(R-1)):
            continue
        cost = c_in[p[0]] + c_out[p[-1]]
        cost += sum(c_edge[p[t], p[t+1]] for t in range(R-1))
        cand.append((float(cost), tuple(p)))
    return _topk_unique(cand, K)


def dp_pairwise(c_in, c_edge, c_out, R, allowed=None):
    if R < 1:
        raise ValueError("Pairwise model requires R >= 1.")
    c_in = np.asarray(c_in, dtype=float)
    c_edge = np.asarray(c_edge, dtype=float)
    c_out = np.asarray(c_out, dtype=float)
    M = len(c_in)
    allowed = np.ones((M, M), dtype=bool) if allowed is None else np.asarray(allowed, dtype=bool)

    prev = c_in.copy()
    parent = np.full((R, M), -1, dtype=np.int32)
    masked_edge = np.where(allowed, c_edge, np.inf)

    for t in range(1, R):
        scores = prev[:, None] + masked_edge
        par = np.argmin(scores, axis=0)
        curr = scores[par, np.arange(M)]
        parent[t] = par
        prev = curr

    final = prev + c_out
    j = int(np.argmin(final))
    best_cost = float(final[j])
    if not np.isfinite(best_cost):
        return float("inf"), None

    path = [j]
    for t in range(R - 1, 0, -1):
        j = int(parent[t, j])
        path.append(j)
    path.reverse()
    return best_cost, tuple(path)


def dp_pairwise_kbest(c_in, c_edge, c_out, R, allowed=None, K=10):
    c_in = np.asarray(c_in, dtype=float)
    c_edge = np.asarray(c_edge, dtype=float)
    c_out = np.asarray(c_out, dtype=float)
    M = len(c_in)
    allowed = np.ones((M, M), dtype=bool) if allowed is None else np.asarray(allowed, dtype=bool)

    states = [[(float(c_in[j]), (j,))] for j in range(M)]

    for _ in range(1, R):
        nxt = [[] for _ in range(M)]
        for i in range(M):
            js = np.flatnonzero(allowed[i])
            for pcost, ppath in states[i]:
                for j in js:
                    nxt[j].append((pcost + float(c_edge[i, j]), ppath + (int(j),)))
        states = [_topk_unique(lst, K) for lst in nxt]

    final = []
    for j in range(M):
        for pcost, ppath in states[j]:
            final.append((pcost + float(c_out[j]), ppath))
    return _topk_unique(final, K)


def brute_force_directional(c_init, c_triple, c_end, R,
                            allowed_pair=None, allowed_triple=None, K=1):
    """
    Exact enumeration for validation only.

    Adjacent-pair feasibility is encoded by allowed_pair[i,j].  Additional
    second-order restrictions (for example immediate i->j->i backtracking)
    are encoded by allowed_triple[i,j,k].
    """
    if R < 2:
        raise ValueError("Directional model requires R >= 2.")
    c_init = np.asarray(c_init, dtype=float)
    c_triple = np.asarray(c_triple, dtype=float)
    c_end = np.asarray(c_end, dtype=float)
    M = c_init.shape[0]
    allowed_pair = (
        np.ones((M, M), dtype=bool)
        if allowed_pair is None
        else np.asarray(allowed_pair, dtype=bool)
    )
    allowed_triple = (
        np.ones((M, M, M), dtype=bool)
        if allowed_triple is None
        else np.asarray(allowed_triple, dtype=bool)
    )

    cand = []
    for p in itertools.product(range(M), repeat=R):
        if not all(allowed_pair[p[t], p[t+1]] for t in range(R-1)):
            continue
        if R >= 3 and not all(
            allowed_triple[p[t-1], p[t], p[t+1]]
            for t in range(1, R-1)
        ):
            continue
        cost = float(c_init[p[0], p[1]] + c_end[p[-2], p[-1]])
        cost += sum(float(c_triple[p[t-1], p[t], p[t+1]]) for t in range(1, R-1))
        cand.append((cost, tuple(p)))
    return _topk_unique(cand, K)


def dp_directional(c_init, c_triple, c_end, R,
                   allowed_pair=None, allowed_triple=None):
    """
    Exact ordered-pair-state DP.

    Adjacent-pair constraints are enforced by allowed_pair; genuinely
    second-order constraints are enforced by allowed_triple.

    Dense worst-case complexity: O(R M^3).
    More naturally: O(sum_t |T_t|) for the allowed lifted transitions.
    """
    if R < 2:
        raise ValueError("Directional model requires R >= 2.")
    c_init = np.asarray(c_init, dtype=float)
    c_triple = np.asarray(c_triple, dtype=float)
    c_end = np.asarray(c_end, dtype=float)
    M = c_init.shape[0]
    allowed_pair = (
        np.ones((M, M), dtype=bool)
        if allowed_pair is None
        else np.asarray(allowed_pair, dtype=bool)
    )
    allowed_triple = (
        np.ones((M, M, M), dtype=bool)
        if allowed_triple is None
        else np.asarray(allowed_triple, dtype=bool)
    )

    prev = np.where(allowed_pair, c_init, np.inf)

    if R == 2:
        final = prev + c_end
        i, j = np.unravel_index(np.argmin(final), final.shape)
        best_cost = float(final[i, j])
        if not np.isfinite(best_cost):
            return float("inf"), None
        return best_cost, (int(i), int(j))

    parents = []
    for _ in range(2, R):
        curr = np.full((M, M), np.inf)
        par = np.full((M, M), -1, dtype=np.int32)
        for j in range(M):
            scores = prev[:, j][:, None] + c_triple[:, j, :]
            mask = allowed_triple[:, j, :] & allowed_pair[j, :][None, :]
            scores = np.where(mask, scores, np.inf)
            best_i = np.argmin(scores, axis=0)
            curr[j, :] = scores[best_i, np.arange(M)]
            par[j, :] = best_i
        prev = curr
        parents.append(par)

    final = prev + c_end
    i, j = np.unravel_index(np.argmin(final), final.shape)
    best_cost = float(final[i, j])
    if not np.isfinite(best_cost):
        return float("inf"), None

    path = [int(i), int(j)]
    for par in reversed(parents):
        h = int(par[path[0], path[1]])
        path.insert(0, h)
    return best_cost, tuple(path)


def dp_directional_kbest(c_init, c_triple, c_end, R,
                         allowed_pair=None, allowed_triple=None, K=10):
    """Transparent exact K-best DP for the direction-dependent model."""
    if R < 2:
        raise ValueError("Directional model requires R >= 2.")
    c_init = np.asarray(c_init, dtype=float)
    c_triple = np.asarray(c_triple, dtype=float)
    c_end = np.asarray(c_end, dtype=float)
    M = c_init.shape[0]
    allowed_pair = (
        np.ones((M, M), dtype=bool)
        if allowed_pair is None
        else np.asarray(allowed_pair, dtype=bool)
    )
    allowed_triple = (
        np.ones((M, M, M), dtype=bool)
        if allowed_triple is None
        else np.asarray(allowed_triple, dtype=bool)
    )

    states = [[[] for _ in range(M)] for _ in range(M)]
    for i in range(M):
        for j in range(M):
            if allowed_pair[i, j]:
                states[i][j] = [(float(c_init[i, j]), (i, j))]

    for _ in range(2, R):
        nxt = [[[] for _ in range(M)] for _ in range(M)]
        for i in range(M):
            for j in range(M):
                ks = np.flatnonzero(allowed_triple[i, j] & allowed_pair[j])
                for pcost, ppath in states[i][j]:
                    for k in ks:
                        nxt[j][k].append(
                            (pcost + float(c_triple[i, j, k]), ppath + (int(k),))
                        )
        states = [[_topk_unique(nxt[i][j], K) for j in range(M)] for i in range(M)]

    final = []
    for i in range(M):
        for j in range(M):
            for pcost, ppath in states[i][j]:
                final.append((pcost + float(c_end[i, j]), ppath))
    return _topk_unique(final, K)


def validate_random(seed=0, n_pairwise=200, n_directional=100, K=10):
    """
    Uses integer random costs so ties are exact rather than floating-roundoff artifacts.
    Compares complete ranked (cost,path) lists from exhaustive search and DP.
    """
    rng = np.random.default_rng(seed)

    pair_ok = 0
    for _ in range(n_pairwise):
        M = int(rng.integers(3, 6))
        R = int(rng.integers(2, 6))
        # Add random integer offsets to make accidental ties less common but exactly representable.
        c_in = rng.integers(0, 1000, M)
        c_out = rng.integers(0, 1000, M)
        c_edge = rng.integers(0, 1000, (M, M))
        allowed = rng.random((M, M)) < 0.8
        np.fill_diagonal(allowed, False)

        b = brute_force_pairwise(c_in, c_edge, c_out, R, allowed, K)
        d = dp_pairwise_kbest(c_in, c_edge, c_out, R, allowed, K)
        if b != d:
            raise AssertionError(("pairwise mismatch", M, R, b, d))
        pair_ok += 1

    dir_ok = 0
    for _ in range(n_directional):
        M = int(rng.integers(3, 5))
        R = int(rng.integers(2, 6))
        c_init = rng.integers(0, 1000, (M, M))
        c_end = rng.integers(0, 1000, (M, M))
        c_triple = rng.integers(0, 1000, (M, M, M))
        allowed_pair = rng.random((M, M)) < 0.9
        np.fill_diagonal(allowed_pair, False)
        allowed_triple = rng.random((M, M, M)) < 0.8

        # Representative second-order restriction: no immediate i->j->i backtracking.
        for i in range(M):
            for j in range(M):
                allowed_triple[i, j, i] = False

        b = brute_force_directional(
            c_init, c_triple, c_end, R,
            allowed_pair=allowed_pair, allowed_triple=allowed_triple, K=K
        )
        d = dp_directional_kbest(
            c_init, c_triple, c_end, R,
            allowed_pair=allowed_pair, allowed_triple=allowed_triple, K=K
        )
        if b != d:
            raise AssertionError(("directional mismatch", M, R, b, d))
        dir_ok += 1

    return {
        "pairwise_instances_passed": pair_ok,
        "directional_instances_passed": dir_ok,
        "K": K,
    }


def benchmark_pairwise(M_values=(10,20,50,100,200,500,1000), R=9, seed=1, repeats=5):
    rng = np.random.default_rng(seed)
    rows = []
    for M in M_values:
        c_in = rng.random(M)
        c_out = rng.random(M)
        c_edge = rng.random((M, M))
        allowed = np.ones((M, M), dtype=bool)
        np.fill_diagonal(allowed, False)

        times = []
        ans = None
        for _ in range(repeats):
            t0 = time.perf_counter()
            ans = dp_pairwise(c_in, c_edge, c_out, R, allowed)
            times.append(time.perf_counter() - t0)

        candidate_count = M * ((M - 1) ** (R - 1))
        transition_evals = (R - 1) * M * (M - 1)
        rows.append({
            "M": M,
            "R": R,
            "candidate_sequences": candidate_count,
            "DP_transition_evals": transition_evals,
            "median_seconds": float(np.median(times)),
            "best_cost": ans[0],
        })
    return rows


if __name__ == "__main__":
    print(validate_random(seed=20261006))
    for row in benchmark_pairwise(seed=20261006):
        print(row)
