from core.models.product import Product
from rest_framework import serializers

from core.serializers.productvariant import ProductVariantSerializer
from .category import CategorySerializer
from .productimage import ProductImageSerializer  # Assuming this is your ProductImageSerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    variants = ProductVariantSerializer(many=True, read_only=True)  # Assuming ProductVariantSerializer exists

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'availability', 'variants']
        extra_kwargs = {
            'name': {'required': True},
            # Add other required fields if needed
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        # Fetch all images associated with variants and add to representation
        all_images = instance.get_all_images()
        image_data = ProductImageSerializer(all_images, many=True).data
        data['images'] = image_data
        return data
