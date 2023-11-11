from rest_framework import serializers
from orders_module.models import OrderDetail, Order
from products_module.models import Product


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        exclude = ['create_at', 'order', 'product']


class OrderSerializer(serializers.ModelSerializer):
    orders = OrderDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = ['user', 'is_open', 'orders']
