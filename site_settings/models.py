from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class SiteSetting(models.Model):
    title = models.CharField(_('title'), max_length=90)
    email = models.EmailField(_('email'), null=True)
    short_description = models.TextField(_('short description'))
    description = models.TextField(_('description'))
    address = models.TextField(_('address'), null=True)
    mobile = models.CharField(_('mobile'), null=True, max_length=11)
    phone_number = models.CharField(_('phone number'), null=True, max_length=11)
    is_active = models.BooleanField(_('is active'), default=False)

    def __str__(self):
        return self.title
