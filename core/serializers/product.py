
from core.models.product import Product
from core.models.user import User
from rest_framework import serializers

from core.serializers.category import CategorySerializer
from core.serializers.productimage import ProductImageSerializer
from core.serializers.unit_of_measurement import UnitOfMeasurementSerializer



class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer()
    units_of_measurement = UnitOfMeasurementSerializer(many=True)


    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'availability', 'status', 'images', "units_of_measurement"]
        # Specify required fields for POST request
        extra_kwargs = {
            'name': {'required': True},
            # 'description': {'required': True},
            # 'category': {'required': True},
            # 'price': {'required': True},
            # 'availability': {'required': True},
            # 'status': {'required': True},
        }
