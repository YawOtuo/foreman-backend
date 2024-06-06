from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from core.models.cart import Cart
from core.models.cartitem import CartItem
from core.models.product import Product
from core.serializers import CartSerializer


class CartAPI(APIView):
    def get(self, request):
        cart_id = request.session.get("cart_id")
        if cart_id:
            cart = get_object_or_404(Cart, id=cart_id)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        else:
            return Response({"message": "Cart is empty"}, status=status.HTTP_200_OK)

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        # Use session to manage cart for anonymous users
        cart_id = request.session.get("cart_id")
        if cart_id:
            cart = get_object_or_404(Cart, id=cart_id)
        else:
            cart = Cart.objects.create()
            request.session["cart_id"] = cart.id

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
        cart_item.save()

        return Response({"message": "Item added to cart"}, status=status.HTTP_200_OK)



class CartAPIDeleteView(APIView):
    def delete(self, request, product_id):
        cart_id = request.session.get("cart_id")
        if cart_id:
            cart = get_object_or_404(Cart, id=cart_id)
            product = get_object_or_404(Product, id=product_id)
            try:
                cart_item = CartItem.objects.get(cart=cart, product=product)
                cart_item.delete()
                return Response({"message": "Item deleted from cart"}, status=status.HTTP_200_OK)
            except CartItem.DoesNotExist:
                return Response({"message": "Item not found in cart"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "Cart is empty"}, status=status.HTTP_404_NOT_FOUND)
