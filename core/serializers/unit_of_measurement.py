from rest_framework import serializers
from core.models.unit_of_measurement import UnitOfMeasurement

class UnitOfMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitOfMeasurement
        fields = ['id', 'unit', 'quantity']
