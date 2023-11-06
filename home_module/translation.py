from modeltranslation.translator import register, TranslationOptions
from .models import MainSlider


@register(MainSlider)
class CourseTranslationOptions(TranslationOptions):
    fields = ('title',)
