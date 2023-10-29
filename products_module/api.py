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
        products = self.paginate_queryset(Product.objects.filter(is_published=True, soft_deleted=False))
        serializer = ProductSerializer(products, many=True)
        if serializer.data:
            return Response({'products': serializer.data}, status.HTTP_200_OK)
        return Response({'products': serializer.data}, status.HTTP_404_NOT_FOUND)
