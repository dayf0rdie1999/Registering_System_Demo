from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivy.properties import ObjectProperty
from signUp.SignUpSystem import Sign_Up_Information, security_pass, user_name_pass
from supportFunction.Verification_System import verification_code_generator, send_verification_email
from supportFunction.Hiding_Password_System import Password_Management
from kivy.clock import Clock
from forgotPassword.ForgotPasswordSystem import Checking_Email_Database


class DialogContent(BoxLayout):
    tf_level = ObjectProperty(None);
    l_level = ObjectProperty(None);
    pass


class RaisedButton(Button):
    pass


class SignUpDemo(FloatLayout):
    verificationCode = None
    Dialog = None
    fullname = ObjectProperty(None)
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    confirmPassword = ObjectProperty(None)
    Password_manager = Password_Management()
    confirmPassword_manager = Password_Management()

    def Hiding_Password_SignUpDemo(self):
        self.secondScreen.mainScreen.logInDemo.username.text = ""
        self.secondScreen.mainScreen.logInDemo.password.text = ""
        self.secondScreen.manager.current = "second"
        self.Password_manager.set_object_id(new_object_id=self.password)
        self.confirmPassword_manager.set_object_id(new_object_id=self.confirmPassword)
        self.Hiding_Password_Clock = Clock.schedule_interval(self.password_confirmPassword_clock_start, 0)

    def password_confirmPassword_clock_start(self, instance):
        self.Password_manager.Hiding_Password_System()
        self.confirmPassword_manager.Hiding_Password_System()

    def sign_up(self):
        self.Hiding_Password_Clock.cancel()
        uncrypted_password = self.Password_manager.return_uncrypted_password()
        uncrypted_confirmPassword = self.confirmPassword_manager.return_uncrypted_password()

        checked_uncrypted_password = security_pass(uncrypted_password)
        checked_email = Checking_Email_Database(email=self.email.text)
        checked_username = user_name_pass(username=self.username.text)

        ''' Checking whether all the input is inputted'''
        if checked_uncrypted_password == 'Not enough letters':
            self.Hiding_Password_Clock()
            self.password.helper_text = 'More than 8 characters'
            self.password.error = True
            return False;
        elif checked_uncrypted_password == 'Too long':
            self.Hiding_Password_Clock()
            self.password.helper_text = 'Less than 21 characters'
            self.password.error = True
            return False;
        elif checked_uncrypted_password == 'Missing uppercase':
            self.Hiding_Password_Clock()
            self.password.helpter_text = 'Missing uppercase'
            self.password.error = True
            return False;
        elif checked_uncrypted_password == 'Missing special character':
            self.Hiding_Password_Clock()
            self.password.helper_text = 'Missing special character'
            self.password.error = True
            return False;
        else:
            self.password.error = False

        if checked_email == self.email.text:
            self.Hiding_Password_Clock()
            self.email.helper_text = "Already Taken"
            self.email.error = True
            return False;
        else:
            self.email.error = False

        if checked_username == 'Too short':
            self.Hiding_Password_Clock()
            self.username.helper_text = 'Too short'
            self.username.error = True
            return False;
        elif checked_username == 'No space':
            self.Hiding_Password_Clock()
            self.username.helper_text = 'No space'
            self.username.error = True
            return False;
        elif checked_username == 'Already taken':
            self.Hiding_Password_Clock()
            self.username.helper_text = 'Already taken'
            self.username.error = True
            return False;
        else:
            self.username.error = False
            
        if uncrypted_confirmPassword != uncrypted_password:
            self.Hiding_Password_Clock()
            self.confirmPassword.helper_text = "Not matched with password"
            self.confirmPassword.error = True
            return False;
        else:
            self.confirmPassword.error = False


        'Creating a 6 random characters and sending to the user'
        if self.username.text == checked_username and checked_email == False and  uncrypted_password == checked_uncrypted_password and uncrypted_confirmPassword == uncrypted_password:
            print("haha")
            try:
                self.Hiding_Password_Clock.cancel()
                self.verificationCode = verification_code_generator()
                if send_verification_email(self.verificationCode, user_email_address=self.email.text) == "Email Not Existed":
                    self.email.helper_text = "Email Not Existed"
                    self.email.error = True
                else:
                    self.verification_dialog()
            except:
                print("Email no exist or OS system is incorrect")


    def verification_dialog(self):
        self.dialog = MDDialog(
            size_hint=(0.8, 0.8),
            title="Account Verification",
            type="custom",
            content_cls=DialogContent(),
            buttons=[
                MDRaisedButton(text="OK", on_press=self.checking_verification_code),
                MDFlatButton(text="CANCEL", on_press=self.dismiss_dialog),
            ],
        )
        self.dialog.content_cls.tf_level.bind(on_text_validate=self.checking_verification_code,
                                              on_focus=self.checking_verification_code)
        self.dialog.open()

    def warning_dialog(self, message):
        'Creating Warning Dialog'
        self.dialog = MDDialog(
            type="alert",
            text=message,
        )
        self.dialog.open()

    def dismiss_dialog(self, instance):
        'Dismissing the dialog'
        self.dialog.dismiss()

    def checking_verification_code(self, instance):
        if self.dialog.content_cls.tf_level.text == self.verificationCode:
            try:
                uncrypted_password = self.Password_manager.return_uncrypted_password()
                Sign_Up_Information(fullname=self.fullname.text, username=self.username.text, email=self.email.text,
                                    password=uncrypted_password);
                self.dismiss_dialog_to_main_screen()
            except:
                print("Error")
        else:
            self.dialog.content_cls.tf_level.error = True

    def dismiss_dialog_to_main_screen(self):
        'Switching Screen'
        self.dialog.content_cls.tf_level.text = ""
        self.fullname.text = ""
        self.password.text = ""
        self.email.text = ""
        self.username.text = ""
        self.confirmPassword.text = ""
        self.secondScreen.manager.current = "main"
        self.dialog.dismiss()

    def return_to_main(self):
        'Clearing all the text input'
        self.secondScreen.mainScreen.logInDemo.Hiding_Password_Clock()
        self.fullname.text = ""
        self.password.text = ""
        self.email.text = ""
        self.username.text = ""
        self.confirmPassword.text = ""
        self.secondScreen.manager.current = "main"
