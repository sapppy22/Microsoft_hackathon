# Microsoft_hackathon
Readme file for the weather forecast tool designed for Fastest Coder Hackathon.


# Weather Forecast

This command line tool fetches the current weather forecast for a given city using the OpenWeatherMap API. It provides information such as temperature, weather description, humidity, pressure, and wind speed.

## Prerequisites

Before running this tool, ensure that you have the following installed:

- Python (version 3 or above)
- Requests library (`pip install requests`)

## Getting Started

1. Clone the repository or download the `weather_forecast.py` file.
2. Open a terminal or command prompt and navigate to the directory containing the `weather_forecast.py` file.
3. Run the following command to execute the script:

   ```shell
   python weather_forecast.py
   ```

## Usage

1. Enter the name of the city for which you want to fetch the weather forecast. For example:

   ```
   Enter city name(quit to exit): London
   ```

2. The tool will display the weather information for the specified city:

   ```
   Weather information for London:
   Temperature: 18.12°C
   Description: Cloudy
   Humidity: 75%
   Pressure: 1012 hPa
   Wind Speed: 2.68 m/s
   ```

3. You can continue entering city names to fetch weather information. Enter "quit" to exit the tool.

## API Key

This tool utilizes the OpenWeatherMap API to fetch weather data. You need to provide an API key in order to make requests to the API. To obtain an API key:

1. Visit the OpenWeatherMap website: [https://openweathermap.org/](https://openweathermap.org/)
2. Sign up for a free account and obtain an API key.
3. Replace the `api_key` variable in the `weather_forecast.py` file with your API key.

Note: Ensure that you keep your API key secure and do not share it publicly.

**#How GitHub Copilot helps for this CLI tool:****
A) API Usage:

1) Code snippets: Copilot can generate code snippets for making HTTP requests to APIs, including GET, POST, PUT, DELETE, and more. It can provide you with the basic structure of the request, including headers, parameters, and body, saving you time and effort.
2) Auto-completion: Copilot can suggest API endpoint URLs and parameters based on the context, making it easier for you to construct the API request.
3) API key handling: Copilot can assist you in securely storing and retrieving API keys. It can generate code snippets for handling API keys as environment variables or in a separate configuration file, following best practices for API key management.
Data Parsing:

B) JSON parsing: Copilot can help you parse JSON responses from API calls. It can generate code snippets for deserializing JSON data into Python objects, making it easier to access and extract the required information from the API response.
1) Data structure suggestions: Copilot can analyze the data structure and provide suggestions on how to access nested JSON data efficiently. It can generate code snippets for traversing complex JSON structures, accessing specific fields, and iterating over arrays or dictionaries.
C) Error Handling:

1) Exception handling: Copilot can suggest code snippets for handling exceptions and errors that may occur during API calls. It can generate try-except blocks and recommend specific exception types to catch, helping you handle network errors, API errors, and other potential issues.
2) Error message handling: Copilot can assist you in processing and displaying error messages returned by the API. It can suggest code snippets for extracting and formatting error messages, making it easier to provide meaningful feedback to the user.
