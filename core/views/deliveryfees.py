from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import DeliveryFee, Area
from core.serializers.delivery_fees import DeliveryFeeSerializer

class DeliveryFeeByAreaAPI(APIView):
    def get(self, request, area_id, *args, **kwargs):
        try:
            # Get the area based on the provided area_id
            area = Area.objects.get(id=area_id)
            
            delivery_fee = DeliveryFee.objects.filter(location=area).first()
            
            # If no delivery fee is found, return a 404 response
            if not delivery_fee:
                return Response({"detail": "No delivery fee found for the specified area."}, status=status.HTTP_404_NOT_FOUND)
            
            # Serialize the single delivery fee object
            serializer = DeliveryFeeSerializer(delivery_fee)
            
            # Return the serialized data
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Area.DoesNotExist:
            return Response({"detail": "Area not found."}, status=status.HTTP_404_NOT_FOUND)
