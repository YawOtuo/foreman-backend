# from django.db import models
# from core.models.order import Order
# from core.models.user import User
# from core.models.product import Product



# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()

#     def __str__(self):
#         return f'{self.product.name} - {self.quantity}'

