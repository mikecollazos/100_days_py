import smtplib
import random
import datetime as dt

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

my_email="roy35@ethereal.email"
pw = "ebKzDeCAfF8SeC77F6"


today = dt.datetime.now()
if today.weekday() == 2:
    try:
        with open("quotes.txt", "r") as f:
            content = f.read().splitlines()
            random_quote = random.choice(content)
    except Exception as e:
        print(e + "\n" + "unable to find 'quotes.txt'")


    with smtplib.SMTP("smtp.ethereal.email", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(from_addr=my_email, to_addrs="first.last@gmail.com", 
                            msg=f"Subject:Motivational Quote\n\n{random_quote}"
                            )

# now = dt.datetime.now()

# #print(now.year)

# #print(now.date())

# date_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(date_of_birth)
