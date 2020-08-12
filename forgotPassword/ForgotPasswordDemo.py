from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDRaisedButton
from forgotPassword.ForgotPasswordSystem import  Checking_Email_Database
from supportFunction.Verification_System import verification_code_generator,send_verification_email

class RaisedButton(Button):
    pass

class forgotPassword_Content_Dialog(BoxLayout):
    label_tf = ObjectProperty(None)
    password_tf = ObjectProperty(None)
    pass

class ForgotPasswordDemo(FloatLayout):
    forgetPasswordDemo_dialog = None
    email_recovery = ObjectProperty(None)

    def checking_email_to_update_password(self):
        'checking the mail is valid or nonvalid'
        Email = Checking_Email_Database(email = self.email_recovery.text)

        if Email is not False:
                self.verification_code = verification_code_generator()
                send_verification_email(verification_code=self.verification_code, user_email_address= Email);
                self.forgotPasswordDemo_verification_dialog()
        else:
            self.email_recovery.error = True
            self.email_recovery.helper_Text = "Not Existed In System"

    def forgotPasswordDemo_verification_dialog(self):
        ' Creating a verification dialog'
        self.forgetPasswordDemo_dialog = MDDialog(
            size_hint = (0.8,0.8),
            title = "Verification Process",
            content_cls = forgotPassword_Content_Dialog(),
            type = "custom",
            buttons = [
                MDFlatButton(text="CANCEL",  on_press = self.dismiss_dialog),
                MDRaisedButton(text="OK", on_press = self.forgotPasswordDemo_checking_verification_code),
            ]
        )
        self.forgetPasswordDemo_dialog.content_cls.password_tf.bind(on_text_validate = self.forgotPasswordDemo_checking_verification_code,on_focus = self.forgotPasswordDemo_checking_verification_code)
        self.forgetPasswordDemo_dialog.open()

    def forgotPasswordDemo_checking_verification_code(self, instance):
        'Checking The Code is valid or nonvalid'
        if self.verification_code == self.forgetPasswordDemo_dialog.content_cls.password_tf.text:
            MDApp.get_running_app().root.receiving_recovery_email(email = self.email_recovery.text)
            self.email_recovery.text = ""
            'Calling the function that is created from the ResetPasswordDemo to maintain proper format of coding'
            self.thirdScreen.fifthScreen.resetPasswordDemo.Hiding_Password_ResetPasswordDemo();
            self.thirdScreen.manager.current = "fifth"
            self.forgetPasswordDemo_dialog.dismiss()

        else:
            self.forgetPasswordDemo_dialog.content_cls.password_tf.error = True;

    def dismiss_dialog(self, instance):
        print('dismiss dialog')
        self.forgetPasswordDemo_dialog.dismiss()

    def return_to_main(self):
        self.email_recovery.text = ""
        self.thirdScreen.manager.current = "main"
