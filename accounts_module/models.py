from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token


class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=150,
                                error_messages={'unique': _("این نام کاربری قبلا ثبت شده است"),
                                                "required": _("این مقدار نباید خالی باشد")})
    email = models.EmailField(_('email address'), unique=True, error_messages={
        'unique': _("این ایمیل آدرس قبلا ثبت شده است"),
        "required": _("این مقدار نباید خالی باشد")})
    avatar = models.ImageField(_('avatar'))
    phone_number = models.CharField(_('phone number'), max_length=11, unique=True, null=True, blank=True)

    def __str__(self):
        return self.email



