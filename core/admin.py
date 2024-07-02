from django.contrib import admin
from core.models.category import Category
from core.models.product import Product
from core.models.productimage import ProductImage
from core.models.productvariant import ProductVariant
from core.models.unit_of_measurement import UnitOfMeasurement

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    ProductImage
    extra = 1

class ProductVariantInline(admin.StackedInline):
    model = ProductVariant
    extra = 1
    inlines = [ProductImageInline]  # Include ProductImageInline within ProductVariantInline

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductVariantInline]

class ProductVariantAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(Category)
admin.site.register(UnitOfMeasurement)
