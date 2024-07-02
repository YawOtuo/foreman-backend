from django.db import models
from django.db.models import Q

from core.models.category import Category

class ProductManager(models.Manager):
    def search(self, **kwargs):
        queryset = self.get_queryset()
        search_query = kwargs.pop('search', None)
        query_objects = Q()

        # Apply initial search_query filter for name or category__name
        if search_query:
            query_objects = Q(name__icontains=search_query) | Q(category__name__icontains=search_query)

        ordering_fields = None

        # Process remaining filters in kwargs
        for field, value in kwargs.items():
            if value:
                if field == "ordering":
                    ordering_fields = value.split(",")
                elif field == "category__name" and value.lower() == "all":
                    # Skip adding category filter if "All" is selected
                    continue
                else:
                    query_objects &= Q(**{f"{field}__icontains": value})

        if query_objects:
            queryset = queryset.filter(query_objects).distinct()

        if ordering_fields:
            queryset = queryset.order_by(*ordering_fields)

        return queryset


class Product(models.Model):

    
    AVAILABILITY_CHOICES = [
        ("available", 'Available'),
        ("unavailable", 'Unavailable'),
        ("pending", 'Pending'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    availability = models.CharField(
        max_length=50, 
        choices=AVAILABILITY_CHOICES, 
        default="available",
        blank=True
    )

    min_order_quantity = models.IntegerField(blank=True, null=True)

    min_order_value = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductManager()

    def __str__(self):
        return self.name
