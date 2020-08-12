from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.button import Button
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from resetPassword.ResetPasswordSystem import reset_user_password,checking_password_database
from kivymd.uix.dialog import MDDialog
from supportFunction.Hiding_Password_System import Password_Management
from kivy.clock import Clock
from signUp.SignUpSystem import security_pass


class RaisedButton(Button):
    pass


class ResetPasswordDemo(FloatLayout):
    dialog = None
    new_password = ObjectProperty(None);
    confirm_new_password = ObjectProperty(None);

    Password_manager = Password_Management()
    confirmPassword_manager = Password_Management()

    def Hiding_Password_ResetPasswordDemo(self):
        self.Password_manager.set_object_id(new_object_id=self.new_password)
        self.confirmPassword_manager.set_object_id(new_object_id=self.confirm_new_password)
        self.Hiding_Password_Clock = Clock.schedule_interval(self.password_confirmPassword_clock_start, 0)

    def password_confirmPassword_clock_start(self, instance):
        self.Password_manager.Hiding_Password_System()
        self.confirmPassword_manager.Hiding_Password_System()

    def reset_user_password(self):
        'Reset the user password'
        self.RecoveryEmail = MDApp.get_running_app().root.sending_recovery_email()
        self.Hiding_Password_Clock.cancel()
        uncrypted_new_password = self.Password_manager.return_uncrypted_password()
        uncrypted_confirm_new_password = self.confirmPassword_manager.return_uncrypted_password()

        checking_new_password = checking_password_database(password = uncrypted_new_password,email = self.RecoveryEmail)
        if checking_new_password is False:
            self.Hiding_Password_Clock()
            self.new_password.helper_text = "Your old password, input new password"
            self.new_password.error = True
            return False
        else:
            pass

        checked_uncrypted_new_password = security_pass(uncrypted_new_password)
        print("Successfully getting the user recovery email")

        if checked_uncrypted_new_password == 'Not enough letters':
            self.Hiding_Password_Clock()
            self.new_password.helper_text = 'More than 8 characters'
            self.new_password.error = True
        elif checked_uncrypted_new_password == 'Too long':
            self.Hiding_Password_Clock()
            self.new_password.helper_text = 'Less than 21 characters'
            self.new_password.error = True
        elif checked_uncrypted_new_password == 'Missing uppercase':
            self.Hiding_Password_Clock()
            self.new_password.helper_text = 'Missing uppercase'
            self.new_password.error = True
        elif checked_uncrypted_new_password == 'Missing special character':
            self.Hiding_Password_Clock()
            self.new_password.helper_text = 'Missing special character'
            self.new_password.error = True
        elif checked_uncrypted_new_password != uncrypted_confirm_new_password:
            self.Hiding_Password_Clock()
            self.confirm_new_password.error = True
            self.new_password.error = False
        else:
            self.Hiding_Password_Clock.cancel()
            self.new_password.text = ""
            self.confirm_new_password.text = ""
            self.fifthScreen.mainScreen.logInDemo.Hiding_Password_Clock()
            reset_user_password(email = self.RecoveryEmail, password=checked_uncrypted_new_password)
            self.fifthScreen.manager.current = "main"







