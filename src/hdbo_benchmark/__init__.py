"""
HDBO Benchmark: High-Dimensional Bayesian Optimization for Discrete Sequences

This package implements and benchmarks Bayesian optimization (BO) methods for optimizing
discrete sequences, with applications in protein engineering, drug design, and molecular optimization.

The paper "A survey and benchmark of high-dimensional Bayesian optimization of discrete sequences"
provides a comprehensive review of BO techniques and categorizes them into several groups:

1. **Variable Selection**: Methods that focus optimization on a subset of high-interest variables
   to reduce effective dimensionality.

2. **Linear Embeddings**: Methods that optimize in a lower-dimensional space with linear 
   transformation back to high-dimensional input space (e.g., REMBO, PCA-BO).

3. **Non-linear Embeddings**: Methods using learned representations like Variational Autoencoders
   (VAEs) to capture complex structure in the data (e.g., LaMBO, LSBO).

4. **Structured Spaces**: Methods that work directly on discrete or mixed-variable spaces
   without explicit embedding (e.g., BODi, Bounce).

5. **Riemannian Manifolds**: Methods optimizing on curved spaces rather than Euclidean spaces.

6. **Gradient-based Methods**: Methods that leverage first-order gradient information when available.

Key Components:
- generative_models: VAE and autoencoder implementations for dimensionality reduction
- experiments: Benchmark experiments on various objectives (PMO, FoldX, RASP, etc.)
- solvers: Interface to Bayesian optimization solvers
- utils: Helper functions for experiments, logging, and data handling
"""

__version__ = "1.0.0"
