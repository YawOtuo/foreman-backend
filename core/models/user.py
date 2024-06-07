from django.db import models

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
