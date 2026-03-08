from typing import Tuple

import numpy as np
import torch
from torch.distributions import Categorical, Normal


class VAE(torch.nn.Module):
    """
    Variational Autoencoder (VAE) base class for discrete sequence optimization.
    
    Implements the core VAE framework for learning compressed latent representations
    of high-dimensional discrete sequences. This enables Bayesian optimization in the
    lower-dimensional latent space (non-linear embedding approach from the survey).
    
    The VAE learns two distributions:
    - Encoder q(z|x): Maps sequences x to latent codes z
    - Decoder p(x|z): Maps latent codes z back to sequences
    
    Training minimizes the ELBO (Evidence Lower Bound):
        ELBO = -KL(q(z|x) || p(z)) + E[log p(x|z)]
    
    This allows optimization to work directly in latent space where BO can exploit
    the learned structure, then decode solutions back to valid sequences.
    
    Attributes:
        latent_dim: Dimensionality of the latent space
        alphabet_s_to_i: Dictionary mapping symbols to integer indices
        alphabet_i_to_s: Reverse mapping from integers to symbols
        p_z: Prior distribution p(z) - standard Gaussian N(0,I)
        device: PyTorch device for computation
        
    References:
        - Kingma & Welling (2014): Auto-Encoding Variational Bayes
        - Survey Section 3.5: Non-linear Embeddings
    """

    def __init__(
        self,
        latent_dim: int,
        alphabet_s_to_i: dict[str, int],
        device: torch.device,
    ):
        super().__init__()
        self.latent_dim = latent_dim
        self.device = device
        self.alphabet_s_to_i = alphabet_s_to_i
        self.alphabet_i_to_s = {v: k for k, v in alphabet_s_to_i.items()}

        # Defines the prior p(z) = N(0, I)
        self.p_z = Normal(
            loc=torch.zeros(latent_dim, device=device),
            scale=torch.ones(latent_dim, device=device),
        )

    def encode(self, x: torch.Tensor) -> Normal:
        """
        Encoder: Learn q(z|x) distribution given sequences.
        
        Args:
            x: One-hot encoded sequences of shape (batch_size, seq_length, vocab_size)
            
        Returns:
            Normal distribution q(z|x) over latent space
        """
        raise NotImplementedError

    def decode(self, z: torch.Tensor) -> Categorical:
        """
        Decoder: Learn p(x|z) distribution given latent codes.
        
        Args:
            z: Latent codes of shape (batch_size, latent_dim)
            
        Returns:
            Categorical distribution p(x|z) over sequence tokens
        """
        raise NotImplementedError

    def forward(self, x: torch.Tensor) -> Tuple[Normal, Categorical]:
        """
        Computes a forward pass through the VAE, returning
        the distributions q_z_given_x and p_x_given_z.
        
        This is used during training to sample latent codes and reconstruct
        the input sequences.
        
        Args:
            x: One-hot encoded sequences
            
        Returns:
            Tuple of (q(z|x), p(x|z)) distributions
        """
        q_z_given_x = self.encode(x)
        z = q_z_given_x.rsample()

        p_x_given_z = self.decode(z)

        return q_z_given_x, p_x_given_z

    def loss_function(self, x: torch.Tensor) -> torch.Tensor:
        """
        Computes the ELBO loss for a given batch of sequences.
        
        The ELBO combines:
        1. KL divergence: Regularizes q(z|x) to match the prior p(z)
        2. Reconstruction loss: Encourages accurate decoding p(x|z)
        
        Lower loss means better compression and reconstruction trade-off.
        
        Args:
            x: Batch of one-hot encoded sequences
            
        Returns:
            Scalar loss value (averaged over batch)
        """
        q_z_given_x, p_x_given_z = self.forward(x)

        # Computes the KL divergence between q(z|x) and p(z)
        kl_div = torch.distributions.kl_divergence(q_z_given_x, self.p_z).sum(dim=-1)

        # Computes the reconstruction loss (negative log likelihood)
        recon_loss = -p_x_given_z.log_prob(x.argmax(dim=-1).to(self.device)).sum(dim=-1)

        # Computes the ELBO loss
        loss: torch.Tensor = (kl_div + recon_loss).mean()

        return loss

    def encode_from_string_array(self, x: np.ndarray) -> np.ndarray:
        """
        Encode string representations to latent codes.
        
        Converts string sequences to numeric representations, passes through
        encoder, and returns latent codes for BO optimization.
        
        Args:
            x: Array of string sequences
            
        Returns:
            Array of latent codes (batch_size, latent_dim)
        """
        raise NotImplementedError

    def decode_to_string_array(self, z: np.ndarray) -> np.ndarray:
        """
        Decode latent codes back to string representations.
        
        Used after BO has found promising latent codes to generate
        the corresponding discrete sequences for evaluation.
        
        Args:
            z: Array of latent codes (batch_size, latent_dim)
            
        Returns:
            Array of string sequences
        """
        raise NotImplementedError


OptimizedVAE = torch._dynamo.eval_frame.OptimizedModule
