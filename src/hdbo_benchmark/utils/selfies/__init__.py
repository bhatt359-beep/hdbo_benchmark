"""
SELFIES Utilities for Molecular Representation

SELFIES (Self-Referencing Embedded Strings) is a 100% robust molecular string
representation that guarantees syntactically and semantically valid molecules.

Why SELFIES for Molecular BO?
============================

The HDBO survey emphasizes representation quality for sequence optimization.
SELFIES addresses key challenges with SMILES:

Advantages over SMILES:
1. **Chemical Validity**: 100% of SELFIES strings decode to valid molecules
   - SMILES: ~5% of random modifications produce invalid strings
   - SELFIES: All modifications valid by construction

2. **BO-Friendly Design**:
   - Unambiguous token stream
   - Reversible encoding/decoding
   - Supports point mutations in latent space
   - Works with character-level BO

3. **Embedding Space Quality**:
   - SELFIES strings can be directly optimized
   - Or encoded to latent space with VAE
   - VAE produces smoother latent space than SMILES
   - Decoding always yields valid molecules

4. **Sequence Properties**:
   - Fixed vocabulary (allowed SELFIES tokens)
   - Hierarchical structure (atoms -> bonds -> molecules)
   - Supports constraint-based generation

Real-World Impact in Survey:
- PMO benchmark uses SELFIES strings
- Molecular design experiments use SELFIES
- VAE training on ZINC250k uses SELFIES
- LaMBO method works with SELFIES

SELFIES Token System
===================

SELFIES atoms: [He], [Li], [B], [C], [N], [O], [F], etc.
SELFIES bonds: [=], [#], special syntax for aromaticity
Structure control: [Ring1], [Ring2], [Branch1], nested constructs

Example:
- Molecule: Ethane
- SMILES: "CC"
- SELFIES: "[C][C]"
- Decode -> Valid ethane molecule

Key Submodules:

1. **tokens**: Token manipulation and validation
   - List valid SELFIES tokens
   - Map molecules <-> tokens
   - Constraint handling
   - Special tokens for rings and branches

2. **visualization**: Molecular structure visualization
   - Draw molecule structures
   - Highlight optimized regions
   - Show property predictions
   - Create benchmark visualizations

Integration with HDBO
====================

The workflow:
1. Start with molecule in SELFIES format
2. Encode with VAE to latent space
3. Run BO in latent space (TuRBO, SAASBO, etc.)
4. Decode discovered latent codes
5. Decode SELFIES -> valid molecules
6. Evaluate with real property predictor

Advantages for the Survey:
- All methods can use SELFIES without worrying about validity
- Fair comparison: no invalid molecule overhead
- Enables larger search spaces
- Better BO performance on valid subspace

Implementation Notes:
- SELFIES vocabulary: ~30-40 tokens
- Average molecule: 15-50 tokens
- Latent space: 2-128 dimensions
- Encoding/decoding: Deterministic and fast

References:
- Krenn et al. (2020): SELFIES: A 100% robust molecular string representation
- PMO benchmark: Uses SELFIES exclusively
- Survey Section 3.5: Non-linear embeddings with SELFIES VAE
- poli-baselines: implementations of molecular BO methods
"""
