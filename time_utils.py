# Axiom/time_utils.py
import math
from .lib_nexus_constants import HUMAN_VALUE

def calculate_agency_decay(time_delta, stress_factor):
    """
    Calculates the preservation of human agency over a time delta.
    
    Using a simplified Fourier-Laplace transformation model:
    The goal is to dampen high-frequency stress signals to prevent
    systemic burnout.
    
    $$ F(s) = \int_{0}^{\infty} f(t) e^{-st} \, dt $$
    
    Where 's' represents the stress frequency of the environment.
    """
    # A stress factor of 0 allows agency to approach HUMAN_VALUE.
    # High stress forces an exponential decay.
    decay_constant = 1 - math.exp(-stress_factor * time_delta)
    
    # We maintain agency as a fraction of the infinite potential.
    agency_coefficient = HUMAN_VALUE * (1 - decay_constant)
    
    return agency_coefficient

def rest_recovery_signal(current_energy, duration):
    """
    Models the recovery of human value. 
    Even in a state of high entropy, rest is a recursive return to 
    the base state of humanity.
    """
    recovery_rate = 0.15 # Constants of the Technomouse ecosystem
    return min(current_energy + (duration * recovery_rate), HUMAN_VALUE)
  
