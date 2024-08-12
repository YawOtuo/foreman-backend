from django.contrib import admin
from core.models.user import User
from core.models.shippingaddress import ShippingAddress

class ShippingAddressInline(admin.StackedInline):
    model = ShippingAddress

class UserAdmin(admin.ModelAdmin):
    inlines = [ShippingAddressInline]
    search_fields = ['username', 'email']

admin.site.register(User, UserAdmin)
