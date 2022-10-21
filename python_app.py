from email.message import EmailMessage  # import email.message
import ssl
import smtplib  # this library will send email

# this is where the sender's email is set
email_sender = 'sender's email'
# this is where the sender's passwork is set generated from Google Security app
email_password = 'password'

email_receiver = 'youremail'

subject = "Learnign Python with free code camp"
body = """
Learn Python every day it's good for you
"""
# create email
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
# smtplib will log in and send email to the reciever
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

