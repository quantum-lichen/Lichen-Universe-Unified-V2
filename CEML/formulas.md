# CEML : Mathematical Index
**Version:** 2.1 (Standardized)
**Scope:** Canonical equations for Cognitive Entropy Minimization.

---


## 1. The Master Equation
The fundamental fitness score for information selection.


### 📐 LaTeX


$$
J(s) = \frac{\mathfrak{C}(s|\Omega)}{S(s) + \epsilon}
$$


### 💻 Python
```python
# CEML Score Calculation
J = coherence / (entropy + epsilon)
```

**Variables:**
* $\mathfrak{C}$: Contextual Coherence (Semantic Alignment).
* $S$: Entropic Cost (Shannon Entropy).
* $\epsilon$: Regularization constant ($10^{-6}$).

---

## 2. Contextual Coherence ($\mathfrak{C}$)
Calculated via Cosine Similarity in vector space.


### 📐 LaTeX


$$
\mathfrak{C}(s|\Omega) = \frac{\vec{v}_{\Omega} \cdot \vec{v}_s}{\|\vec{v}_{\Omega}\| \|\vec{v}_s\|}
$$


### 💻 Python
```python
# Cosine Similarity
C = np.dot(v_ctx, v_s) / (np.linalg.norm(v_ctx) * np.linalg.norm(v_s))
```

---

## 3. Entropic Cost ($S$)
Calculated via Shannon Entropy.

### 📐 LaTeX


$$
S(s) = -\sum_{i} p_i \log_2 p_i
$$


### 💻 Python
```python
# Shannon Entropy
S = -sum(p * math.log2(p) for p in probs if p > 0)
```


---

## 4. Resonance Threshold ($\tau$)
The acceptance limit based on the Golden Ratio.

### 📐 LaTeX


$$
\tau \geq \varphi = \frac{1 + \sqrt{5}}{2} \approx 1.618
$$


### 💻 Python
```python
# Resonance Check
is_resonant = J_score >= 1.61803398875
```
