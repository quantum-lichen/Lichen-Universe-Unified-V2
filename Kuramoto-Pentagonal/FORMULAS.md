# Kuramoto Pentagonal : Mathematical Index
**Version:** 1.0
**Scope:** Hamiltonians and Topology.

---

## 1. The Total Hamiltonian
The governing equation of the 5-qubit system.

### 📐 LaTeX
$$
\hat{H} = \sum_{i=1}^5 \omega_i \hat{\sigma}_z^{(i)} + \sum_{\langle i,j \rangle} J_{ij} \vec{\sigma}^{(i)} \cdot \vec{\sigma}^{(j)} + \sum_{\langle i,j \rangle} K_{ij} \sin(\theta_i - \theta_j)
$$

### 💻 Python (QuTiP Style)
```python
# H_total = H_local + H_coupling + H_kuramoto
H = sum(w[i] * sigma_z[i] for i in range(5)) + \
    sum(J * (sigma_x[i]*sigma_x[j] + sigma_y[i]*sigma_y[j]) for i,j in pairs)
