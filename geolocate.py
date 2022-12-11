import requests
import time

path = "https://us1.locationiq.com/v1/search"

LOCATIONIQ_API_KEY = "pk.d1dd6d8d2991132436d478d3ed7ada02"

seven_wonders = [
    "Great Wall of China",
    "Petra",
    "Colosseum",
    "Chichen Itza",
    "Machu Picchu",
    "Taj Mahal",
    "Christ the Redeemer",
    ]

query_params = {
    "key": LOCATIONIQ_API_KEY,
    "format": "json"
}

coordinates = {}

for i in range(len(seven_wonders)):
    query_params["q"] = seven_wonders[i] 
    response = requests.get(path, params=query_params)
    time.sleep(0.35)
    response_body = response.json()
    response_section = response_body[0]

    lat = response_section["lat"]
    lon = response_section["lon"]

    coordinates[seven_wonders[i]] = {
         "latitude": lat, 
         "longitude": lon,
    }

print(coordinates)