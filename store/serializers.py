from rest_framework import serializers

from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):

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
        first_image_serializer = ProductImageSerializer(first_image)
        return first_image_serializer.data


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    class Meta:
        model = Product
        fields = ("name", "price", "description", "data_create", "images",)

    def get_images(self, obj):
        images = ProductImage.objects.filter(product=obj).all()
        images_serializer = ProductImageSerializer(images)
        return images_serializer.data
