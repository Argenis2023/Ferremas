from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, InventoryMovementViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('inventory-movements', InventoryMovementViewSet, basename='inventorymovement')

urlpatterns = [
    path('', include(router.urls)),
]
