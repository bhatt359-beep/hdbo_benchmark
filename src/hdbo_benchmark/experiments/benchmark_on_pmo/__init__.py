"""
PMO (Practical Molecular Optimization) Benchmark Experiments

This module contains experiments for benchmarking Bayesian optimization methods
on practical molecular design tasks from the PMO benchmark suite.

The PMO benchmark (Gao et al., 2022) includes realistic drug-like molecule optimization
objectives with emphasis on practical utility and computational feasibility.

Objectives:
- albuterol_similarity: Design molecules similar to albuterol (bronchodilator drug)
- GSK3β inhibition: Predict GSK3β inhibition activity for drug discovery
- JNK3 inhibition: Predict JNK3 inhibition activity

Representation:
- Uses SELFIES (Self-Referencing Embedded Strings) for discrete molecular representation
- SELFIES guarantees chemically valid molecules, unlike SMILES
- Reference: Krenn et al. (2020)

Experimental Setup:
1. Load PMO objective function from the poli benchmark suite
2. Train or load a VAE on ZINC250k molecular database (in latent space mode)
3. Run BO solver for a fixed budget
4. Track and log optimization progress

Key Methods Tested:
- Latent space methods: VAE + BO (LaMBO, LSBO variants)
- Direct discrete methods: BODi, Bounce, etc.
- Continuous methods in latent space: TuRBO, SAASBO, etc.

The experiments evaluate the trade-off between:
- Sample efficiency (BO goodness)
- Representation quality (VAE compression)
- Computational efficiency

References:
- Gao et al. (2022): Sample efficiency matters: A benchmark for practical molecular optimization
- Krenn et al. (2020): SELFIES: A 100% robust molecular string representation
- Survey Section 4: Experiments on PMO
"""
