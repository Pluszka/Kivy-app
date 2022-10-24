import os

from dotenv import load_dotenv
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from token import EmailToken

load_dotenv()
emailToken = EmailToken(os.environ.get('SECRET_KEY'))


class WindowManager(ScreenManager):
    pass


class SignUpWindow(Screen):
    username = ObjectProperty(None).text
    email = ObjectProperty(None).text
    age = ObjectProperty(None).text
    pwd = ObjectProperty(None).text
    pwd2 = ObjectProperty(None).text

    def authenticate(self):
        pass
#TODO Check if username or already exist
#TODO Send authentication e-mail


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
