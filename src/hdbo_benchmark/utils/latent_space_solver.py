"""Implements an abstract latent space solver for non-linear embeddings.

A latent space solver enables Bayesian optimization in a learned lower-dimensional space,
which is a key technique in the HDBO survey for scaling BO to high-dimensional discrete
sequences.

Architecture:
1. Encode discrete sequences to latent codes using a learned encoder (e.g., VAE)
2. Run continuous BO in the latent space
3. Decode promising latent codes back to valid discrete sequences
4. Evaluate decoded sequences and update both latent and discrete histories

This approach solves the high-dimensionality problem by:
- Reducing effective dimensionality through learned representations
- Exploiting structure learned by generative models
- Enabling the use of powerful continuous BO methods (e.g., TuRBO, SAASBO)

Applications:
- Molecular design with VAE-encoded molecule representations
- Protein sequence optimization with learned embeddings
- Any discrete optimization over sequences with VAE

The survey covers multiple non-linear embedding methods:
- LaMBO (Latent space Molecular BO): Uses VAE for molecule encoding
- LSBO: Generic latent space BO framework
- Weighted Retraining: Focuses on high-value regions of latent space

Key components:
- continuous_optimizer: BO solver running in latent space (TuRBO, SAASBO, etc.)
- encoder: Function mapping discrete sequences to latent codes
- decoder: Function mapping latent codes back to sequences

References:
- Tripp et al. (2020): Sample-efficient optimization in latent space of deep generative models
- Stanton et al. (2022): Accelerating BO for biological sequence design with autoencoders
- Survey Section 3.5: Non-linear Embeddings
"""

from typing import Callable, Tuple, Type

import numpy as np
from poli.core.abstract_black_box import AbstractBlackBox  # type: ignore[import]
from poli_baselines.core.abstract_solver import AbstractSolver  # type: ignore[import]


class LatentSpaceSolver(AbstractSolver):
    """
    Bayesian Optimization in a learned latent space.
    
    Wraps a continuous BO solver to operate in the latent space of a generative model,
    enabling efficient optimization of high-dimensional discrete sequences.
    
    Attributes:
        continuous_optimizer: The underlying BO solver (e.g., TuRBO)
        encoder: Maps discrete sequences x to latent codes z
        decoder: Maps latent codes z back to sequences x
        black_box: The objective function to optimize
    """

    def __init__(
        self,
        black_box: AbstractBlackBox,
        x0: np.ndarray,
        y0: np.ndarray,
        continuous_optimizer_class: Type[AbstractSolver],
        encoder: Callable[[np.ndarray], np.ndarray],
        decoder: Callable[[np.ndarray], np.ndarray],
        **kwargs_for_continuous_optimizer,
    ):
        """
        Initialize a latent space solver.
        
        Args:
            black_box: The discrete sequence optimization objective
            x0: Initial discrete sequences (batch_size, ...)
            y0: Initial objective values
            continuous_optimizer_class: BO solver class (must accept black_box, x0, y0)
            encoder: Function encoding discrete sequences to latent codes
            decoder: Function decoding latent codes to sequences
            **kwargs_for_continuous_optimizer: Additional arguments for the BO solver
        """
        super().__init__(black_box, x0, y0)

        # Initialize the continuous optimizer in latent space
        continuous_optimizer = continuous_optimizer_class(
            black_box=black_box,
            x0=encoder(x0),  # Start from encoded initial points
            y0=y0,
            **kwargs_for_continuous_optimizer,
        )
        self.continuous_optimizer = continuous_optimizer
        self.encoder = encoder
        self.decoder = decoder

    def step(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Executes one iteration of latent space BO.
        
        Process:
        1. Get next candidate in latent space from continuous optimizer
        2. Decode it back to a discrete sequence
        3. Evaluate the sequence with the black box
        4. Update both latent space history and discrete sequence history
        
        Returns:
            Tuple of (new_sequence, new_value)
        """
        # Get next candidate in latent space
        z = self.continuous_optimizer.next_candidate()
        
        # Decode to discrete sequence
        x = self.decoder(z)
        
        # Evaluate the discrete sequence
        y = self.black_box(x)

        # Update this solver's history (discrete space)
        self.update(x, y)
        self.post_update(x, y)

        # Update the continuous optimizer's history (latent space)
        # This allows the optimizer to learn from the evaluation
        self.continuous_optimizer.update(z, y)
        self.continuous_optimizer.post_update(z, y)
        
        return x, y

        self.iteration += 1

        return x, y
