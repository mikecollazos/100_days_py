import requests
from datetime import datetime
import smtplib
import time
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

my_email="roy35@ethereal.email"
pw = "ebKzDeCAfF8SeC77F6"

# MY_LAT = 51.507351 # Your latitude
# MY_LONG = -0.127758 # Your longitude

MY_LAT = -44 # Your latitude
MY_LONG = 162 # Your longitude



# get my location sunrise and sunset and the current time

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    #sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    current_hour = datetime.now().hour
    if current_hour >= sunset:
        return True
    else: 
        return False

while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    lat_diff = MY_LAT - iss_latitude
    long_diff = MY_LONG - iss_longitude

    if (6 > lat_diff > -6) and (6 > long_diff > -6) and is_night():
        print(f"you are within {lat_diff, long_diff} degrees from ISS")
        with smtplib.SMTP("smtp.ethereal.email", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=pw)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, 
                                msg="Subject:ISS is above \n\nLook up for the ISS"
                                )
        print("email sent")
    elif (lat_diff > 5 or lat_diff < -5) or (long_diff > 5 or long_diff < -5):
        print(iss_latitude, iss_longitude, "ISS is more than 5 degrees from you")

    elif is_night():
        print("it not dark yet")
    else:
        print("something went wrong")
    
    time.sleep(60)



#print(json.dumps(data, indent=4))

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

