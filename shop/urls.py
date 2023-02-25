from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.show_categories),
    path('<str:category_slug>', views.show_category_assortment, name='assortment-by-category'),

]