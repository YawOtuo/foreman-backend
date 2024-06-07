# from django.db import models
# from core.models.user import User
# from core.models.product import Product

# class Order(models.Model):
#     PENDING = 'pending'
#     COMPLETED = 'completed'

#     STATUS_CHOICES = [
#         (PENDING, 'Pending'),
#         (COMPLETED, 'Completed'),
#     ]

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     items = models.ManyToManyField(Product, through='OrderItem')
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Order #{self.id} - {self.user.username}'