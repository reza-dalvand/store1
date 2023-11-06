from modeltranslation.translator import register, TranslationOptions
from .models import Product, ProductBrand, ProductCategory


@register(Product)
class CourseTranslationOptions(TranslationOptions):
    fields = ('name', 'short_desc', 'long_desc')


@register(ProductBrand)
class CourseTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(ProductCategory)
class CourseTranslationOptions(TranslationOptions):
    fields = ('name',)

