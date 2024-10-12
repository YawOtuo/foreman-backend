# urls.py

from django.urls import path

from core.views.location import ConstituenciesWithAreasAPI

urlpatterns = [
    path('', ConstituenciesWithAreasAPI.as_view(), name='locations-list'),

]
