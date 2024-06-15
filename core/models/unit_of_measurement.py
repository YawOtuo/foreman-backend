from django.db import models

class UnitOfMeasurement(models.Model):
    UNIT_CHOICES = [
        ('BAGS', 'Bags'),
        ('PIECES', 'Pieces'),
        ('TRIPS', 'Trips'),
        ('TONNES', 'Tonnes'),
        ('CUBIC_METERS', 'Cubic Meters')
    ]

    product = models.ForeignKey('Product', related_name='units_of_measurement', on_delete=models.CASCADE)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.unit} ({self.quantity})"
