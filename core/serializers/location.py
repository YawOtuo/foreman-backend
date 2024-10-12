from rest_framework import serializers
from core.models import Constituency, Area

class AreaSerializer(serializers.ModelSerializer):
    """
    Serializer for the Area model
    """
    class Meta:
        model = Area
        fields = ['id', 'name']  # Adjust fields based on your Area model

class ConstituencyWithAreasSerializer(serializers.ModelSerializer):
    """
    Serializer for the Constituency model, including related areas.
    """
    areas = AreaSerializer(many=True)  # Define areas as a nested serializer

    class Meta:
        model = Constituency
        fields = ['id', 'name', 'areas']  # Include areas in the response
