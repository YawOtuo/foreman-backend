from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')

    description = models.TextField(blank=True)
    min_order_quantity = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    min_order_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


    def __str__(self):
        return self.name
