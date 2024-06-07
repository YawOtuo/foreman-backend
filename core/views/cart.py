from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from core.models.cart import Cart
from core.models.cartitem import CartItem
from core.models.product import Product
from core.models.user import User
from core.serializers.cart import CartItemSerializer, CartSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from core.serializers.product import ProductSerializer

# from drf_yasg.utils import swagger_auto_schema,
# from drf_yasg import openapi




class CartAPI(APIView):
    # get a cart
    def get(self, request, user_id):
        cart = get_object_or_404(Cart, user=user_id)
        serializer = CartSerializer(cart)

        cart_items = CartItem.objects.filter(cart=cart)
        cart_item_serializer = CartItemSerializer(cart_items, many=True)

        data = {"cart": serializer.data, "cart_items": cart_item_serializer.data}
        return Response(data)

    # add to cart
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
    def post(self, request, cart_id):
        product_id = request.data.get("product_id")  # Get product_id from request data
        product = get_object_or_404(Product, id=product_id)

        cart = get_object_or_404(Cart, id=cart_id)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            return Response(
                {"message": f"{product.name} already added to cart"},
                status=status.HTTP_200_OK,
            )
        cart_item.save()

        return Response(
            {"message": f"{product.name} added to cart"}, status=status.HTTP_200_OK
        )


class CartAPIDeleteView(APIView):
    # remove item from cart
    def delete(self, request, cart_id, product_id):
        cart = get_object_or_404(Cart, id=cart_id)
        product = get_object_or_404(Product, id=product_id)

        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
            cart_item.delete()
            return Response(
                {"message": "Item deleted from cart"}, status=status.HTTP_200_OK
            )
        except CartItem.DoesNotExist:
            return Response(
                {"message": "Item not found in cart"}, status=status.HTTP_404_NOT_FOUND
            )
