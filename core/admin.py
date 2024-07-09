from django.contrib import admin
from core.models.category import Category
from core.models.order import Order, OrderItem
from core.models.product import Product
from core.models.productimage import ProductImage
from core.models.productvariant import ProductVariant
from core.models.unit_of_measurement import UnitOfMeasurement

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    list_display = ['id', 'image', 'is_main']  # Customize displayed columns
    fields = ['image', 'is_main']  # Specify editable fields for ProductImage creation/editing

class ProductVariantInline(admin.StackedInline):
    model = ProductVariant
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariantInline]
    search_fields = ['name', 'description']  # Add searchable fields for Product

class ProductVariantAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    search_fields = ['name', 'sku']  # Add searchable fields for ProductVariant

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(Category)
admin.site.register(UnitOfMeasurement)
admin.site.register(Order)
admin.site.register(OrderItem)


