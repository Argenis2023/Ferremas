from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from products.views import ProductViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
