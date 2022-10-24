from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class WindowManager(ScreenManager):
    pass

class SignUpWindow(Screen):
    pass

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
