from django.urls import include, path
from django.conf import settings
from core.views import home

urlpatterns = [
    path("products/", include("core.urls.products")),
    path("", home.home),
]
