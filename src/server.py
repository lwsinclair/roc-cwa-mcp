import sys
import requests
import json
from mcp.server.fastmcp import FastMCP

# 檢查命令行參數
if len(sys.argv) < 2:
    print("使用方式: python src/server.py <api_key>")
    sys.exit(1)

# 獲取 API Key
API_KEY = sys.argv[1]

# 初始化 MCP Server
mcp = FastMCP("Taiwan Weather API")

# 合法的縣市名稱列表
VALID_LOCATIONS = ["宜蘭縣", "花蓮縣", "臺東縣", "澎湖縣", "金門縣", "連江縣", 
                  "臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市", 
                  "基隆市", "新竹縣", "新竹市", "苗栗縣", "彰化縣", "南投縣", 
                  "雲林縣", "嘉義縣", "嘉義市", "屏東縣"]

def validate_location(location):
    """驗證地區名稱是否有效"""
    if location not in VALID_LOCATIONS:
        return False
    return True

def fetch_weather_data(location):
    """從中央氣象局 API 獲取天氣數據"""
    url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-089"
    params = {
        "Authorization": API_KEY,
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

def clean_weather_data(data):
    """清理和轉換天氣數據"""
    try:
        # 獲取 WeatherElement 部分
        weather_elements = data["records"]["Locations"][0]["Location"][0]["WeatherElement"]
        
        # 處理後的結果
        result = []
        
        # 遍歷每個天氣要素
        for element in weather_elements:
            element_name = element["ElementName"]
            
            # 跳過露點溫度
            if element_name == "露點溫度":
                continue
                
            # 處理時間和數值
            cleaned_element = {
                "ElementName": element_name,
                "Time": []
            }
            
            for time_data in element["Time"]:
                # 處理時間格式
                if "DataTime" in time_data:
                    # 移除秒和時區，只保留日期和小時
                    time_str = time_data["DataTime"].split("+")[0]
                    # 只保留到分鐘
                    time_str = time_str[:16]
                elif "StartTime" in time_data:
                    # 對於降雨機率等使用 StartTime 的字段
                    time_str = time_data["StartTime"].split("+")[0]
                    time_str = time_str[:16]
                
                # 處理數值
                if "ElementValue" in time_data and len(time_data["ElementValue"]) > 0:
                    # 根據不同的天氣要素類型獲取對應的值
                    value = None
                    element_value = time_data["ElementValue"][0]
                    
                    if element_name == "溫度" and "Temperature" in element_value:
                        value = element_value["Temperature"]
                    elif element_name == "相對濕度" and "RelativeHumidity" in element_value:
                        value = element_value["RelativeHumidity"]
                    elif element_name == "體感溫度" and "ApparentTemperature" in element_value:
                        value = element_value["ApparentTemperature"]
                    elif element_name == "舒適度指數" and "ComfortIndex" in element_value:
                        value = element_value["ComfortIndex"]
                    elif element_name == "風向" and "WindDirection" in element_value:
                        value = element_value["WindDirection"]
                    elif element_name == "風速" and "WindSpeed" in element_value:
                        value = element_value["WindSpeed"]
                    elif element_name == "3小時降雨機率" and "ProbabilityOfPrecipitation" in element_value:
                        value = element_value["ProbabilityOfPrecipitation"]
                    elif element_name == "天氣現象" and "Weather" in element_value:
                        value = element_value["Weather"]
                    elif element_name == "天氣預報綜合描述" and "WeatherDescription" in element_value:
                        value = element_value["WeatherDescription"]
                    
                    # 添加到結果
                    if value is not None:
                        cleaned_element["Time"].append([time_str, value])
            
            # 只有當有時間數據時才添加到結果
            if cleaned_element["Time"]:
                result.append(cleaned_element)
            
        return result
    
    except Exception as e:
        raise Exception(f"數據清理過程中出錯: {str(e)}")

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
    raw_data = fetch_weather_data(location_name)
    
    # 清理和轉換數據
    cleaned_data = clean_weather_data(raw_data)
    
    return cleaned_data

if __name__ == "__main__":
    mcp.run()
