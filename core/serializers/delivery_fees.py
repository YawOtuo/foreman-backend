from rest_framework import serializers
from core.models import DeliveryFee

class DeliveryFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryFee
        fields = ['id', 'location', 'weight_range', 'delivery_method', 'fee', 'minimum_order', 'free_shipping_above']
