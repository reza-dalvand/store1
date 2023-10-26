from modeltranslation.translator import register, TranslationOptions
from .models import SiteSettings


@register(SiteSettings)
class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description', 'address')
