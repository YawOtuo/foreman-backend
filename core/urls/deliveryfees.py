# urls.py

from django.urls import path

from core.views.deliveryfees import DeliveryFeeByAreaAPI

urlpatterns = [
    path('area/<int:area_id>/', DeliveryFeeByAreaAPI.as_view(), name='delivery-list'),

]
