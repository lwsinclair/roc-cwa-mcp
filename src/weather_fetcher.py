"""
提供天氣資料獲取功能的模組。
"""
import requests
from constants import THREE_DAYS_FORECAST_ENDPOINT, ONE_WEEK_FORECAST_ENDPOINT

def fetch_three_days_forecast(location, api_key):
    """從中央氣象局 API 獲取三天天氣預報數據
    
    Args:
        location: 縣市名稱
        api_key: API 金鑰
        
    Returns:
        dict: 原始天氣數據
        
    Raises:
        Exception: 如果 API 請求失敗或出錯
    """
    url = THREE_DAYS_FORECAST_ENDPOINT
    params = {
        "Authorization": api_key,
        "LocationName": location
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API 請求失敗，狀態碼: {response.status_code}")
    except Exception as e:
        raise Exception(f"獲取天氣數據時出錯: {str(e)}")

def fetch_one_week_forecast(location, api_key):
    """從中央氣象局 API 獲取一週天氣預報數據
    
    Args:
        location: 縣市名稱
        api_key: API 金鑰
        
    Returns:
        dict: 原始天氣數據
        
    Raises:
        Exception: 如果 API 請求失敗或出錯
    """
    url = ONE_WEEK_FORECAST_ENDPOINT
    params = {
        "Authorization": api_key,
        "LocationName": location
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API 請求失敗，狀態碼: {response.status_code}")
    except Exception as e:
        raise Exception(f"獲取天氣數據時出錯: {str(e)}")