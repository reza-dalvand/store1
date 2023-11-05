from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=150,
                                error_messages={'unique': _("this username is already in exists"),
                                                "required": _("this field is required")})
    email = models.EmailField(_('email address'), unique=True,
                                error_messages={
                                    'unique': _("this email is already in exists"),
                                    "required": _("this field is required")})
    avatar = models.ImageField(_('avatar'))
    phone_number = models.CharField(_('phone number'), max_length=11, unique=True, null=True, blank=True)

    def __str__(self):
        return self.email
