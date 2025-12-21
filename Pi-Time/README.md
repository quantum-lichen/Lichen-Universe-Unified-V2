# π-Time : Universal Cosmic Clock
## Le Standard Temporel Fractal

[![Status](https://img.shields.io/badge/status-specification-blue)](docs/specification.md)
[![Version](https://img.shields.io/badge/version-1.1-green)](docs/specification.md)
[![Proof of Time](https://img.shields.io/badge/Proof-BBP_Algorithm-purple)](poc/pi_clock.js)

> **"Time is not a line. It is a coordinate in the circle."**

**π-Time** replaces the arbitrary linear second with the **π-Cycle**. It acts as the heartbeat of the Lichen Universe, providing a self-verifying timestamp format where every moment is a specific digit in the infinite sequence of $\pi$.

## 🕰️ The Format
$$\pi[CYCLE].[SUB].[POSITION].[DIGIT]$$
*Example:* `π1234.057.890321.4`

## 🌌 Core Features
1.  **Universal Anchoring**: Time based on math constants, not political timezones.
2.  **Proof of Time**: The final digit acts as a checksum. If the digit doesn't match the position in $\pi$, the timestamp is fake.
3.  **Lichen Native**: Used to synchronize **FC-496** cells across the distributed system.

## 📂 Contents
* **`docs/specification.md`**: Technical specs and BBP algorithm integration.
* **`poc/pi_clock.js`**: A working JS prototype of the clock and validator.
* **`FORMULAS.md`**: The mathematical definitions of the π-Cycle.

---

V2.0

# Pi-Time : Mathematical Index
**Scope:** Temporal Indexing & Spiral Mapping.

---

## 1. The Spiral Projection (Phyllotaxis)
How we map linear time $t$ into a 2D Holographic Disk.

### 📐 LaTeX


$$
\theta_n = n \times \Psi_{gold} = n \times 2\pi(1 - \frac{1}{\varphi})
$$



$$
r_n = c \sqrt{n}
$$



Where:
* $n$ is the $\pi$-Index (derived from time).
* $\Psi_{gold}$ is the Golden Angle ($\approx 137.508^\circ$).
* $c$ is a scaling factor.

---

## 2. The $\pi$-Index Function
The conversion from linear Unix time to the immutable $\pi$ sequence.

### 📐 LaTeX



$$
I_{\pi}(t) = \lfloor t \cdot \pi \cdot 10^k \rfloor \pmod{L_{max}}
$$



*(Simplified for simulation. In production, this maps to the exact offset in the Chudnovsky algorithm stream).*

---

## 3. Stability Metric
Determining if a moment in time is "structurally sound" for write operations.

### 📐 LaTeX



$$
S_{tability} = 1 - \left| (r_n \pmod \varphi) - \frac{\varphi}{2} \right|
$$


