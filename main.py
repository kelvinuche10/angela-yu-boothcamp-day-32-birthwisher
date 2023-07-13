import smtplib
from datetime import datetime
import random

password = 'app_password'
my_email = 'senders_email'

day = datetime.now().weekday()
if day == 1:
	with open('quotes.txt', 'r') as file:
		content = file.readlines()
	with smtplib.SMTP('smtp.gmail.com') as connection:
		connection.starttls()
		connection.login(user=my_email, password=password)
		connection.sendmail(from_addr=my_email, 
			to_addrs=my_email, 
			msg=f'Subject: Tuesday quotes \n\n {random.choice(content)} ')



