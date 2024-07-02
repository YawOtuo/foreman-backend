from django.db import models
from core.models.category import Category

class UnitOfMeasurement(models.Model):
    UNIT_CHOICES = [
        ('BAGS', 'Bags'),
        ('PIECES', 'Pieces'),
        ('TRIPS', 'Trips'),
        ('TONNES', 'Tonnes'),
        ('CUBIC_METERS', 'Cubic Meters')
    ]

    category = models.ForeignKey(Category, related_name='units_of_measurement', on_delete=models.CASCADE)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
    # quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description = models.TextField(blank=True, null=True)  # Adding the description field

    def __str__(self):
        return f"{self.category.name} - {self.unit}"
