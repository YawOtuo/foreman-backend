from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    # location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    availability = models.CharField(max_length=50, blank=True)
    # size = models.CharField(max_length=100)
    # features = models.TextField()
    # completion_date = models.DateField()
    # contractor = models.CharField(max_length=255)
    # client = models.CharField(max_length=255)
    status = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
