from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Category, OilType, Viscosity, Compound, Fuel, Product

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
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category = category, available=True)
    if oiltype_slug:
        oil_type = get_object_or_404(OilType, slug = oiltype_slug)
        products = Product.objects.filter(category=category, oiltype = oil_type, available=True)
    if viscosity_slug:
        visc = get_object_or_404(Viscosity, slug = viscosity_slug)
        products = Product.objects.filter(category=category, oiltype=oil_type, viscosity = visc, available=True )
    if compound_slug:
        comp = get_object_or_404(Compound, slug = compound_slug)
        products = Product.objects.filter(category=category, oiltype=oil_type, viscosity=visc, compound = comp, available=True)
    if fuel_slug:
        fuel = get_object_or_404(Fuel, slug = fuel_slug)
        products = Product.objects.filter(category=category, oiltype=oil_type, viscosity=visc, compound = comp, fuel = fuel, available=True)

    data = {
        'category': category,
        'oil_type': oil_type,
        'visc': visc,
        'comp': comp,
        'fuel': fuel,
        'products': products,
    }
    return render(request, f'shop/product_list.html', data)

def show_product_detail(request, product_code:str):
    product = get_object_or_404(Product, code = product_code)
    data = {
        'product': product,
    }

    return render(request, 'shop/product_detail.html', data)

