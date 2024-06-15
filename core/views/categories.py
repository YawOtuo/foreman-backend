from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models.category import Category
from core.serializers.category import CategorySerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CategoryAPI(APIView):

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="List of categories",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'name': openapi.Schema(type=openapi.TYPE_STRING),
                        },
                    ),
                ),
            ),
            # 401: "Unauthorized",
        }
    )
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
