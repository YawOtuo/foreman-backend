# core/serializers.py

from rest_framework import serializers
from core.models.shippingaddress import ShippingAddress

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'  # Or list the fields explicitly
