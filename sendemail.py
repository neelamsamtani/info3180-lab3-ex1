import smtplib

from_addr = 'neelam11297@gmail.com'
to_addr = 'neelamsamtani@outlook.com'
message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""
from_name = "Neelam"
to_name = "A friend"
subject = "Your day"
msg = "Hey! Hope you have a great day!"

message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)

# Credentials (if needed)
username = 'neelam11297@gmail.com'
password = 'uezkyfbzzrhfidru'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()