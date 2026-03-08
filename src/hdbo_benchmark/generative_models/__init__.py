"""
Generative Models for Non-Linear Embeddings in Bayesian Optimization

This module implements Variational Autoencoders (VAEs) and other generative models
used for dimensionality reduction in high-dimensional Bayesian optimization.

Non-linear embeddings using learned representations (like VAEs) are a key technique 
in the HDBO survey. They allow BO to scale to high-dimensional discrete spaces by:

1. Learning a compressed latent representation of the discrete sequences
2. Performing optimization in the lower-dimensional latent space
3. Decoding latent points back to valid discrete sequences

Key classes:
- VAE: Base class for variational autoencoders
- VAESelfies: VAE for SELFIES molecular representations
- VAEMario: VAE for Mario level representations

These models enable methods like LaMBO (Latent space Molecular Bayesian Optimization)
and other latent space BO techniques referenced in the survey.

References:
- Gómez-Bombarelli et al. (2018): Automatic chemical design using VAE
- Kingma & Welling (2014): Auto-Encoding Variational Bayes
- Stanton et al. (2022): Accelerating BO for biological sequence design with DAE
"""

from .vae_mario import VAEMario
from .vae_selfies import VAESelfies

__all__ = ["VAEMario", "VAESelfies"]
