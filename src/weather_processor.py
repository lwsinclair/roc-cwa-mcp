"""
提供天氣資料處理和清理功能的模組。
"""

def clean_three_days_forecast_data(data):
    """清理和轉換三天天氣預報數據
    
    Args:
        data: 原始天氣數據
        
    Returns:
        list: 處理後的天氣數據
        
    Raises:
        Exception: 如果數據處理過程中出錯
    """
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

def clean_one_week_forecast_data(data):
    """清理和轉換一週天氣預報數據
    
    Args:
        data: 原始天氣數據
        
    Returns:
        list: 處理後的天氣數據
        
    Raises:
        Exception: 如果數據處理過程中出錯
    """
    try:
        # 獲取 WeatherElement 部分
        weather_elements = data["records"]["Locations"][0]["Location"][0]["WeatherElement"]
        
        # 處理後的結果
        result = []
        
        # 遍歷每個天氣要素
        for element in weather_elements:
            element_name = element["ElementName"]
            
            # 跳過平均露點溫度
            if element_name == "平均露點溫度":
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
                    
                    if element_name == "平均溫度" and "Temperature" in element_value:
                        value = element_value["Temperature"]
                    elif element_name == "最高溫度" and "MaxTemperature" in element_value:
                        value = element_value["MaxTemperature"]
                    elif element_name == "最低溫度" and "MinTemperature" in element_value:
                        value = element_value["MinTemperature"]
                    elif element_name == "平均相對濕度" and "RelativeHumidity" in element_value:
                        value = element_value["RelativeHumidity"]
                    elif element_name == "最高體感溫度" and "MaxApparentTemperature" in element_value:
                        value = element_value["MaxApparentTemperature"]
                    elif element_name == "最低體感溫度" and "MinApparentTemperature" in element_value:
                        value = element_value["MinApparentTemperature"]
                    elif element_name == "最大舒適度指數" and "MaxComfortIndex" in element_value:
                        value = element_value["MaxComfortIndex"]
                    elif element_name == "最小舒適度指數" and "MinComfortIndex" in element_value:
                        value = element_value["MinComfortIndex"]
                    elif element_name == "風速" and "WindSpeed" in element_value:
                        value = element_value["WindSpeed"]
                    elif element_name == "風向" and "WindDirection" in element_value:
                        value = element_value["WindDirection"]
                    elif element_name == "12小時降雨機率" and "ProbabilityOfPrecipitation" in element_value:
                        value = element_value["ProbabilityOfPrecipitation"]
                    elif element_name == "紫外線指數" and "UVExposureLevel" in element_value:
                        value = element_value["UVExposureLevel"]
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