# urls.py
from django.urls import path

from core.views.email import send_general_email

urlpatterns = [
    path('general-email', send_general_email, name='send_general_email'),
]
