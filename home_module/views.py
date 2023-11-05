from django.shortcuts import render
from django.utils import translation
from django.views import View
from rest_framework.permissions import AllowAny

from products_module.models import ProductCategory
from store import settings


# Create your views here.

class home(View):

    def get(self, request):
        categories = ProductCategory.objects.filter(parent__name=None)
        context = {
            'categories': categories,
        }

        return render(request, './index.html', context)

def about_us(request):
    return render(request, './about-us/about-us.html', {})


class HeaderComponent(View):

    def get(self, request):
        """change language by user"""
        translation.activate(request.GET.get('lang'))
        request.LANGUAGE_CODE = translation.get_language()
        return render(request, '_shared/header.html', {})

