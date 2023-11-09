from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts_module.models import CustomUser
from products_module.models import Product


class Order(models.Model):
    user = models.ForeignKey(CustomUser, related_name='users', on_delete=models.CASCADE)
    is_open = models.BooleanField(default=False)
    payment_Date = models.DateTimeField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name()


class OrderDetail(models.Model):
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='orders', on_delete=models.CASCADE)
    final_price = models.IntegerField(null=True, blank=True)
    count = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.order.user.get_full_name()} - {self.product.name}'

    def get_total_amount(self):
        return self.count * self.product.price
