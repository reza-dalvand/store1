from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

# class ProductCategory(models.Model):
#     name = models.CharField(_('name'), max_length=255)
#     slug = models.SlugField(_('slug'), max_length=255)
#     image = models.ImageField(_('image'), upload_to='products')
#     short_desc = models.TextField(_('short description'), null=True, blank=True)
#     long_desc = models.TextField(_('long description'), null=True, blank=True)
#     is_published = models.BooleanField(_('is product published'), default=False)
#     soft_deleted = models.BooleanField(_('is product soft deleted'), default=False)
#     price = models.IntegerField(_('price'))
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name

class Product(models.Model):
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)
    image = models.ImageField(_('image'), upload_to='products')
    short_desc = models.TextField(_('short description'), null=True, blank=True)
    long_desc = models.TextField(_('long description'), null=True, blank=True)
    is_published = models.BooleanField(_('is product published'), default=False)
    soft_deleted = models.BooleanField(_('is product soft deleted'), default=False)
    price = models.IntegerField(_('price'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
