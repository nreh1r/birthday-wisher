##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import smtplib
import random

my_email = "pgpahnder@gmail.com"
password = "tbuunelzwugygrqd"
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

date = dt.datetime.now()

# Read the csv file
people = pandas.read_csv("./birthdays.csv")
people_dict = people.to_dict(orient="list")
birthdays = people_dict["day"]
months = people_dict["month"]


for i in range(len(birthdays)):
    if months[i] == date.month and birthdays[i] == date.day:
        print("Birthday Found! Wishing them a happy birthday!")
        letter_index = random.randint(1, 3)
        with open(f"./letter_templates/letter_{letter_index}.txt") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", people_dict["name"][i])
            letter = letter.replace("Angela", "Nick")

            # Send email
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email, to_addrs=people_dict["email"][i], msg=f"Subject: Happy Birthday!\n\n{letter}")
        print("Happy Birthday Message Sent!")
        print("---------------------------------------------------------")
