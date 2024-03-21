import smtplib
import random
import datetime as dt
import pandas
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

my_email="roy35@ethereal.email"
pw = "ebKzDeCAfF8SeC77F6"

##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

today = (dt.datetime.now().month, dt.datetime.now().day)

try:
    df = pandas.read_csv("birthdays.csv")
except Exception as e:
    print(f"{e} \n File not found")

#birthday_dict = df.to_dict(orient="records")
birthday_dict = {(row.month,row.day):row for (index, row)in df.iterrows()}
#print(birthday_dict)

if today in birthday_dict:
    name = birthday_dict[today]["name"]
    email = birthday_dict[today]["email"]
    try:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as f:
            bday_message = f.read().replace("[NAME]", name)
    except Exception as e:
        print(e)

    with smtplib.SMTP("smtp.ethereal.email", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(from_addr=my_email, to_addrs=email, 
                            msg=f"Subject:Happy Birthday \n\n{bday_message}"
                            )

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)




