from django.urls import path, include
from . import views
urlpatterns = [
    path('category', views.show_categories),
    path('category/<str:category_slug>', views.show_category_assortment, name='assortment-by-category'),
    path('category/<str:category_slug>/<str:oiltype_slug>', views.show_category_assortment, name='assortment-by-category-oiltype'),
    path('category/<str:category_slug>/<str:oiltype_slug>/<str:viscosity_slug>', views.show_category_assortment, name='assortment-by-category-oiltype-viscosity'),
    path('category/<str:category_slug>/<str:oiltype_slug>/<str:viscosity_slug>/<str:compound_slug>', views.show_category_assortment, name='assortment-by-category-oiltype-viscosity-compound'),
    path('category/<str:category_slug>/<str:oiltype_slug>/<str:viscosity_slug>/<str:compound_slug>/<str:fuel_slug>', views.show_category_assortment, name='assortment-by-category-oiltype-viscosity-compound-fuel'),

    path('product/<str:product_code>', views.show_product_detail, name='product-detail')
]