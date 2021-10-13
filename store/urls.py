from django.urls import path
from .views import ProductView, ProductDetailView, ProductCRUDView


urlpatterns = [
    path('product/', ProductView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/CRUD-id<int:pk>/', ProductCRUDView.as_view(), name='product_crud')
]

