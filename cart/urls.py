from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.cart_detail, name='cart-detail'),
    path('add/<str:product_code>', views.cart_add, name='cart-add'),
    path('remove/<str:product_code>', views.cart_remove, name='cart-remove'),
]
