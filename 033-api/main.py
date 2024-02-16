import requests

# API for the International Space Station
ISS_BASE_URL = "http://api.open-notify.org"
SUNRISE_SUNSET_BASE_URL = "https://api.sunrise-sunset.org/json"

response = requests.get(url=f"{ISS_BASE_URL}/iss-now.json")
# Raises HTTPError if one occurred
response.raise_for_status()

response_dict = response.json()

# Can use lat/long to view ISS position on World map: https://gps-coordinates.org/
iss_position = (
    float(response_dict['iss_position']['latitude']),
    float(response_dict['iss_position']['longitude'])
)

response = requests.get(url=SUNRISE_SUNSET_BASE_URL,
                        params={
                        "lat": iss_position[0],
                        "lng": iss_position[1]
                    })
response.raise_for_status()

print(f"For the International Space Station's current position: {iss_position}\n"
      f"    Sunrise: {response.json()['results']['sunrise']} ({response.json()['tzid']})\n"
      f"    Sunset:  {response.json()['results']['sunset']} ({response.json()['tzid']})")
