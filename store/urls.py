from django.urls import path

from .views import ProductView, ProductDetailView, ProductCRUDView, ListProductsMixionsView, DetailProductMixionsView


urlpatterns = [
    path('product/', ProductView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/CRUD-id<int:pk>/', ProductCRUDView.as_view(), name='product_crud'),
    path('product/mixtin/', ListProductsMixionsView.as_view(), name='product_mixtin'),
    path('product/mixtin/<int:pk>/', DetailProductMixionsView.as_view(), name='product_mixtin_detail')
]

