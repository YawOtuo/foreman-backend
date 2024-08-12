from django.contrib import admin
from core.models.product import Product
from core.models.productimage import ProductImage
from core.models.productvariant import ProductVariant
from core.models.productvariantprice import ProductVariantPrice


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    list_display = ["id", "image", "is_main"]
    fields = ["image", "is_main"]


class ProductVariantInline(admin.StackedInline):
    model = ProductVariant
    extra = 1


class ProductVariantPriceInline(admin.StackedInline):
    model = ProductVariantPrice
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariantInline]
    search_fields = ["name", "description"]


class ProductVariantAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductVariantPriceInline]
    search_fields = ["name", "sku"]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
