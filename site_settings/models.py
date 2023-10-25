from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class SiteSettings(models.Model):
    title = models.CharField(_('title'), max_length=90)
    email = models.EmailField(_('email'))
    short_description = models.TextField(_('short description'))
    description = models.TextField(_('description'))
    address = models.TextField(_('address'))
    mobile = models.IntegerField(_('phone number'))
    phone_number = models.IntegerField(_('phone number'))

    def __str__(self):
        return self.title
