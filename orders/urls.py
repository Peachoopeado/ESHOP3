from django.urls import path, include
from . import views
urlpatterns = [
    path('create', views.order_create, name='order-create'),
    path('created', views.order_create, name='order-created'),

]

