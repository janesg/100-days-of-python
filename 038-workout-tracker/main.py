import os
import requests
import datetime as dt
from dotenv import load_dotenv

load_dotenv()

NUTRITIONIX_BASE_URL = "https://trackapi.nutritionix.com"
SHEETY_BASE_URL = "https://api.sheety.co"
SHEETY_USER_NAME = os.getenv("SHEETY_USER_NAME")
SHEETY_PROJECT_NAME = os.getenv("SHEETY_PROJECT_NAME")
SHEETY_SHEET_NAME = os.getenv("SHEETY_SHEET_NAME")
SHEETY_SHEET_URL = f"{SHEETY_BASE_URL}/{SHEETY_USER_NAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}"

headers = {
    "Content-Type": "application/json",
    "x-app-id": f"{os.getenv("NUTRITIONIX_APP_ID")}",
    "x-app-key": f"{os.getenv("NUTRITIONIX_APP_KEY")}"
}

request_body = {
    "query": "swam for 1 hour",
    "gender": f"{os.getenv("MY_GENDER")}",
    "age": f"{os.getenv("MY_AGE")}",
    "weight_kg": f"{os.getenv("MY_WEIGHT_KG")}",
    "height_cm": f"{os.getenv("MY_HEIGHT_CM")}"
}

response = requests.post(url=f"{NUTRITIONIX_BASE_URL}/v2/natural/exercise",
                         headers=headers,
                         json=request_body)

response.raise_for_status()

exercise_data = response.json()

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv("SHEETY_TOKEN")}"
}

right_now = dt.datetime.now()

for exercise in exercise_data["exercises"]:
    request_body = {
        SHEETY_SHEET_NAME: {
            "date": f"{right_now.strftime('%d/%m/%Y')}",
            "time": f"{right_now.strftime('%X')}", # %X = Locale’s appropriate time representation in 24hr clock
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=SHEETY_SHEET_URL,
                             headers=headers,
                             json=request_body)

    response.raise_for_status()

    print(response.text)