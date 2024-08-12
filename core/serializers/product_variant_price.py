from rest_framework import serializers
from core.models.productvariantprice import ProductVariantPrice
from core.models.productvariant import ProductVariant
from core.models.unit_of_measurement import UnitOfMeasurement


class UnitOfMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitOfMeasurement
        fields = ["id", "unit", "description"]  # Adjust based on what you need


class ProductVariantPriceSerializer(serializers.ModelSerializer):
    unit_of_measurement = UnitOfMeasurementSerializer()  # Using nested serializer

    class Meta:
        model = ProductVariantPrice
        fields = ["unit_of_measurement", "price"]
