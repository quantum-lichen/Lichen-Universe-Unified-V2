# H-Scale : Mathematical Index
**Version:** 1.1 (Standardized)
**Scope:** Harmonic Metrics and Decision Thresholds.

---

## 1. The Harmonic Equation
The weighted vector sum for decision scoring.

### 📐 LaTeX
$$
\mathcal{H} = 0.3\mathfrak{C} + 0.2E_{ff} + 0.3R + 0.2D
$$

### 💻 Python
```python
# H-Scale Calculation
# E_ff must be (1 - Entropy) if Entropy is provided
H = (0.3 * C) + (0.2 * E_ff) + (0.3 * R) + (0.2 * D)
```

**Variables:**
* $\mathfrak{C}$: Coherence ($w=0.3$).
* $E_{ff}$: Efficiency ($w=0.2$).
* $R$: Resonance ($w=0.3$).
* $D$: Durability ($w=0.2$).

---

## 2. The Golden Threshold ($H_0$)
The binary pass/fail limit for any cognitive action.

### 📐 LaTeX
$$
H_0 = \frac{1}{\varphi} = \frac{2}{1 + \sqrt{5}} \approx 0.61803
$$

### 💻 Python
```python
PHI = 1.61803398875
H_THRESHOLD = 1.0 / PHI  # ~0.618
is_valid = H_score >= H_THRESHOLD
```

---

## 3. Efficiency Derivation
Converting Entropic cost to Efficiency score.

### 📐 LaTeX
$$
E_{ff} = 1 - \frac{S(s)}{S_{max}}
$$

### 💻 Python
```python
# Assuming normalized entropy between 0 and 1
efficiency = 1.0 - entropy_normalized
```
