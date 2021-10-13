from rest_framework import serializers

from .models import Product, ProductImage


class ProductImageShowAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        exclude = ("product",)

class ProductSerializer(serializers.ModelSerializer):
    first_image = serializers.SerializerMethodField()

    class Meta:
        model = Product 
        fields = ("id","name", "price", "first_image",)

    def get_first_image(self, obj):
        first_image = ProductImage.objects.filter(product=obj).first()
        first_image_serializer = ProductImageShowAllSerializer(first_image)
        return first_image_serializer.data

class ProductDetailSerializer(serializers.ModelSerializer):

    images = ProductImageShowAllSerializer(many=True)

    class Meta:
        model = Product
        fields = ("name", "price", "description", "data_create", "images",)

