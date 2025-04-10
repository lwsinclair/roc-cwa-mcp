"""
Module providing weather data fetching functionality.
"""
import requests
from constants import THREE_DAYS_FORECAST_ENDPOINT, ONE_WEEK_FORECAST_ENDPOINT, HISTORICAL_RAINFALL_ENDPOINT

def fetch_three_days_forecast(location, api_key):
    """Fetch 3-day weather forecast data from CWA API
    
    Args:
        location: County/city name
        api_key: API key
        
    Returns:
        dict: Raw weather data
        
    Raises:
        Exception: If API request fails or errors occur
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
            raise Exception(f"API request failed, status code: {response.status_code}")
    except Exception as e:
        raise Exception(f"Error fetching weather data: {str(e)}")

def fetch_one_week_forecast(location, api_key):
    """Fetch 1-week weather forecast data from CWA API
    
    Args:
        location: County/city name
        api_key: API key
        
    Returns:
        dict: Raw weather data
        
    Raises:
        Exception: If API request fails or errors occur
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
            raise Exception(f"API request failed, status code: {response.status_code}")
    except Exception as e:
        raise Exception(f"Error fetching weather data: {str(e)}")

def fetch_historical_rainfall(api_key):
    """Fetch rainfall data for the past three days from CWA API
    
    Args:
        api_key: API key
        
    Returns:
        dict: Raw rainfall data
        
    Raises:
        Exception: If API request fails or errors occur
    """
    url = HISTORICAL_RAINFALL_ENDPOINT
    params = {
        "Authorization": api_key
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API request failed, status code: {response.status_code}")
    except Exception as e:
        raise Exception(f"Error fetching rainfall data: {str(e)}")