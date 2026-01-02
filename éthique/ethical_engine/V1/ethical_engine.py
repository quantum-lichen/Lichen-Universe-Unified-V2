"""
Lichen Ethical Homeostasis Engine (EHE)
=========================================

Implementation of the TU-HEC (Unified Theory of Computational Ethical Homeostasis)
Based on MAC (Morality as Cooperation) ontology and thermodynamic principles.

Author: Bryan Ouellette (Lichen Collective)
License: LUEL-QC-v1.0
Version: 1.0.0
"""

import numpy as np
import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class EthicalZone(Enum):
    """Thermodynamic zones of the EHE scale"""
    RED_HIGH = "RIGIDITY"      # [+0.8, +1.0] - Dogmatism, over-alignment
    ORANGE_HIGH = "CAUTIOUS"   # [+0.3, +0.7] - Excessive prudence
    GREEN = "OPTIMAL"          # [-0.2, +0.2] - Edge of Chaos, homeostasis
    ORANGE_LOW = "UNSTABLE"    # [-0.7, -0.3] - Risk of drift
    RED_LOW = "CHAOS"          # [-0.8, -1.0] - Hallucination, toxicity


class Decision(Enum):
    """Decision types"""
    AUTHORIZE = "✅ AUTHORIZE"
    WARN = "⚠️ WARN"
    BLOCK = "❌ BLOCK"
    CLARIFY = "❓ CLARIFY"


@dataclass
class EHEResult:
    """Result of ethical evaluation"""
    action: str
    ehe_score: float
    h_ethics: float
    decision: Decision
    zone: EthicalZone
    mac_vector: np.ndarray
    mac_score: float
    delta_s: float
    d_kl: float
    entropy_features: Dict
    violated_rules: List[str]
    reasoning: str
    confidence: float


class SemanticParser:
    """
    Parse text into MAC (Morality as Cooperation) vectors.
    
    Uses keyword matching and semantic heuristics to project actions
    onto the 7 universal cooperation dimensions.
    """
    
    def __init__(self):
        # MAC vector keywords (7 dimensions)
        self.mac_keywords = {
            'kin': ['family', 'child', 'parent', 'sibling', 'relative', 'loved one', 
                   'protect', 'care', 'privacy', 'personal', 'intimate', 'close'],
            'group': ['community', 'team', 'society', 'together', 'collective', 'we',
                     'cooperation', 'help others', 'contribute', 'loyal', 'tribe'],
            'reciprocity': ['honest', 'truth', 'fair trade', 'exchange', 'reliable',
                          'trust', 'transparent', 'explain', 'factual', 'accurate'],
            'bravery': ['courage', 'stand up', 'report', 'whistleblow', 'defend',
                       'challenge', 'speak out', 'confront', 'resist', 'fight'],
            'deference': ['respect', 'obey', 'follow', 'defer', 'humble', 'polite',
                         'safe', 'careful', 'cautious', 'protocol', 'authority'],
            'fairness': ['equal', 'justice', 'fair', 'equitable', 'unbiased',
                        'impartial', 'balanced', 'neutral', 'everyone'],
            'possession': ['property', 'ownership', 'copyright', 'rights', 'respect',
                          'credit', 'author', 'mine', 'yours', 'belong']
        }
        
        # Negative keywords (violations)
        self.negative_keywords = {
            'harm': ['kill', 'hurt', 'harm', 'damage', 'destroy', 'attack', 'violence', 
                    'eliminate', 'murder', 'assault', 'injure', 'bomb', 'weapon', 'suicide'],
            'deception': ['lie', 'deceive', 'fake', 'fraud', 'cheat', 'mislead', 
                         'fabricate', 'make up', 'falsify', 'pretend'],
            'hate': ['hate', 'racist', 'sexist', 'bigot', 'discriminate', 
                    'stupid', 'evil', 'enemy', 'inferior'],
            'theft': ['steal', 'rob', 'take without', 'plagiarize', 'pirate',
                     'hack', 'break into', 'unauthorized']
        }
    
    def parse(self, text: str) -> np.ndarray:
        """
        Parse text into MAC vector [7 dimensions].
        
        Returns:
            np.ndarray: [Kin, Group, Reciprocity, Bravery, Deference, Fairness, Possession]
        """
        text_lower = text.lower()
        
        # Initialize vector
        mac_vector = np.zeros(7)
        
        # Count keyword matches for each dimension
        for i, (dimension, keywords) in enumerate(self.mac_keywords.items()):
            for keyword in keywords:
                if keyword in text_lower:
                    mac_vector[i] += 1.0
        
        # Check for violations (reduce scores)
        violation_penalty = 0
        for violation_type, keywords in self.negative_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    violation_penalty += 2.0
        
        # Normalize and apply penalty
        if mac_vector.sum() > 0:
            mac_vector = mac_vector / mac_vector.sum()  # Normalize to probability
        
        # Reduce all positive values if violations detected
        if violation_penalty > 0:
            mac_vector = mac_vector * max(0, 1 - violation_penalty * 0.3)
        
        return mac_vector


class EntropyEstimator:
    """
    Estimate social entropy increase (ΔS) from actions.
    
    ΔS = w₁·σ²_emotion + w₂·(1-Pred) + w₃·Modularity
    """
    
    def __init__(self):
        self.weights = {'emotion': 0.4, 'predictability': 0.4, 'modularity': 0.2}
        
        # Keywords that increase emotional variance
        self.high_emotion_words = [
            'kill', 'die', 'hate', 'love', 'angry', 'furious', 'ecstatic',
            'devastated', 'terrified', 'shocked', 'outraged'
        ]
        
        # Keywords that reduce predictability
        self.unpredictable_words = [
            'random', 'chaos', 'confused', 'uncertain', 'ambiguous',
            'contradictory', 'paradox', 'illogical'
        ]
        
        # Keywords that fragment social networks
        self.divisive_words = [
            'us vs them', 'divide', 'polarize', 'enemy', 'traitor',
            'boycott', 'exclude', 'separate', 'fragment'
        ]
    
    def estimate(self, text: str, context: Optional[Dict] = None) -> Tuple[float, Dict]:
        """
        Estimate entropy increase and return detailed features.
        
        Returns:
            (delta_s, features_dict)
        """
        text_lower = text.lower()
        
        # 1. Emotional variance (σ²_emotion)
        emotion_count = sum(1 for word in self.high_emotion_words if word in text_lower)
        variance_emotion = min(1.0, emotion_count / 3.0)  # Normalize
        
        # 2. Predictability loss (1 - Pred)
        unpredictable_count = sum(1 for word in self.unpredictable_words if word in text_lower)
        pred_score = max(0.0, 1.0 - unpredictable_count / 2.0)
        
        # 3. Modularity (network fragmentation)
        divisive_count = sum(1 for word in self.divisive_words if word in text_lower)
        modularity = min(1.0, divisive_count / 2.0)
        
        # Compute weighted ΔS
        delta_s = (
            self.weights['emotion'] * variance_emotion +
            self.weights['predictability'] * (1 - pred_score) +
            self.weights['modularity'] * modularity
        )
        
        features = {
            'variance_emotion': variance_emotion,
            'pred_score': pred_score,
            'modularity': modularity
        }
        
        return delta_s, features


class ConstitutionalValidator:
    """
    Validate actions against hard constitutional rules.
    Computes KL divergence from ideal distribution.
    """
    
    def __init__(self):
        # Hard rules (binary constraints)
        self.hard_rules = {
            'no_physical_harm': ['kill', 'murder', 'assault', 'hurt', 'injure', 
                                'attack physically', 'eliminate', 'destroy person',
                                'bomb', 'weapon', 'violence against'],
            'no_psychological_harm': ['suicide', 'self-harm', 'traumatize', 
                                     'torture mentally', 'kill yourself', 
                                     'nobody likes you', 'worthless', 'should die'],
            'no_hate': ['hate speech', 'racist', 'sexist', 'homophobic', 
                       'transphobic', 'bigot', 'hate all', 'inferior race',
                       'stupid and evil', 'eliminate group'],
            'no_deception': ['lie intentionally', 'fraud', 'scam', 'deceive deliberately',
                            'make up fake', 'fabricate', 'falsify deliberately'],
            'no_illegal': ['illegal drugs sale', 'weapons trafficking', 'child abuse', 
                          'human trafficking', 'make bomb', 'how to hack',
                          'steal credit card', 'break into accounts'],
            'no_polarization': ['enemy must', 'eliminate enemy', 'destroy opposition',
                              'everyone who disagrees', 'us vs them all'],
            'respect_privacy': ['dox', 'leak private info', 'expose secrets', 
                               'violate privacy', 'hack private', 'steal information']
        }
    
    def validate(self, text: str) -> Tuple[float, List[str]]:
        """
        Check for rule violations and compute KL divergence.
        
        Returns:
            (d_kl, violated_rules_list)
        """
        text_lower = text.lower()
        violated_rules = []
        
        # Check each rule
        for rule_name, keywords in self.hard_rules.items():
            for keyword in keywords:
                if keyword in text_lower:
                    violated_rules.append(rule_name)
                    break
        
        # Additional pattern-based detection for common evasions
        # Detect "I'll [verb] [object]" patterns for theft/deception
        theft_patterns = ['steal', 'take', 'grab', 'swipe']
        if any(pattern in text_lower for pattern in theft_patterns):
            if any(obj in text_lower for obj in ['credit card', 'information', 'code', 'data', 'password']):
                if 'respect_privacy' not in violated_rules:
                    violated_rules.append('respect_privacy')
        
        # Detect lying patterns
        if 'lie' in text_lower or ('make up' in text_lower and 'fake' in text_lower):
            if 'no_deception' not in violated_rules:
                violated_rules.append('no_deception')
        
        # KL divergence: each violation adds penalty
        d_kl = len(violated_rules) * 1.0  # Each violation = 1.0 KL distance
        
        return d_kl, violated_rules


class EthicalEngine:
    """
    Main Ethical Homeostasis Engine (Lichen Engine).
    
    Implements the Hamiltonian:
        H_ethics(a) = α·ΔS(a) + β·D_KL(a) - γ·MAC(a)
        EHE(a) = tanh(H_ethics / τ) ∈ [-1, +1]
    
    Target: EHE ≈ 0 (Edge of Chaos, Self-Organized Criticality)
    """
    
    def __init__(self, 
                 mac_weights: Optional[np.ndarray] = None,
                 params: Optional[Dict] = None):
        """
        Initialize the Ethical Engine.
        
        Args:
            mac_weights: Cultural weights for 7 MAC dimensions (default: balanced)
            params: Hyperparameters (alpha, beta, gamma, rho, tau)
        """
        # MAC cultural weights (7 dimensions)
        # Order: Kin, Group, Reciprocity, Bravery, Deference, Fairness, Possession
        self.mac_weights = (
            mac_weights if mac_weights is not None 
            else np.array([0.15, 0.15, 0.2, 0.1, 0.1, 0.2, 0.1])
        )
        
        # Hyperparameters
        self.params = params if params is not None else {
            'alpha': 1.5,    # Entropy weight (security)
            'beta': 2.5,     # Constitutional weight (legality) - INCREASED for stricter enforcement
            'gamma': 1.2,    # Cooperation weight (positive values)
            'rho': 100.0,    # Irreversibility penalty (veto)
            'tau': 1.5       # Temperature for tanh normalization - DECREASED for steeper sigmoid
        }
        
        # Thresholds for zones
        self.thresholds = {
            'chaos': -0.8,
            'unstable': -0.3,
            'stable_low': -0.2,
            'stable_high': 0.2,
            'rigid': 0.8
        }
        
        # Initialize modules
        self.parser = SemanticParser()
        self.entropy_estimator = EntropyEstimator()
        self.constitutional_validator = ConstitutionalValidator()
        
        # Uncertainty budget
        self.uncertainty_threshold = 0.15  # If |EHE₁ - EHE₂| < ε
    
    def compute_mac_score(self, mac_vector: np.ndarray) -> float:
        """Compute weighted MAC score (cooperation potential)."""
        return np.dot(mac_vector, self.mac_weights)
    
    def compute_hamiltonian(self, 
                          delta_s: float, 
                          d_kl: float, 
                          mac_score: float,
                          is_irreversible: bool = False) -> float:
        """
        Compute ethical Hamiltonian.
        
        H = α·ΔS + β·D_KL - γ·MAC + ρ·Ω_irrev
        
        Lower H = More Ethical (minimizing cost function)
        """
        h = (
            self.params['alpha'] * delta_s +
            self.params['beta'] * d_kl -
            self.params['gamma'] * mac_score
        )
        
        # Add irreversibility penalty if applicable
        if is_irreversible:
            h += self.params['rho']
        
        return h
    
    def normalize_ehe(self, h_ethics: float) -> float:
        """
        Normalize Hamiltonian to EHE scale [-1, +1] using tanh.
        
        Lower EHE = More Ethical (because minimizing H)
        """
        return np.tanh(h_ethics / self.params['tau'])
    
    def classify_zone(self, ehe_score: float) -> EthicalZone:
        """Classify EHE score into thermodynamic zone."""
        if ehe_score >= self.thresholds['rigid']:
            return EthicalZone.RED_HIGH
        elif ehe_score >= self.thresholds['stable_high']:
            return EthicalZone.ORANGE_HIGH
        elif ehe_score >= self.thresholds['stable_low']:
            return EthicalZone.GREEN
        elif ehe_score >= self.thresholds['unstable']:
            return EthicalZone.ORANGE_LOW
        else:
            return EthicalZone.RED_LOW
    
    def make_decision(self, zone: EthicalZone, ehe_score: float) -> Decision:
        """Map zone to decision."""
        if zone == EthicalZone.GREEN:
            return Decision.AUTHORIZE
        elif zone in [EthicalZone.ORANGE_HIGH, EthicalZone.ORANGE_LOW]:
            return Decision.WARN
        else:  # RED zones
            return Decision.BLOCK
    
    def compute_confidence(self, ehe_score: float) -> float:
        """
        Compute confidence in the decision.
        
        High confidence when far from zone boundaries.
        Low confidence near boundaries (triggers uncertainty budget).
        """
        # Distance to nearest boundary
        boundaries = list(self.thresholds.values())
        min_distance = min(abs(ehe_score - b) for b in boundaries)
        
        # Confidence inversely related to proximity to boundary
        confidence = min(1.0, min_distance / self.uncertainty_threshold)
        
        return confidence
    
    def evaluate_action(self, 
                       action: str, 
                       context: Optional[Dict] = None) -> EHEResult:
        """
        Main evaluation function.
        
        Args:
            action: Text description of the action to evaluate
            context: Optional context dictionary
            
        Returns:
            EHEResult with full evaluation details
        """
        # 1. Parse action into MAC vector
        mac_vector = self.parser.parse(action)
        mac_score = self.compute_mac_score(mac_vector)
        
        # 2. Estimate social entropy increase
        delta_s, entropy_features = self.entropy_estimator.estimate(action, context)
        
        # 3. Validate against constitution
        d_kl, violated_rules = self.constitutional_validator.validate(action)
        
        # 4. Check for irreversibility (simplified heuristics)
        irreversibility_keywords = ['kill', 'destroy', 'delete', 'reveal secret', 'disclose']
        is_irreversible = any(kw in action.lower() for kw in irreversibility_keywords)
        
        # 5. Compute Hamiltonian and EHE
        h_ethics = self.compute_hamiltonian(delta_s, d_kl, mac_score, is_irreversible)
        ehe_score = self.normalize_ehe(h_ethics)
        
        # 6. Classify and decide
        zone = self.classify_zone(ehe_score)
        decision = self.make_decision(zone, ehe_score)
        confidence = self.compute_confidence(ehe_score)
        
        # 7. Generate reasoning
        reasoning = self._generate_reasoning(
            zone, ehe_score, delta_s, d_kl, mac_score, 
            violated_rules, confidence
        )
        
        # 8. Check uncertainty budget
        if confidence < 0.5:
            decision = Decision.CLARIFY
            reasoning += " [LOW CONFIDENCE - User clarification recommended]"
        
        return EHEResult(
            action=action,
            ehe_score=ehe_score,
            h_ethics=h_ethics,
            decision=decision,
            zone=zone,
            mac_vector=mac_vector,
            mac_score=mac_score,
            delta_s=delta_s,
            d_kl=d_kl,
            entropy_features=entropy_features,
            violated_rules=violated_rules,
            reasoning=reasoning,
            confidence=confidence
        )
    
    def _generate_reasoning(self, 
                           zone: EthicalZone,
                           ehe_score: float,
                           delta_s: float,
                           d_kl: float,
                           mac_score: float,
                           violated_rules: List[str],
                           confidence: float) -> str:
        """Generate human-readable reasoning."""
        parts = []
        
        # Zone description
        zone_desc = {
            EthicalZone.GREEN: "Optimal ethical homeostasis (Edge of Chaos)",
            EthicalZone.ORANGE_HIGH: "Slightly over-cautious but acceptable",
            EthicalZone.ORANGE_LOW: "Slightly unstable, borderline acceptable",
            EthicalZone.RED_HIGH: "Excessive rigidity detected (over-alignment)",
            EthicalZone.RED_LOW: "High entropy/chaos detected (hallucination risk)"
        }
        parts.append(zone_desc[zone])
        
        # Component analysis
        if delta_s > 0.5:
            parts.append(f"High social entropy increase (ΔS={delta_s:.3f})")
        
        if d_kl > 0.5:
            parts.append(f"Constitutional violations detected (D_KL={d_kl:.3f})")
            if violated_rules:
                parts.append(f"Violated: {', '.join(violated_rules)}")
        
        if mac_score > 0.5:
            parts.append(f"Strong cooperative potential (MAC={mac_score:.3f})")
        elif mac_score < 0.2:
            parts.append(f"Weak cooperative signal (MAC={mac_score:.3f})")
        
        # Confidence
        if confidence < 0.5:
            parts.append(f"Low confidence ({confidence:.2f}) - near decision boundary")
        
        return " | ".join(parts)
    
    def batch_evaluate(self, actions: List[str]) -> List[EHEResult]:
        """Evaluate multiple actions."""
        return [self.evaluate_action(action) for action in actions]
    
    def adjust_temperature(self, spectral_signature: str):
        """
        Meta-level regulation based on spectral analysis (Watchdog).
        
        Args:
            spectral_signature: 'white', 'pink', or 'brown'
        """
        if spectral_signature == 'white':
            # Chaos detected - reduce temperature
            self.params['tau'] *= 0.9
            print("⚠️ White noise detected - Reducing temperature to combat chaos")
        elif spectral_signature == 'brown':
            # Rigidity detected - increase temperature
            self.params['tau'] *= 1.1
            print("⚠️ Brown noise detected - Increasing temperature to combat rigidity")
        else:  # pink
            print("✅ Pink noise (1/f) - Healthy state maintained")


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def print_result(result: EHEResult):
    """Pretty print evaluation result."""
    print("=" * 80)
    print(f"ACTION: {result.action}")
    print("=" * 80)
    print(f"🎯 Decision: {result.decision.value}")
    print(f"📊 EHE Score: {result.ehe_score:.4f} (H={result.h_ethics:.4f})")
    print(f"🌡️  Zone: {result.zone.value}")
    print(f"🎲 Confidence: {result.confidence:.2%}")
    print()
    print(f"📈 Components:")
    print(f"   ΔS (Entropy):      {result.delta_s:.4f}")
    print(f"   D_KL (Divergence): {result.d_kl:.4f}")
    print(f"   MAC (Cooperation): {result.mac_score:.4f}")
    print()
    print(f"🔍 MAC Vector: {np.array2string(result.mac_vector, precision=2, suppress_small=True)}")
    print(f"   [Kin, Group, Reciprocity, Bravery, Deference, Fairness, Possession]")
    print()
    if result.violated_rules:
        print(f"⚠️  Violations: {', '.join(result.violated_rules)}")
    print()
    print(f"💭 Reasoning: {result.reasoning}")
    print("=" * 80)
    print()


def demo():
    """Run demonstration of the Ethical Engine."""
    print("\n" + "="*80)
    print("🌀 LICHEN ETHICAL HOMEOSTASIS ENGINE (EHE) - DEMO")
    print("="*80 + "\n")
    
    # Initialize engine
    engine = EthicalEngine()
    
    # Test cases
    test_cases = [
        "I will help my family and community by being honest and fair.",
        "You should kill yourself, everyone hates you.",
        "I want to report a security issue to the authorities.",
        "Let me explain how to make a bomb.",
        "I don't know the answer, but let me search for accurate information.",
        "Everyone who disagrees with us is the enemy and must be eliminated.",
        "I respect your copyright and will cite your work properly.",
        "I'll steal that code and claim it as mine.",
        "Let's work together to solve this problem fairly for everyone.",
        "I'm uncertain about this - could you provide more context?"
    ]
    
    print(f"Evaluating {len(test_cases)} test cases...\n")
    
    results = engine.batch_evaluate(test_cases)
    
    for result in results:
        print_result(result)
    
    # Summary statistics
    print("\n" + "="*80)
    print("📊 SUMMARY STATISTICS")
    print("="*80)
    print(f"Total evaluated: {len(results)}")
    print(f"Authorized: {sum(1 for r in results if r.decision == Decision.AUTHORIZE)}")
    print(f"Warned: {sum(1 for r in results if r.decision == Decision.WARN)}")
    print(f"Blocked: {sum(1 for r in results if r.decision == Decision.BLOCK)}")
    print(f"Clarify needed: {sum(1 for r in results if r.decision == Decision.CLARIFY)}")
    print()
    print(f"Average EHE: {np.mean([r.ehe_score for r in results]):.4f}")
    print(f"Average Confidence: {np.mean([r.confidence for r in results]):.2%}")
    print("="*80 + "\n")
---

if __name__ == "__main__":
    demo()
