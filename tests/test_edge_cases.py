from __future__ import annotations
import sys
from pathlib import Path
import unittest
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from propagation_path_dp_reference import (
    brute_force_pairwise, dp_pairwise, dp_pairwise_kbest,
    brute_force_directional, dp_directional, dp_directional_kbest,
)
from propagation_path_dp_layered import Edge, TripleTransition, pairwise_layered_dp, directional_layered_dp
from propagation_qubo_equivalence import exact_qubo_ground_states, decode_onehot

class EdgeCases(unittest.TestCase):
    def test_pairwise_r1(self):
        a=np.array([2.,-1.]); e=np.zeros((2,2)); z=np.array([1.,2.])
        self.assertEqual(dp_pairwise_kbest(a,e,z,1,K=10),brute_force_pairwise(a,e,z,1,K=10))
        self.assertEqual(dp_pairwise(a,e,z,1)[0],1.)
    def test_pairwise_single_object(self):
        self.assertEqual(dp_pairwise([2.],[[3.]],[4.],3),(12.,(0,0,0)))
    def test_pairwise_all_ties(self):
        z=np.zeros(3); e=np.zeros((3,3))
        self.assertEqual(dp_pairwise_kbest(z,e,z,4,K=10),brute_force_pairwise(z,e,z,4,K=10))
    def test_pairwise_infeasible(self):
        z=np.zeros(2); e=np.zeros((2,2)); m=np.zeros((2,2),dtype=bool)
        self.assertEqual(dp_pairwise(z,e,z,2,m),(float('inf'),None))
        self.assertEqual(dp_pairwise_kbest(z,e,z,2,m,K=10),[])
    def test_pairwise_negative(self):
        a=np.array([1.,-4.]); e=np.array([[0.,-2.],[3.,1.]])
        self.assertEqual(dp_pairwise_kbest(a,e,a,4,K=10),brute_force_pairwise(a,e,a,4,K=10))
    def test_directional_r2_and_initial_mask(self):
        z=np.zeros((3,3)); t=np.zeros((3,3,3)); m=~np.eye(3,dtype=bool)
        d=dp_directional_kbest(z,t,z,2,allowed_pair=m,K=20)
        self.assertEqual(d,brute_force_directional(z,t,z,2,allowed_pair=m,K=20))
        self.assertEqual(len(d),6)
    def test_directional_ties(self):
        z=np.zeros((3,3)); t=np.zeros((3,3,3))
        self.assertEqual(dp_directional_kbest(z,t,z,4,K=10),brute_force_directional(z,t,z,4,K=10))
    def test_directional_infeasible(self):
        z=np.zeros((2,2)); t=np.zeros((2,2,2)); m=np.zeros((2,2),dtype=bool)
        self.assertEqual(dp_directional(z,t,z,3,allowed_pair=m),(float('inf'),None))
        self.assertEqual(dp_directional_kbest(z,t,z,3,allowed_pair=m,K=10),[])
    def test_directional_negative_single_best(self):
        z=np.array([[2.,-1.],[0.,-3.]]); t=np.arange(8,dtype=float).reshape(2,2,2)-5
        b=brute_force_directional(z,t,z,4,K=1)
        d=dp_directional(z,t,z,4)
        self.assertEqual(d[0],b[0][0])
    def test_layered_pairwise(self):
        edges=[[Edge(0,1,-2.),Edge(1,0,4.)],[Edge(1,0,1.),Edge(0,1,0.)]]
        self.assertEqual(pairwise_layered_dp([0.,1.],edges,[0.,2.]),(-1.,(0,1,0)))
    def test_layered_directional(self):
        d=directional_layered_dp(3,[(0,1,2.)],[[TripleTransition(0,1,2,-4.)]],lambda i,j:1.)
        self.assertEqual(d,(-1.,(0,1,2)))
    def test_all_degenerate_qubo_ground_states(self):
        best,states=exact_qubo_ground_states(2,2,np.zeros(2),np.zeros((2,2)),np.zeros(2),1.,1.)
        self.assertEqual(best,0.)
        self.assertEqual({decode_onehot(s,2,2) for s in states},{(0,1),(1,0)})

if __name__ == '__main__': unittest.main()
