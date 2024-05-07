import requests
import os

bot_token = os.environ.get("bot_token")
bot_chatID = os.environ.get("bot_chatID")
bot_name = "nattekbot"



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, bot_message):
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        self.response = response.json()
        #for debug print response
        #print(self.response)

    # def telegram_bot_sendtext(self, bot_message):
    #     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    #     response = requests.get(send_text)
    #     return response.json()
