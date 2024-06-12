from django.urls import path

from core.views.cart import CartAPI,  CartAPIIncrementDecrementDeleteView


urlpatterns = [
    # path('/', AddToCartAPI.as_view(), name='add_to_cart_api'),
    path("<int:cart_id>/", CartAPI.as_view(), name="cart_api"),
    path(
        "<int:cart_id>/products/<int:product_id>",
        CartAPIIncrementDecrementDeleteView.as_view(),
        name="cart_increment_decrement",
    ),

]
