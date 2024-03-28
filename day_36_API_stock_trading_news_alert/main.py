import requests
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
api_key_stocks = os.environ.get("alpha_vantage_api_key")
api_key_news = os.environ.get("api_news")
bot_token = os.environ.get("bot_token")
bot_name = "nattekbot"
bot_chatID = os.environ.get("bot_chatID")

#0B54ZTX4ZE11T4Z9


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
#TODO 2. - Get the day before yesterday's closing stock price
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 

def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def stock_data_api():
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol":STOCK_NAME,
        "apikey": api_key_stocks
    }

    response = requests.get(
        url=STOCK_ENDPOINT, params=parameters
    )
    response.raise_for_status()
    stock_data = (response.json())["Time Series (Daily)"]
    return stock_data

stock_data = stock_data_api()

yesterday_price = float(list(stock_data.items())[1][1]['4. close'])
day_before_price = float(list(stock_data.items())[2][1]['4. close'])
price_diff = yesterday_price - day_before_price


percent_change = round((price_diff / yesterday_price) * 100)
if percent_change > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

yesterday_date = list(stock_data.items())[1][0]
day_before_yesterday = list(stock_data.items())[2][0]

def news_data_api():
    parameters = {
        "q": STOCK_NAME,
        "pageSize":3,
        "from": day_before_yesterday, #"2024-03-26"
        "to":  yesterday_date, #"2024-03-25"
        "language": "en",
        "apikey": api_key_news
    }

    response = requests.get(
        url=NEWS_ENDPOINT, params=parameters
    )
    response.raise_for_status()
    news_data = (response.json())["articles"]
    return news_data


# Check if stock perct changed by more than 1%
if abs(percent_change) > 3:
    news_data = news_data_api()
    news_list = [f"{STOCK_NAME}: {up_down}{percent_change}%\nHeadline: {i['title']}. \nBrief: {i['description']}" for i in news_data]
    for article in news_list:
        print(article)
        telegram_bot_sendtext(article)





#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

