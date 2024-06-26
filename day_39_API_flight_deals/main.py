from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import  NotificationManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
ORIGIN_CITY_IATA = "LON"


if sheet_data[0]["iataCode"] == "": 
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()



tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        #print(f"{flight.destination_city}: ${flight.price}")
        send_message = NotificationManager(
            f"Low price alert! \nOnly ${flight.price} to fly \nfrom {flight.origin_city}-{flight.origin_airport} \nto {flight.destination_city}-{flight.destination_airport}, \nfrom {flight.out_date} \nto {flight.return_date}"
            )