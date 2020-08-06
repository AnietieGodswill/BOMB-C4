#############################
'''
        RETURN 2HACK
'''
#############################

#MODULES
import smtplib
import random
import string
#import time

small_letters = string.ascii_lowercase
capital_letters = string.ascii_uppercase
#rs = random.choice(small_letters)
#rc = random.choice(capital_letters)
#email_subject = random.choice()
#FOR GMAIL
GMAIL_USERNAME = input("ENTER YOUR GMAIL ADDRESS: ")
GMAIL_PASSWORD = input("ENTER YOUR GMAIL PASSWORD: ")
GMAIL_RECIPIENT = input("ENTER RECEIVER'S GMAIL ADDRESS: ")
BODY = input('ENTER MESSAGE: ')
ENTER_TIME = int(input("ENTER NUMBER OF SEND: "))
# creates SMTP session  
SMTP_MAIL = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security  
SMTP_MAIL.starttls()  
#login with our gmail account
SMTP_MAIL.login(GMAIL_USERNAME,GMAIL_PASSWORD)  
for i in range(1,ENTER_TIME):
    email_subject = "".join((random.choice(capital_letters+small_letters)) for i in range(0,10))
    # message masala
    type_sent = f"from: {GMAIL_USERNAME}\nsubject: {email_subject}\nto: {GMAIL_RECIPIENT}\n"
    result = type_sent+ "\n" +BODY
    SMTP_MAIL.sendmail(GMAIL_USERNAME,GMAIL_RECIPIENT,result)
    print(f"{i}|MAIL HAS BEEN SENT")


SMTP_MAIL.quit()

