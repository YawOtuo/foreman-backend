# views/favorites.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from core.models.favourite import Favourite
from core.models.product import Product
from core.models.user import User
from core.serializers.favourite import FavoriteSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class FavoriteAPI(APIView):

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        favorites = Favourite.objects.filter(user=user)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,  # Top-level type should be specified
            oneOf=[
                openapi.Schema(type=openapi.TYPE_STRING),
                openapi.Schema(type=openapi.TYPE_INTEGER),
            ],
            description="Product ID, can be a string or an integer",
            properties={
                "product_id": openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=["product_id"],
        ),
        responses={
            201: "Created",
            400: "Bad Request",
        },
    )
    def post(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        product_id = request.data.get("product_id")
        if not product_id:
            return Response(
                {"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        favorite, created = Favourite.objects.get_or_create(user=user, product=product)
        if created:
            serializer = FavoriteSerializer(favorite)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"message": "Product is already in favorites"},
                status=status.HTTP_200_OK,
            )

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,  # Top-level type should be specified
            oneOf=[
                openapi.Schema(type=openapi.TYPE_STRING),
                openapi.Schema(type=openapi.TYPE_INTEGER),
            ],
            description="Product ID, can be a string or an integer",
            properties={
                "product_id": openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=["product_id"],
        ),
        responses={
            201: "Created",
            400: "Bad Request",
        },
    )
    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        product_id = request.data.get("product_id")
        if not product_id:
            return Response(
                {"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            favorite = Favourite.objects.get(user=user, product=product)
        except Favourite.DoesNotExist:
            return Response(
                {"error": "Favorite not found"}, status=status.HTTP_404_NOT_FOUND
            )

        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
