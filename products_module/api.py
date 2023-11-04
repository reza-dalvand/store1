from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from products_module.models import Product, ProductComment
from products_module.serializers import ProductSerializer, CommentSerializer


class ProductApi(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        products = Product.objects.select_related('category', 'brand').filter(is_published=True, soft_deleted=False)
        category = request.query_params.get('category')
        brand = request.query_params.get('brand')
        if category or brand:
            products = Product.objects.filter(Q(brand__slug__exact=brand) |
                                              Q(category__slug__exact=category),
                                              is_published=True, soft_deleted=False)
        '''other filters ...'''
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, validated_data):
        data = validated_data.POST.dict().copy()
        product = Product.objects.get(id=int(data.pop('product_id')))
        if not ProductComment.objects.filter(email=data['email']).exists():
            comment = ProductComment.objects.create(product=product, **data)
            comment.save()
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response('Forbidden', status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.filter(is_published=True, soft_deleted=False)
        products = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(products)
        return Response(serializer.data)
