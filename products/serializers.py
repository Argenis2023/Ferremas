# products/serializers.py
from rest_framework import serializers
from .models import Product, Price

class PriceSerializer(serializers.ModelSerializer):
    Fecha = serializers.DateTimeField(source='date')
    Valor = serializers.DecimalField(source='value', max_digits=10, decimal_places=2)

    class Meta:
        model = Price
        fields = ['Fecha', 'Valor']

class ProductSerializer(serializers.ModelSerializer):
    Precio = PriceSerializer(many=True, source='prices')
    Código_del_producto = serializers.CharField(source='code')
    Marca = serializers.CharField(source='brand')
    Código = serializers.CharField(source='brand_code')
    Nombre = serializers.CharField(source='name')

    class Meta:
        model = Product
        fields = ['Código_del_producto', 'Marca', 'Código', 'Nombre', 'Precio']
