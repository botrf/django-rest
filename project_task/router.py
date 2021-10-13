from store.viewsets import ProductViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('product-viewset-list', ProductViewset)

