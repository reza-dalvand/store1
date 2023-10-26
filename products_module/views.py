from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.permissions import AllowAny
from products_module.models import Product


class ProductsListView(ListView):
    context_object_name = 'products'
    template_name = 'products/products_list.html'

    def get_queryset(self):
        queryset = Product.objects.filter(is_published=True)
        return queryset

