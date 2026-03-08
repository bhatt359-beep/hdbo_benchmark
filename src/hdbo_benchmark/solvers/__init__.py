"""
Solver Interface and Registry

This module provides the interface to Bayesian optimization solvers.
All solver implementations are in poli-baselines as a separate package,
but this module registers and configures them for the benchmark.

The survey evaluates 50+ Bayesian optimization methods across 7 categories:

**Category 1: Variable Selection** (Section 3.1)
Focus on optimizing a subset of variables, reducing effective dimension.
Methods:
- Add-GP-UCB: Gaussian process with additive structure
- Active Subspaces: Identify low-dimensional projections
- Dropout: Probabilistic dimension reduction
- ASM: Active subspace methods

Use when: Problem has clear low-dimensional structure
Advantages: Interpretable, computationally efficient
Challenges: Need to identify important variables

**Category 2: Linear Embeddings** (Section 3.4)
Project high-dimensional problem to lower-dimensional space.
Methods:
- REMBO: Random embeddings with Bayesian optimization
- ALEBO: Active learning with embeddings
- LineBO: One-dimensional subspaces
- PCA-BO: Principal component analysis embeddings
- Quantile-GP: Quantile-based embeddings

Use when: Effective dimension is low but unknown
Advantages: Simple, interpretable, theoretically justified
Challenges: May miss important structure in high dimensions

**Category 3: Non-linear Embeddings** (Section 3.5)
Learn representations with autoencoders/VAEs.
Methods:
- LaMBO: Latent space Molecular Bayesian Optimization
- LSBO: Generic latent space BO framework
- Weighted Retraining: Focus optimization on high-value regions
- VAE+DML: VAE with deep metric learning
- SGVAE: Structured generative VAE
- Amortized BO: Learn optimization procedure itself

Use when: Have training data to learn representation
Advantages: Captures complex structure, enables very large reductions
Challenges: Requires quality training data

**Category 4: Structured Spaces** (Section 3.6)
Handle discrete/categorical/mixed variables directly.
Methods:
- BODi: Discrete BO with integer programming
- Bounce: Reliable high-dimensional BO for combined spaces
- COMBO: Combinatorial Bayesian Optimization
- BOSS: Bayesian Optimization over String Spaces
- CASMOPOLITAN: Categorical variable BO
- HEBO: Heterogeneous search space BO

Use when: Want to optimize directly on discrete space
Advantages: No representation needed, direct applicability
Challenges: Kernel design for discrete variables

**Category 5: Riemannian Manifolds** (Section 3.4)
Optimize on curved spaces rather than Euclidean.
Methods:
- GaBO: Geodesic-aware Bayesian Optimization
- HD-GaBO: High-dimensional Riemannian BO
- Jaquier et al. methods: Manifold-aware kernels

Use when: Solution space has manifold structure
Advantages: Theoretically grounded, exploits geometry
Challenges: Complex kernel and embedding computations

**Category 6: Gradient-based Methods** (Section 3.3)
Leverage first-order or second-order derivative information.
Methods:
- d-KG: Information gain with derivatives
- TuRBO+Gradients: Trust region BO with gradients
- Wu et al.: Gradient-informed acquisition
- Derivative-free but gradient-compatible methods

Use when: Gradients available (simulators, differentiable functions)
Advantages: Powerful when gradients accurate
Challenges: Requires gradient computation

**Category 7: Baseline Methods**
Reference implementations and variants.
Methods:
- TuRBO: Trust region BO (strong baseline)
- Ensemble BO: Multiple model ensemble
- Vanilla BO: Standard Gaussian process BO
- Random Search: Simple baseline

Use when: Studying algorithm improvements
Advantages: Well-understood, good reference points
Challenges: Often not competitive for high-dimensional

Solver Configuration
====================

Each solver is registered via:
1. Implementation in poli-baselines
2. Environment file specifying dependencies
3. Entry in load_solvers.py registry

Common Parameters:
- n_initial_points: Random exploration phase size
- max_iter: Total evaluation budget
- seed: Random number control
- latent_dim: For latent space methods (when using VAE)

Running Solvers
===============

Example: Run LaMBO on molecular optimization
```python
from hdbo_benchmark.utils.experiments.load_solvers import load_solver_class

LaMBO = load_solver_class("lambo")
solver = LaMBO(black_box, x0, y0, latent_dim=128)

for _ in range(100):
    x_next = solver.next_candidate()
    y_next = black_box(x_next)
    solver.update(x_next, y_next)
    solver.post_update(x_next, y_next)
```

Solver Benchmarking Notes
=========================

**Fair Comparison Requires**:
1. Equal evaluation budget across all solvers
2. Same random seeds for reproducibility
3. Same problem representations (e.g., SELFIES for molecules)
4. Adequate solver-specific tuning
5. Reporting confidence intervals over multiple seeds

**Performance Metrics**:
- Regret: Distance from best found to true optimum
- Sample efficiency: Function evaluations to reach target
- Convergence rate: How quickly value improves
- Robustness: Performance across different seeds

**Domain-Specific Considerations**:
- PMO: Molecular design, need valid molecules
- Proteins: Sequence constraints, stability trade-offs
- Games: Discrete design, learnable patterns
- Synthetic: Controlled experiments, known optima

Integration with poli-baselines
===============================

This benchmark uses solvers from poli-baselines, a unified framework for:
- Implementing new BO methods consistently
- Testing across different problems
- Comparing against other methods
- Publishing reproducible research

The registry (load_solvers.py) connects poli-baselines implementations to
benchmark experiments.

References:
- Survey Section 3: Complete taxonomy of methods
- poli-baselines documentation for implementation details
- Each method's original paper for theoretical background
- Survey Table 3: Bibliography of all 50+ methods
"""
