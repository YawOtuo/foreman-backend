# core/admin.py

from django import forms
from django.contrib import admin
from core.models.category import Category
from core.models.order import Order, OrderItem
from core.models.product import Product
from core.models.productimage import ProductImage
from core.models.productvariant import ProductVariant
from core.models.unit_of_measurement import UnitOfMeasurement
from core.models.shippingaddress import ShippingAddress
from core.models.user import User

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    list_display = ['id', 'image', 'is_main']
    fields = ['image', 'is_main']

class ProductVariantInline(admin.StackedInline):
    model = ProductVariant
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariantInline]
    search_fields = ['name', 'description']

class ProductVariantAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    search_fields = ['name', 'sku']

class ShippingAddressInline(admin.StackedInline):
    model = ShippingAddress


class UserAdmin(admin.ModelAdmin):
    inlines = [ShippingAddressInline]
    search_fields = ['username', 'email']

class OrderItemInline(admin.TabularInline):
    readonly_fields = ['product', 'quantity', 'total_cost']
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    # readonly_fields = ['user', 'created_at', 'updated_at', 'is_paid', 'total_cost', 'total_quantity', 'shipping_address', 'status', 'confirmed_at', 'shipped_at', 'delivered_at']
    inlines = [OrderItemInline]
    search_fields = ['user__username', 'status']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(Category)
admin.site.register(UnitOfMeasurement)
admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem)
admin.site.register(User, UserAdmin)
admin.site.register(ShippingAddress)
