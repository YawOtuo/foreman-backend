from django.core.management.base import BaseCommand
from core.models import Area, DeliveryFee

class Command(BaseCommand):
    help = 'Create or update delivery fees for all areas to 50'

    def handle(self, *args, **kwargs):
        areas = Area.objects.all()  # Get all areas
        for area in areas:
            delivery_fee, created = DeliveryFee.objects.get_or_create(
                location=area,
                defaults={'fee': 50}
            )
            
            if not created:
                delivery_fee.amount = 50
                delivery_fee.save()
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created delivery fee for {area.name} with amount 50.'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Updated delivery fee for {area.name} to 50.'))
