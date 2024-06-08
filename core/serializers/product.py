
from core.models.product import Product
from core.models.user import User
from rest_framework import serializers



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'availability', 'status']
        # Specify required fields for POST request
        extra_kwargs = {
            'name': {'required': True},
            # 'description': {'required': True},
            # 'category': {'required': True},
            # 'price': {'required': True},
            # 'availability': {'required': True},
            # 'status': {'required': True},
        }
