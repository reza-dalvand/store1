# from django.db import models
#
# # Create your models here.
# class Product(models.Model):
#     class Product(models.Model):
#         symbol = models.CharField(max_length=128, blank=True)
#         category = models.ForeignKey(Category, verbose_name=_('category'), related_name='products')
#         name = models.CharField(_('name'), max_length=255)
#         short_desc = models.TextField(_('short description'), null=True, blank=True)
#         long_desc = models.TextField(_('long description'), null=True, blank=True)
#         is_published = models.BooleanField(_('is product published'))
#         ext_code = models.CharField(max_length=128, null=True, blank=True)
#         custom1 = models.CharField(max_length=255, null=True, blank=True)
#         custom2 = models.CharField(max_length=255, null=True, blank=True)
#         custom3 = models.CharField(max_length=255, null=True, blank=True)
#         custom4 = models.CharField(max_length=255, null=True, blank=True)
#         groups = models.ManyToManyField(Group, null=True, blank=True)
#         attributes = models.ManyToManyField(Attribute, through='ProductAttribute')
#         created_at = models.DateTimeField(auto_now_add=True)
#         updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)