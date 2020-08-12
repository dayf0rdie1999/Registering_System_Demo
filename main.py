from kivymd.app import MDApp
from logIn.LogInDemo import LogInDemo
from forgotPassword.ForgotPasswordDemo import ForgotPasswordDemo
from signUp.SignUpDemo import SignUpDemo
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from market.MarketPage import MarketPageDemo
from kivy.properties import ObjectProperty
from logIn.LogInSystem import Checking_Auto_SignIn_System
from resetPassword.ResetPasswordDemo import ResetPasswordDemo
from supportFunction.Hiding_Password_System import Password_Management
from kivy.clock import Clock
from supportFunction.Local_Database_System import Create_Local_Database


class RaisedButton(Button):
    pass


class MainScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class ThirdScreen(Screen):
    pass


class FourthScreen(Screen):
    pass


class FifthScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    manager = ObjectProperty(None);

    def receiving_recovery_email(self, email):
        'receiving from one screen'
        self.recovery_email = email

    def sending_recovery_email(self):
        'Sending to different file or screen'
        email = self.recovery_email
        self.recovery_email = ''
        return email;


class MyMainApp(MDApp):
    Create_Local_Database()
    def on_start(self):
        checking = Checking_Auto_SignIn_System()
        if checking is True:
            self.root.current = "fourth"
        else:
            self.root.mainScreen.logInDemo.Hiding_Password_LogInDemo()


if __name__ == "__main__":
    MyMainApp().run()
