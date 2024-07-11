from rest_framework import serializers
from core.models.user import User
from core.models.cart import Cart
from core.serializers.shippingaddress import ShippingAddressSerializer

class UserSerializer(serializers.ModelSerializer):
    cart_id = serializers.SerializerMethodField()
    shipping_addresses = ShippingAddressSerializer(many=True, read_only=True)  # Use a nested serializer

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'uid', 'cart_id', 'shipping_addresses']

    def get_cart_id(self, obj):
        cart = Cart.objects.filter(user=obj).first()
        return cart.id if cart else None
