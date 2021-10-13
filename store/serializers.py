from rest_framework import serializers

from .models import Product

class ProductListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ("id", "name", "price", "images"  )



class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'