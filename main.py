import os

from dotenv import load_dotenv
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from email_token import EmailToken

load_dotenv()
emailToken = EmailToken(os.environ.get('SECRET_KEY'))


class WindowManager(ScreenManager):
    pass


class SignUpWindow(Screen):
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    age = ObjectProperty(None)
    pwd = ObjectProperty(None)
    pwd2 = ObjectProperty(None)

    def validateData(self):
        try:
            print('dupa')
            self.checkUsername()
            self.checkPwd()
            print('ee')
        except Exception as e:
            print(e)

    def authenticate(self):
        print('dupa')
        # emailToken.generate_confirmation_token(self.email)
#TODO Check if username or already exist
#TODO Send authentication e-mail

    def checkUsername(self):
        if self.username.text == '':
            print('www')
            raise Exception('Choose a username')


    def checkPwd(self):
        pwd = self.pwd.text
        if pwd != self.pwd2.text:
            raise Exception("Passwords doesn't match")
        if len(pwd) < 10:
            raise Exception("Password isn't long enough")
        if [letter.isupper() for letter in pwd].count(True) < 1:
            raise Exception("Password need to contain at least one uppercase letter")
        if [letter.islower() for letter in pwd].count(True) < 1:
            raise Exception("Password need to contain at least one lowercase letter")
        if pwd.isalnum():
            raise Exception("Password need to contain at least one special character")
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
