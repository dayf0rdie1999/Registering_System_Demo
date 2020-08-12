import smtplib
import os
from email.message import EmailMessage
from kivy.utils import platform
import string
import random


def main():
    print("Let's send some emails")

def verification_code_generator():
    'Generating 6 random upper,lower,number'
    list_string = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(list_string) for _ in range(6))


def send_verification_email(verification_code, user_email_address):
    'send verification email to the user'
    if platform == 'win':
        'if the system is windows'
        Email_Address = os.environ.get('testingapplication1999@gmail.com')
        Password = os.environ.get('tmdjatvteicxdbai')

    elif platform == 'android':
        'If the system is android'
        Email_Address = "testingapplication1999@gmail.com"
        Password = "fhlsxtxbltvbrcik"
    elif platform == 'ios':
        Email_Address = "testingapplication1999@gmail.com"
        Password = 'ypdmsaopoqtxctng'
    else:
        Email_Address = "testingapplication1999@gmail.com"
        Password = 'qlocgpsugubniynm'

    try:
        """ Creating an email message"""
        msg = EmailMessage()
        msg['Subject'] = 'Verification Code'
        msg['From'] = Email_Address
        msg['To'] = user_email_address
        content = "Verification Code:" + verification_code
        msg.set_content(content)
        print('Finish creating an email')

        """ Sending The Message To User"""
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            ''' Logging in the email '''
            smtp.login(Email_Address, Password)

            ''' Sending the message'''
            smtp.send_message(msg)
        print("Successfully deploy the message")

    except:
        return "Email Not Existed"

if __name__ == "__main__":
    main()
