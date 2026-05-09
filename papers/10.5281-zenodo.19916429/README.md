---
title: "The 731 Instruction Set Architecture (Origami ISA): Machine Code, Pachner Opcodes, Geometric Constraint Satisfaction, and Simplicial Paging"
paper_number: "258"
doi: "10.5281/zenodo.19916429"
zenodo_url: "https://zenodo.org/records/19916429"
portfolio: "C"
portfolio_desc: "Quantum Hardware"
tags:
  - asa
  - portfolio-c
  - paper-258
layout: default
parent: Papers
nav_order: 258
has_code: false
status: published
---

# The 731 Instruction Set Architecture (Origami ISA): Machine Code, Pachner Opcodes, Geometric Constraint Satisfaction, and Simplicial Paging

**Paper:** 258 | **Portfolio C** — Quantum Hardware

**DOI:** [10.5281/zenodo.19916429](https://zenodo.org/records/19916429)

## Abstract

Specifies the Origami ISA: a machine-code level instruction set for the 731-RPU (Resonance Processing Unit) using Pachner moves as opcodes and simplicial paging for memory management.

**v2.0** adds the Peirce Register Architecture: the full 27-dimensional state space $\mathfrak{J}_3(\mathbb{O}) = \mathcal{J}_1(P) \oplus \mathcal{J}_{1/2}(P) \oplus \mathcal{J}_0(P)$ is identified as three distinct registers — the 16-dimensional Peirce-½ exceptional core as the quantum working register, the 1-dimensional $\mathcal{J}_1$ as the output register, and the 10-dimensional $\mathcal{J}_0$ as the classical ancilla. Algebraic noise protection (from Paper 235 Theorem 3.2) is distinguished from thermodynamic error suppression.

## Key Results

- **4 base opcodes**: Inject ($1\to 4$ Pachner), Collapse ($4\to 1$), Cleave ($2\to 3$), Fuse ($3\to 2$)
- **Peirce register architecture** (v2.0): $\mathcal{J}_{1/2}(P)$ as quantum working register; Fano-Slots ($e_1\ldots e_7$) are its generators
- **Simplicial Paging**: saturated Fano-crystals compressed to 0-skeleton pointers; constant VRAM overhead
- **Error suppression**: Associator Penalty thermodynamically disfavours non-$PSL(2,7)$ states; reinforced by algebraic protection of $\mathcal{J}_{1/2}(P)$

## Zenodo

[View on Zenodo](https://zenodo.org/records/19916429)

## Related Papers

- [Paper 207 — 731-Calculus](../10.5281-zenodo.19713350/) (magmoidal string diagrams; diagrammatic calculus for the ISA)
- [Paper 205 — RPU](../10.5281-zenodo.19743800/) (hardware target; 1531-Anvil triorthogonal codes)
- [Paper 206 — FTCs](../10.5281-zenodo.19821692/) (error correction codes running on the 731-RPU)
- [Paper 235 — Fano-Token](../10.5281-zenodo.20100531/) (Map Collapse theorem grounding the $\mathcal{J}_{1/2}$ noise protection)
- [Paper 257 — NA-QEC](../10.5281-zenodo.20088536/) (Peirce decomposition machinery; U-operator)

