# core/models/shippingaddress.py

from django.db import models

class ShippingAddress(models.Model):
    user = models.ForeignKey("core.User", on_delete=models.CASCADE, related_name='shipping_addresses')
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True,blank=True)
    country = models.CharField(max_length=255, default="Ghana")
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.address_line_1}, {self.city}, {self.state}, {self.country}"
