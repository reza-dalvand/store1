from django.shortcuts import render
from django.utils import translation
from django.views import View
from rest_framework.permissions import AllowAny

from store import settings


# Create your views here.

def home(request):
    return render(request, './index.html', {})


def about_us(request):
    return render(request, './about-us/about-us.html', {})


class HeaderComponent(View):

    def get(self, request):
        return render(request, '_shared/header.html', {})

    def post(self, request, **kwargs):
        """change language by user"""
        translation.activate(request.POST.get('lang'))
        request.LANGUAGE_CODE = translation.get_language()
        return render(request, '_shared/header.html', {})
