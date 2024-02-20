import os
import requests
from dotenv import load_dotenv
import datetime as dt
from dateutil.relativedelta import relativedelta
import random
import time

load_dotenv()

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
USER_NAME = "gjanes"
GRAPH_ID = "example-graph"

PIXELA_BASE_URL = "https://pixe.la"
CREATE_USER_ENDPOINT = "v1/users"
CREATE_GRAPH_ENDPOINT = f"v1/users/{USER_NAME}/graphs"
GRAPH_DATA_ENDPOINT = f"v1/users/{USER_NAME}/graphs/{GRAPH_ID}"

request_body = {
    "token": PIXELA_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# One-time user creation:
# response = requests.post(url=f"{PIXELA_BASE_URL}/{CREATE_USER_ENDPOINT}",
#                          json=request_body)
#
# response.raise_for_status()
#
# print(response.text)
# Returned:
#   {"message":"Success. Let's visit https://pixe.la/@gjanes , it is your profile page!","isSuccess":true}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

request_body = {
    "id": GRAPH_ID,
    "name": GRAPH_ID,
    "unit": "commit",
    "type": "int",
    "color": "shibafu"      # Japanese for grass .. i.e. green
}

# One-time graph creation:
# response = requests.post(url=f"{PIXELA_BASE_URL}/{CREATE_GRAPH_ENDPOINT}",
#                          headers=headers,
#                          json=request_body)
#
# response.raise_for_status()
#
# print(response.text)

# Post data to graph:
six_months_ago = dt.date.today() - relativedelta(months=6)
print(six_months_ago)

for i in range(1, 31, 3):
    date = f"{(six_months_ago + dt.timedelta(days=i)).strftime("%Y%m%d")}"
    print(date)

    time.sleep(5)

    request_body = {
        "date": date,
        "quantity": str(random.randint(1, 10))
    }

    response = requests.post(url=f"{PIXELA_BASE_URL}/{GRAPH_DATA_ENDPOINT}",
                             headers=headers,
                             json=request_body)

    response.raise_for_status()

# Update (using PUT) the data previously submitted
for i in range(1, 31, 3):
    date = f"{(six_months_ago + dt.timedelta(days=i)).strftime('%Y%m%d')}"
    print(date)

    time.sleep(5)

    request_body = {
        "quantity": str(random.randint(1, 10))
    }

    response = requests.put(url=f"{PIXELA_BASE_URL}/{GRAPH_DATA_ENDPOINT}/{date}",
                            headers=headers,
                            json=request_body)

    # Not sure why, but I get following exception at some point despite waiting using sleep:
    # requests.exceptions.HTTPError: 503 Server Error:
    #       Service Unavailable for url: https://pixe.la/v1/users/gjanes/graphs/example-graph/20230917

    # response.raise_for_status()

# Remove (using DELETE) the data previously updated
for i in range(1, 31, 3):
    date = f"{(six_months_ago + dt.timedelta(days=i)).strftime('%Y%m%d')}"
    print(date)

    time.sleep(5)

    response = requests.delete(url=f"{PIXELA_BASE_URL}/{GRAPH_DATA_ENDPOINT}/{date}",
                               headers=headers)

    # response.raise_for_status()

