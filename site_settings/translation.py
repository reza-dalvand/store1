from modeltranslation.translator import register, TranslationOptions
from .models import SiteSetting


@register(SiteSetting)
class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description', 'address')
