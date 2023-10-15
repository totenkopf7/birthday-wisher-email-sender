##################### Extra Hard Starting Project ######################


import pandas
import smtplib
import random
import datetime as dt

PLACEHOLDER = "[NAME]"
my_email = "procoder1990@gmail.com"
my_password = "coder1990coder"

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
today = dt.datetime.now()
today_tuple = (today.month, today.day)

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    pick_a_letter = random.choice(letters)
    with open(f"./letter_templates/{pick_a_letter}") as data_file:
        letter = data_file.read()
        letter = letter.replace(PLACEHOLDER, birthday_person["name"])
        print(letter)

    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
    # name from birthdays.csv

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                            msg=f"subject: Happy Birthday!\n\n{letter}")
