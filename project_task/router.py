from store.viewsets import ProductViewset, ProductDetailViewset
from rest_framework import routers




router = routers.DefaultRouter()
router.register('product', ProductViewset)
router.register('product/<int:pk>/', ProductDetailViewset)

urlpatterns = router.urls
