from django.db import models

from core.models.location import Area

class DeliveryFee(models.Model):
    # LOCATION_CHOICES = [
    #     ('Local', 'Local'),
    #     ('Regional', 'Regional'),
    #     ('International', 'International'),
    #     # Add more location categories based on your business needs
    # ]
    
    DELIVERY_METHOD_CHOICES = [
        ('Standard', 'Standard'),
        ('Express', 'Express'),
        ('Same-day', 'Same-day'),
        # Add more delivery methods if necessary
    ]
    
    location = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)  # ForeignKey to Area
    weight_range = models.CharField(max_length=50, null=True, blank=True)  
    delivery_method = models.CharField(max_length=100, choices=DELIVERY_METHOD_CHOICES)
    fee = models.DecimalField(max_digits=10, decimal_places=2)  # Delivery fee
    minimum_order = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Optional
    free_shipping_above = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Optional
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated when the record is updated


    def __str__(self):
        return f"{self.location} - {self.weight_range} ({self.delivery_method})"
    
    class Meta:
        verbose_name = "Delivery Fee"
        verbose_name_plural = "Delivery Fees"
        ordering = ['location', 'weight_range', 'delivery_method']

