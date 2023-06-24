#make a cli application to input city name and give weather informtion using openweather API 

import requests
import json
import sys


def get_weather(city):
    api_key = '42cfff5f25e4f66b6cbef918d3824e1e'
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(base_url)
    data = json.loads(response.text)

    if data['cod'] == '404':
        print(f"City '{city}' not found. Please try again.")
    else:
        print(f"Weather information for {city}:")
        #format the temp to 2 decimals 
        temp = round(data['main']['temp'] - 273.15, 2)
        print(f"Temperature: {temp}°C")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Pressure: {data['main']['pressure']} hPa")
        print(f"Wind Speed: {data['wind']['speed']} m/s")

def main():
    while(True):
        city = input("Enter city name( type quit to exit): ")
        if city.lower() not in 'quit':
            get_weather(city)
            print()
            print()
        else:
            sys.exit()

if __name__ == '__main__':
    main()
