from django.contrib import admin
from core.models.delivery_fees import DeliveryFee


@admin.register(DeliveryFee)
class DeliveryFeeAdmin(admin.ModelAdmin):
    list_display = ('location', 'weight_range', 'delivery_method', 'fee', 'minimum_order', 'free_shipping_above', 'created_at', 'updated_at')
    list_filter = ('location', 'delivery_method')
    search_fields = ('location', 'weight_range', 'delivery_method')