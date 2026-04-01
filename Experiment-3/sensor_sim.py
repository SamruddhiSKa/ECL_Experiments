import requests
import random
import time
import os

SERVICE_A_URL = os.getenv("SERVICE_A_URL", "http://data-logger:8000/log")

print("Simulator started...")

while True:
    temp = round(random.uniform(20.0, 30.0), 2)
    try:
        response = requests.post(SERVICE_A_URL, json={"temperature": temp})
        print(f"Sent {temp}C, Status: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(10)
