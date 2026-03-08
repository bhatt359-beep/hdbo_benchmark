"""
Result Analysis and Leaderboard Generation

This module handles post-processing and visualization of benchmark results
for the HDBO survey.

Key Functionality:

1. **Leaderboard Generation**:
   - Aggregate results across seeds
   - Rank methods by performance
   - Compute confidence intervals
   - Statistical significance testing

2. **Table Generation**:
   - print_tables_for_website_and_paper.py: Format results for publication
   - Creates LaTeX tables for paper
   - Generates HTML leaderboards for website
   - Highlights top-performing methods

3. **Result Download**:
   - download_tables.py: Fetch results from WandB
   - Caching for offline analysis
   - Handle incomplete experiments
   - Verify data consistency

4. **Benchmarking Structure**:
   - benchmark_on_pmo/: Molecular optimization leaderboards
   - benchmark_on_rasp/: RNA aptamer design results
   - other_results/: Protein, synthetic, and other benchmarks

The Evaluation Framework
=======================

Each benchmark evaluates solvers on:
1. **Multiple Problems**: PMO has 3 objectives, FoldX has variants, etc.
2. **Multiple Latent Dimensions**: 2, 32, 64, 128 (tests representation quality)
3. **Multiple Seeds**: 5-10 per configuration (statistical significance)
4. **Success Metrics**:
   - Best value found
   - Sample efficiency (iterations to reach target)
   - Optimization curve (value vs iterations)
   - Cumulative regret

Solver Taxonomy from Survey
===========================

Results are organized by method category:

**Category 1: Variable Selection** (Section 3.1)
- Add-GP-UCB: Additive structure exploitation
- Active Subspaces: Gradient-based dimension reduction
- Dropout: Probabilistic dimension reduction
- ASM: Active subspace methods

**Category 2: Linear Embeddings** (Section 3.4)
- REMBO: Random embeddings
- ALEBO: Active learning with embeddings
- LineBO: One-dimensional subspaces
- PCA-BO: Data-driven linear embeddings

**Category 3: Non-linear Embeddings** (Section 3.5)
- LaMBO: VAE + latent space BO
- LSBO: Latent space generic framework
- Weighted Retraining: Focus on high-value region
- VAE+DML: VAE with deep metric learning

**Category 4: Structured Spaces** (Section 3.6)
- BODi: Discrete BO with integer programming
- Bounce: Reliable high-dimensional BO for mixed spaces
- COMBO: Combinatorial BO with categorical variables
- BOSS: Bayesian optimization over string spaces

**Category 5: Riemannian Manifolds** (Section 3.4)
- GaBO: Geodesic-aware Bayesian optimization
- HD-GaBO: High-dimensional riemannian BO

**Category 6: Gradient-based Methods** (Section 3.3)
- d-KG: Gradient-informed acquisition function
- TuRBO+Gradients: Incorporating derivatives

**Category 7: Others**
- TuRBO: Trust region BO (baseline)
- Ensemble BO: Multiple surrogate models
- SCoreBO: Self-correcting BO

Leaderboard Organization
=======================

For each benchmark domain:

1. **Problem Level**:
   - Overall ranking across all latent dimensions
   - Shows which solvers are most robust

2. **Latent Dimension**:
   - Rankings for each latent_dim (2, 32, 64, 128)
   - Shows if method exploits representation structure
   - Low latent_dim: harder problem (test robustness)
   - High latent_dim: easier problem (more info)

3. **Metric Details**:
   - Best value: Minimum/maximum achieved
   - Iteration count: Function evaluations used
   - Optimization curve shape
   - Statistical confidence intervals

Key Leaderboard Insights
========================

From PMO benchmark:
- Non-linear embedding methods often top performers
- LaMBO, Weighted Retraining strong across problems
- Linear embedding (REMBO, ALEBO) competitive with less data
- Direct discrete (BODi, Bounce) struggle on higher-dim spaces
- TuRBO in latent space very effective

From Protein Design (FoldX):
- Latent space methods handle discrete constraints
- Structure-aware methods valuable
- Need sufficient representation quality
- Trade-off between expressivity and optimization difficulty

From Synthetic Benchmarks (Toy Objectives):
- HDBO methods scale better than vanilla BO
- Effective dimension critical to performance
- Methods exploiting structure > random embeddings
- Gradient-based methods improve with large budgets

Statistical Analysis
===================

Results tracked with:
- Mean performance across seeds
- Standard deviation or confidence intervals
- Rank (1st place, 2nd, etc.)
- Win/tie/loss statistics vs other solvers
- Significance tests (where applicable)

This enables:
- Identifying clearly superior methods
- Distinguishing strong performers from statistical noise
- Validating algorithmic improvements
- Supporting paper claims with statistics

Website Integration
==================

The leaderboards feed into:
- Project website (machinelearninglifescience.github.io/hdbo_benchmark)
- Interactive visualizations
- Downloadable results
- Paper supplementary materials
- Continuing updates as new methods added

References:
- Survey Section 4: Experimental Results and Analysis
- Survey Table 3: Method bibliography and code availability
- Survey figures: Performance comparisons and rankings
"""
