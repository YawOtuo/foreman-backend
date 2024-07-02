from core.models.product import Product
from rest_framework import serializers

from core.serializers.productvariant import ProductVariantSerializer
from .productimage import ProductImageSerializer
from .category import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer()
    variants = ProductVariantSerializer(many=True, read_only=True)  # Add this line for ProductVariant

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'availability', 'images', 'variants']
        extra_kwargs = {
            'name': {'required': True},
            # Add other required fields if needed
        }
