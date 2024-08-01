# core/models/shippingaddress.py

from django.db import models


class ShippingAddress(models.Model):
    user = models.ForeignKey(
        "core.User", on_delete=models.CASCADE, related_name="shipping_addresses"
    )
    constituency = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    recipient_name = models.CharField(max_length=255)
    recipient_phone = models.CharField(max_length=20)
    nearest_landmark = models.CharField(max_length=255, null=True, blank=True)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        parts = [
            f"Recipient: {self.recipient_name}",
            f"Phone: {self.recipient_phone}",
            f"Location: {self.location}, {self.area}, {self.constituency}",
        ]
        if self.nearest_landmark:
            parts.append(f"Landmark: {self.nearest_landmark}")
        return " | ".join(parts)
