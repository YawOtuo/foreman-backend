# urls.py

from django.urls import path

from core.views.favourite import FavoriteAPI

urlpatterns = [
    path('users/<int:user_id>/', FavoriteAPI.as_view(), name='favorite-list'),
    # path('products/<int:product_id>/users/<int:user_id>', FavoriteDetail.as_view(), name='favorite-detail'),
    # other URL patterns
]
