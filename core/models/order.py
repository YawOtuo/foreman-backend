from django.db import models
from django.utils import timezone  # Add this import

from core.models.product import Product
from core.models.shippingaddress import ShippingAddress
from core.models.user import User

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Total cost of the order
    total_quantity = models.PositiveIntegerField(default=0)  # Total quantity of items in the order
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True, blank=True)  # Add shipping_address field
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    confirmed_at = models.DateTimeField(null=True, blank=True)
    shipped_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

    def update_status(self, new_status):
        self.status = new_status
        if new_status == 'confirmed':
            self.confirmed_at = timezone.now()
        elif new_status == 'shipped':
            self.shipped_at = timezone.now()
        elif new_status == 'delivered':
            self.delivered_at = timezone.now()
        self.save()
    # def update_totals(self):
    #     self.total_cost = sum(item.total_cost for item in self.items.all())
    #     self.total_quantity = sum(item.quantity for item in self.items.all())
    #     self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Total cost of this item

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    # def save(self, *args, **kwargs):
    #     self.total_cost = self.product.price * self.quantity
    #     super(OrderItem, self).save(*args, **kwargs)
    #     self.order.update_totals()  # Update order's total_cost and total_quantity after saving

    # def delete(self, *args, **kwargs):
    #     super(OrderItem, self).delete(*args, **kwargs)
    #     self.order.update_totals()  # Update order's total_cost and total_quantity after deletion
