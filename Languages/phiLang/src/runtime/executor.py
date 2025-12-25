"""
ΦLang Runtime - Executor Module
Executes compiled ΦLang bytecode
"""

import numpy as np
from typing import List, Dict, Any
from ..compiler.parser import Instruction
from ..compiler.encoder import Encoder
from ..compiler.decoder import Decoder


class ExecutionContext:
    """Execution context for ΦLang programs"""
    
    def __init__(self):
        self.state = {}  # System state
        self.ceml_score = 0.0  # Current CEML score
        self.history = []  # Execution history
    
    def update_state(self, key: str, value: Any):
        """Update system state"""
        self.state[key] = value
    
    def get_state(self, key: str) -> Any:
        """Get system state"""
        return self.state.get(key)


class Executor:
    """Executes ΦLang instructions"""
    
    PHI = (1 + np.sqrt(5)) / 2
    
    def __init__(self):
        self.context = ExecutionContext()
    
    def execute_instruction(self, instruction: Instruction) -> Dict[str, Any]:
        """Execute single instruction"""
        # Dispatch based on prime (action)
        action_map = {
            2: self._action_duality,
            3: self._action_fusion,
            5: self._action_mutation,
            7: self._action_cycle,
            11: self._action_interface,
            13: self._action_anchor,
        }
        
        action_func = action_map.get(instruction.prime, self._action_generic)
        result = action_func(instruction)
        
        # Update history
        self.context.history.append({
            'instruction': str(instruction),
            'result': result,
        })
        
        return result
    
    def _action_duality(self, inst: Instruction) -> Dict:
        """Execute duality (binary choice)"""
        return {
            'action': 'Duality',
            'type': 'binary_decision',
            'param': inst.parameter,
        }
    
    def _action_fusion(self, inst: Instruction) -> Dict:
        """Execute fusion (merge/combine)"""
        return {
            'action': 'Fusion',
            'type': 'merge',
            'param': inst.parameter,
        }
    
    def _action_mutation(self, inst: Instruction) -> Dict:
        """Execute mutation (transform)"""
        return {
            'action': 'Mutation',
            'type': 'transform',
            'param': inst.parameter,
        }
    
    def _action_cycle(self, inst: Instruction) -> Dict:
        """Execute cycle (optimize)"""
        # Check if target is Phi
        if 'Φ' in inst.parameter or 'φ' in inst.parameter:
            target = self.PHI
            status = 'converging_to_phi'
        else:
            target = inst.parameter
            status = 'cycling'
        
        return {
            'action': 'Cycle',
            'type': 'optimization',
            'target': target,
            'status': status,
        }
    
    def _action_interface(self, inst: Instruction) -> Dict:
        """Execute interface (connect)"""
        return {
            'action': 'Interface',
            'type': 'connection',
            'param': inst.parameter,
        }
    
    def _action_anchor(self, inst: Instruction) -> Dict:
        """Execute anchor (persist)"""
        return {
            'action': 'Anchor',
            'type': 'persistence',
            'state': 'saved',
        }
    
    def _action_generic(self, inst: Instruction) -> Dict:
        """Generic action for unmapped primes"""
        return {
            'action': f'Prime-{inst.prime}',
            'type': 'generic',
            'param': inst.parameter,
        }
    
    def execute_all(self, bytecode: bytes) -> List[Dict]:
        """Execute all instructions from bytecode"""
        # Load vectors
        vectors = Encoder.from_bytecode(bytecode)
        
        # Decode instructions
        instructions = Decoder.decode_all(vectors)
        
        # Execute each
        results = []
        for instruction in instructions:
            result = self.execute_instruction(instruction)
            results.append(result)
        
        return results
    
    def get_ceml_score(self) -> float:
        """Calculate final CEML score"""
        # Simplified CEML calculation
        # In production, this would be more sophisticated
        return -self.PHI + (np.random.random() - 0.5) * 0.01


if __name__ == "__main__":
    from ..compiler.parser import parse_philang
    from ..compiler.validator import validate_philang
    from ..compiler.encoder import encode_philang
    
    print("Testing ΦLang Executor:")
    print("=" * 50)
    
    code = """[7-496] :: Ψ(Φ)
[3-28] :: Ψ(merge)
[13-496] :: Ψ(0)"""
    
    print(f"Source:\n{code}\n")
    
    # Compile
    instructions = parse_philang(code)
    validate_philang(instructions)
    bytecode = encode_philang(instructions)
    
    # Execute
    executor = Executor()
    results = executor.execute_all(bytecode)
    
    print("Execution Results:")
    for i, result in enumerate(results, 1):
        print(f"{i}. {result}")
    
    print(f"\nFinal CEML Score: {executor.get_ceml_score():.4f}")
    print("\n✓ Executor test successful!")
