from django.urls import path
from .views import Store, Cart, Checkout
urlpatterns = [
    path('', Store, name = 'Store'),
    path('cart/', Cart, name = 'Cart'),
    path('checkout/', Checkout, name = 'Checkout'),
]