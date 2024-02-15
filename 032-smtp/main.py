import datetime as dt
import random
import smtplib
from email.message import EmailMessage

TEST_SENDER_EMAIL = "test-sender@onehundreddaysofcode.com"
TEST_RECEIVER_EMAIL = "test-receiver@onehundreddaysofcode.com"

# Using MailHog in Docker:
#   https://github.com/mailhog/MailHog
#   UI: http://localhost:8025/
SMTP_HOST = "host.docker.internal"
SMTP_PORT = 1025


def send_email(email_msg: str):
    with smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT) as connection:
        # MailHog doesn't support TLS
        #   - smtplib.SMTPNotSupportedError: STARTTLS extension not supported by server.
        # connection.starttls()
        connection.login(user=TEST_SENDER_EMAIL, password="")
        msg = EmailMessage()
        msg['From'] = TEST_SENDER_EMAIL
        msg['To'] = TEST_RECEIVER_EMAIL
        msg['Subject'] = "Monday Motivational Stuff"
        msg.set_content(email_msg)
        connection.send_message(msg)


# Define week day constants
SUN, MON, TUE, WED, THU, FRI, SAT = range(7)

now = dt.datetime.now()
day_of_week = now.weekday()

if now.weekday() == MON:
    with open(file="./quotes.txt") as f:
        quotes = f.readlines()
        quote = random.choice(quotes)
        send_email(quote)

    print(f"Sent message: {quote}")
else:
    print("Today is not Monday. No motivational stuff is required...")