from django.db import models

from core.models.product import Product


class Favorite(models.Model):
    user = models.ForeignKey("core.User", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'product']  # Ensure each product can be favorited only once per user

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.product.name}"