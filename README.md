# Taiwan Central Weather Administration MCP Server

This project provides a Model Context Protocol (MCP) server that interfaces with the Taiwan Central Weather Administration (CWA) API, allowing you to easily access weather data for Taiwan.

[中文版](README_ZH.md)

## CWA API Resources

To use this project, you need to obtain an API key from the Central Weather Administration:

- CWA Open Data Platform: https://opendata.cwa.gov.tw/index
- API Documentation: https://opendata.cwa.gov.tw/dist/opendata-swagger.html
- API Key Application Guide: https://www.hlbh.hlc.edu.tw/resource/openfid.php?id=38959

## Features

- Get 3-day weather forecast data for Taiwan counties and cities
- Get 1-week weather forecast data for Taiwan counties and cities
- Get historical rainfall data for the past three days
- Automatic data cleaning and format conversion
- Simplified API output with only essential information

## System Requirements

- Python 3.10+
- MCP CLI 1.6.0+
- uv package manager

## Installation

1. Ensure you have Python 3.10 or higher installed

2. Install dependencies using uv:

```bash
# Install project dependencies using uv
uv pip install -e .
```

## Usage

### Starting the Server

#### Windows Users

```bash
# Execute in Command Prompt or PowerShell
uv --directory your_project_path run src/server.py your_API_key
```

#### Mac and Linux Users

```bash
# Execute in Terminal
uv --directory your_project_path run src/server.py your_API_key
```

### Available MCP Tools

This server provides the following three main tools:

#### 1. get_3_days_weather

Get 3-day weather forecast data for a specified county or city.

Parameters:

- `location_name` (string): County or city name, must be a valid Taiwan county or city name

Valid county/city names include: Yilan County, Hualien County, Taitung County, Penghu County, Kinmen County, Lienchiang County, Taipei City, New Taipei City, Taoyuan City, Taichung City, Tainan City, Kaohsiung City, Keelung City, Hsinchu County, Hsinchu City, Miaoli County, Changhua County, Nantou County, Yunlin County, Chiayi County, Chiayi City, Pingtung County

#### 2. get_1_week_weather

Get 1-week weather forecast data for a specified county or city.

Parameters:

- `location_name` (string): County or city name, must be a valid Taiwan county or city name

#### 3. get_historical_rainfall

Get rainfall data for the past three days.

No parameters required.

### Data Format

#### Weather Forecast Data Format

```json
[
  {
    "ElementName": "Temperature",
    "Time": [
      ["2025-04-11T00:00", "21"],
      ["2025-04-11T01:00", "21"],
      ...
    ]
  },
  {
    "ElementName": "Relative Humidity",
    "Time": [
      ["2025-04-11T00:00", "90"],
      ["2025-04-11T01:00", "89"],
      ...
    ]
  },
  ...
]
```

#### Rainfall Data Format

```json
{
  "rain_labels": ["Now", "Past10Min", "Past1hr", "Past3hr", "Past6Hr", "Past12hr", "Past24hr", "Past2days", "Past3days"],
  "stations": [
    {
      "name": "Station Name",
      "time": "Observation Time",
      "loc": "County,Town",
      "geo": [latitude, longitude],
      "rain": [current, past10min, past1hr, past3hr, past6hr, past12hr, past24hr, past2days, past3days]
    },
    ...
  ]
}
```

### Supported Weather Elements

#### 3-Day Forecast

- Temperature
- Relative Humidity
- Apparent Temperature
- Comfort Index
- Wind Direction
- Wind Speed
- 3-hour Precipitation Probability
- Weather Phenomenon
- Comprehensive Weather Description

#### 1-Week Forecast

- Average Temperature
- Maximum Temperature
- Minimum Temperature
- Average Relative Humidity
- Maximum Apparent Temperature
- Minimum Apparent Temperature
- Maximum Comfort Index
- Minimum Comfort Index
- Wind Speed
- Wind Direction
- 12-hour Precipitation Probability
- UV Index
- Weather Phenomenon
- Comprehensive Weather Description

## API Data Sources

This project uses the following open data APIs from the Taiwan Central Weather Administration:

- 3-Day Forecast: Taiwan Township Weather Forecast - 3-Day Forecast (3-hour intervals)
- 1-Week Forecast: Taiwan Township Weather Forecast - 1-Week Weather Forecast
- Rainfall Data: Automatic Rainfall Station - Rainfall Observation Data
