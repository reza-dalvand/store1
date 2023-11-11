from django.db.models import Sum, F
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from orders_module.api import ZP_API_VERIFY
from orders_module.models import Order
import requests
import json


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


ZP_API_REQUEST = f"https://www.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://www.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://www.zarinpal.com/pg/StartPay/"

amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8080/verify/'


def send_request(request):
    basket = Order.objects.annotate(total_amount=Sum(F('orders__product__price') * F('orders__count'))).filter(
        user=request.user.id, is_open=True).first()
    data = {
        "MerchantID": 'xxxxxxxxxx.xxxxx.xxxxx.xxxxxxxxxx.xxxxxxxx',
        "Amount": basket.total_amount,
        "Description": description,
        "Phone": phone,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    try:
        response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)
        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']),
                        'authority': response['Authority']}
            else:
                return {'status': False, 'code': str(response['Status'])}
        return response

    except requests.exceptions.Timeout:
        return {'status': False, 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False, 'code': 'connection error'}


def verify(authority, request: HttpRequest):
    """check again  the total amount of the response"""
    basket = Order.objects.prefetch_related('orders').annotate(
        total_amount=Sum(F('orders__product__price') * F('orders__count'))).filter(
        user=request.user.id, is_open=True).first()
    data = {
        "MerchantID": 'xxxxxxxxxx.xxxxx.xxxxx.xxxxxxxxxx.xxxxxxxx',
        "Amount": basket.total_amount,
        "Authority": authority,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

    if response.status_code == 200:
        orders = basket.orders.all()
        for order in orders:
            order.final_price = order.product.price
            order.save()
        basket.is_open = False
        basket.save()
        response = response.json()
        if response['Status'] == 100:
            return {'status': True, 'RefID': response['RefID']}
        else:
            return {'status': False, 'code': str(response['Status'])}
    return response
