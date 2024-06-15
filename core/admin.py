# admin.py

from django.contrib import admin

from core.models.category import Category
from core.models.product import Product
from core.models.productimage import ProductImage
from core.models.unit_of_measurement import UnitOfMeasurement

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(UnitOfMeasurement)


