from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.apps import apps

ProductVariant = apps.get_model('core', 'ProductVariant')

@receiver(post_save, sender=ProductVariant)
@receiver(post_delete, sender=ProductVariant)
def update_product_price(sender, instance, **kwargs):
    instance.product.update_price()
