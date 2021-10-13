from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from .models import Product, ProductImage
from .serializers import ProductListSerializer, ProductDetailSerializer, ProductCreateSerializer


class ProductListView(APIView):

    def get(self, request):
        product = Product.objects.all()
        serializer = ProductListSerializer(product, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)


class ProductCreateView(APIView):

    def post(self, request):
        product = ProductCreateSerializer(data=request.data)
        if product.is_valid():
            product.save()

        return Response(status=201)