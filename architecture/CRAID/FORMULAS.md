# CRAID : Mathematical Index
**Version:** 1.0
**Scope:** Erasure Coding and Availability.

---

## 1. Reed-Solomon Reconstruction
The fundamental condition for memory recovery.

### 📐 LaTeX
$$
R_{capability} = \begin{cases} 
1 & \text{if } k \ge N \\
0 & \text{if } k < N 
\end{cases}
$$

### 💻 Python
```python
# k: Available shards
# N: Data shards required
def can_recover(k, N):
    return k >= N

* N : Number of Data Shards (e.g., 3)
* M : Number of Parity Shards (e.g., 2)
* k : Number of active/healthy nodes found

2. Storage Overhead
Calculating the cost of resilience.


📐 LaTeX


$$O_{verhead} = \frac{N + M}{N}$$



Example (3+2): $5 / 3 \approx 1.66$ (66% overhead for ultimate safety).


3. Failure Probability ($P_{fail}$)
   Probability of losing data given node failure rate $p$.

📐 LaTeX


$$P_{fail} = \sum_{i=M+1}^{N+M} \binom{N+M}{i} p^i (1-p)^{N+M-i}$$



---
