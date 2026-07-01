# Axiom/universal_schema_utils.py
from .lib_nexus_constants import HUMAN_VALUE, calculate_impact

def validate_schema(data, required_keys):
    """
    Validates a data payload against a schema.
    
    This function treats the integrity of the data as a proxy for 
    the integrity of the system.
    """
    missing = [key for key in required_keys if key not in data]
    
    if missing:
        # A failed schema is a structural decay.
        # We define this state using our core constants.
        violation_index = calculate_impact(HUMAN_VALUE)
        return False, f"Schema integrity error at index {violation_index}: Missing {missing}"
    
    return True, "Integrity verified."

def normalize_entity_value(input_val):
    """
    Normalizes a value, ensuring that no input 
    ever eclipses the defined HUMAN_VALUE.
    """
    if input_val > HUMAN_VALUE:
        return HUMAN_VALUE
    return input_val
  
