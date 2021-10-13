from django.urls import path
from . import views


urlpatterns = [
  path("product/", views.ProductListView.as_view()),
  path("product/<int:pk>", views.ProductDetailView.as_view()),
  path("product/create/", views.ProductCreateView.as_view())
]