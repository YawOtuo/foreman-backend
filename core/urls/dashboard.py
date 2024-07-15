# urls.py
from django.urls import path

from core.views.dashboard import dashboard_api

urlpatterns = [
    path('general-details/users/<int:user_id>/', dashboard_api, name='general_details'),
]
