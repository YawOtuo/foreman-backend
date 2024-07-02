from rest_framework import serializers
from core.models.productvariant import ProductVariant
from core.models.product import Product  # Assuming this is your Product model
from .productimage import (
    ProductImageSerializer,
)  # Adjust import as per your project structure


class RelatedProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "name", "image"]

    def get_image(self, obj):
        # Assuming Product has a related image through ProductImage model
        if obj.images.exists():
            return (
                obj.images.first().image.url
            )  # Adjust as per your ProductImage model structure
        return None


class ProductVariantSerializer(serializers.ModelSerializer):
    related_products = RelatedProductSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)  # Add images field

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
            "related_products",
        ]
