from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary.uploader import upload

from core.models.productvariant import ProductVariant  # Adjust import as per your project structure

class ProductImage(models.Model):
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    image = CloudinaryField('image')
    is_main = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.variant:
            # Check if this is the first image added to the variant
            if not self.variant.images.exists():
                # If so, set it as the main image
                self.is_main = True
            else:
                # If not the first image, check if this image should be the main image
                if self.is_main:
                    # If this image is marked as the main image, update other images to not be the main image
                    self.variant.images.exclude(pk=self.pk).update(is_main=False)
                else:
                    # If this image is not marked as the main image, ensure there's only one main image
                    self.variant.images.filter(is_main=True).update(is_main=False)
        
        # if self.image and hasattr(self.image, 'file'):
        #     upload_response = upload(self.image.file, upload_preset='foreman')
        #     self.image = upload_response['secure_url']

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image for ProductVariant: {self.variant.name}" if self.variant else "Unnamed Image"
