import smtplib
import time


def send_email(too, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("hrithikpuri16@gmail.com", "hrithik16@#")
    server.sendmail("hrithikpuri16@gmail.com", too, content)
    server.close()


send_email("kashishpuri2006@gmail.com", "Hello How are your")
print("Sending mail.....")
time.sleep(10)
print("\nEmail Sent!!")