from core.models.product import Product
from django.db import models



class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    sku = models.CharField(max_length=100, unique=True, null=False)
    name = models.CharField(max_length=255, null=False)
    brief_description = models.CharField(max_length=255, blank=True, null=True)
    detailed_description = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=100, blank=True, null=True)
    length = models.CharField(max_length=100, blank=True, null=True)
    width = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    availability = models.CharField(max_length=50, blank=True)
    related_products = models.ManyToManyField(Product, related_name='related_products', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"
    
    @property
    def min_order_quantity(self):
        return self.product.category.min_order_quantity
    
    @property
    def min_order_value(self):
        return self.product.category.min_order_value
