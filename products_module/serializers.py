from rest_framework import serializers
from rest_framework.response import Response

from .models import Product, ProductComment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        exclude = ['created_at']


class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']
