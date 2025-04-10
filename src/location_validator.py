"""
Module providing location validation functionality.
"""
from constants import VALID_LOCATIONS

def validate_location(location):
    """Validate whether the location name is valid
    
    Args:
        location: The location name to validate
        
    Returns:
        bool: Returns True if the location name is valid, otherwise False
    """
    if location not in VALID_LOCATIONS:
        return False
    return True