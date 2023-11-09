from django.db.models import F, Sum
from django.shortcuts import render
from django.utils import translation
from django.views import View
from home_module.models import MainSlider
from orders_module.models import Order, OrderDetail
from products_module.models import ProductCategory, Product
from site_settings.models import SiteSetting


# Create your views here.

class Home(View):

    def get(self, request):
        latest_products = Product.objects.filter(is_published=True, soft_deleted=False).order_by('-created_at')
        categories = ProductCategory.objects.prefetch_related('productcategory_set').filter(parent__name=None)
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
        order: Order = Order.objects.filter(
            user_id=request.user.id).annotate(
            total_amount=Sum(F('orders__product__price') * F('orders__count'))).first()

        product_id = request.GET.get('product_id')
        if product_id:
            product = order.orders.filter(id=product_id)
            product.delete()

        context = {
            'detail_of_order': order,
            'total_price': order.total_amount
        }
        return render(request, '_shared/header.html', context)


class FooterComponent(View):

    def get(self, request):
        site_settings = SiteSetting.objects.filter(is_active=True).first()
        context = {
            'site_settings': site_settings
        }
        return render(request, '_shared/footer.html', context)


def custom_404(request, exception):
    return render(request, '404.html', status=404)
