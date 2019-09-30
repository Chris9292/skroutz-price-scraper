import os
import smtplib
from email.message import EmailMessage


def send_mail(products):
    # retrieve email and password
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    EMAIL_PASS = os.environ.get('EMAIL_PASS')

    # construct message and send to myself
    msg = EmailMessage()
    msg['Subject'] = 'Scraper Alert!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    content = ''
    for product in products:
        content += f"\n{product['name']} current price is {product['price']}\n{product['url']}\n"

    msg.set_content(content)

    with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
        smtp.send_message(msg)
    
    print('Mail sent.')