from django.urls import reverse

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


# Create your models here.


class ProductBrand(models.Model):
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), blank=True, max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(ProductBrand, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    parent = models.ForeignKey('ProductCategory', null=True, blank=True,
                               on_delete=models.CASCADE)
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), blank=True, max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(ProductCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, null=True, blank=True, related_name='products_category',
                                 on_delete=models.CASCADE)
    brand = models.ForeignKey(ProductBrand, null=True, blank=True, related_name='products_brand', on_delete=models.CASCADE)
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

    def get_absolute_url(self):
        return reverse('products:products_detail', args=[self.id])


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, related_name='product_gallery',
                                on_delete=models.CASCADE)
    image = models.ImageField(_('image'), upload_to='products', null=True, blank=True)

    def __str__(self):
        return self.product.name
