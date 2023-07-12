import smtplib
from datetime import datetime
import random

password = 'fezrcyvsvdrxoklt'
my_email = 'amkelvinuche@gmail.com'

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



