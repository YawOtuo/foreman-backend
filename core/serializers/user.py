from rest_framework import serializers
from core.models.user import User
from core.models.cart import Cart

class UserSerializer(serializers.ModelSerializer):
    cart_id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'uid', 'cart_id']

    def get_cart_id(self, obj):
        cart = Cart.objects.filter(user=obj).first()
        return cart.id if cart else None
