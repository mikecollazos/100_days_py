import requests


# MY_LAT = 40.825661
# MY_LONG = -74.108521
#memphis
MY_LAT = 35.149532
MY_LONG = -90.048981

"""telegram bot"""
bot_token = "7102044194:AAGjePlQazu7gbot1XxILcIhEi6ZP9eDPoo"
bot_name = "nattekbot"
bot_chatID = '6840675274'

def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

"""Weather data API KEY"""
api_key = "c89087696cfb81dd7844092cae6570a9"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast", params=parameters
)
response.raise_for_status()
weather_data = response.json()

# print(weather_data["list"][1]["weather"][0]["id"])

"""Send text message when weather api says it will rain"""
will_rain = False
for i in weather_data["list"]:
    id_code = i["weather"][0]["id"]
    #print(type(id_code))
    if id_code < 700:
        will_rain = True

if will_rain:
    telegram_bot_sendtext("It will rain today. Bring an Umbrella ☂️")

