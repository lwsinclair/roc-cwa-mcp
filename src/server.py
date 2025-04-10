import sys
from mcp.server.fastmcp import FastMCP
from weather_fetcher import fetch_three_days_forecast, fetch_one_week_forecast, fetch_historical_rainfall
from weather_processor import clean_three_days_forecast_data, clean_one_week_forecast_data, clean_historical_rainfall_data
from location_validator import validate_location, VALID_LOCATIONS

# Check command line arguments
if len(sys.argv) < 2:
    print("Usage: python src/server.py <api_key>")
    sys.exit(1)

# Get API Key
API_KEY = sys.argv[1]

# Initialize MCP Server
mcp = FastMCP("Taiwan Weather API")

@mcp.tool()
def get_3_days_weather(location_name: str) -> list:
    """Get 3-day weather forecast data for the specified county/city
    
    Args:
        location_name: County/city name, must be a valid Taiwan county/city name
            Valid county/city names: 宜蘭縣, 花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 
            臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 
            基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 
            雲林縣, 嘉義縣, 嘉義市, 屏東縣
        
    Returns:
        list: Cleaned weather data containing various weather elements and their time series
    """
    # Validate location name
    if not validate_location(location_name):
        valid_locations_str = ", ".join(VALID_LOCATIONS)
        raise ValueError(f"Invalid location name. Valid location names are: {valid_locations_str}")
    
    # Get weather data
    raw_data = fetch_three_days_forecast(location_name, API_KEY)
    
    # Clean and transform data
    cleaned_data = clean_three_days_forecast_data(raw_data)
    
    return cleaned_data

@mcp.tool()
def get_1_week_weather(location_name: str) -> list:
    """Get 1-week weather forecast data for the specified county/city
    
    Args:
        location_name: County/city name, must be a valid Taiwan county/city name
            Valid county/city names: 宜蘭縣, 花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 
            臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 
            基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 
            雲林縣, 嘉義縣, 嘉義市, 屏東縣
        
    Returns:
        list: Cleaned weather data containing various weather elements and their time series
    """
    # Validate location name
    if not validate_location(location_name):
        valid_locations_str = ", ".join(VALID_LOCATIONS)
        raise ValueError(f"Invalid location name. Valid location names are: {valid_locations_str}")
    
    # Get weather data
    raw_data = fetch_one_week_forecast(location_name, API_KEY)
    
    # Clean and transform data
    cleaned_data = clean_one_week_forecast_data(raw_data)
    
    return cleaned_data

@mcp.tool()
def get_historical_rainfall() -> dict:
    """Get rainfall data for the past three days
    
    Returns:
        dict: Cleaned rainfall data containing rainfall labels and information for various stations
    """
    # Get rainfall data
    raw_data = fetch_historical_rainfall(API_KEY)
    
    # Clean and transform data
    cleaned_data = clean_historical_rainfall_data(raw_data)
    
    return cleaned_data

if __name__ == "__main__":
    mcp.run()
