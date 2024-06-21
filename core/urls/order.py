# urls.py
from django.urls import path

from core.views.order import OrderDetailAPI, OrderListAPI

urlpatterns = [
    path('users/<int:user_id>/', OrderListAPI.as_view(), name='order_create'),
    path('<int:order_id>/users/<int:user_id>/', OrderDetailAPI.as_view(), name='add_order_items'),
]