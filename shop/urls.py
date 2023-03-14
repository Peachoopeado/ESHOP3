from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.show_categories, name='assortment'),
    path('assortment/<str:category_slug>', views.show_category_assortment, name='assortment-by-category'),
    path('assortment/<str:category_slug>/<str:oiltype_slug>', views.show_category_assortment, name='assortment-by-category-oiltype'),
    path('assortment/<str:category_slug>/<str:oiltype_slug>/<str:viscosity_slug>', views.show_category_assortment, name='assortment-by-category-oiltype-viscosity'),
    path('assortment/<str:category_slug>/<str:oiltype_slug>/<str:viscosity_slug>/<str:compound_slug>', views.show_category_assortment, name='assortment-by-category-oiltype-viscosity-compound'),
    path('assortment/<str:category_slug>/<str:oiltype_slug>/<str:viscosity_slug>/<str:compound_slug>/<str:fuel_slug>', views.show_category_assortment, name='assortment-by-category-oiltype-viscosity-compound-fuel'),
    path('assortment/<str:category_slug>/<str:oiltype_slug>/<str:viscosity_slug>/<str:compound_slug>/<str:fuel_slug>/<str:transmission_slug>',
         views.show_category_assortment, name='assortment-by-category-oiltype-viscosity-compound-fuel-transmission'),

    path('product/<str:product_code>', views.show_product_detail, name='product-detail'),
    path('search/', views.Search.as_view(), name='search'),
    path('search/<int:page>', views.Search.as_view(), name='search-page'),
    path('contact/', views.show_contact_page, name='contacts'),
    path('about/', views.show_about_page, name='about'),
    path('partners/', views.show_partners, name='partners'),
    path('partners/<int:partner_id>', views.show_one_partner, name='one-partner')

]