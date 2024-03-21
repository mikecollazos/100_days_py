import requests
from datetime import datetime


MY_LAT = 40.825661
MY_LONG = -74.108521


"""ISS API"""

def ISS_cordinates():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]

    iss_position = (longitude, latitude)
    return iss_position

iss_position = ISS_cordinates()
"""Sunset and Sunrise"""

# parameters = {"lat": float(iss_position[1]),
#               "lng": float(iss_position[0])}


parameters = {"lat": MY_LAT,
              "lng": MY_LONG,
              "formatted": 0}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
time_now = datetime.now()

print(sunrise)
print(sunset)
print(time_now.hour)

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
