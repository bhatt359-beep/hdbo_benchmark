# A survey and benchmark of High-Dimensional Bayesian Optimization for discrete sequence optimization

[![Link to Project website](https://img.shields.io/badge/GitHub-Project_Website-100000?logo=github&logoColor=white)](https://machinelearninglifescience.github.io/hdbo_benchmark)
[![Link to Project website](https://img.shields.io/badge/GitHub-poli_docs-100000?logo=github&logoColor=white)](https://machinelearninglifescience.github.io/poli-docs)
[![Tests on hdbo (conda, python 3.10)](https://github.com/MachineLearningLifeScience/hdbo_benchmark/actions/workflows/tox-lint-and-pytest.yml/badge.svg)](https://github.com/MachineLearningLifeScience/hdbo_benchmark/actions/workflows/tox-lint-and-pytest.yml)

This repository contains the code for our survey and benchmark of **high-dimensional Bayesian optimization** of discrete sequences using [poli](https://github.com/MachineLearningLifeScience/poli) and [poli-baselines](https://github.com/MachineLearningLifeScience/poli-baselines).

## About the Survey

This benchmark accompanies a comprehensive survey on Bayesian Optimization (BO) for high-dimensional discrete sequence optimization. The survey:

- **Reviews 50+ BO methods** across several categories
- **Categorizes approaches** into 7 main groups:
  1. **Variable Selection**: Focus on high-interest dimensions (Add-GP-UCB, Active Subspaces)
  2. **Linear Embeddings**: Project to lower-dimensional subspaces (REMBO, ALEBO, PCA-BO)
  3. **Non-linear Embeddings**: Learn representations with VAEs/AEs (LaMBO, LSBO, Weighted Retraining)
  4. **Structured Spaces**: Work directly on discrete/mixed variables (BODi, Bounce, COMBO)
  5. **Riemannian Manifolds**: Optimize on curved spaces (GaBO, HD-GaBO)
  6. **Gradient-based Methods**: Leverage first-order information (d-KG, TuRBO+Gradients)
  7. **Other Methods**: TuRBO, Ensemble BO, and variants

- **Benchmarks on real applications**:
  - **PMO**: Practical molecular design (Gao et al., 2022)
  - **FoldX**: Protein engineering and stability
  - **RASP**: RNA aptamer design
  - **Toy objectives**: Controlled synthetic benchmarks
  - **Protein fitness**: Evolution and design

- **Key insights**:
  - Non-linear embeddings often excel for high-dimensional problems
  - Representation quality crucial for latent space BO
  - Trade-off between sample efficiency and computational cost
  - Method effectiveness depends on problem structure

## Understanding the Repository

### Module Structure

```
src/hdbo_benchmark/
├── generative_models/       # VAEs and autoencoders for dimensionality reduction
│   ├── vae.py              # Base VAE interface (non-linear embeddings)
│   ├── vae_selfies.py      # VAE for molecular SELFIES strings
│   └── vae_mario.py        # VAE for game level design
│
├── experiments/             # Benchmark experiments on various objectives
│   ├── benchmark_on_pmo/   # Practical molecular optimization (PMO)
│   ├── benchmark_on_foldx/ # Protein stability (FoldX)
│   ├── benchmark_on_rasp/  # RNA aptamer selection
│   ├── training_vae_on_zinc250k/  # Train VAE on ZINC molecules
│   ├── training_ae_on_rfp_pool/   # Train AE on RFP proteins
│   └── pool.py             # Parallel experiment execution
│
├── solvers/                 # Solver registry (interface to poli-baselines)
│   └── (Points to poli-baselines implementations)
│
└── utils/                   # Utility functions
    ├── latent_space_solver.py  # Generic latent space BO wrapper
    ├── experiments/         # Loader utilities for solvers, models, problems
    ├── logging/            # WandB integration, reproducibility tracking
    ├── data/               # ZINC250k, Mario dataset utilities
    ├── selfies/            # Molecular SELFIES string utilities
    └── results/            # Leaderboard generation and analysis
```

### Key Concepts

**Non-linear Embeddings** (the approach behind LaMBO, LSBO):
- Train VAE on molecules or proteins
- Optimize in learned latent space (much lower dimension)
- Decode discovered latent codes back to valid sequences
- Enables 100-1000x dimensionality reduction

**Variable Selection**:
- Focus optimization on key dimensions
- Identify important residues in proteins
- Select mutable positions in forward design

**Linear Embeddings**:
- Project problem to random or data-driven subspace
- Faster than non-linear but less flexible
- Works when effective dimension is low

**Structured Spaces**:
- Handle discrete variables directly
- Use specialized kernels for categorical variables
- No embedding needed (what you optimize is what you get)

## Checking ongoing results

[Check our leaderboards in our project website.](https://machinelearninglifescience.github.io/hdbo_benchmark)

## Adding a new solver

### Adding necessary files

We expect contributions to this benchmark to be implemented as solvers in [`poli-baselines`](https://github.com/MachineLearningLifeScience/poli-baselines). [Follow the documentation therein](https://machinelearninglifescience.github.io/poli-docs/contributing/a_new_solver.html).

In a few words, we expect you to provide the following folder structure:

```bash
# In poli-baselines' solvers folder
solvers
├── your_solver_name
│   ├── __init__.py
│   ├── environment.your_solver_name.yml
│   └── your_solver_name.py
```

We expect `environment.your_solver_name.yml` to create a conda environment in which `your_solver_name.py` could be imported. See a template here:

```yml
name: poli__your_solver_name
channels:
  - defaults
dependencies:
  - python=3.10
  - pip
  - pip:
      - your
      - dependencies
      - here
      - "git+https://github.com/MachineLearningLifeScience/poli.git@dev"
      - "git+https://github.com/MachineLearningLifeScience/poli-baselines.git@main"
```

Provide said code as **as a pull request to poli-baselines.** Afterwards, we will register it, run it, and add its reports to our ongoing benchmarks.


### (Optional) Running your solver locally

If you feel eager to test it in our problems, you could prepare for local testing here. We provide a `requirements.txt`/`environment.yml` you can use to create an environment for running the benchmarks. Afterwards, install this package:

```bash
conda create -n hdbo_benchmark python=3.10
conda activate hdbo_benchmark
pip install -r requirements.txt
pip install -e .
```

Change the `WANDB_PROJECT` and `WANDB_ENTITY` in `src/hdbo_benchmark/utils/constants.py`.

After implementing a solver in `poli-baselines`, you can **register it** in `src/hdbo_benchmark/utils/experiments/load_solvers.py`.

The scripts used to run the benchmarks can be found in `src/hdbo_benchmark/experiments`. To run e.g. `albuterol_similarity` [of the PMO benchmark](https://openreview.net/forum?id=yCZRdI0Y7G) you can run:

```bash
conda run -n hdbo_benchmark python src/hdbo_benchmark/experiments/benchmark_on_pmo/run.py \
    --function-name=albuterol_similarity \
    --solver-name=line_bo \
    --latent-dim=128 \
    --max-iter=300 \
```

assuming `hdbo_benchmark` is an environment in which you can run your solver, and in which this package is installed. Examples of environments where solvers have been tested to run can be found in `poli-baselines`.

## Replicating the data preprocessing for downloading zinc250k

We use [torchdrug](https://torchdrug.ai/docs/installation.html) to download the dataset. It has very picky dependencies, but you should be able to install it by running

```bash
conda env create --file environment.data_preprocessing.yml
```

and following the scripts in `src/hdbo_benchmark/data_preprocessing/zinc250k` inside that env (`conda activate hdbo__data_preprocessing`).

## Citing all the relevant work

Depending on the black box you use within `poli`, we expect you to cite a set of references. [Check the documentation of the black box for a list (including `bibtex`)](https://machinelearninglifescience.github.io/poli-docs/using_poli/objective_repository/all_objectives.html).




## Adding a new solver

### Adding necessary files

We expect contributions to this benchmark to be implemented as solvers in [`poli-baselines`](https://github.com/MachineLearningLifeScience/poli-baselines). [Follow the documentation therein](https://machinelearninglifescience.github.io/poli-docs/contributing/a_new_solver.html).

In a few words, we expect you to provide the following folder structure:

```bash
# In poli-baselines' solvers folder
solvers
├── your_solver_name
│   ├── __init__.py
│   ├── environment.your_solver_name.yml
│   └── your_solver_name.py
```

We expect `environment.your_solver_name.yml` to create a conda environment in which `your_solver_name.py` could be imported. See a template here:

```yml
name: poli__your_solver_name
channels:
  - defaults
dependencies:
  - python=3.10
  - pip
  - pip:
      - your
      - dependencies
      - here
      - "git+https://github.com/MachineLearningLifeScience/poli.git@dev"
      - "git+https://github.com/MachineLearningLifeScience/poli-baselines.git@main"
```

Provide said code as **as a pull request to poli-baselines.** Afterwards, we will register it, run it, and add its reports to our ongoing benchmarks.


### (Optional) Running your solver locally

If you feel eager to test it in our problems, you could prepare for local testing here. We provide a `requirements.txt`/`environment.yml` you can use to create an environment for running the benchmarks. Afterwards, install this package:

```bash
conda create -n hdbo_benchmark python=3.10
conda activate hdbo_benchmark
pip install -r requirements.txt
pip install -e .
```

Change the `WANDB_PROJECT` and `WANDB_ENTITY` in `src/hdbo_benchmark/utils/constants.py`.

After implementing a solver in `poli-baselines`, you can **register it** in `src/hdbo_benchmark/utils/experiments/load_solvers.py`.

The scripts used to run the benchmarks can be found in `src/hdbo_benchmark/experiments`. To run e.g. `albuterol_similarity` [of the PMO benchmark](https://openreview.net/forum?id=yCZRdI0Y7G) you can run:

```bash
conda run -n hdbo_benchmark python src/hdbo_benchmark/experiments/benchmark_on_pmo/run.py \
    --function-name=albuterol_similarity \
    --solver-name=line_bo \
    --latent-dim=128 \
    --max-iter=300 \
```

assuming `hdbo_benchmark` is an environment in which you can run your solver, and in which this package is installed. Examples of environments where solvers have been tested to run can be found in `poli-baselines`.

## Replicating the data preprocessing for downloading zinc250k

We use [torchdrug](https://torchdrug.ai/docs/installation.html) to download the dataset. It has very picky dependencies, but you should be able to install it by running

```bash
conda env create --file environment.data_preprocessing.yml
```

and following the scripts in `src/hdbo_benchmark/data_preprocessing/zinc250k` inside that env (`conda activate hdbo__data_preprocessing`).

## Citing all the relevant work

Depending on the black box you use within `poli`, we expect you to cite a set of references. [Check the documentation of the black box for a list (including `bibtex`)](https://machinelearninglifescience.github.io/poli-docs/using_poli/objective_repository/all_objectives.html).

