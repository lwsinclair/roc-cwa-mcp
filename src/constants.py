"""
Constants and configuration module for storing shared constants.
"""

# List of valid county/city names
VALID_LOCATIONS = ["宜蘭縣", "花蓮縣", "臺東縣", "澎湖縣", "金門縣", "連江縣", 
                  "臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市", 
                  "基隆市", "新竹縣", "新竹市", "苗栗縣", "彰化縣", "南投縣", 
                  "雲林縣", "嘉義縣", "嘉義市", "屏東縣"]

# API endpoints
THREE_DAYS_FORECAST_ENDPOINT = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-089"
ONE_WEEK_FORECAST_ENDPOINT = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-091"
HISTORICAL_RAINFALL_ENDPOINT = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0002-001"