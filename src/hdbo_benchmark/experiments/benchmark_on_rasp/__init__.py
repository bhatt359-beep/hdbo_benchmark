"""
RASP Benchmark Experiments

This module contains experiments for benchmarking Bayesian optimization methods
on RNA aptamer design tasks (RASP).

RASP is a benchmark for RNA aptamer selection and design through
in-vitro selection procedures. RNA aptamers are short RNA molecules that bind
specific target molecules with high affinity and specificity.

Applications:
- Biosensor design for diagnostics
- Therapeutic RNA aptamers
- RNA aptamer catalysts (ribozymes)
- Synthetic biology tools

Experimental Setup:
1. Define RNA binding or function objectives
2. Represent RNA sequences (typically A, G, C, U nucleotides)
3. Run BO solver on sequence space
4. Track evolution of best discovered aptamers

Sequence Representation Challenges:
- RNA secondary structure constrains sequence space
- Watson-Crick base pairing rules limit valid sequences
- Higher-order 3D structure important for function
- Need to balance sequence diversity with validity

Representation Options:
- Direct discrete: Discrete BO on ACGU sequences
- Structure-aware: Methods that respect secondary structure constraints
- Latent embeddings: VAE on RNA sequences (learns valid structure implicitly)
- String kernels: BOSS method with string metrics

Key Methods Evaluated:
- Methods handling discrete/structured spaces
- Gradient-free optimization (BO)
- Direct sequence representation (no embedding)
- Variable selection on mutable positions

The Challenge:
- RNA secondary structure adds constraints not present in simple sequences
- Large search space (4^L for L nucleotides)
- Expensive fitness evaluation (binding kinetics, structure prediction)
- Trade-off between solution quality and evaluation cost

References:
- Notin et al. (2023): ProteinGym: Large-scale benchmarks for protein design
- Shervashidze et al. (2011): Weisfeiler–Lehman graph kernels
- Survey Section 4: Experiments on RNA and protein design
"""
