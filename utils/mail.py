from django.core.mail import send_mail
from store import settings


def send_mail_to_users(subject, message, recipient_list):
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, recipient_list)
