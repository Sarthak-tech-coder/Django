import smtplib
import os
email = input("enter email: ")
password = input("enter password: ")
print('\n' * 100)
target = input("target: ")
subject = input("subject: ")
message = input("message: ")
with smtplib.SMTP('smtp-mail.outlook.com', 587)as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email, password)
    server.sendmail(email, target, f"SUBJECT:{subject} \n\n {message}")
