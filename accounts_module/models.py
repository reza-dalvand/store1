import uuid

from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
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
    token = models.CharField(_('token'), max_length=300, default=uuid.uuid4())

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('accounts:user_profile', args=[self.id])
