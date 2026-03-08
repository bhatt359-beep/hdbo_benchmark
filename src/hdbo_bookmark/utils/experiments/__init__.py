"""
Experiment Utilities

This submodule provides utilities for configuring and running HDBO experiments.
It handles loading of solvers, problems, generative models, and manages experiment
metadata and validation.

Key Components:

1. **load_solvers**: Registry of available Bayesian optimization solvers
   - Maps solver names to implementation classes
   - Loads solvers from poli_baselines
   - Handles solver-specific configuration
   - Contains all methods from the survey (50+ algorithms)

2. **load_generative_models**: Utilities for importing pre-trained encoders/decoders
   - Load VAEs trained on ZINC250k
   - Load autoencoders from RFP sequences
   - Handle different latent dimensions
   - Cache models for efficiency

3. **load_metadata_for_vaes**: Metadata for various benchmark problems
   - Alphabet mappings (token -> index)
   - Sequence length distributions
   - Problem-specific configurations
   - Handles PMO, RASP, FoldX, etc.

4. **load_problems**: Interface to benchmark objectives from poli
   - Create black-box functions
   - Configure evaluation budgets
   - Handle different string representations
   - Manage function-specific parameters

5. **training_vaes**: Scripts for training new VAEs
   - Training pipelines for ZINC250k
   - Different VAE architectures (RNN, Transformer)
   - Hyperparameter configuration
   - Model persistence and loading

6. **training_gps**: Gaussian Process model utilities
   - GP kernels (RBF, Matern, string kernels, etc.)
   - Hyperparameter optimization
   - Surrogate model configuration for BO

7. **normalization**: Input/output normalization utilities
   - Standardize problem evaluations
   - Handle different value ranges
   - Dimensionality-aware scaling

8. **problem_transformations**: Transform black-box functions
   - Add noise to simulations
   - Create composite objectives
   - Constraint handling

9. **verify_status_pre_experiment**: Pre-experiment validation
   - Check for uncommitted code changes
   - Verify reproducibility setup
   - Validate configuration before expensive runs

The HDBO Taxonomy
================

These utilities support evaluation of methods across the 7 categories in the survey:

1. **Variable Selection** (Section 3.1)
   - Methods: Add-GP-UCB, Active Subspaces, Dropout
   - Loader: load_solvers with these specific methods

2. **Linear Embeddings** (Section 3.2)
   - Methods: REMBO, ALEBO, LineBO, PCA-BO
   - Configuration: Random or data-driven embedding matrices

3. **Non-linear Embeddings** (Section 3.5)
   - Methods: LaMBO, LSBO, Weighted Retraining, VAE+DML
   - Loader: load_generative_models for VAE/AE configs

4. **Structured Spaces** (Section 3.6)
   - Methods: BODi, Bounce, COMBO, BOSS
   - Configuration: Handle categorical and mixed variables

5. **Riemannian Manifolds** (Section 3.4)
   - Methods: GaBO, HD-GaBO
   - Loader: Manifold-specific kernel configurations

6. **Gradient-based Methods** (Section 3.3)
   - Methods: TuRBO+Gradients, d-KG, Wu et al.
   - Support: When gradient info available

7. **Others**: TuRBO (vanilla BO), Ensemble methods, etc.

Experiment Workflow
==================

1. **Setup Phase**:
   - verify_status_pre_experiment()
   - load_solvers() to get BO method
   - load_problems() to get objective
   - load_generative_models() if using latent space

2. **Configuration Phase**:
   - load_metadata_for_vaes() for problem-specific params
   - training_vaes() if need fresh encoder/decoder
   - normalization settings

3. **Execution Phase**:
   - Initialize solver with black box
   - Run optimization loop
   - Track progress with logging utilities

4. **Analysis Phase**:
   - Aggregate results across seeds
   - Compare methods from results/ module

References:
- Survey Section 4: Experimental Setup and Methodology
- Individual method papers cited in poli and poli-baselines
"""
