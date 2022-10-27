import os
from email.utils import parseaddr
import requests

from dotenv import load_dotenv
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from kivy.uix.screenmanager import ScreenManager, Screen

from email_token import EmailToken
from send_emails import Emails

load_dotenv()
SECRET = os.environ.get('SECRET_KEY')
EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('APP_PASSWORD')
emailToken = EmailToken()
send_email = Emails(EMAIL, PASSWORD)


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
        send_email.sendEmail(self.email.text, token)
        requests.get(
            f'http://127.0.0.1:5000/{self.pwd.text}/{self.username.text}/{self.email.text}/{self.age.text}/{token}'
        )


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


class ContentWindow(Screen):
    def show(self, name):
        data = requests.get(f'http://127.0.0.1:5000/find/{name}').json()
        print(data)
        labels = [
            Label(text=f'Username: {data[0]}',  pos_hint={'center_x':.5, 'center_y':.8}),
            Label(text=f'Email: {data[1]}', pos_hint={'center_x':.5, 'center_y':.6}),
            Label(text=f'Age: {data[2]}', pos_hint={'center_x':.5, 'center_y':.4})]
        [self.add_widget(label) for label in labels]


class LoginWindow(Screen):
    username = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def login(self):
        requests.get(f'http://127.0.0.1:5000/login/{self.username.text}/{self.pwd.text}')


kv = Builder.load_file('loginSystem.kv')


class LoginSystemApp(App):

    def build(self):
        return kv



if __name__ == "__main__":
    LoginSystemApp().run()
