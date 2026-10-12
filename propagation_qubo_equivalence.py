"""Small-instance exact check of constrained path DP vs. penalty QUBO.

This script is intentionally exponential and is only for unit tests at small M,R.
It uses the canonical pairwise propagation-path QUBO structure:
  objective L + A*J_onehot + B*J_repeat.
"""
from __future__ import annotations
import itertools
import numpy as np


def decode_onehot(bits, M, R):
    q=np.asarray(bits,dtype=int).reshape(R,M)
    path=[]
    for t in range(R):
        inds=np.flatnonzero(q[t])
        if len(inds)!=1:
            return None
        path.append(int(inds[0]))
    return tuple(path)


def path_cost(path,c_tx,c_edge,c_rx):
    val=float(c_tx[path[0]]+c_rx[path[-1]])
    val += sum(float(c_edge[path[t],path[t+1]]) for t in range(len(path)-1))
    return val


def qubo_energy(bits,M,R,c_tx,c_edge,c_rx,A,B):
    q=np.asarray(bits,dtype=int).reshape(R,M)
    L=float(np.dot(c_tx,q[0])+np.dot(c_rx,q[-1]))
    for t in range(R-1):
        L += float(q[t] @ c_edge @ q[t+1])
    J1=sum((int(q[t].sum())-1)**2 for t in range(R))
    J2=sum(int(q[t,i]*q[t+1,i]) for t in range(R-1) for i in range(M))
    return L + A*J1 + B*J2


def exact_qubo_ground_states(M,R,c_tx,c_edge,c_rx,A,B):
    """Enumerate all binary ground states (tiny instances only)."""
    best=float('inf')
    ground=[]
    for bits in itertools.product((0,1),repeat=M*R):
        e=qubo_energy(bits,M,R,c_tx,c_edge,c_rx,A,B)
        if e < best - 1e-12:
            best=e
            ground=[bits]
        elif abs(e-best) <= 1e-12:
            ground.append(bits)
    return best, ground


def exact_qubo(M,R,c_tx,c_edge,c_rx,A,B):
    """Backward-compatible helper returning one representative ground state."""
    best, ground = exact_qubo_ground_states(M,R,c_tx,c_edge,c_rx,A,B)
    bits = ground[0]
    return best,bits,decode_onehot(bits,M,R)


def constrained_exact(M,R,c_tx,c_edge,c_rx):
    best=float('inf'); bp=None
    for p in itertools.product(range(M),repeat=R):
        if any(p[t]==p[t+1] for t in range(R-1)):
            continue
        v=path_cost(p,c_tx,c_edge,c_rx)
        if v<best:
            best=v; bp=tuple(p)
    return best,bp


def validate(seed=20261006,n=30):
    rng=np.random.default_rng(seed)
    passed=0
    for _ in range(n):
        M=int(rng.integers(2,4))
        R=int(rng.integers(2,4))
        c_tx=rng.integers(0,20,M).astype(float)
        c_rx=rng.integers(0,20,M).astype(float)
        c_edge=rng.integers(0,20,(M,M)).astype(float)
        opt,p=constrained_exact(M,R,c_tx,c_edge,c_rx)
        # Since costs are nonnegative, any A,B greater than a known feasible
        # upper bound is a simple sufficient choice for this test formulation.
        U=path_cost(p,c_tx,c_edge,c_rx)
        A=B=U+1.0
        qe,ground=exact_qubo_ground_states(M,R,c_tx,c_edge,c_rx,A,B)
        if not ground:
            raise AssertionError(('no QUBO ground state',M,R,U,qe))
        for bits in ground:
            qp=decode_onehot(bits,M,R)
            if qp is None:
                raise AssertionError(('infeasible QUBO ground state',M,R,U,qe,bits))
            if any(qp[t]==qp[t+1] for t in range(R-1)):
                raise AssertionError(('repeat constraint violated',M,R,U,qe,qp))
            qpc=path_cost(qp,c_tx,c_edge,c_rx)
            if abs(qpc-opt)>1e-12:
                raise AssertionError(('mismatch',M,R,opt,p,qe,qp,qpc))
        passed+=1
    return passed

if __name__=='__main__':
    print('passed',validate())
