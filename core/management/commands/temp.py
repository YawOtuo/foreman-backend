from django.core.management.base import BaseCommand
from core.models.productvariant import ProductVariant
from core.models.productvariantprice import ProductVariantPrice
from core.models.unit_of_measurement import UnitOfMeasurement

class Command(BaseCommand):
    help = 'Migrates prices from ProductVariant to ProductVariantPrice'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting the migration process...'))

        # Retrieve all product variants
        variants = ProductVariant.objects.all()
        for variant in variants:
            if variant.price is not None:
                # Determine the appropriate unit of measurement
                # Adjust logic here to select the unit; this is just an example
                unit = UnitOfMeasurement.objects.filter(
                    category=variant.product.category
                ).first()  # Replace with your logic for selecting the unit

                if unit:
                    # Create or update ProductVariantPrice
                    price, created = ProductVariantPrice.objects.get_or_create(
                        product_variant=variant,
                        unit_of_measurement=unit
                    )
                    price.price = variant.price
                    price.save()

                    self.stdout.write(f'Updated price for variant {variant.sku} with price {variant.price}')

                    # Optionally clear the price from the variant if desired
                    # variant.price = None
                    # variant.save()

        self.stdout.write(self.style.SUCCESS('Migration process completed.'))
