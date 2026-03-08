"""
Logging Utilities for Experiment Tracking and Reproducibility

This submodule ensures reproducible and traceable HDBO experiments through
comprehensive logging and monitoring.

Key Components:

1. **wandb_observer**: WandB (Weights & Biases) integration
   - Centralized result storage and visualization
   - Track all hyperparameters and metrics
   - Compare solvers across different problems
   - Real-time monitoring of optimization progress
   - Leaderboard generation

2. **benchmark_observer**: Problem-specific logging
   - Wraps black-box functions for observation
   - Tracks evaluation history
   - Records solver decisions and outcomes
   - Handles data serialization

3. **idempotence_of_experiments**: Prevent duplicate runs
   - Check if experiment already completed
   - Skip redundant computations
   - Enable iterative experiment development
   - Save computational resources

4. **uncommited_changes**: Code version control
   - Detect uncommitted git changes
   - Enforce clean working directory
   - Prevent irreproducible experiments
   - Track software versions

5. **library_hashes**: Component version tracking
   - Hash poli, poli-baselines, hdbo_benchmark versions
   - Ensure algorithm consistency
   - Handle solver implementations in different commits
   - Support reproducibility across time

6. **back_up**: Result persistence
   - Save experiment results locally
   - Create backups of important runs
   - Handle distributed experiment scenarios
   - Emergency recovery

Why Reproducibility Matters for HDBO Survey
============================================

The survey benchmarks 50+ methods across 6 domains. Reproducibility is critical:

1. **Code Versioning**:
   - Git commit hashes recorded for all components
   - Different solvers in different repositories (poli-baselines)
   - Track implementation changes over time

2. **Deterministic Seeding**:
   - Set seeds for numpy, torch, poli
   - Ensures identical results across runs
   - Enables statistical significance testing

3. **Hyperparameter Recording**:
   - Log all solver-specific parameters
   - Different BO methods have different configs
   - Enable fair comparison across methods

4. **Experimental Conditions**:
   - Hardware specification (GPU/CPU)
   - Timing information
   - Memory usage
   - Computational resource constraints

5. **Result Aggregation**:
   - Run each method with multiple seeds
   - Compute statistics (mean, std dev)
   - Enable rank-based comparisons

Experiment Tracking Workflow
===========================

Setup:
1. Check git status (uncommited_changes.py)
2. Record library versions (library_hashes.py)
3. Verify experiment not already run (idempotence_of_experiments.py)

During Optimization:
4. Wrap black box with benchmark_observer
5. Log all evaluations to local storage
6. Initialize WandB run with all metadata

After Completion:
7. Backup results locally (back_up.py)
8. WandB syncs results to cloud
9. Results visualized in leaderboards

Recovery and Debugging:
- Restart experiments from checkpoints
- Re-run with different hyperparameters
- Compare across hardware configurations
- Statistical analysis of results

Integration with Survey
======================

The survey's benchmarking table (Table 3) tracks:
- Method name and first publication date
- Whether open-source implementation available
- BO results on each benchmark

This logging infrastructure enables:
- Continuous benchmark updates
- New method submissions
- Leaderboard maintenance
- Transparent method comparison

References:
- Survey Section 4: Experimental Methodology
- WandB documentation for experiment tracking
- Git hooks for pre-commit validation
"""

from .idempotence_of_experiments import experiment_has_already_run
from .library_hashes import get_git_hash_of_library
from .uncommited_changes import has_uncommitted_changes
from .wandb_observer import WandbObserver

__all__ = [
    "experiment_has_already_run",
    "get_git_hash_of_library",
    "has_uncommitted_changes",
    "WandbObserver",
]
