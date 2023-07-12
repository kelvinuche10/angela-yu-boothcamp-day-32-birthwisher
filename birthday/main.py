##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
from datetime import datetime
from random import randint

password = 'your_app_password'
my_email = 'your_email'


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
birthday_data = pd.read_csv('birthday/birthdays.csv')
for index, row in birthday_data.iterrows():
	if row['day'] == datetime.now().day and row['month'] == datetime.now().month:
		# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
		with open(f'birthday/letter_templates/letter_{randint(1, 3)}.txt') as file:
			letter = file.read()
			new_letter = letter.replace('[NAME]', row['name'])
			# 4. Send the letter generated in step 3 to that person's email address.
			with smtplib.SMTP('smtp.gmail.com') as connection:
				connection.starttls()
				connection.login(user=my_email, password=password)
				connection.sendmail(from_addr=my_email,
					to_addrs='recipient_email',
					msg=f'Subject: Happy Birthday\n\n {new_letter}')






