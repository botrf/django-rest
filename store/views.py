# from rest_framework import serializers
# from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


from .models import Product, ProductImage
from .serializers import ProductDetailSerializer



# class ProductListView(APIView):

#     def get(self, request):
#         product = Product.objects.all()
#         serializer = ProductListSerializer(product, many=True)
#         return Response(serializer.data)

# class ProductDetailView(APIView):
#     # ProductDetailSerializer
#     product = Product.objects.all()
#     serializer = ProductDetailSerializer(product)
    
    # def get(self, request, pk):
    #     product = Product.objects.get(id=pk)
    #     serializer = ProductDetailSerializer(product)
    #     return Response(serializer.data)

    # def create(self, request):
    #     pass

    # def update(self, request, pk=None):
    #     product = Product.objects.get(id=pk)
    #     serializer = ProductDetailSerializer(product)
    #     return Response(serializer.data)


    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk):
    #     product = Product.objects.get(id=pk)
    #     self.perform_destroy(product)
    #     if product.is_valid():
    #        product.delete()
    #     return Response(status=204)

# class ProductCreateView(APIView):

#     def post(self, request):
#         product = ProductCreateSerializer(data=request.data)
#         if product.is_valid():
#             product.save()

#         return Response(status=201)

