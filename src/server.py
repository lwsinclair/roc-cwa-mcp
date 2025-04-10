import sys
from mcp.server.fastmcp import FastMCP
from weather_fetcher import fetch_three_days_forecast, fetch_one_week_forecast, fetch_historical_rainfall
from weather_processor import clean_three_days_forecast_data, clean_one_week_forecast_data, clean_historical_rainfall_data
from location_validator import validate_location, VALID_LOCATIONS

# 檢查命令行參數
if len(sys.argv) < 2:
    print("使用方式: python src/server.py <api_key>")
    sys.exit(1)

# 獲取 API Key
API_KEY = sys.argv[1]

# 初始化 MCP Server
mcp = FastMCP("Taiwan Weather API")

@mcp.tool()
def get_3_days_weather(location_name: str) -> list:
    """獲取指定縣市未來3天的天氣預報數據
    
    Args:
        location_name: 縣市名稱，必須是有效的台灣縣市名稱
        
    Returns:
        list: 清理後的天氣數據，包含各種天氣要素及其時間序列
    """
    # 驗證地區名稱
    if not validate_location(location_name):
        valid_locations_str = ", ".join(VALID_LOCATIONS)
        raise ValueError(f"無效的地區名稱。有效的地區名稱為: {valid_locations_str}")
    
    # 獲取天氣數據
    raw_data = fetch_three_days_forecast(location_name, API_KEY)
    
    # 清理和轉換數據
    cleaned_data = clean_three_days_forecast_data(raw_data)
    
    return cleaned_data

@mcp.tool()
def get_1_week_weather(location_name: str) -> list:
    """獲取指定縣市未來1週的天氣預報數據
    
    Args:
        location_name: 縣市名稱，必須是有效的台灣縣市名稱
        
    Returns:
        list: 清理後的天氣數據，包含各種天氣要素及其時間序列
    """
    # 驗證地區名稱
    if not validate_location(location_name):
        valid_locations_str = ", ".join(VALID_LOCATIONS)
        raise ValueError(f"無效的地區名稱。有效的地區名稱為: {valid_locations_str}")
    
    # 獲取天氣數據
    raw_data = fetch_one_week_forecast(location_name, API_KEY)
    
    # 清理和轉換數據
    cleaned_data = clean_one_week_forecast_data(raw_data)
    
    return cleaned_data

@mcp.tool()
def get_historical_rainfall() -> dict:
    """獲取過去三天的雨量資料
    
    Returns:
        dict: 清理後的雨量資料，包含雨量標籤和各測站雨量資訊
    """
    # 獲取雨量數據
    raw_data = fetch_historical_rainfall(API_KEY)
    
    # 清理和轉換數據
    cleaned_data = clean_historical_rainfall_data(raw_data)
    
    return cleaned_data

if __name__ == "__main__":
    mcp.run()
