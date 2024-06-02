import re
import threading

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from rest_framework.exceptions import ValidationError
from twilio.rest import Client

email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
phone_number_regex = re.compile(r"^\+?(\d{1,3})?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})$")
username_regex = re.compile(r"^[a-zA-Z0-9_.-]+$")


def check_email_or_phone_number(email_or_phone_number):
    if re.fullmatch(email_regex, email_or_phone_number):
        email_or_phone_number = "email"
    elif re.fullmatch(phone_number_regex, email_or_phone_number):
        email_or_phone_number = "phone_number"
    else:
        data = {
            "success": False,
            "message": "Email or phone number is not valid"
        }
        return ValidationError(data)

    return email_or_phone_number


def check_user_type(user_input):
    if re.fullmatch(email_regex, user_input):
        user_input = "email"
    elif re.fullmatch(phone_number_regex, user_input):
        user_input = "phone_number"
    elif re.fullmatch(username_regex, user_input):
        user_input = "username"
    else:
        data = {
            "success":False,
            "message":"Invalid email,phone number or username"
        }
        raise ValidationError(data)
    return user_input

class EmailThread(threading.Thread):

    def __init__(self, email):
        super().__init__()
        self.email = email

    def run(self):
        self.email.send()


class Email:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            from_email=data['to_email']
        )
        if data.get("content_type") == "html":
            email.content_subtype = "html"
        EmailThread(email).start()


def send_email(email, code):
    html_content = render_to_string(template_name="authentication.html",
                                    context={"code": code})
    print(html_content)
    data = {
        "subject": "Register Instagram",
        "to_email": email,
        "body": html_content,
        "content_type": "html"
    }
    Email.send_email(data=data)


def send_phone_numer_code(phone_number, code):
    account_id = "ACCOUNT_ID"
    auth_token = "AUTH_TOKEN"
    client = Client(account_id, auth_token)
    messages = client.messages.create(
        body=f"Your code {code}",
        from_='+17733210345',
        to=phone_number
    )
