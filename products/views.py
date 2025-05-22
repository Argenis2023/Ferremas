from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

from rest_framework import routers
from products.views import ProductViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    # otras URLs
] + router.urls
