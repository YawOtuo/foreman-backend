# core/models/user.py

from django.db import models
from core.models.cart import Cart
from core.models.cartitem import CartItem
from core.models.favourite import Favourite
from core.models.product import Product
from core.models.shippingaddress import ShippingAddress  # Import the ShippingAddress model

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    uid = models.CharField(unique=True, null=True, max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.username

    def set_default_shipping_address(self, address_id):
        # Unset any existing default addresses
        ShippingAddress.objects.filter(user=self, is_default=True).update(is_default=False)
        
        # Set the new default address
        address = ShippingAddress.objects.get(id=address_id, user=self)
        address.is_default = True
        address.save()
        return address

    def get_default_shipping_address(self):
        return ShippingAddress.objects.filter(user=self, is_default=True).first()
    
    def favorites(self):
        return Product.objects.filter(favorite__user=self)
    
    def get_cart(self):
        cart = Cart.objects.filter(user=self).first()
        if cart:
            cart_items = CartItem.objects.filter(cart=cart)
            return cart, cart_items
        else:
            return None, None

    def add_to_cart(self, product):
        # Get or create the user's cart
        cart, _ = Cart.objects.get_or_create(user=self)

        # Check if the product is already in the cart
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        # If the product is not already in the cart, increase its quantity by 1
        if not created:
            return cart_item, f"{cart_item.product.name} already in cart"

        return cart_item, f"{cart_item.product.name} added to cart"
