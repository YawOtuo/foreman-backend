from django.db import models

from core.models.cart import Cart
from core.models.cartitem import CartItem
from core.models.favourite import Favorite
from core.models.product import Product


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    uid = models.CharField(null=True, max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.username
    
    
    def add_to_favorites(self, product):
        Favorite.objects.get_or_create(user=self, product=product)

    def remove_from_favorites(self, product):
        Favorite.objects.filter(user=self, product=product).delete()

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
            return cart_item, "Item already in cart"
        
        return cart_item, "Item added to cart"
