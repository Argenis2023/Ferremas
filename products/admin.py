from django.contrib import admin
from .models import Product, Price

class PriceInline(admin.TabularInline):
    model = Price
    extra = 1  # número de formularios extra para nuevos precios
    min_num = 1
    can_delete = True

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'brand', 'brand_code', 'name')
    inlines = [PriceInline]
    search_fields = ('code', 'brand', 'name')
