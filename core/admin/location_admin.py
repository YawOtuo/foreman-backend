from django.contrib import admin
from core.models import Constituency, Area, DeliveryFee

# Inline class for showing Areas in ConstituencyAdmin
class AreaInline(admin.TabularInline):  # You can also use StackedInline for a different style
    model = Area
    extra = 0  # Number of empty forms to display. Set to 0 to avoid showing extra empty forms.
    fields = ['name']  # Fields to display in the inline
    show_change_link = True  # Adds a link to the edit page for the related Area

# Admin for Constituency
@admin.register(Constituency)
class ConstituencyAdmin(admin.ModelAdmin):
    list_display = ['name']  # Display name field in the list view
    search_fields = ['name']  # Enable search by constituency name
    inlines = [AreaInline]  # Add the inline to display related Areas in the ConstituencyAdmin

# Admin for Area
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'constituency']  # Show area name and related constituency
    search_fields = ['name', 'constituency__name']  # Search by area name or constituency name
    list_filter = ['constituency']  # Filter by constituency
