"""
Ehrlich Benchmark Experiments

This module contains experiments for benchmarking Bayesian optimization on
discrete sequence search problems.

The Ehrlich experiments include various target search tasks in discrete spaces,
representing practical problems where gradient information is unavailable and
the search space is combinatorial.

Applications:
- Combinatorial design problems
- Hyperparameter optimization (categorical variables)
- Program synthesis and code search
- Design space exploration with discrete parameters

Experimental Setup:
1. Define discrete sequence optimization objective
2. Choose representation (direct or latent)
3. Run BO solver with budget constraints
4. Track convergence to optimal or near-optimal solutions

Key Challenges:
- Very large combinatorial search spaces
- No gradient information
- Expensive function evaluations
- Need for sample-efficient optimization

Representation Considerations:
- Direct discrete: Methods that work directly on discrete variables
  (BODi, Bounce, COMBO, BOSS)
- Linear embeddings: Random or selected projections to lower dimensions
  (REMBO, ALEBO variants)
- Non-linear embeddings: Learned representations if training data available
- Kernel methods: String kernels for sequence similarity

Methods Evaluated:
- Discrete BO with specialized kernels
- Mixed-variable BO (BOUNCE, CASMOPOLITAN)
- Variable selection for high-dimensional discrete spaces
- Tree-structured decompositions (Tree Add-GP-UCB)

The Challenge:
- Effective dimension unclear a priori
- Cannot assume smoothness or continuity
- Need to handle categorical variables properly
- Balance exploration vs. exploitation in discrete space

References:
- Deshwal et al. (2023): Bayesian optimization over high-dimensional combinatorial spaces
- Oh et al. (2018): BOCK - Bayesian optimization with cylindrical kernels
- Oh et al. (2019): COMBO - Combinatorial BO
- Survey Section 3: Various approaches to discrete BO
"""
