"""
Autoencoder Training on RFP (Red Fluorescent Protein) Pool

This module contains scripts for training autoencoders on evolved RFP sequences.

RFP (Red Fluorescent Protein) Overview:
======================================

RFP is a fluorescent protein from coral and sea anemones, widely used as
a molecular marker in cell biology and biotechnology. Evolution of RFP has
produced variants with altered:
- Excitation/emission wavelengths (mCherry, mRuby, etc.)
- Brightness and photostability
- Maturation rate
- Localization properties

Why Autoencoders for Protein Design?
===================================

The HDBO survey discusses using learned representations (Section 3.5)
for protein sequence optimization:

1. **Sequence Compression**:
   - RFP sequences: ~250-300 amino acids
   - One-hot encoding: 20 * 250 = 5000 dimensions
   - Autoencoder latent: 32-128 dimensions
   - Dramatic dimensionality reduction

2. **Capturing Evolutionary Structure**:
   - Autoencoders learn patterns from RFP variants
   - Capture which mutations are tolerated
   - Learn valid folding patterns
   - Enable smooth BO in learned space

3. **Protein-Specific Inductive Bias**:
   - Positional information from sequences
   - Learned complementarity between positions
   - Secondary structure hints
   - Domain-specific regularization

Autoencoder Architectures:

Simple Autoencoder:
- Encoder: Fully connected layers (gradually reducing dimension)
- Latent: Dense bottleneck layer
- Decoder: Symmetric structure reconstructing full sequences
- Good for interpretability

Convolutional Autoencoder:
- Encoder: 1D convolutions + pooling
- Captures local sequence patterns (binding sites, motifs)
- Preserves positional information
- Better for capturing sequence features

Variational Autoencoder:
- Probabilistic version for sampling
- Enables generative modeling
- Creates smooth latent space for BO
- KL-regularized latent distribution

Why RFP Instead of VAE?
- Simpler training than full VAE
- Deterministic latent codes better for discrete BO
- Focus on reconstruction of known variants
- Faster inference for real-time BO

Training Data:
- RFP natural variants (mCherry, mRuby, etc.)
- Computationally saturated mutants
- Directly evolved sequences
- ~1000-5000 unique RFP variants

Applications:
- Design of novel RFP variants
- Wavelength tuning through sequence optimization
- Brightness improvement
- Photostability enhancement

Downstream Use:
1. Train autoencoder on RFP variants
2. Use encoder in BO optimization
3. Optimize for new properties:
   - FoldX stability predictions
   - Fluorescence predictions
   - Specific absorption wavelength
4. Validate discovered sequences experimentally

The Challenge:
- Limited training data compared to ZINC250k
- Protein sequences have strong constraints
- Need efficient learning from small datasets
- Trade-off between generalization and overfitting

References:
- Penner (2022): Protein geometry, function and mutation
- Stanton et al. (2022): Accelerating BO for biological sequences
- Notin et al. (2023): ProteinGym benchmarks for design
- Survey Section 3.5: Non-linear embeddings for proteins
"""
