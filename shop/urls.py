from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.show_categories),
    path('<str:category_slug>', views.show_category_assortment, name='assortment-by-category'),
    path('<str:category_slug>/<str:oiltype_slug>', views.show_category_assortment, name='assortment-by-category-oiltype'),
    path('<str:category_slug>/<str:oiltype_slug>/<str:viscosity_slug>', views.show_category_assortment, name='assortment-by-category-oiltype-viscosity'),
    path('<str:category_slug>/<str:oiltype_slug>/<str:viscosity_slug>/<str:compound_slug>', views.show_category_assortment, name='assortment-by-category-oiltype-viscosity-compound'),
    path('<str:category_slug>/<str:oiltype_slug>/<str:viscosity_slug>/<str:compound_slug>/<str:fuel_slug>', views.show_category_assortment, name='assortment-by-category-oiltype-viscosity-compound-fuel'),
]