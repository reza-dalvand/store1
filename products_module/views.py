from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.permissions import AllowAny
from products_module.models import Product
from rest_framework.generics import ListAPIView
from products_module.serializers import ProductSerializer
from django.utils.translation import gettext_lazy as _


class ProductsListView(ListAPIView, ListView):
    context_object_name = 'products'
    queryset = Product.objects.filter(Q(is_published=True) & Q(soft_deleted=False))
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    template_name = 'products/products_list.html'

    def get(self, request, *args, **kwargs):
        serializer = self.list(request, *args, **kwargs)
        print(serializer.data)
        if serializer.data:
            return render(request, 'products/products_list.html', {'products': serializer.data})
        # return Response({'products': serializer.data}, status.HTTP_404_NOTFOUND)
        return render(request, 'products/products_list.html', {'error': _('No products found')})
