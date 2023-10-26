from modeltranslation.translator import register, TranslationOptions
from .models import Product


@register(Product)
class CourseTranslationOptions(TranslationOptions):
    fields = ('name','short_desc','long_desc')
