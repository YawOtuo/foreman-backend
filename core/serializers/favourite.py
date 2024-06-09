# serializers.py

from rest_framework import serializers
from core.models.favourite import Favourite
from core.models.product import Product
from core.serializers.product import ProductSerializer

class FavoriteSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Favourite
        fields = ['id', 'user', 'product', 'created_at']
        read_only_fields = ['user', 'created_at']
