import os

from dotenv import load_dotenv
from email_token import EmailToken
import smtplib

load_dotenv()
emailToken = EmailToken()
EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')

class Emails:

    def __init__(self):
        self.msg = f'Subject:Confirm an e-mail\n\nPlease click link above to confirm your e-mail.'

    def sendEmail(self, form_email):
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=form_email,
            msg=f'{self.msg} <button type="button">Click Me!</button>'
        )