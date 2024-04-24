import smtplib
import datetime as dt
import random

# gmail smtp server
MY_EMAIL = 'your_email@gmail.com'
MY_PASSWORD = 'your passord here'

# whatever day today is, send an auto email motivational qoute to yourself via email from the quotes.txt file

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            todays_quote = random.choice(all_quotes)

    # send quote from gmail
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(
            user=MY_EMAIL,
            password=MY_PASSWORD
        )
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='recipient@email.com',
            msg=f"Subject:Today's Quote\n\n{todays_quote}"
        )
