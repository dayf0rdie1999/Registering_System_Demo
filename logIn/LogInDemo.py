from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from logIn.LogInSystem import Sign_In, Checking_Auto_SignIn_System, Creating_Auto_SignIn_System, Deleting_Auto_SignIn_System
from supportFunction.Hiding_Password_System import Password_Management
from kivy.clock import Clock


class RaisedButton(Button):
    pass


class LogInDemo(FloatLayout):
    remember_check = ObjectProperty(None);
    username = ObjectProperty(None);
    password = ObjectProperty(None);
    Password_manager = Password_Management()

    def stop_Hiding_Password_Clock_to_switch_to_forgotPasswordDemo(self):
        self.password.text = ""
        self.username.text = ""
        self.Hiding_Password_Clock.cancel();
        self.mainScreen.manager.current = "third"

    def Hiding_Password_LogInDemo(self):
        self.Password_manager.set_object_id(new_object_id=self.password)
        self.Hiding_Password_Clock = Clock.schedule_interval(self.password_confirmPassword_clock_start, 0)

    def password_confirmPassword_clock_start(self, instance):
        self.Password_manager.Hiding_Password_System()

    def user_sign_in(self):
        self.Hiding_Password_Clock.cancel()
        uncryptedText = self.Password_manager.return_uncrypted_password()

        if self.remember_check.state == "normal":
            result = Sign_In(username=self.username.text, password=uncryptedText);
            if result == "Not Existed":
                self.username.helper_text = "Not existed"
                self.username.error = True
                self.Hiding_Password_Clock()
            elif result == "Either Password or Username is incorrect":
                self.username.error = False
                self.password.helper_text = "Incorrect Password"
                self.password.error = True
                self.Hiding_Password_Clock()
            else:
                self.Hiding_Password_Clock.cancel()
                self.username.error = False
                self.password.error = False
                self.username.text = ""
                self.password.text = ""
                self.mainScreen.manager.current = "fourth"

        elif self.remember_check.state == "down":
            result = Sign_In(username=self.username.text, password=uncryptedText);
            if result == "Not Existed":
                self.Hiding_Password_Clock()
                print("Not Existed")
            elif result == "Either Password or Username is incorrect":
                self.Hiding_Password_Clock()
                print("Password or User is incorrect")

            else:
                self.Hiding_Password_Clock.cancel()
                self.username.text = ""
                self.password.text = ""
                Creating_Auto_SignIn_System(options=1);
                self.mainScreen.manager.current = "fourth"


