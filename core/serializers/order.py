
    
from core.models.order import OrderItem, Order
from core.models.productvariant import ProductVariant
from core.serializers.product import ProductSerializer
from rest_framework import serializers

from core.serializers.productimage import ProductImageSerializer
from core.serializers.productvariant import ProductVariantSerializer
from core.serializers.shippingaddress import ShippingAddressSerializer


class OrderDetailProductVariantSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = ProductVariant
        fields = [
            "id",
            "sku",
            "name",
            "images",
            "brief_description",
            "detailed_description",
            "size",
            "length",
            "width",
            "price",
            "availability",
            "created_at",
            "updated_at",
            "product",
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    product_variant = OrderDetailProductVariantSerializer(read_only=True)

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