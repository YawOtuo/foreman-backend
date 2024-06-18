from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from decimal import Decimal



class Cart(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(
        "core.User", on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of {self.user.username}" if self.user else "Anonymous Cart"

    def empty_cart(self):
        self.cartitem_set.all().delete()

    def get_total_items(self):
        return (
            self.cartitem_set.aggregate(total_items=models.Sum("quantity"))[
                "total_items"
            ]
            or 0
        )

    def get_total_price(self):
        total_price = self.cartitem_set.aggregate(
            total_price=models.Sum(
                models.F("quantity") * models.F("product__price"),
                output_field=models.DecimalField(),
            )
        )["total_price"] or Decimal("0.00")
        return format(total_price, ".2f")


@receiver(post_save, sender='core.User')
def create_cart_for_new_user(sender, instance, created, **kwargs):
    if created:  # Check if a new user instance has been created
        Cart.objects.create(user=instance)
