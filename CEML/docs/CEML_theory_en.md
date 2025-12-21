# The Cognitive Entropy Minimization Law (CEML)

**A Unified Mathematical Framework for Information Selection in Cognitive Systems**

* **Author:** Bryan Ouellette
* **Date:** December 13, 2025
* **Version:** 2.0 (Unified)

---

## 1. Abstract

This paper introduces the **Cognitive Entropy Minimization Law (CEML)**, a fundamental principle governing how intelligent systems—biological or artificial—select information from infinite possibilities under finite resource constraints. We postulate that cognitive agents act to maximize the **Contextual Coherence** of a representation while simultaneously minimizing its **Internal Entropy** (description length). This trade-off is mathematically formalized as an objective function that unifies Karl Friston’s Free Energy Principle, Occam’s Razor, and Landauer’s Principle into a single predictive metric.

## 2. Fundamental Postulate: The Principle of Least Cognitive Action

Intelligence is not merely the accumulation of data, but the efficient compression of reality. We propose the following axiom:

> **The Axiom of Cognitive Efficiency:**
> Every cognitive agent, constrained by finite processing resources (metabolic or computational), preferentially selects information structures that maximize semantic utility while minimizing energetic cost.

Just as physical systems follow the path of least action, cognitive systems navigate the "information space" by following gradients of minimal entropy.


## 3. Mathematical Formalization

Let $S$ be the set of all possible candidate information structures (a thought, a sentence, a vector representation). The system seeks to identify the optimal structure $s^*$ by maximizing the objective function $J(s)$.

### 3.1 The Master Equation

$$J(s) = \frac{\mathcal{C}(s \mid \Omega)}{\mathcal{H}(s) + \epsilon}$$

Where:
* **$s$**: The candidate structure (e.g., a token sequence, a neural pathway).
* **$\Omega$**: The current external context or ground truth.
* **$\epsilon$**: A regularization constant ($\epsilon \to 0^+$) to prevent singularity.

### 3.2 Component Definition

#### A. Contextual Coherence $\mathcal{C}(s \mid \Omega)$
This term represents the **Semantic Utility**. It quantifies how well the structure $s$ aligns with the context $\Omega$.

In Vector Space (AI/NLP), it is defined as the Cosine Similarity between the context vector $\vec{v}_{\Omega}$ and the candidate vector $\vec{v}_s$:

$$\mathcal{C}(s \mid \Omega) = \frac{\vec{v}_{\Omega} \cdot \vec{v}_s}{\lVert \vec{v}_{\Omega} \rVert \, \lVert \vec{v}_s \rVert}$$

*Interpretation:* High coherence implies truth, relevance, and semantic alignment.

#### B. Entropic Cost $\mathcal{H}(s)$
This term represents the **Metabolic or Computational Cost**. It is the Shannon Entropy or Kolmogorov Complexity of the structure.

**Thermodynamic Link:** Per Landauer’s Principle, processing high-entropy information dissipates more heat.
$$E_{\text{cost}} \propto k \cdot \mathcal{H}(s) = -k \sum p_i \log_2 p_i$$

*Interpretation:* High entropy implies chaos, noise, and high cognitive load. Low entropy implies order, compression, and efficiency.

## 4. The Selection Logic

The CEML predicts the viability of an information structure based on the ratio of the two components.

| State Type | Coherence $\mathcal{C}$ | Entropy $\mathcal{H}$ | CEML Score $J(s)$ | System Decision | Example |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Resonance** | High (↑) | Low (↓) | **Maximum** | **SELECT** | "The sky is blue." |
| **Dissonance** | Low (↓) | Low (↓) | Low | **REJECT** | "The cat is cubic." |
| **Chaos** | High/Low | High (↑) | Low | **REJECT** | "Blue sky... 37x... random noise." |
| **Hallucination** | High (↑) | Artificial Low | False Max | **Pathology** | Plausible but false cliché. |

The optimal state $s^*$ is the solution to the maximization argument:

$$s^* = \underset{s \in \mathcal{S}}{\mathrm{argmax}} \left( \frac{\mathcal{C}(s \mid \Omega)}{\mathcal{H}(s) + \epsilon} \right)$$

## 5. Scientific Anchoring

The CEML serves as a unifying bridge between distinct scientific disciplines:

1.  **Thermodynamics (Landauer):** Intelligence emerges from the necessity to predict the environment with the least amount of heat dissipation.
2.  **Neuroscience (Friston):** The brain minimizes "Surprise" (Free Energy). In CEML, minimizing $\mathcal{H}(s)$ is mathematically equivalent to minimizing surprise in the internal model.
3.  **Information Theory (Rissanen/Shannon):** The denominator $\mathcal{H}(s)$ enforces **Occam's Razor**—the simplest explanation (shortest description length) that fits the data is preferred.

## 6. Algorithmic Validation

To validate the theory, we define an operational algorithm for computational systems (like LLMs).

**Algorithm: CEML-Select**
* **Input:** Context $\Omega$, Candidates $S = \{s_1, s_2, ...\}$
* **Process:**
    1.  Compute Vector Embedding for $\Omega$ and each $s_i$.
    2.  Calculate Coherence $\mathcal{C} = \cos(\theta)$.
    3.  Estimate Entropy $\mathcal{H}$ via Compression Ratio (Zlib/Gzip) or Log-Probability.
* **Output:** Select $s_i$ with max ratio.

**Experimental Results:** Preliminary tests on probability distributions confirm that the system rejects both "Uniform Distributions" (Max Entropy) and "Dirac Deltas" (Zero Entropy but often low contextual fit), converging on **Ordered Complexity** (High Coherence, Low-to-Medium Entropy).

## 7. Conclusion

The Cognitive Entropy Minimization Law offers a rigorous framework for understanding intelligence. It suggests that "understanding" is effectively a compression algorithm. By maximizing the $\mathcal{C}/\mathcal{H}$ ratio, biological and artificial agents ensure their survival by maintaining alignment with reality while conserving the energy required to represent it.

---

### Terminology & Scope
The term “law” in Cognitive Entropy Minimization Law (CEML) is used in an operational and heuristic sense, inspired by analogies with physical selection principles, not as a claim of a proven universal physical law. CEML is proposed as a candidate cognitive selection principle: a formal, testable, and falsifiable framework describing how intelligent systems may preferentially select informational structures under constraints of context, memory, and energy. Its validity is empirical and conditional, and it is intended to guide analysis, experimentation, and system design rather than to assert absolute epistemic truth.
