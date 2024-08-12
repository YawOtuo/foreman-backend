from django.contrib import admin
from core.models.order import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    readonly_fields = ['product_variant', 'quantity', 'total_cost']
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    search_fields = ['user__username', 'status']

admin.site.register(Order, OrderAdmin)
