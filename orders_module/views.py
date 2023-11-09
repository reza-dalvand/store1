from django.db.models import Sum, F
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from orders_module.models import Order


# Create your views here.


class OrderView(View):

    def get(self, request, *args, **kwargs):
        product_id = request.GET.get('product_id')
        order: Order = Order.objects.filter(
            user_id=request.user.id).annotate(
            total_amount=Sum(F('orders__product__price') * F('orders__count'))).first()

        if product_id:
            product = order.orders.filter(id=product_id)
            product.delete()

        context = {
            'detail_of_order': order.orders.order_by('-create_at'),
            'total_price': order.total_amount
        }
        return render(request, 'order/order_basket.html', context)
