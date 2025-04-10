"""
Module providing weather data processing and cleaning functionality.
"""

def clean_three_days_forecast_data(data):
    """Clean and transform 3-day weather forecast data
    
    Args:
        data: Raw weather data
        
    Returns:
        list: Processed weather data
        
    Raises:
        Exception: If an error occurs during data processing
    """
    try:
        # Get WeatherElement section
        weather_elements = data["records"]["Locations"][0]["Location"][0]["WeatherElement"]
        
        # Processed result
        result = []
        
        # Iterate through each weather element
        for element in weather_elements:
            element_name = element["ElementName"]
            
            # Skip dew point temperature
            if element_name == "露點溫度":
                continue
                
            # Process time and values
            cleaned_element = {
                "ElementName": element_name,
                "Time": []
            }
            
            for time_data in element["Time"]:
                # Process time format
                if "DataTime" in time_data:
                    # Remove seconds and timezone, keep date and hour only
                    time_str = time_data["DataTime"].split("+")[0]
                    # Keep only up to minutes
                    time_str = time_str[:16]
                elif "StartTime" in time_data:
                    # For fields using StartTime such as precipitation probability
                    time_str = time_data["StartTime"].split("+")[0]
                    time_str = time_str[:16]
                
                # Process values
                if "ElementValue" in time_data and len(time_data["ElementValue"]) > 0:
                    # Get corresponding value based on different weather element types
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
                    
                    # Add to result
                    if value is not None:
                        cleaned_element["Time"].append([time_str, value])
            
            # Only add to result when there is time data
            if cleaned_element["Time"]:
                result.append(cleaned_element)
            
        return result
    
    except Exception as e:
        raise Exception(f"Error during data cleaning: {str(e)}")

def clean_one_week_forecast_data(data):
    """Clean and transform 1-week weather forecast data
    
    Args:
        data: Raw weather data
        
    Returns:
        list: Processed weather data
        
    Raises:
        Exception: If an error occurs during data processing
    """
    try:
        # Get WeatherElement section
        weather_elements = data["records"]["Locations"][0]["Location"][0]["WeatherElement"]
        
        # Processed result
        result = []
        
        # Iterate through each weather element
        for element in weather_elements:
            element_name = element["ElementName"]
            
            # Skip average dew point temperature
            if element_name == "平均露點溫度":
                continue
                
            # Process time and values
            cleaned_element = {
                "ElementName": element_name,
                "Time": []
            }
            
            for time_data in element["Time"]:
                # Process time format
                if "DataTime" in time_data:
                    # Remove seconds and timezone, keep date and hour only
                    time_str = time_data["DataTime"].split("+")[0]
                    # Keep only up to minutes
                    time_str = time_str[:16]
                elif "StartTime" in time_data:
                    # For fields using StartTime such as precipitation probability
                    time_str = time_data["StartTime"].split("+")[0]
                    time_str = time_str[:16]
                
                # Process values
                if "ElementValue" in time_data and len(time_data["ElementValue"]) > 0:
                    # Get corresponding value based on different weather element types
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
                    
                    # Add to result
                    if value is not None:
                        cleaned_element["Time"].append([time_str, value])
            
            # Only add to result when there is time data
            if cleaned_element["Time"]:
                result.append(cleaned_element)
            
        return result
    
    except Exception as e:
        raise Exception(f"Error during data cleaning: {str(e)}")

def clean_historical_rainfall_data(data):
    """Clean and transform historical rainfall data
    
    Args:
        data: Raw rainfall data
        
    Returns:
        dict: Processed rainfall data containing rainfall labels and information for various stations
        
    Raises:
        Exception: If an error occurs during data processing
    """
    try:
        # Define rainfall labels
        rain_labels = [
            "Now", "Past10Min", "Past1hr", 
            "Past3hr", "Past6Hr", "Past12hr",
            "Past24hr", "Past2days", "Past3days"
        ]
        
        # Process station data
        stations = []
        
        for station_data in data["records"]["Station"]:
            # Get station name
            name = station_data["StationName"]
            
            # Get observation time
            time = station_data["ObsTime"]["DateTime"]
            
            # Get location information
            county = station_data["GeoInfo"]["CountyName"]
            town = station_data["GeoInfo"]["TownName"]
            loc = f"{county},{town}"
            
            # Find WGS84 coordinate system latitude and longitude
            lat = None
            lon = None
            for coord in station_data["GeoInfo"]["Coordinates"]:
                if coord["CoordinateName"] == "WGS84":
                    lat = coord["StationLatitude"]
                    lon = coord["StationLongitude"]
                    break
            
            # Get rainfall data for different time periods
            rainfall_element = station_data["RainfallElement"]
            rain = [
                rainfall_element["Now"]["Precipitation"],
                rainfall_element["Past10Min"]["Precipitation"],
                rainfall_element["Past1hr"]["Precipitation"],
                rainfall_element["Past3hr"]["Precipitation"],
                rainfall_element["Past6Hr"]["Precipitation"],
                rainfall_element["Past12hr"]["Precipitation"],
                rainfall_element["Past24hr"]["Precipitation"],
                rainfall_element["Past2days"]["Precipitation"],
                rainfall_element["Past3days"]["Precipitation"]
            ]
            
            # Add to result
            station_info = {
                "name": name,
                "time": time,
                "loc": loc,
                "geo": [lat, lon],
                "rain": rain
            }
            
            stations.append(station_info)
        
        # Build final result
        result = {
            "rain_labels": rain_labels,
            "stations": stations
        }
        
        return result
        
    except Exception as e:
        raise Exception(f"Error during rainfall data cleaning: {str(e)}")