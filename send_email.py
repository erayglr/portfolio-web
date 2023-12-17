import smtplib
import ssl

host = 'smtp.gmail.com'
port = 465

username = "erayguler5767@gmail.com"
password = "xcit gqhk blap hdzd"

receiver = "erayguler5767@gmail.com"
my_context = ssl.create_default_context()

message = """\
Subject: Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)