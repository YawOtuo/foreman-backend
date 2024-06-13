from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')

    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
