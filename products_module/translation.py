from modeltranslation.translator import register, TranslationOptions
from .models import Product, ProductBrand, ProductCategory


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'short_desc', 'long_desc')


@register(ProductBrand)
class ProductBrandTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

