from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class SiteSettings(models.Model):
    title = models.CharField(_('title'), max_length=90)
    short_description = models.TextField(_('description'))
    description = models.TextField(_('description'))

    def __str__(self):
        return self.title
