from rest_framework import serializers
from core.models.product import Product
from core.models.productvariantprice import ProductVariantPrice
from core.serializers.category import CategorySerializer
from core.serializers.product_variant_price import ProductVariantPriceSerializer
from .productimage import (
    ProductImageSerializer,
)  # Adjust import as per your project structure
from rest_framework import serializers
from core.models.productvariant import ProductVariant
from .productimage import (
    ProductImageSerializer,
)  # Adjust import as per your project structure


class RelatedProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    category = CategorySerializer()
    # price = (
    #     serializers.SerializerMethodField()
    # )  # Use SerializerMethodField to fetch the price

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "images",
            "price",
            "category",
            "description",
            "availability",
        ]

    def get_images(self, obj):
        # Fetch all images associated with the related product
        if obj.get_all_images():
            return ProductImageSerializer(obj.get_all_images(), many=True).data
        return []



class ProductVariantSerializer(serializers.ModelSerializer):
    related_products = RelatedProductSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    min_order_quantity = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )
    min_order_value = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )
    price = (
        serializers.SerializerMethodField()
    )  # Use SerializerMethodField to fetch the price
    # price = serializers.SerializerMethodField()  # Use SerializerMethodField to fetch the price

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
            "min_order_quantity",
            "min_order_value",
            "availability",
            "created_at",
            "updated_at",
            "product",
            "related_products",
        ]

    def get_price(self, obj):
        # Fetch the price from ProductVariantPrice model
        prices = ProductVariantPrice.objects.filter(product_variant=obj)
        return ProductVariantPriceSerializer(prices, many=True).data
