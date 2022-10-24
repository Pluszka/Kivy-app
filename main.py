import os
from email.message import EmailMessage
from email.utils import parseaddr

from dotenv import load_dotenv
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

from email_token import EmailToken
import ssl
import smtplib

load_dotenv()
SECRET = os.environ.get('SECRET_KEY')
EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('APP_PASSWORD')
EMAIL_BODY = 'Please click link above to confirm your e-mail.'
EMAIL_SUBJECT = 'Confirm an e-mail'
emailToken = EmailToken()
send_email = EmailMessage()

class WindowManager(ScreenManager):
    pass


class P(FloatLayout):
    pass

def show_pop_up(msg):
    show = P()
    popUpWindow = Popup(title='Warning', content=Label(text=msg), size_hint=(None, None), size=(400, 400))
    popUpWindow.open()

class SignUpWindow(Screen, FloatLayout):
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    age = ObjectProperty(None)
    pwd = ObjectProperty(None)
    pwd2 = ObjectProperty(None)

    def validate_data(self):
        try:
            # self.check_username()
            # self.check_email()
            # self.check_pwd()
            # self.check_age()
            self.authenticate_email()
        except Exception as e:
            print(e)
            show_pop_up(str(e))

    def authenticate_email(self):
        token = emailToken.generate_confirmation_token(self.email.text)
        send_email['From'] = EMAIL
        send_email['To'] = self.email.text
        send_email['Subject'] = EMAIL_SUBJECT
        send_email.set_content(EMAIL_BODY)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(EMAIL, PASSWORD)
            smtp.sendmail(EMAIL, self.email.text, send_email.as_string())
#TODO Check if username or already exist
#TODO Send authentication e-mail

    def check_username(self):
        if self.username.text == '':
            raise Exception('Choose a username')


    def check_age(self):
        if self.age.text == "":
            raise Exception('Type an age.')


    def check_email(self):
        if parseaddr(self.email.text)[1] == '':
            raise Exception("Email not valid")

    def check_pwd(self):
        pwd = self.pwd.text
        if pwd != self.pwd2.text:
            raise Exception("Passwords doesn't match")
        if len(pwd) < 12:
            raise Exception("Password isn't long enough (min 12 char)")
        if [letter.isupper() for letter in pwd].count(True) < 1:
            raise Exception("Password need to contain at least one uppercase letter")
        if [letter.islower() for letter in pwd].count(True) < 1:
            raise Exception("Password need to contain at least one lowercase letter")
        if pwd.isalnum():
            raise Exception("Password need to contain at least one special character")
        if [letter.isdigit() for letter in pwd].count(True) < 1:
            raise Exception("Password need to contain at least one number")
# class ContentWindow(Screen):
#     pass

class LoginWindow(Screen):
    username = ObjectProperty(None)
    pwd = ObjectProperty(None)


kv = Builder.load_file('loginSystem.kv')


class LoginSystemApp(App):

    def build(self):
        return kv


if __name__ == "__main__":
    LoginSystemApp().run()
