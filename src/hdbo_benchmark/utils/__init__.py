"""
Utilities for HDBO Benchmark

This package provides helper utilities for the high-dimensional Bayesian optimization
benchmark, organized into several sub-modules:

1. **constants**: Configuration constants (device, paths, wandb settings)

2. **experiments**: Experiment utilities
   - Load solvers and configure experiment parameters
   - Load metadata and representations (VAEs, alphabets)
   - Track experiment status and reproducibility

3. **logging**: Experiment monitoring and reproducibility
   - WandB integration for centralized result tracking
   - Idempotence checking to avoid duplicate runs
   - Git commit hash tracking for code versioning

4. **data**: Data preprocessing and handling
   - ZINC250k dataset utilities
   - Sequence processing and validation

5. **latent_space_solver**: BO solver wrapper for latent space optimization
   - Bridges between BO methods and VAE representations
   - Handles encoding/decoding during optimization

6. **selfies**: SELFIES molecular string utilities
   - String parsing and validation
   - Atom and bond counting for molecular analysis

7. **ax**: Ax-specific utilities (for Adaptive Experimentation Platform)

8. **mario**: Mario game level dataset utilities

9. **results**: Analysis and aggregation of benchmark results
   - Leaderboard generation
   - Statistical comparisons between solvers
   - Visualization of performance

10. **visualization**: Plotting and result visualization

The utilities enforce reproducibility through:
- Seeding for random number generation
- Git commit tracking
- Idempotence checking
- Centralized logging via WandB
"""
