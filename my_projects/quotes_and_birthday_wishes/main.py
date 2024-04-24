# 1. Update the birthdays.csv file with your friends and family's birthdays, and emails

import datetime as dt
import pandas as pd
import random
import smtplib


# email smtp server
MY_EMAIL = 'insert_your_email@here.com'
MY_PASSWORD = 'insert_your_email_password_here'

# check todays date
now = dt.datetime.now()
today = (now.month, now.day)

# read the birthdays.csv file
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

# 2. Check if today matches a birthday in the birthdays.csv file
if today in birthdays_dict:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    range = random.randint(1, 3)
    with open(f"letter_templates/letter_{range}.txt") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", birthdays_dict[today]["name"])

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays_dict[today]["email"],
            msg=f"Subject:Happy Birthday\n\n{letter}")
