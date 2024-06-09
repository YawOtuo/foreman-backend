# models.py

from django.db import models
from cloudinary.models import CloudinaryField
from core.models.product import Product

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')
    is_main = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        # Check if this is the first image added to the product
        if not self.product.images.exists():
            # If so, set it as the main image
            self.is_main = True
        else:
            # If not the first image, check if this image should be the main image
            if self.is_main:
                # If this image is marked as the main image, update other images to not be the main image
                self.product.images.exclude(pk=self.pk).update(is_main=False)
            else:
                # If this image is not marked as the main image, ensure there's only one main image
                self.product.images.filter(is_main=True).update(is_main=False)
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Image for {self.product.name}"
