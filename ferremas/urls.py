from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from products.views import ProductViewSet
from frontend import views as frontend_views

router = routers.DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # tus APIs
    path('', frontend_views.index, name='index'),  # página principal frontend
]