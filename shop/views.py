from django.shortcuts import render, get_object_or_404
from .models import Category, OilType, Viscosity, Compound, Fuel

# Create your views here.
def show_categories(request):
    categories = Category.objects.all()
    data = {
        'categories': categories,
    }
    return render(request, 'shop/categories.html', data)

def show_category_assortment(request, category_slug = None, oiltype_slug = None, viscosity_slug = None,
                             compound_slug = None, fuel_slug = None):
    category = None
    oil_type = None
    visc = None
    comp = None
    fuel = None
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
    if oiltype_slug:
        oil_type = get_object_or_404(OilType, slug = oiltype_slug)
    if viscosity_slug:
        visc = get_object_or_404(Viscosity, slug = viscosity_slug)
    if compound_slug:
        comp = get_object_or_404(Compound, slug = compound_slug)
    if fuel_slug:
        fuel = get_object_or_404(Fuel, slug = fuel_slug)

    data = {
        'category': category,
        'oil_type': oil_type,
        'visc': visc,
        'comp': comp,
        'fuel': fuel,
    }
    return render(request, f'shop/product_list.html', data)
