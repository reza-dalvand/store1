from rest_framework import serializers
from rest_framework.response import Response

from .models import Product, ProductComment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = ['product', 'full_name', 'email', 'message']


class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)


    def create(self, validated_data):
        print(validated_data)
        # tracks_data = validated_data.pop('tracks')
        # album = Album.objects.create(**validated_data)
        # for track_data in tracks_data:
        #     Track.objects.create(album=album, **track_data)
        return Response(status=201)

    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']
