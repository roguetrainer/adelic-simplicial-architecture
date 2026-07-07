---
layout: default
title: "The Maslov-Gibbs Einsum (MGE)"
parent: Explainers
nav_exclude: false
tags: [core-engine, mge, tropical, beta, maslov, gibbs, einsum, partition-function, origami-isa, forge-isa, meld-isa, ambient, dodecagon, log-sum-exp, semiring, phase-transition, snap-event]
portfolio: A
---

## One Equation, Every Computational Model

*Plain-language explainer for [doi:10.5281/zenodo.17981393](https://doi.org/10.5281/zenodo.17981393) (#201)*

---

## The central idea in one sentence

The Maslov-Gibbs Einsum is a single parameterised equation — the Gibbs partition function written as a tensor contraction — whose behaviour changes continuously from smooth probability distribution to hard discrete logic as a single parameter β rises from zero to infinity, and which reproduces twelve foundational constructs of mathematics and computer science as exact limiting cases.

---

## The equation

$$\pi_k(\beta) = \frac{e^{-\beta E_k}}{\sum_j e^{-\beta E_j}}$$

This is the Boltzmann/Gibbs distribution, written for a system with energy levels $E_k$ and inverse temperature β. It is also the softmax function used in every neural network. It is also the forward algorithm in hidden Markov models. It is also the Viterbi algorithm at the limit. It is also the attention mechanism in Transformers. These are not analogies — they are the same equation at different values of β, different index structures, or different choices of energy tensor.

The MGE is the formal packaging of this observation: write the equation as a high-dimensional **einsum tensor contraction** over an energy tensor $\mathbf{E}$, so that the same code path handles all cases by varying β and the contraction pattern.

---

## What β does

β is the inverse temperature — the single dial that controls what kind of computation you get.

| β | Arithmetic | What it computes |
|---|---|---|
| 0 | Uniform weights | The Ambient — no commitment, pure exploration |
| real, finite | Gibbs weights | Statistical mechanics; the Forge ISA |
| real, large | Tropical max | Hard discrete logic; the Origami ISA |
| imaginary ($it$) | Complex phases | Quantum amplitudes; the Meld ISA |
| negative | Inverted Boltzmann | Population inversion; lasers |
| p-adic | Ultrametric | p-adic computation |

The transition from Gibbs weights to the tropical maximum is the key limit. As β → ∞, the softmax concentrates all weight on the single lowest-energy configuration:

$$\lim_{\beta \to \infty} \frac{e^{-\beta E_k}}{\sum_j e^{-\beta E_j}} \;\to\; \delta_{k,\,\mathrm{argmin}_j\, E_j}$$

A smooth probability distribution over all paths collapses to a point — the ground state. This is Maslov dequantisation: the passage from the real number field to the tropical semiring $(\mathbb{R} \cup \{-\infty\}, \max, +)$. Continuous gradient descent crystallises into discrete combinatorial logic. The **snap event** at $\beta^\star$ is the threshold at which the distribution commits to its answer.

---

## The MGE Dodecagon: twelve constructs, one equation

The paper demonstrates that twelve foundational constructs across mathematics, physics, and computer science are exact limiting cases of the MGE at specific values of β and specific contraction patterns:

| Construct | β regime | Field |
|---|---|---|
| Softmax / attention | Finite real | Machine learning |
| Boltzmann distribution | Finite real | Statistical mechanics |
| Gibbs free energy | Finite real | Thermodynamics |
| Log-sum-exp | Finite real | Convex analysis |
| Viterbi algorithm | Large real | Sequence decoding |
| Tropical maximum | Large real | Tropical geometry |
| Dynamic programming | Large real | Combinatorial optimisation |
| Optimal transport (Sinkhorn) | Finite real | Geometry / logistics |
| Forward-backward algorithm | Finite real | Hidden Markov models |
| Hamilton-Jacobi equation | Large real | Control theory |
| Schrödinger bridge | Imaginary | Quantum mechanics |
| Extreme value statistics (Gumbel) | Large real | Probability theory |

These are not approximations or analogies. Each is obtained by choosing the right index structure for $\mathbf{E}$ and taking the appropriate limit of β. The MGE is the common parent.

---

## Three geometric invariances

Beyond the dodecagon, the paper establishes three structural properties of the MGE:

**1. Conformal invariance.** Uniform scaling of all energies $E_k \mapsto \lambda E_k$ is equivalent to rescaling β → β/λ. The shape of the distribution is invariant under joint rescaling — only the ratio $\beta / \Delta E$ matters, where $\Delta E$ is the spectral gap.

**2. Symplectic volume preservation.** The flow on the probability simplex induced by varying β preserves symplectic volume (Liouville's theorem). The MGE is a Hamiltonian flow on the space of distributions.

**3. Adiabatic topological protection.** If β is ramped slowly relative to the spectral gap, the ground state is tracked adiabatically — the same protection that underlies quantum annealing. The convergence rate is exponential: $\mathcal{O}(e^{-\beta \Delta E})$.

---

## Where this sits in the ISA framework

The MGE is the engine underneath all three operative ISAs:

**Origami ISA** (β → ∞): the tropical limit — the MGE frozen to its ground state. Classical Boolean logic, dynamic programming, shortest paths. Every FLIP, FLOP, ORBIT opcode is a tropical operation.

**Forge ISA** (β real, finite): the MGE in full Gibbs mode — statistical mechanics, annealing, thermodynamic computation. The snap event $\beta^\star$ separates the exploratory phase from the committed phase.

**Meld ISA** (β = it): Wick-rotate β to imaginary — the MGE becomes a sum of complex phases, i.e. a quantum amplitude. Unitary evolution, interference, and Shor's algorithm all live here.

The **Ambient** (β = 0) is the uniform limit: no energy landscape, no preference, pure Hodge theory. All three operative ISAs precipitate from the Ambient as β moves away from zero.

Paper 543 extends this picture to the full adèlic β-plane, showing that negative β (lasers, population inversion), complex β (PT-symmetric quantum mechanics), and p-adic β are also exact regimes of the same equation — and that Ostrowski's theorem closes the map.

---

## The snap event

The phase transition at $\beta^\star$ is the central computational event. Below $\beta^\star$ the system is exploratory; above it the system is frozen. Every classical algorithm, every catalytic cycle in chemistry, every annealing schedule is a trajectory on the positive real β-axis that crosses $\beta^\star$.

The snap event is not an approximation threshold. It is the moment at which continuous optimisation becomes discrete logic — the functor connecting the two halves of computer science.

---

## What this paper does and does not claim

The softmax, Viterbi, log-sum-exp, and Boltzmann distribution were all known before this paper. What is new is:

1. The formal unification as a single parameterised tensor contraction (the einsum packaging)
2. The MGE Dodecagon — systematic enumeration of the twelve limiting cases
3. The three geometric invariances (conformal, symplectic, adiabatic)
4. The identification of β as the parameter whose domain determines the computational regime

The MGE is not the equation that computes things. It is the equation that explains why so many different computations are the same thing.

---

*See also:*
- [The Adèlic β-Plane](https://doi.org/10.5281/zenodo.21245459) (#543) — the full parameter space: β complex, negative, and p-adic; why ℏ = 1/β; PT-symmetry; Ostrowski's theorem closes the map
- [Planck's Constant in Disguise](https://doi.org/10.5281/zenodo.20752384) (#443) — six classical dualities (Cole-Hopf, Black-Scholes, Sinkhorn, Viterbi, Hamilton-Jacobi) as semiring deformations of the MGE
- [The Forge ISA](https://doi.org/10.5281/zenodo.20694527) (#419) — the positive real axis: snap event, vorton architecture, thermodynamic computation
- [The Meld ISA](https://doi.org/10.5281/zenodo.20773563) (#454) — the imaginary axis: Wick rotation, quantum algorithms, T-gate as obstruction
- [Hodge Theory as the Smooth Limit](https://doi.org/10.5281/zenodo.20684838) (#417) — the β = 0 Ambient: discrete algorithms as tropical shadows of smooth manifold problems

*For the full technical treatment, see [doi:10.5281/zenodo.17981393](https://doi.org/10.5281/zenodo.17981393)*
