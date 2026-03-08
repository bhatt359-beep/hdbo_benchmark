"""
Toy Objective Benchmark Experiments

This module contains synthetic toy objectives for quick validation and
algorithm comparison in controlled settings.

Toy objectives are essential for:
1. Rapid algorithm validation without expensive function evaluations
2. Controlled studies of algorithm performance
3. Understanding algorithm behavior in simplified settings
4. Quick checks during development and debugging

These objectives are used in the HDBO survey to:
- Validate new methods before expensive real evaluations
- Compare solvers under controlled conditions
- Test different representation approaches
- Understand scaling with dimensionality

Typical Toy Functions:
- Rastrigin function: Highly multimodal, tests exploration
- Ackley function: Deceptive, tests robustness
- Sphere function: Simple convex baseline
- Rosenbrock function: Valley-shaped, tests exploitation
- Synthetic discrete spaces: Created from continuous functions

Experimental Setup:
1. Choose a toy function with known properties
2. Vary dimensionality using linear/non-linear embeddings
3. Generate initial random points
4. Run BO solver
5. Compare convergence to known optima

Key Metrics:
- Regret: Distance from best found to true optimum
- Sample efficiency: Iterations needed to reach target value
- Scalability: Performance vs. dimensionality

Advantages:
- Instantaneous function evaluations
- Parallel experiment runs (no resource contention)
- Statistical significance with many seeds
- Clear ground truth for validation

The survey uses toy objectives to:
- Demonstrate scaling of different HDBO approaches
- Show how effective dimension affects performance
- Validate theory of dimensionality reduction
- Establish baseline comparisons

References:
- Rasmussen & Williams (2006): Gaussian Processes for Machine Learning
- Garnett (2023): Bayesian Optimization
- Survey Section 4: Evaluation includes synthetic benchmarks
"""
