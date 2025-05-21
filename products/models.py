from django.db import models

class Product(models.Model):
    code = models.CharField(max_length=20, unique=True)
    brand = models.CharField(max_length=100)
    brand_code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    date = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.product.code} - {self.value} ({self.date})"
