from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'Update product prices based on the lowest price of their variants'

    def handle(self, *args, **kwargs):
        Product = apps.get_model('core', 'Product')
        products = Product.objects.all()

        for product in products:
            product.update_price()
            self.stdout.write(self.style.SUCCESS(f'Successfully updated price for product {product.name}'))
