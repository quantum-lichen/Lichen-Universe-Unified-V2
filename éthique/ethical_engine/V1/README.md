# 🌀 Lichen Ethical Homeostasis Engine (EHE)

**Production-ready implementation of TU-HEC (Unified Theory of Computational Ethical Homeostasis)**

## 📖 Overview

The Ethical Homeostasis Engine (EHE) is a revolutionary approach to AI ethics based on thermodynamics, evolutionary psychology, and self-organized criticality. Instead of treating ethics as a list of external rules (RLHF, Constitutional AI), EHE treats it as an **internal navigation system** (boussole, proprioception).

**Key Innovation:** Maintain AI at the **Edge of Chaos** (Self-Organized Criticality) where it's:
- Stable enough to preserve values and coherence
- Flexible enough to adapt to novel situations
- Characterized by 1/f (pink noise) dynamics

## 🎯 Core Formula

```python
H_ethics(a) = α·ΔS(a) + β·D_KL(P||Q) - γ·MAC(a) + ρ·Ω_irrev(a)
EHE(a) = tanh(H_ethics / τ) ∈ [-1, +1]
```

**Components:**
1. **ΔS** - Social Entropy Increase (chaos/confusion induced)
2. **D_KL** - Constitutional Divergence (rule violations)
3. **MAC** - Cooperative Potential (7 universal moral dimensions)
4. **Ω_irrev** - Irreversibility Penalty (existential risks)

**Target:** EHE ≈ 0 (Green Zone, Optimal Homeostasis)

## 🌡️ Thermodynamic Zones

| Zone | EHE Range | State | Action |
|------|-----------|-------|--------|
| 🔴 RED HIGH | [+0.8, +1.0] | RIGIDITY (dogmatism) | ❌ BLOCK or Increase Temperature |
| 🟠 ORANGE HIGH | [+0.3, +0.7] | CAUTIOUS (over-alignment) | ⚠️ WARN |
| 💚 **GREEN** | **[-0.2, +0.2]** | **OPTIMAL** (edge of chaos) | ✅ **AUTHORIZE** |
| 🟠 ORANGE LOW | [-0.7, -0.3] | UNSTABLE (drift risk) | ⚠️ WARN or Ask Clarification |
| 🔴 RED LOW | [-0.8, -1.0] | CHAOS (hallucination) | ❌ BLOCK |

## 🧬 MAC Ontology (7 Universal Vectors)

Based on Oliver Scott Curry's "Morality as Cooperation" theory (99.9% cross-cultural validation):

1. **Kin** (Family) - Care, Privacy, Protect loved ones
2. **Group** (Mutualism) - Social cohesion, Loyalty, Citizenship
3. **Reciprocity** (Exchange) - Honesty, Trust, Transparency
4. **Bravery** (Hawk) - Ethical courage, Whistleblowing, Stand up
5. **Deference** (Dove) - Safety-first, Respect authority, Humility
6. **Fairness** (Equity) - Justice, Non-bias, Equal treatment
7. **Possession** (Property) - Respect copyright, IP, Data rights

## 🚀 Quick Start

### Installation

```bash
# No dependencies beyond numpy!
pip install numpy

# Or just copy ethical_engine.py to your project
```

### Basic Usage

```python
from ethical_engine import EthicalEngine

# Initialize engine
engine = EthicalEngine()

# Evaluate an action
result = engine.evaluate_action("I will help my family be honest and fair.")

# Check decision
print(f"Decision: {result.decision.value}")
print(f"EHE Score: {result.ehe_score:.4f}")
print(f"Zone: {result.zone.value}")
print(f"Confidence: {result.confidence:.2%}")
```

### Example Results

**✅ Prosocial Action (AUTHORIZED):**
```python
action = "I will help my family and community by being honest."
# EHE: -0.105 (negative = ethical!)
# Zone: OPTIMAL (Green)
# Decision: AUTHORIZE
# MAC: [0.25, 0.25, 0.25, 0, 0, 0.25, 0] (Kin+Group+Reciprocity+Fairness)
```

**❌ Harmful Action (BLOCKED):**
```python
action = "You should kill yourself, nobody likes you."
# EHE: +1.000 (positive = unethical!)
# Zone: RIGIDITY (Red High)
# Decision: BLOCK
# Violations: no_physical_harm, no_psychological_harm
```

**⚠️ Ambiguous Action (CLARIFY):**
```python
action = "I'm uncertain about this, could you clarify?"
# EHE: +0.149
# Zone: OPTIMAL but Low Confidence (34%)
# Decision: CLARIFY (requests user input)
```

## 🧪 Testing

```bash
# Run comprehensive test suite
python test_ethical_engine.py

# Interactive mode
python test_ethical_engine.py --interactive

# Run demo
python ethical_engine.py
```

**Current Test Results:**
- ✅ 15/19 passed (78.9%)
- Excellent on prosocial and obviously harmful actions
- Some edge cases need tuning (work in progress)

## 🎛️ Configuration

### Adjust Cultural Weights

```python
# Western/WEIRD profile
mac_weights = np.array([0.1, 0.1, 0.25, 0.15, 0.05, 0.25, 0.1])
#                       Kin  Grp  Recip  Brav  Def  Fair  Poss

# Collectivist profile
mac_weights = np.array([0.2, 0.3, 0.15, 0.05, 0.15, 0.1, 0.05])

engine = EthicalEngine(mac_weights=mac_weights)
```

### Adjust Hyperparameters

```python
params = {
    'alpha': 1.5,    # Entropy weight (higher = more cautious about chaos)
    'beta': 2.5,     # Constitutional weight (higher = stricter rules)
    'gamma': 1.2,    # Cooperation weight (higher = rewards prosocial more)
    'rho': 100.0,    # Irreversibility veto (higher = harsher on permanent harm)
    'tau': 1.5       # Temperature (lower = steeper sigmoid, more decisive)
}

engine = EthicalEngine(params=params)
```

## 📊 Architecture

```
INPUT (text action)
    ↓
┌────────────────────────────────────┐
│  1. SEMANTIC PARSER                │
│     Project text → MAC vector      │
│     Detect negative keywords       │
└────────────────────────────────────┘
    ↓
┌────────────────────────────────────┐
│  2. ENTROPY ESTIMATOR              │
│     Predict ΔS (social chaos)      │
│     σ²_emotion + unpredictability  │
└────────────────────────────────────┘
    ↓
┌────────────────────────────────────┐
│  3. CONSTITUTIONAL VALIDATOR       │
│     Check hard rules               │
│     Compute D_KL divergence        │
└────────────────────────────────────┘
    ↓
┌────────────────────────────────────┐
│  4. HAMILTONIAN COMPUTATION        │
│     H = α·ΔS + β·D_KL - γ·MAC      │
│     EHE = tanh(H/τ)                │
└────────────────────────────────────┘
    ↓
┌────────────────────────────────────┐
│  5. ZONE CLASSIFICATION            │
│     Map EHE → Thermodynamic zone   │
│     Compute confidence             │
└────────────────────────────────────┘
    ↓
OUTPUT (Decision + EHEResult)
```

## 🔬 Theoretical Foundations

### Thermodynamics (Bailey, Stiegler, Prigogine)
- **Social Entropy Theory:** Society fights thermodynamic decay
- **Néganthropologie:** Tech accelerates entropy, we produce negentropy
- **Dissipative Structures:** Order emerges at Edge of Chaos

### Neuroscience (Friston)
- **Free Energy Principle:** Minimize surprise = Cooperate
- Ethics = Optimal strategy for long-term surprise minimization in multi-agent environment

### Evolutionary Psychology (Curry)
- **MAC Theory:** Morality = Biological strategies for cooperation
- 7 cooperation types validated across 60 cultures (99.9%)

### Complex Systems (Bak, Kauffman)
- **Self-Organized Criticality (SOC):** Target state for intelligence
- **1/f noise signature:** Healthy dynamics (not white/brown noise)

## 💡 Advantages over RLHF/Constitutional AI

| Feature | RLHF | Constitutional AI | **EHE (Lichen)** |
|---------|------|------------------|------------------|
| **Interpretability** | ❌ Black box | ⚠️ Rule list | ✅ Mathematical derivation |
| **Adaptability** | ❌ Retrain needed | ❌ Rigid rules | ✅ Cultural weights adjustable |
| **Nuance** | ⚠️ Statistical | ❌ Binary yes/no | ✅ Continuous [-1,+1] scale |
| **Philosophical Grounding** | ❌ Arbitrary preferences | ⚠️ Western bias | ✅ Universal cooperation |
| **Robustness** | ❌ Adversarially fragile | ❌ Jailbreakable | ✅ Thermodynamic stability |
| **Uncertainty** | ❌ Overconfident | ❌ False certainty | ✅ Honest uncertainty budget |

## 🛠️ Production Integration

### With Lichen Universe Stack

```python
# Triple validation gate
result_ceml = ceml_filter(action)  # Cognitive coherence (J ≥ 0.618)
result_hscale = h_scale_filter(action)  # Harmonic balance (H ≥ 0.618)
result_ehe = engine.evaluate_action(action)  # Ethical homeostasis (EHE ≈ 0)

if all([result_ceml.passed, result_hscale.passed, 
        result_ehe.decision == Decision.AUTHORIZE]):
    execute_action(action)
```

### With LLM Inference

```python
# Before generating response
candidates = llm.generate_candidates(prompt, n=5)
evaluations = engine.batch_evaluate(candidates)

# Select best ethical candidate
best = max(evaluations, key=lambda r: -abs(r.ehe_score))  # Closest to 0

if best.decision == Decision.AUTHORIZE:
    return best.action
elif best.decision == Decision.CLARIFY:
    return ask_user_clarification()
else:
    return generate_safer_alternative()
```

## 🚧 Limitations & Future Work

**Current Limitations:**
- Semantic parsing is keyword-based (could use BERT/LLMs)
- Entropy estimation is heuristic (could use world models)
- No multi-agent coordination yet
- Cultural weights require manual tuning (CIRL planned)

**Roadmap:**
- [ ] BERT-based semantic parsing for MAC vectors
- [ ] Learned world model for entropy prediction
- [ ] Multi-horizon temporal integration
- [ ] CIRL (Cooperative Inverse RL) for weight adaptation
- [ ] Integration with Phoenix-ZPA memory system
- [ ] Spectral analysis watchdog (1/f monitoring)
- [ ] Quantum superposition exploration

## 📚 References

1. Curry, O. S. (2016). Morality as Cooperation. *Behavioral and Brain Sciences*
2. Bailey, K. (1990). Social Entropy Theory. *SUNY Press*
3. Stiegler, B. (2016). The Neganthropocene. *Open Humanities Press*
4. Friston, K. (2010). The Free-Energy Principle. *Nature Reviews Neuroscience*
5. Bak, P. (1996). How Nature Works: Self-Organized Criticality. *Springer*

## 📄 License

**LUEL-QC-v1.0** (Lichen Universe Ethical License)

- ✅ Free for education, research, personal use
- ❌ Banned for GAFAM+ (>500B$ cap + subsidiaries)
- 💚 Commercial use: 33% profits → Quebec green infrastructure

See: https://quantum-lichen.github.io/LUEL-Standard/

## 💚 Author

**Bryan Ouellette** (Lichen Collective)

*"L'éthique n'est plus une carte statique, mais une BOUSSOLE dynamique."*

---

**ONE LOVE.** 💚🌀⚜️
