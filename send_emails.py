import smtplib
from email.message import EmailMessage

from email_token import EmailToken

emailToken = EmailToken()


class Emails:
    def __init__(self, email, pwd):
        self.my_email = email
        self.app_pwd = pwd

    def send_email(self, email_user, token):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(self.my_email, self.app_pwd)
            connection.send_message(self.write_msg(email_user, token))

    def write_msg(self, user_email, token):
        msg = EmailMessage()
        msg['Subject'] = 'Confirm an email'
        msg['From'] = self.my_email
        msg['To'] = user_email
        msg.add_header('Content-Type', 'text/html')
        content = f'<p>Please click link above to confirm your e-mail.</p>' \
                  f'<a href="http://127.0.0.1:5000/confirm_email/{token}">Click</a>'
        msg.set_content(content, subtype='html')
        return msg
