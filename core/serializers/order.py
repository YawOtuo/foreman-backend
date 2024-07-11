
    
from core.models.order import OrderItem, Order
from core.serializers.product import ProductSerializer
from rest_framework import serializers

from core.serializers.shippingaddress import ShippingAddressSerializer




class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderListSerializer(serializers.ModelSerializer):
    # items = OrderItemSerializer(many=True, read_only=True)
    shipping_address = ShippingAddressSerializer()

    class Meta:
        model = Order
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     status = validated_data.get('status', instance.status)
    #     if status != instance.status:
    #         instance.update_status(status)
    #     return super().update(instance, validated_data)
    
class OrderDetailSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    shipping_address = ShippingAddressSerializer()

    class Meta:
        model = Order
        fields = '__all__'

    def update(self, instance, validated_data):
        status = validated_data.get('status', instance.status)
        if status != instance.status:
            instance.update_status(status)
        return super().update(instance, validated_data)