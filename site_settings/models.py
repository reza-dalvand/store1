from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class SiteSettings(models.Model):
    title = models.CharField(_('title'), max_length=90)
    email = models.EmailField(_('email'), null=True)
    short_description = models.TextField(_('short description'))
    description = models.TextField(_('description'))
    address = models.TextField(_('address'), null=True)
    mobile = models.IntegerField(_('phone number'), null=True)
    phone_number = models.IntegerField(_('phone number'), null=True)

    def __str__(self):
        return self.title
