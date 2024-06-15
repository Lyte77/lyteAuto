from django.urls import path

from .views import (
    add_to_cart,
    remove_from_cart,
    cart_detail,
    update_cart
)

app_name = 'cart'

urlpatterns = [
    path('add_to_cart/<int:id>/', add_to_cart,name='add_to_cart'),
    path('remove/<int:id>/', remove_from_cart,name='remove_from_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('update_cart/<int:id>/', update_cart, name='update_cart')
]