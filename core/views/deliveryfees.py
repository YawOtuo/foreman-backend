from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import DeliveryFee, Area
from core.serializers.delivery_fees import DeliveryFeeSerializer  # Assuming DeliveryFee and Area models are in core.models

class DeliveryFeeByAreaAPI(APIView):
    def get(self, request, area_id, *args, **kwargs):
        try:
            area = Area.objects.get(id=area_id)
            

            delivery_fees = DeliveryFee.objects.filter(location=area)
            
            serializer = DeliveryFeeSerializer(delivery_fees, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Area.DoesNotExist:
            # Return a 404 error if the area does not exist
            return Response({"detail": "Area not found."}, status=status.HTTP_404_NOT_FOUND)
