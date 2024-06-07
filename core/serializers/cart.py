from core.models.cart import Cart
from core.models.cartitem import CartItem
from core.models.user import User
from rest_framework import serializers

from core.serializers.product import ProductSerializer
from core.serializers.user import UserSerializer

class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Serialize the user details
    user_id = serializers.IntegerField(source='user.id', read_only=True)  # Include user id

    class Meta:
        model = Cart
        fields = ['id', 'user', 'user_id', 'created_at', 'updated_at']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'added_at']


