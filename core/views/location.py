from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Constituency
from core.serializers.location import ConstituencyWithAreasSerializer  # Import your Constituency model

class ConstituenciesWithAreasAPI(APIView):
    """
    API View to get all constituencies and their corresponding areas.
    """
    def get(self, request, *args, **kwargs):
        try:
            # Query all constituencies along with their related areas
            constituencies = Constituency.objects.prefetch_related('areas').all()
            
            # Serialize the constituencies and areas
            serializer = ConstituencyWithAreasSerializer(constituencies, many=True)
            
            # Return the serialized data
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            # Handle any errors that might occur
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
