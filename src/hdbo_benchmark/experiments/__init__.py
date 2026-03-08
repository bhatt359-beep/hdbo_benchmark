"""
Benchmark Experiments for High-Dimensional Bayesian Optimization

This module contains the experimental scripts for benchmarking various Bayesian optimization
methods across different discrete sequence optimization problems.

According to the survey paper, these experiments evaluate methods across several domains:

1. **PMO (Practical Molecular Optimization)**: Focus on practical drug-like molecule design
   - Targets: Albuterol similarity, GSK3β inhibition, JNK3 inhibition
   - Representation: SELFIES (Self-Referencing Embedded Strings)
   - Reference: Gao et al. (2022)

2. **FoldX**: Protein folding stability and design
   - Optimizes protein sequences for improved stability
   - FoldX force field for fitness evaluation
   - Applications: Directed protein evolution

3. **RASP**: RNA aptamer design and selection
   - RNA sequence optimization
   - Direct sequence representation or embeddings

4. **Ehrlich**: Target search in discrete spaces
   - Various discrete optimization tasks

5. **Toy Objectives**: Synthetic benchmarks for controlled evaluation
   - Used for quick validation and algorithm comparison

6. **Training Experiments**:
   - Training VAEs on ZINC250k molecular database
   - Training autoencoders on RFP (Red Fluorescent Protein) sequences
   - These trained models are used as representations in downstream BO tasks

Experiment Flow:
1. Load or train a generative model (VAE) if optimization in latent space
2. Create a black-box optimization problem (from poli benchmark suite)
3. Run a BO solver for a fixed number of iterations
4. Track optimization progress and final best found solution
5. Log results to wandb for analysis and comparison

Each experiment can be run with different:
- Solvers: Various BO algorithms from poli-baselines
- Latent dimensions: For representation learning
- Seeds: For statistical significance
- Maximum iterations: For fairness of comparison

References:
- Survey Section 4: Experimental Setup
- Gao et al. (2022): Sample efficiency matters
- All referenced works in survey.pdf
"""
