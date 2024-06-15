# urls.py

from django.urls import path

from core.views.categories import CategoryAPI
from core.views.favourite import FavoriteAPI

urlpatterns = [
    path('', CategoryAPI.as_view(), name='favorite-list'),
    # path('products/<int:product_id>/users/<int:user_id>', FavoriteDetail.as_view(), name='favorite-detail'),
    # other URL patterns
]
