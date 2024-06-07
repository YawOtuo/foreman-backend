from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

from core.models.user import User

class Cart(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Cart of {self.user.username}' if self.user else 'Anonymous Cart'

    def empty_cart(self):
        self.cartitem_set.all().delete()

@receiver(post_save, sender=User)
def create_cart_for_new_user(sender, instance, created, **kwargs):
    if created:  # Check if a new user instance has been created
        Cart.objects.create(user=instance)
