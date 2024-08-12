from django.db import models

from core.models.productvariant import ProductVariant
from core.models.unit_of_measurement import UnitOfMeasurement


class ProductVariantPrice(models.Model):
    product_variant = models.ForeignKey(ProductVariant, related_name='prices', on_delete=models.CASCADE)

    unit_of_measurement = models.ForeignKey(UnitOfMeasurement, related_name='variant_prices'
    , on_delete=models.CASCADE)
    
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = ('product_variant', 'unit_of_measurement')

    def __str__(self):
        return f"{self.product_variant.name} - {self.unit_of_measurement.unit} - {self.price}"
