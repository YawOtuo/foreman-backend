from django.db import models
from cloudinary.models import CloudinaryField
from core.models.product import Product
from core.models.productvariant import ProductVariant  # Adjust import as per your project structure

class ProductImage(models.Model):
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    image = CloudinaryField('image')
    is_main = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.product:
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
        elif self.variant:
            # Similar logic for ProductVariant
            if not self.variant.images.exists():
                self.is_main = True
            else:
                if self.is_main:
                    self.variant.images.exclude(pk=self.pk).update(is_main=False)
                else:
                    self.variant.images.filter(is_main=True).update(is_main=False)

        super().save(*args, **kwargs)

    def __str__(self):
        if self.product:
            return f"Image for Product: {self.product.name}"
        elif self.variant:
            return f"Image for ProductVariant: {self.variant.name}"
        else:
            return "Unnamed Image"
