"""
LICHEN UNIVERSE: FUNDAMENTAL CONSTANTS
Version: 1.0
Author: Bryan Ouellette / Lichen Collective
"""

import math

# --- 1. MATHEMATICAL INVARIANTS ---
PHI = (1 + math.sqrt(5)) / 2  # ~1.61803398875
PI  = math.pi                 # ~3.14159265359
UNITY = 1.0
PERFECT_NUMBER = 496

# --- 2. FC-496 CELL GEOMETRY ---
# The cell is partitioned according to the Golden Ratio
CELL_SIZE_BITS = 496
# 496 / PHI = 306.54... -> Rounded to optimize integer alignment
SEGMENT_MAJOR = 306  # Content Payload
SEGMENT_MINOR = 190  # Headers, Time, Checksums
# Verification: 306 + 190 = 496

# --- 3. TEMPORAL CONSTANTS (π-Time) ---
# Frequency of the Kernel Pulse
FREQ_PI = 1.0 / PI  # ~0.3183 Hz
TIME_CYCLE_BASE = PI

# --- 4. H-SCALE THRESHOLDS ---
H_THRESHOLD_CHAOS = 1.0 / PHI  # ~0.618 (Rejection Limit)
H_TARGET_HARMONY  = UNITY      # 1.0 (Perfection)

# --- 5. PHYSICAL CONSTANTS (UICT) ---
# Base Unit for Calculations
PLANCK_MASS_KG = 2.176434e-8
KAPPA_COMPRESSION = 0.9997     # UICT Coefficient

def get_phi_ratio(a, b):
    """Returns the divergence from Phi for two segments."""
    if b == 0: return 0.0
    ratio = a / b
    return abs(ratio - PHI)
