"""
Data Utilities for HDBO Benchmarks

This submodule handles data loading, preprocessing, and result aggregation
for the HDBO benchmark experiments.

Key Components:

1. **zinc_250k**: ZINC 250k molecular database utilities
   - Download and preprocess ZINC molecules
   - Convert SMILES to SELFIES representation
   - Split into train/val/test sets
   - Create vocabulary and metadata files
   - Used for training VAEs in molecular optimization

2. **mario**: Mario level dataset utilities
   - Load Mario level configurations
   - One-hot encoding of level designs
   - Used for discrete sequence optimization
   - VAE training on game level data

3. **experiments/loading_results**: Result aggregation from WandB
   - load_results_as_dataframe: Load experiment results locally
   - load_results_as_dataframe_from_wandb: Fetch results from cloud
   - load_all_results_as_dataframe_from_wandb: Aggregate across all methods
   - Convert to pandas DataFrame for analysis

Dataset Overview
================

The HDBO survey benchmarks on multiple domains:

ZINC250k - Molecular Design
- 250,000 drug-like compounds from ZINC database
- Large chemical diversity
- Used to train VAEs for molecular latent space
- Then used to optimize for drug properties
- Representation: SELFIES (guarantees valid molecules)
- Latent dimensions: 2, 32, 64, 128

Mario Levels - Game Design
- Procedurally generated game levels
- Discrete representation (platforms, enemies, etc.)
- Sequence optimization on level design
- VAE learns valid level structure
- One-hot encoding of level tokens

Why Diverse Datasets Matter
===========================

Different domains test different aspects of BO methods:

1. **ZINC250k** (Molecules):
   - Large dataset (250k compounds)
   - Learning-based methods excel
   - VAE captures chemical validity
   - Tests for sample efficiency

2. **Protein sequences** (FoldX, RASP):
   - Smaller dataset (~1000s variants)
   - Structure constraints matter
   - Need pre-trained embeddings
   - Tests for exploitation vs exploration

3. **Game levels** (Mario):
   - Synthetic discrete sequences
   - Clear structure (platformer rules)
   - Tests for structure learning
   - Good for visualization

Result Loading and Analysis
===========================

The results submodule enables:
- Aggregating experiments across seeds
- Computing statistics (mean, std, confidence intervals)
- Creating leaderboards ranking methods
- Statistical significance testing
- Visualization of performance across problems

Workflow:
1. Run experiments -> Results to WandB
2. load_results_as_dataframe_from_wandb()
3. Aggregate by solver, problem, latent_dim
4. Compute rankings and statistics
5. Visualize in leaderboards

Integration with Benchmark
==========================

This data infrastructure supports:
- Continuous leaderboard updates
- New method submissions
- Fair performance comparison
- Statistical analysis of solver ranking

References:
- Irwin et al. (2020): ZINC20 database
- Survey Section 4: Benchmark preparation
- results/ module for leaderboard generation
"""

from .experiments.loading_results import (
    load_all_results_as_dataframe_from_wandb,
    load_results_as_dataframe,
    load_results_as_dataframe_from_wandb,
)

__all__ = [
    "load_all_results_as_dataframe_from_wandb",
    "load_results_as_dataframe",
    "load_results_as_dataframe_from_wandb",
]