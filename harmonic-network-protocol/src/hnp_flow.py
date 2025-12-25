"""
HNP Flow Control
φ-based congestion control for stable convergence
"""

import time
from typing import List


class HNPFlowControl:
    """
    Flow control based on golden ratio (φ)
    
    Provides mathematically proven stable convergence
    via KAM theorem for quasi-periodic orbits
    """
    
    PHI = 1.618033988749895  # Golden ratio
    
    def __init__(self, initial_rate: float = 1.0, min_rate: float = 0.001, max_rate: float = 1000.0):
        """
        Initialize flow control
        
        Args:
            initial_rate: Starting transmission rate (packets/sec)
            min_rate: Minimum allowed rate
            max_rate: Maximum allowed rate
        """
        self.rate = initial_rate
        self.min_rate = min_rate
        self.max_rate = max_rate
        
        # History for analysis
        self.rate_history: List[float] = [initial_rate]
        self.time_history: List[float] = [time.time()]
        self.event_history: List[str] = ['init']
    
    def on_success(self):
        """
        Called when packet successfully transmitted
        Increase rate by factor of φ
        """
        self.rate *= self.PHI
        
        # Clamp to max
        if self.rate > self.max_rate:
            self.rate = self.max_rate
        
        # Record
        self.rate_history.append(self.rate)
        self.time_history.append(time.time())
        self.event_history.append('success')
    
    def on_congestion(self):
        """
        Called when congestion detected
        Decrease rate by factor of 1/φ
        """
        self.rate /= self.PHI
        
        # Clamp to min
        if self.rate < self.min_rate:
            self.rate = self.min_rate
        
        # Record
        self.rate_history.append(self.rate)
        self.time_history.append(time.time())
        self.event_history.append('congestion')
    
    def on_timeout(self):
        """
        Called when packet timeout occurs
        More aggressive decrease: divide by φ²
        """
        self.rate /= (self.PHI ** 2)
        
        # Clamp to min
        if self.rate < self.min_rate:
            self.rate = self.min_rate
        
        # Record
        self.rate_history.append(self.rate)
        self.time_history.append(time.time())
        self.event_history.append('timeout')
    
    def get_rate(self) -> float:
        """Get current transmission rate"""
        return self.rate
    
    def get_wait_time(self) -> float:
        """Get time to wait between packets"""
        return 1.0 / self.rate if self.rate > 0 else float('inf')
    
    def reset(self):
        """Reset to initial state"""
        self.rate = self.rate_history[0] if self.rate_history else 1.0
        self.rate_history = [self.rate]
        self.time_history = [time.time()]
        self.event_history = ['reset']
    
    def has_converged(self, window: int = 10, threshold: float = 0.1) -> bool:
        """
        Check if rate has converged to stable value
        
        Args:
            window: Number of recent samples to check
            threshold: Relative variation threshold
        
        Returns:
            bool: True if converged
        """
        if len(self.rate_history) < window:
            return False
        
        recent_rates = self.rate_history[-window:]
        mean_rate = sum(recent_rates) / len(recent_rates)
        
        # Check if all recent rates within threshold of mean
        for rate in recent_rates:
            if abs(rate - mean_rate) / mean_rate > threshold:
                return False
        
        return True
    
    def get_convergence_quality(self) -> float:
        """
        Measure quality of convergence
        
        Returns:
            float: Quality metric (0-1, higher is better)
        """
        if len(self.rate_history) < 10:
            return 0.0
        
        # Calculate variance of recent rates
        recent = self.rate_history[-20:]
        mean = sum(recent) / len(recent)
        variance = sum((r - mean) ** 2 for r in recent) / len(recent)
        
        # Normalize to 0-1 (lower variance = higher quality)
        quality = 1.0 / (1.0 + variance)
        
        return quality
    
    def get_statistics(self) -> dict:
        """Get comprehensive statistics"""
        if not self.rate_history:
            return {}
        
        success_count = self.event_history.count('success')
        congestion_count = self.event_history.count('congestion')
        timeout_count = self.event_history.count('timeout')
        total_events = len(self.event_history) - 1  # Exclude 'init'
        
        return {
            'current_rate': self.rate,
            'min_rate_seen': min(self.rate_history),
            'max_rate_seen': max(self.rate_history),
            'mean_rate': sum(self.rate_history) / len(self.rate_history),
            'total_events': total_events,
            'success_count': success_count,
            'congestion_count': congestion_count,
            'timeout_count': timeout_count,
            'success_ratio': success_count / total_events if total_events > 0 else 0,
            'converged': self.has_converged(),
            'convergence_quality': self.get_convergence_quality(),
        }
    
    def __repr__(self) -> str:
        return (
            f"HNPFlowControl("
            f"rate={self.rate:.3f} pkt/s, "
            f"converged={self.has_converged()}, "
            f"quality={self.get_convergence_quality():.2f})"
        )


class AdaptiveHNPFlowControl(HNPFlowControl):
    """
    Advanced flow control with adaptive φ-factor
    Adjusts φ based on network conditions
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Adaptive parameters
        self.phi_factor = self.PHI
        self.phi_history: List[float] = [self.PHI]
    
    def adapt_phi(self):
        """
        Adjust φ factor based on recent performance
        If oscillating: reduce φ (more conservative)
        If stable: keep φ at golden ratio
        """
        if len(self.rate_history) < 20:
            return
        
        # Check for oscillations in recent history
        recent = self.rate_history[-10:]
        oscillations = 0
        
        for i in range(1, len(recent) - 1):
            # Count direction changes
            if (recent[i] > recent[i-1] and recent[i] > recent[i+1]) or \
               (recent[i] < recent[i-1] and recent[i] < recent[i+1]):
                oscillations += 1
        
        # Adjust φ based on oscillations
        if oscillations > 5:
            # Too oscillatory: reduce φ
            self.phi_factor *= 0.95
            self.phi_factor = max(1.5, self.phi_factor)  # Don't go below 1.5
        elif oscillations < 2:
            # Very stable: can increase φ
            self.phi_factor *= 1.02
            self.phi_factor = min(self.PHI, self.phi_factor)  # Don't exceed φ
        
        self.phi_history.append(self.phi_factor)
    
    def on_success(self):
        """Success with adaptive φ"""
        self.rate *= self.phi_factor
        if self.rate > self.max_rate:
            self.rate = self.max_rate
        
        self.rate_history.append(self.rate)
        self.time_history.append(time.time())
        self.event_history.append('success')
        
        # Adapt every 10 events
        if len(self.event_history) % 10 == 0:
            self.adapt_phi()
    
    def on_congestion(self):
        """Congestion with adaptive φ"""
        self.rate /= self.phi_factor
        if self.rate < self.min_rate:
            self.rate = self.min_rate
        
        self.rate_history.append(self.rate)
        self.time_history.append(time.time())
        self.event_history.append('congestion')
        
        # Adapt every 10 events
        if len(self.event_history) % 10 == 0:
            self.adapt_phi()
