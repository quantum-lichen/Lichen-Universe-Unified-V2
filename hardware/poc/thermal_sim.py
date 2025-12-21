"""
FC-496 Thermal Simulation (Revised S/V Ratio)
Author: Lichen Collective
"""

import numpy as np

def calculate_fractal_metrics(levels=3, branches=496, scaling_factor=22.27):
    # Initial unit size (meters)
    L0 = 0.01 # 1cm base branch
    
    total_surface = 0
    total_volume = 0
    
    current_L = L0
    current_count = branches
    
    print(f"--- FRACTAL METRICS (N={branches}, Levels={levels}) ---")
    
    for i in range(levels):
        # Simplified cylindrical model for branches
        radius = current_L / 10.0
        surf = 2 * np.pi * radius * current_L
        vol = np.pi * (radius**2) * current_L
        
        layer_surface = current_count * surf
        layer_volume = current_count * vol
        
        total_surface += layer_surface
        total_volume += layer_volume
        
        print(f"Level {i+1}: Count={current_count:,.0f} | L={current_L:.2e}m")
        
        # Scaling for next level
        current_L /= scaling_factor
        current_count *= branches

    sv_ratio = total_surface / total_volume
    print(f"\nTotal Surface: {total_surface:.4f} m²")
    print(f"Total Volume:  {total_volume:.6f} m³")
    print(f"S/V Ratio:     {sv_ratio:.2f}")
    
    return sv_ratio

if __name__ == "__main__":
    # Parameters derived from Whitepaper V1.2
    # Scaling factor adjusted to match D=2.077 target
    sv = calculate_fractal_metrics(levels=3, branches=496, scaling_factor=22.27)
    
    if sv > 180000:
        print("✅ VALIDATION: S/V Ratio exceeds 1.8x10^5 target.")
    else:
        print("⚠️ WARNING: Geometry needs optimization.")
