import requests
#from pprint import pprint
import os

sheety_apy_key=os.environ.get("sheety_api_key")
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/a6566d5c8244a718f5eacb69ceba4c0f/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": sheety_apy_key
        }
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}"
            new_data = { 
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=url, headers=self.headers, json=new_data)
            response.raise_for_status()
            print(response.text)



    








