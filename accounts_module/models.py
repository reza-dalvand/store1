from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.ImageField()
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.email
