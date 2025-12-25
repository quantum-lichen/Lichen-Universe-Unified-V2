"""
Kuramoto synchronization model for ΦLang execution
"""

import numpy as np
from typing import List, Dict, Optional, Tuple


class KuramotoEngine:
    """
    Kuramoto oscillator network for synchronizing ΦLang execution
    """
    
    def __init__(
        self,
        n_agents: int,
        coupling: float = 0.5,
        dt: float = 0.01,
        threshold: float = 0.01
    ):
        """
        Initialize Kuramoto engine
        
        Args:
            n_agents: Number of agents/oscillators
            coupling: Coupling strength K
            dt: Time step for integration
            threshold: Synchronization threshold
        """
        self.n_agents = n_agents
        self.coupling = coupling
        self.dt = dt
        self.threshold = threshold
        
        # Initialize phases randomly
        self.phases = np.random.uniform(0, 2 * np.pi, n_agents)
        
        # Natural frequencies (slightly different for each agent)
        self.frequencies = np.random.normal(1.0, 0.1, n_agents)
        
        # History
        self.phase_history = [self.phases.copy()]
        self.order_history = [self.order_parameter()]
    
    def order_parameter(self) -> float:
        """
        Calculate Kuramoto order parameter r(t)
        
        r = |1/N Σ e^(iθ_j)|
        
        Returns:
            Order parameter in [0, 1]
            0 = desynchronized
            1 = fully synchronized
        """
        complex_sum = np.mean(np.exp(1j * self.phases))
        return np.abs(complex_sum)
    
    def phase_differences(self) -> np.ndarray:
        """
        Calculate all pairwise phase differences
        
        Returns:
            Matrix of phase differences
        """
        diff_matrix = np.zeros((self.n_agents, self.n_agents))
        for i in range(self.n_agents):
            for j in range(self.n_agents):
                diff_matrix[i, j] = self.phases[j] - self.phases[i]
        return diff_matrix
    
    def update(self) -> float:
        """
        Perform one Kuramoto update step
        
        dθ_i/dt = ω_i + (K/N) Σ sin(θ_j - θ_i)
        
        Returns:
            Current order parameter
        """
        new_phases = np.zeros(self.n_agents)
        
        for i in range(self.n_agents):
            # Natural frequency term
            drift = self.frequencies[i]
            
            # Coupling term
            coupling_sum = 0.0
            for j in range(self.n_agents):
                if i != j:
                    coupling_sum += np.sin(self.phases[j] - self.phases[i])
            
            coupling_term = (self.coupling / self.n_agents) * coupling_sum
            
            # Update phase
            new_phases[i] = self.phases[i] + self.dt * (drift + coupling_term)
        
        # Normalize phases to [0, 2π)
        self.phases = new_phases % (2 * np.pi)
        
        # Record history
        self.phase_history.append(self.phases.copy())
        order = self.order_parameter()
        self.order_history.append(order)
        
        return order
    
    def synchronize(self, max_steps: int = 1000) -> Tuple[bool, int]:
        """
        Run synchronization until convergence or max steps
        
        Args:
            max_steps: Maximum number of steps
            
        Returns:
            (success, num_steps)
        """
        for step in range(max_steps):
            order = self.update()
            
            # Check if synchronized
            if order > (1.0 - self.threshold):
                return True, step + 1
        
        return False, max_steps
    
    def is_synchronized(self, i: int = None, j: int = None) -> bool:
        """
        Check if agents are synchronized
        
        Args:
            i: Agent index (None = check all)
            j: Second agent index (for pairwise check)
            
        Returns:
            True if synchronized
        """
        if i is None:
            # Check global synchronization
            return self.order_parameter() > (1.0 - self.threshold)
        elif j is None:
            # Check if agent i is synchronized with mean phase
            mean_phase = np.angle(np.mean(np.exp(1j * self.phases)))
            diff = np.abs(self.phases[i] - mean_phase)
            return min(diff, 2*np.pi - diff) < self.threshold
        else:
            # Check if agents i and j are synchronized
            diff = np.abs(self.phases[i] - self.phases[j])
            return min(diff, 2*np.pi - diff) < self.threshold
    
    def get_phase(self, agent_id: int) -> float:
        """
        Get current phase of an agent
        
        Args:
            agent_id: Agent index
            
        Returns:
            Phase in [0, 2π)
        """
        return self.phases[agent_id]
    
    def set_phase(self, agent_id: int, phase: float):
        """
        Set phase of an agent
        
        Args:
            agent_id: Agent index
            phase: New phase
        """
        self.phases[agent_id] = phase % (2 * np.pi)
    
    def reset(self):
        """
        Reset all phases to random values
        """
        self.phases = np.random.uniform(0, 2 * np.pi, self.n_agents)
        self.phase_history = [self.phases.copy()]
        self.order_history = [self.order_parameter()]
    
    def critical_coupling(self) -> float:
        """
        Estimate critical coupling K_c
        
        For Lorentzian distribution: K_c ≈ 2γ
        For uniform: K_c ≈ πγ
        
        Returns:
            Estimated K_c
        """
        gamma = np.std(self.frequencies)
        return 2 * gamma  # Lorentzian approximation
    
    def get_stats(self) -> Dict[str, float]:
        """
        Get synchronization statistics
        
        Returns:
            Dictionary of stats
        """
        order = self.order_parameter()
        mean_phase = np.angle(np.mean(np.exp(1j * self.phases)))
        phase_std = np.std(self.phases)
        
        return {
            'order_parameter': order,
            'mean_phase': mean_phase,
            'phase_std': phase_std,
            'coupling': self.coupling,
            'critical_coupling': self.critical_coupling(),
            'synchronized': order > (1.0 - self.threshold)
        }


class ΦLangSynchronizer:
    """
    High-level synchronizer for ΦLang instruction execution
    """
    
    def __init__(self, agents: List[str]):
        """
        Initialize synchronizer for ΦLang agents
        
        Args:
            agents: List of agent IDs
        """
        self.agents = agents
        self.engine = KuramotoEngine(len(agents))
        self.agent_map = {agent: i for i, agent in enumerate(agents)}
    
    def can_execute(self, agent_a: str, agent_b: str) -> bool:
        """
        Check if two agents are synchronized enough to communicate
        
        Args:
            agent_a: First agent ID
            agent_b: Second agent ID
            
        Returns:
            True if agents can communicate
        """
        i = self.agent_map[agent_a]
        j = self.agent_map[agent_b]
        return self.engine.is_synchronized(i, j)
    
    def wait_for_sync(
        self,
        agent_a: str,
        agent_b: str,
        timeout: int = 1000
    ) -> bool:
        """
        Wait for two agents to synchronize
        
        Args:
            agent_a: First agent ID
            agent_b: Second agent ID
            timeout: Max steps to wait
            
        Returns:
            True if synchronized within timeout
        """
        i = self.agent_map[agent_a]
        j = self.agent_map[agent_b]
        
        for _ in range(timeout):
            if self.engine.is_synchronized(i, j):
                return True
            self.engine.update()
        
        return False
    
    def broadcast_sync(self, timeout: int = 1000) -> bool:
        """
        Synchronize all agents for broadcast
        
        Args:
            timeout: Max steps to wait
            
        Returns:
            True if all synchronized
        """
        success, steps = self.engine.synchronize(timeout)
        return success
    
    def get_agent_phase(self, agent: str) -> float:
        """
        Get current phase of an agent
        
        Args:
            agent: Agent ID
            
        Returns:
            Phase in [0, 2π)
        """
        i = self.agent_map[agent]
        return self.engine.get_phase(i)
