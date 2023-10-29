from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from products_module.models import Product
from rest_framework.generics import ListAPIView
from products_module.serializers import ProductSerializer


class ProductsListApi(ListAPIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        slug = request.query_params.get('slug')
        brand = request.query_params.get('brand')
        products = self.paginate_queryset(Product.objects.filter(is_published=True, soft_deleted=False))
        if slug or brand:
            products = Product.objects.filter(Q(brand__slug__exact=brand) |
                                              Q(category__slug__exact=slug),
                                              is_published=True, soft_deleted=False)
        serializer = ProductSerializer(products, many=True)
        if serializer.data:
            return Response({'products': serializer.data}, status.HTTP_200_OK)
        return Response({'products': serializer.data}, status.HTTP_404_NOT_FOUND)
