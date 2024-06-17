from rest_framework import serializers
from core.models.category import Category
from core.serializers.unit_of_measurement import UnitOfMeasurementSerializer

class CategorySerializer(serializers.ModelSerializer):
    units_of_measurement = UnitOfMeasurementSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', "units_of_measurement"]
