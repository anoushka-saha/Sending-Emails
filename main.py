#Anoushka Saha
#SMTP Intro
#Day 32 Practice
#July 5th, 2024

import smtplib

my_email = "pythonpractice859@gmail.com"

#New SMTP object
connection = smtplib.SMTP("smtp.gmail.com")

#Transport layer security to secure connection to email server
connection.starttls

#Username and password
connection.login(user = my_email , password = "oulk dqmu luus saad")

#Sending email
connection.sendmail(from_addr = my_email, to_addrs = "saha.anoushka@gmail.com", msg = "Hello")

#Closing connection
connection.close()