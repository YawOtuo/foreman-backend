# Admin for Constituency

from django.contrib import admin
from core.models import Constituency, Area, DeliveryFee
@admin.register(Constituency)
class ConstituencyAdmin(admin.ModelAdmin):
    list_display = ['name']  # Display name field in the list view
    search_fields = ['name']  # Enable search by constituency name

# Admin for Area
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'constituency']  # Show area name and related constituency
    search_fields = ['name', 'constituency__name']  # Search by area name or constituency name
    list_filter = ['constituency']  # Filter by constituency