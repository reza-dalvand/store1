from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from products_module.models import Product, ProductCategory
from products_module.serializers import ProductSerializer


class ProductsListApi(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        products = Product.objects.filter(is_published=True, soft_deleted=False)
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
        print('validated_data', validated_data.POST)
        # songs_data = validated_date.pop("songs")
        # artist = Artist.objects.create(**validated_data)
        # for song_data in songs_data:
        #     Song.objects.create(artist=artist, song= ** song_data)
        # serializer = ProductSerializer(products, many=True)
        return Response(status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.filter(is_published=True, soft_deleted=False)
        user = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(user)
        return Response(serializer.data)
