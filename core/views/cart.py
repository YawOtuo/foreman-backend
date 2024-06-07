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
    def get(self, request, cart_id):
        cart = get_object_or_404(Cart, pk=cart_id)
        user = cart.user

        if user:
            cart, cart_items = user.get_cart()

            if cart:
                cart_serializer = CartSerializer(cart)
                cart_item_serializer = CartItemSerializer(cart_items, many=True)

                data = {"cart": cart_serializer.data, "cart_items": cart_item_serializer.data}
                return Response(data)
        
        return Response({"message": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

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
        user = cart.user

        cart_item, message = user.add_to_cart(product)

        if cart_item:
            return Response({"message": message}, status=status.HTTP_200_OK)
        else:
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)

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
