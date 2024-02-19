import os
import requests
from dotenv import load_dotenv

# Latitude, Longitude values from https://www.latlong.net/
LONDON_POSITION = (51.507351, -0.127758)
WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5"

load_dotenv()

API_KEY = os.getenv('API_KEY')

response = requests.get(url=f"{WEATHER_BASE_URL}/forecast",
                        params={
                           "lat": LONDON_POSITION[0],
                           "lon": LONDON_POSITION[1],
                           "appid": API_KEY,
                           "cnt": 1
                        })

response.raise_for_status()

weather_data = response.json()
latest_report = weather_data["list"][0]["weather"]

print(f"The current weather for {weather_data["city"]["name"]}:")
for weather in latest_report:
    print(f"    {weather["main"]} - {weather["description"]}")
