import requests
from datetime import datetime
import os

nutrition_api_id=os.environ.get("nutrition_api_id")
nutrition_api_key=os.environ.get("nutrition_api_key")
sheety_apy_key=os.environ.get("sheety_apy_key")

query = input("Tell me which exercises you did: ")

def trackapi():
    headers = {
        "x-app-id": nutrition_api_id,
        "x-app-key": nutrition_api_key
    }

    data = {
        "query": query,
        "gender": "male",
        "weight_kg": 87,
        "height_cm": 183,
        "age": 34 
            }
    
    url = "https://trackapi.nutritionix.com/v2/natural/exercise"
    response = requests.post(url=url , json=data, headers=headers)
    response.raise_for_status()
    return response.json()

def sheetyapi(exercise, duration, calories_burned):
    headers = {
        "Content-Type": "application/json",
        "Authorization": sheety_apy_key
    }

    data = { "workout": 
            {
                "date": datetime.now().strftime("%d/%m/%Y"),
                "time": datetime.now().strftime("%X"),
                "exercise": exercise,
                "duration": duration,
                "calories": calories_burned
            } 
            }
    
    url = "https://api.sheety.co/a6566d5c8244a718f5eacb69ceba4c0f/myWorkout/workouts"
    response = requests.post(url=url, json=data, headers=headers)
    response.raise_for_status()
    print(response.json())
    return response.json()


track_response = trackapi()

for excercise in track_response["exercises"]:
    exercise_name = excercise["name"].title()
    duration= excercise["duration_min"]
    calories_burned = excercise["nf_calories"]
    sheetyapi(exercise_name, duration, calories_burned)




