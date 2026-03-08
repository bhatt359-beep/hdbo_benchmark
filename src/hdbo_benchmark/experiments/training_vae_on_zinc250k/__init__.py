"""
VAE Training on ZINC250k

This module contains scripts for training Variational Autoencoders on
the ZINC250k molecular dataset.

ZINC is a large database of drug-like compounds in 3D format. ZINC250k
is a 250,000-compound subset commonly used for benchmarking molecular
design methods.

Why Train VAEs on Molecular Data?
================================

The HDBO survey emphasizes non-linear embeddings (Section 3.5) where
learned representations like VAEs enable efficient BO:

1. **Dimensionality Reduction**:
   - ZINC molecules: ~300 heavy atoms typical
   - Direct SMILES strings: ~100-150 characters
   - VAE latent dim: 2-128 (configurable)
   - Reduces effective dimension dramatically

2. **Learning Valid Regions**:
   - VAE captures chemical space structure
   - Decoder produces chemically valid molecules
   - Unlike random embeddings, structure is meaningful

3. **Sample Efficiency**:
   - Smooth latent space enables effective BO
   - Gaussian Processes work well in latent space
   - Can use powerful continuous BO solvers (TuRBO, etc.)

4. **Transfer Learning**:
   - Trained VAE can be reused across optimization tasks
   - Saves computation for multiple molecular targets

VAE Architecture for Molecules:
==============================

Input: SELFIES strings (Self-Referencing Embedded Strings)
- Advantages: Always produces valid molecules (unlike SMILES)
- Fixed vocabulary of safe atomic operations
- Enables discrete BO on atoms rather than characters

Encoder q(z|x):
- Input: One-hot encoded SELFIES tokens
- Architecture: Bidirectional RNN/Transformer (seq2seq)
- Output: Mean and log-variance for latent distribution

Decoder p(x|z):
- Input: Latent code z
- Architecture: Autoregressive RNN (generates token by token)
- Output: Token probabilities at each position

Loss (ELBO):
- KL divergence: Regularizes latent space to N(0,I)
- Reconstruction loss: Negative log-likelihood of decoding
- Trade-off controlled by β (beta-VAE)

Training Data:
- ZINC250k: 250,000 drug-like molecules
- Representations: SMILES or SELFIES strings
- Train/val/test split for evaluation

Latent Dimensions Studied:
- latent_dim=2: Interpretable toy model
- latent_dim=32, 64: Practical for visualization
- latent_dim=128: Full expressivity
- Dimension trades off compression vs reconstruction

Applications:
- Molecular optimization: LAMBp (Latent Molecular BO)
- Structure-property prediction
- Generative design
- Hit-to-lead optimization

The Benchmark:
This trained VAE is used as the encoder/decoder in downstream
molecular optimization experiments (PMO, etc.) where BO methods
are tested for their ability to find better molecules in latent space.

References:
- Gómez-Bombarelli et al. (2018): Chemical design using VAE in latent space
- Kingma & Welling (2014): Auto-Encoding Variational Bayes
- Krenn et al. (2020): SELFIES: 100% robust molecular string representation
- Irwin et al. (2020): ZINC20 - ultralarge chemical database
- Survey Section 3.5: Non-linear embeddings
"""
