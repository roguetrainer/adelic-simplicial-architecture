---
title: "The Self-Dual G₂ Architecture: Pachner Unitarity, CSS Symmetry, and the Crystal Spectrum Halving"
paper_number: "271"
doi: "10.5281/zenodo.20101634"
zenodo_url: "https://zenodo.org/records/20101634"
portfolio: "E"
portfolio_desc: "Grand Challenges"
tags:
  - asa
  - portfolio-e
  - paper-271
layout: default
parent: Papers
nav_order: 271
has_code: true
status: draft
---

**Paper:** 271 | **Portfolio E** — Grand Challenges

**DOI:** [10.5281/zenodo.20101634](https://zenodo.org/records/20101634)

## Abstract

The exceptional Lie group $G_2$ is self-dual as a root system: its coroot system is isomorphic to its root system, with long and short roots exchanged. The Fano plane $\mathrm{PG}(2,2)$ — the combinatorial object governing $G_2$ — is projectively self-dual: swapping its 7 points and 7 lines is an automorphism of the incidence structure. We show that this single algebraic fact has three distinct and calculable consequences for the Adelic Simplicial Architecture:

1. **Pachner unitarity**: The 1↔4 (■ Split / ◇ Splat) and 2↔3 (▲ Flip / ▷ Flop) opcode pairs of the 731 Origami ISA are exact inverses on Fano-compatible states. Information loss equals the associator on the boundary, which vanishes by the Map Collapse theorem (Paper 235, Theorem 3.2). The 731-Calculus restricted to Fano-compatible states is strictly unitary.

2. **CSS symmetry**: The X-type and Z-type stabilisers of the Fibrational Tensor Codes (Paper 206) are isomorphic under G₂ root/coroot exchange. The bit-flip and phase-flip error thresholds are identical. No asymmetric tuning is required.

3. **Crystal spectrum halving**: The Fano crystal spectrum requires computing eigenvalues of only 4 of the 7 $G_2$ generators; the remaining 3 are determined by the self-dual map. We verify this numerically for the $7 \times 7$ Fano incidence matrix.

Together these results establish $G_2$ self-duality as a unifying computational principle across the ISA, QEC, and optimisation layers of the ASA stack.

## Key Results

- **Theorem 2.1 (Pachner Unitarity)**: $◇ \circ ■ = \mathrm{id}$ and $▷ \circ ▲ = \mathrm{id}$ in the $G_2$ simplicial complex on Fano-compatible states. The residual from non-Fano boundary terms equals $\mathcal{A}(x,y,z) = (xy)z - x(yz)$, which is zero on the seven Fano lines.

- **Theorem 3.1 (CSS Symmetry from G₂ Self-Duality)**: The Fibrational Tensor Code stabiliser group satisfies $H_X \cong H_Z$ under the $G_2$ root/coroot isomorphism. The Steane $[[7,1,3]]$ self-dual CSS structure is a corollary.

- **Proposition 4.1 (Crystal Spectrum Halving)**: The $G_2$ Fano crystal spectrum has a $\mathbb{Z}/2$ symmetry exchanging long- and short-root eigenvalues. Independent calculations reduce from 7 to 4 generators.

- **Section 5 (Computational Equivalence Principle)**: $G_2$ self-duality guarantees that the MGE continuous relaxation (BOIL phase, $\beta \to 0$) and the Fano crystallisation (SNAP phase, $\beta \to \infty$) are governed by the same geometric object. The phase transition is lossless on Fano-compatible states.

## Relation to Portfolio

| Result | Consequence | Relevant Papers |
| --- | --- | --- |
| Pachner unitarity | 731-Calculus is reversible | Paper 207, 258 |
| CSS symmetry | FTC thresholds equalised | Paper 206, 257, 217 |
| Spectrum halving | Fano crystal computation halved | Paper 207, 211 |
| Equivalence principle | BOIL/SNAP lossless | Paper 201, 202 |

## Zenodo

[View on Zenodo](https://zenodo.org/records/20101634)

## Related Papers

- [Paper 207 — The 731-Calculus](../10.5281-zenodo.19713350/) (magmoidal string diagrams; Pachner move rewrite rules)
- [Paper 258 — Origami ISA](../10.5281-zenodo.19916429/) (■◇▲▷ Split/Splat/Flip/Flop opcodes; Peirce register architecture)
- [Paper 206 — Fibrational Tensor Codes](../10.5281-zenodo.19821692/) (G₂ fibre bundle stabilisers; FTC thresholds)
- [Paper 257 — NA-QEC](../10.5281-zenodo.20088536/) (Exceptional Jordan–KL Condition; Peirce decomposition)
- [Paper 235 — Fano-Token](../10.5281-zenodo.20100531/) (Map Collapse theorem; associator = 0 on Fano lines)
- [Paper 217 — Fibrational Lattice Surgery LS2.0](../10.5281-zenodo.19922441/) (fault-tolerant gates on fibre bundle codes)
- [Paper 211 — Non-Associative Calculus](../10.5281-zenodo.20025384/) (octonionic foundation; right-division norm)
- [Paper 201 — MGE](../10.5281-zenodo.17981393/) (thermodynamic routing; BOIL/SNAP schedule)
- [Paper 202 — TRS](../10.5281-zenodo.19858021/) (Fano crystallisation; phase transition)
- [Paper 267 — Fano-SYK](../10.5281-zenodo.20057808/) (thermodynamic reversibility; Bruhat-Tits building)

## Code

[Code for this paper](../../code/10.5281-zenodo.20101634/)
