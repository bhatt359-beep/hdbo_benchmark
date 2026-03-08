"""
FoldX Benchmark Experiments

This module contains experiments for benchmarking Bayesian optimization methods
on protein design tasks using the FoldX force field.

FoldX is a protein structure prediction and design tool that evaluates protein
stability. It's particularly relevant for directed protein evolution where the
goal is to discover sequences with improved properties (e.g., increased stability,
altered activity).

Applications:
- Protein stability optimization (ΔΔG prediction)
- Directed evolution of protein sequences
- Protein engineering for industrial applications

Experimental Setup:
1. Load a target protein structure (e.g., from PDB)
2. Define FoldX-based fitness function
3. Run BO solver on sequence space (or latent space with VAE)
4. Track best discovered mutations and their effects

Sequence Representation Options:
- Direct discrete optimization (BODi, Bounce): Optimize mutations directly
- Latent space methods: Use learned embeddings from protein sequences
- Gradient-based: If gradient information available from structure
- Variable selection: Focus on mutable residue positions

The challenge:
- Large sequence space (20^L possible sequences for L residues)
- Expensive fitness evaluations (FoldX structure prediction)
- Multiple-objective trade-offs (stability vs. activity vs. expression)

Key Methods Evaluated:
- TuRBO in latent space (combined with VAE encoder)
- LADDER: Combines discrete and continuous optimization
- BOUNCE: For mixed-variable spaces
- Direct discrete methods: BODi with protein-specific kernels

References:
- Delgado et al. (2019): FoldX 5.0: working with RNA, small molecules
- Penner (2022): Protein geometry, function and mutation
- Survey Section 4: Experiments on protein engineering tasks
"""
