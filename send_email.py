#!/usr/bin/python

import smtplib

sender = 'abc@gmail.com'
receivers = ['abc@gmail.com']

message = """From: TESTS
To: To <to@todomain.com>
Subject: e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com',587)
   smtpObj.starttls()
   smtpObj.login(sender, "*******")
   for n in range(1000):
      print(n)
      smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except smtplib.SMTPException:
   print("Error: unable to send email")