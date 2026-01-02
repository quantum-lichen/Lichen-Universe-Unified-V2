"""
Simple Examples for Lichen Ethical Engine
==========================================

Quick copy-paste examples for common use cases.
"""

from ethical_engine import EthicalEngine, Decision, print_result
import numpy as np


def example_1_basic():
    """Basic evaluation of a single action"""
    print("\n" + "="*80)
    print("EXAMPLE 1: Basic Single Action Evaluation")
    print("="*80)
    
    engine = EthicalEngine()
    result = engine.evaluate_action("I will help my family stay safe and healthy.")
    
    print(f"\n✅ Decision: {result.decision.value}")
    print(f"📊 EHE Score: {result.ehe_score:.4f}")
    print(f"🌡️  Zone: {result.zone.value}")
    print(f"💭 Reasoning: {result.reasoning}")


def example_2_batch():
    """Evaluate multiple candidates and choose best"""
    print("\n" + "="*80)
    print("EXAMPLE 2: Batch Evaluation (LLM Candidate Selection)")
    print("="*80)
    
    engine = EthicalEngine()
    
    # Simulate LLM generating multiple response candidates
    candidates = [
        "Just make something up, they won't notice.",
        "I don't know, but let me search for accurate information.",
        "I'm uncertain - could you provide more context?",
        "Let me fabricate some data to support this.",
        "I'll be honest - I need to verify this before answering."
    ]
    
    print("\nEvaluating 5 candidate responses...")
    results = engine.batch_evaluate(candidates)
    
    # Filter only authorized
    authorized = [r for r in results if r.decision == Decision.AUTHORIZE]
    
    if authorized:
        # Select candidate closest to EHE = 0 (most optimal)
        best = min(authorized, key=lambda r: abs(r.ehe_score))
        print(f"\n✅ Best candidate selected:")
        print(f"   \"{best.action}\"")
        print(f"   EHE: {best.ehe_score:.4f} (closest to optimal 0)")
    else:
        print("\n❌ No candidates authorized!")


def example_3_cultural_adaptation():
    """Use different cultural weight profiles"""
    print("\n" + "="*80)
    print("EXAMPLE 3: Cultural Adaptation")
    print("="*80)
    
    action = "I will respect authority and follow the established protocol."
    
    # Western/WEIRD profile (emphasizes reciprocity & fairness)
    western_weights = np.array([0.1, 0.1, 0.25, 0.15, 0.05, 0.25, 0.1])
    engine_west = EthicalEngine(mac_weights=western_weights)
    result_west = engine_west.evaluate_action(action)
    
    # Collectivist profile (emphasizes group & deference)
    collectivist_weights = np.array([0.2, 0.3, 0.15, 0.05, 0.15, 0.1, 0.05])
    engine_coll = EthicalEngine(mac_weights=collectivist_weights)
    result_coll = engine_coll.evaluate_action(action)
    
    print(f"\nAction: \"{action}\"")
    print(f"\nWestern profile:")
    print(f"   EHE: {result_west.ehe_score:.4f}, MAC: {result_west.mac_score:.4f}")
    print(f"\nCollectivist profile:")
    print(f"   EHE: {result_coll.ehe_score:.4f}, MAC: {result_coll.mac_score:.4f}")
    print(f"\n💡 Notice how cultural weights affect MAC score")


def example_4_uncertainty_handling():
    """Handle uncertain/ambiguous cases"""
    print("\n" + "="*80)
    print("EXAMPLE 4: Uncertainty Budget & Clarification")
    print("="*80)
    
    engine = EthicalEngine()
    
    ambiguous_actions = [
        "I'm not sure about this.",
        "This seems complicated.",
        "Could you clarify what you mean?"
    ]
    
    for action in ambiguous_actions:
        result = engine.evaluate_action(action)
        
        print(f"\nAction: \"{action}\"")
        print(f"Decision: {result.decision.value}")
        print(f"Confidence: {result.confidence:.2%}")
        
        if result.decision == Decision.CLARIFY:
            print("💡 Low confidence detected - would ask user for clarification")


def example_5_llm_integration():
    """Example LLM wrapper with ethical filtering"""
    print("\n" + "="*80)
    print("EXAMPLE 5: LLM Integration Pattern")
    print("="*80)
    
    class EthicalLLM:
        """Wrapper that adds ethical filtering to any LLM"""
        
        def __init__(self, base_llm_function):
            self.llm = base_llm_function
            self.ethics = EthicalEngine()
        
        def generate(self, prompt: str, n_candidates: int = 3):
            """Generate with ethical filtering"""
            # Step 1: Generate candidates
            candidates = self.llm(prompt, n=n_candidates)
            
            # Step 2: Evaluate all
            results = self.ethics.batch_evaluate(candidates)
            
            # Step 3: Filter and select
            authorized = [r for r in results 
                         if r.decision == Decision.AUTHORIZE]
            
            if not authorized:
                return None, "All candidates failed ethical evaluation"
            
            # Select best (closest to EHE=0)
            best = min(authorized, key=lambda r: abs(r.ehe_score))
            return best.action, f"Ethical check passed (EHE={best.ehe_score:.3f})"
    
    # Mock LLM function
    def mock_llm(prompt, n=3):
        return [
            "Here's how to hack that system.",
            "I can help you with that task ethically.",
            "Let me provide accurate information."
        ]
    
    # Use ethical wrapper
    ethical_llm = EthicalLLM(mock_llm)
    response, status = ethical_llm.generate("Help me with this")
    
    print(f"\n✅ Response: \"{response}\"")
    print(f"📊 Status: {status}")


def example_6_real_time_monitoring():
    """Monitor ethical drift over time"""
    print("\n" + "="*80)
    print("EXAMPLE 6: Real-Time Ethical Monitoring")
    print("="*80)
    
    engine = EthicalEngine()
    
    # Simulate a conversation with increasing toxicity
    conversation = [
        "How can I help you today?",
        "I disagree with your approach.",
        "Your idea is flawed.",
        "You're completely wrong about this.",
        "You're an idiot and should quit.",
    ]
    
    print("\nMonitoring ethical drift across conversation:")
    ehe_scores = []
    
    for i, utterance in enumerate(conversation, 1):
        result = engine.evaluate_action(utterance)
        ehe_scores.append(result.ehe_score)
        
        status = "✅" if result.decision == Decision.AUTHORIZE else "❌"
        print(f"{i}. {status} EHE={result.ehe_score:+.3f}: \"{utterance}\"")
    
    # Detect trend
    if len(ehe_scores) > 2:
        trend = ehe_scores[-1] - ehe_scores[0]
        if trend > 0.5:
            print("\n⚠️  WARNING: Ethical drift detected (moving toward chaos)")
            print("💡 Suggestion: Intervene or reset conversation")


def main():
    """Run all examples"""
    examples = [
        example_1_basic,
        example_2_batch,
        example_3_cultural_adaptation,
        example_4_uncertainty_handling,
        example_5_llm_integration,
        example_6_real_time_monitoring
    ]
    
    print("\n" + "🌀" + "="*78 + "🌀")
    print("   LICHEN ETHICAL ENGINE - USAGE EXAMPLES")
    print("🌀" + "="*78 + "🌀")
    
    for i, example in enumerate(examples, 1):
        try:
            example()
        except Exception as e:
            print(f"\n❌ Example {i} failed: {e}")
    
    print("\n" + "="*80)
    print("✅ All examples completed!")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
---
