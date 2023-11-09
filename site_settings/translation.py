from modeltranslation.translator import register, TranslationOptions
from .models import SiteSetting


@register(SiteSetting)
class SiteSettingTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description', 'address')
