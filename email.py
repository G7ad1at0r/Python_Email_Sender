#!/usr/bin/python3

### Always use Enviroment Variables ###
## This Example Uses Gmail ##

#import os    ### for Enviroment Variables
import smtplib

email_address = '*********@mail.com'
### email_address = os.environ.get(EMAIL_ADD)
email_password = 'password_here'
### email_password = os.environ.get(EMAIL_PASS)



with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(email_address, email_password)
    
    subject = "Hello Mr....."
    body = "One day. you will master Python.. \n\n\nGrasshopper"
    
    msg = f'Subject: {subject}\n\n{body}'
    
    smtp.sendmail('*******@mail.com', '*******@mail.com', msg)