from django.shortcuts import render
from django.utils import translation
from django.views import View
from home_module.models import MainSlider
from products_module.models import ProductCategory, Product


# Create your views here.

class Home(View):

    def get(self, request):
        latest_products = Product.objects.filter(is_published=True, soft_deleted=False).order_by('-created_at')
        categories = ProductCategory.objects.filter(parent__name=None)
        slides = MainSlider.objects.all()
        context = {
            'latest_products': latest_products,
            'categories': categories,
            'slides': slides,
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
