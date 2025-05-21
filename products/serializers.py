from rest_framework import serializers
from .models import Product, Price

class PriceSerializer(serializers.ModelSerializer):
    Valor = serializers.DecimalField(source='value', max_digits=10, decimal_places=2)

    class Meta:
        model = Price
        fields = ['Valor']

class ProductSerializer(serializers.ModelSerializer):
    Código_del_producto = serializers.CharField(source='code')
    Marca = serializers.CharField(source='brand')
    Código = serializers.CharField(source='brand_code')
    Nombre = serializers.CharField(source='name')
    Precio = PriceSerializer(many=True, source='prices', read_only=True)

    class Meta:
        model = Product
        fields = ['Código_del_producto', 'Marca', 'Código', 'Nombre', 'Precio']

    def create(self, validated_data):
        precios_data = self.initial_data.get('Precio', [])
        product = Product.objects.create(
            code=validated_data.get('code'),
            brand=validated_data.get('brand'),
            brand_code=validated_data.get('brand_code'),
            name=validated_data.get('name')
        )
        for precio_data in precios_data:
            Price.objects.create(product=product, value=precio_data['Valor'])
        return product

    def update(self, instance, validated_data):
        precios_data = self.initial_data.get('Precio', [])
        instance.code = validated_data.get('code', instance.code)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.brand_code = validated_data.get('brand_code', instance.brand_code)
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        # Reemplazar precios existentes
        instance.prices.all().delete()
        for precio_data in precios_data:
            Price.objects.create(product=instance, value=precio_data['Valor'])
        return instance
