from kivy.app import App
from kivy.uix.widget import Widget


class LoginWindow(Widget):
    pass


class LoginSystemApp(App):

    def build(self):
        return LoginWindow()


if __name__ == "__main__":
    LoginSystemApp().run()
