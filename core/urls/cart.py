from django.urls import path

from core.views.cart import CartAPI, CartAPIDeleteView


urlpatterns = [
    # path('/', AddToCartAPI.as_view(), name='add_to_cart_api'),
    path('<int:user_id>/', CartAPI.as_view(), name='cart_api'),
    path('<int:user_id>/products/<int:product_id>', CartAPIDeleteView.as_view(), name='cart_api'),

]
