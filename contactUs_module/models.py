from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class ContactUs(models.Model):
    fullname = models.CharField(_('fullname'), max_length=150)
    email = models.EmailField(_('email'))
    subject = models.TextField(_('subject'))
    message = models.TextField(_('message'))
    date = models.DateTimeField(_('date'), auto_now_add=True)
    is_read = models.BooleanField(_('read / unread'), default=False)

    def __str__(self):
        return self.fullname
