# Optional email draft — do not send without author review

Subject: Confirming public release of propagation-DP reference code (BSD 3-Clause)

Dear all,

As part of preparing our propagation-QUBO/DP paper for submission, I have collected the reference implementations, synthetic-instance generators, and numerical validation scripts in a private GitHub repository:

https://github.com/ueda1984/propagation-dp-baselines

The package is intended to allow readers to reproduce the exact small-instance checks in the manuscript (pairwise and direction-dependent top-K paths, plus the small penalty-QUBO checks). It does not include real propagation-loss matrices, proprietary datasets, or end-to-end ray-tracing benchmarks.

The Python reference code was newly prepared at my direction with AI assistance. To my knowledge, it does not incorporate pre-existing source code from SoftBank or RIKEN. This statement is about source origin; applicable copyright, employment, contribution and release permissions still need confirmation.

I propose releasing the code under the permissive BSD 3-Clause License, which also permits commercial and closed-source downstream use while preserving notices and prohibiting unauthorized endorsement by contributors.

Before making it public, could you please confirm:
(1) whether any of the files incorporate code or data from your work or institution, and whether additional credit/notices are needed;
(2) whether you are aware of any confidentiality, IP, patent, employer or collaboration restrictions;
(3) whether you are comfortable with the planned public release and proposed license, subject to clearance by the actual code rights holder(s); and
(4) the appropriate software citation authors/contributors, which need not be identical to the manuscript authors?

No public release will take place until these points are clarified.

Best regards,
Hiroshi Ueda

---

Notes for the sender: This is a draft. Confirm each recipient and send separately or jointly as appropriate. Avoid claiming that recipients personally own the software or can approve institutional rights on behalf of an employer.
