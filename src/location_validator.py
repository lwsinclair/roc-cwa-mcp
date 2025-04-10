"""
提供地點驗證功能的模組。
"""
from constants import VALID_LOCATIONS

def validate_location(location):
    """驗證地區名稱是否有效
    
    Args:
        location: 要驗證的地區名稱
        
    Returns:
        bool: 如果地區名稱有效，則返回 True，否則返回 False
    """
    if location not in VALID_LOCATIONS:
        return False
    return True