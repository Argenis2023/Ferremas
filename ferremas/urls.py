from django.contrib import admin
from django.urls import path, include
from frontend import views as frontend_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),  # Incluir rutas API products
    path('', frontend_views.index, name='index'),
]
