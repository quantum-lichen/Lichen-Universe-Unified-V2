# π-Time : Mathematical Index
**Version:** 1.1
**Scope:** Temporal Conversion and Validation.

---


## 1. The Fundamental Frequency ($f_{\pi}$)
The beat frequency of the Lichen Kernel.


### 📐 LaTeX


$$
f_{\pi} = \frac{1}{\pi} \text{ Hz} \approx 0.3183 \text{ Hz}
$$



### 💻 Python
```python
import math
FREQ_PI = 1.0 / math.pi
```

2. The Timestamp Vector ($T_{\pi}$)
The structured representation of an instant.
📐 LaTeX


$$T_{\pi} = \{ C, S, P, D \}$$


Where:

$C = \lfloor t / \pi \r

floor$ (Cycle)$D = \text{BBP}(P)$ (Digit at Position P)

3. Bailey–Borwein–Plouffe (BBP) Formula

Used to calculate the $n$-th digit of $\pi$ without computing the preceding ones (hexadecimal basis, adapted for validation).

📐 LaTeX


$$\pi = \sum_{k=0}^{\infty} \frac{1}{16^k} \left( \frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6} \right)$$



