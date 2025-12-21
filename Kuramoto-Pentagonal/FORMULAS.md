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
```

* omega_i : Natural frequency of qubit i.
  
* J_ij    : Spin-spin coupling strength.
  
* K_ij    : Kuramoto synchronization strength.
  
* theta   : Phase angle of the qubit state.


2. Schrödinger Evolution
  
   The time-dependent dynamics of the self-correction.

   📐 LaTeX


   $$i\hbar \frac{\partial}{\partial t} |\Psi(t)\rangle = \hat{H}_{total} |\Psi(t)\rangle$$



   3. The 5-Qubit Encoding (Laflamme)
      The logical state definition.

      📐 LaTeX


      $$|0_L\rangle = \frac{1}{4} \left( |00000\rangle + \text{cyclic permutations} - \text{odd weight terms} \right)$$



      ---

