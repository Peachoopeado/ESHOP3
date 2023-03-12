from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, OilType, Viscosity, Compound, Fuel, Transmission, Product, Partner, PartnerImage
from cart.forms import CartAddProductForm
from django.views.generic import ListView
from .forms import User_RequestForm
from django.db.models import Q


# Create your views here.
def show_categories(request):
    categories = Category.objects.all()
    data = {
        'categories': categories,
    }
    return render(request, 'shop/categories.html', data)


def show_category_assortment(request, category_slug=None, oiltype_slug=None, viscosity_slug=None,
                             compound_slug=None, fuel_slug=None, transmission_slug=None):
    category = None
    oil_type = None
    visc = None
    comp = None
    fuel = None
    transmission = None
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, available=True)
    if oiltype_slug:
        oil_type = get_object_or_404(OilType, slug=oiltype_slug)
        products = Product.objects.filter(category=category, oiltype=oil_type, available=True)
    if viscosity_slug:
        visc = get_object_or_404(Viscosity, slug=viscosity_slug)
        products = Product.objects.filter(category=category, oiltype=oil_type, viscosity=visc, available=True)
    if compound_slug:
        comp = get_object_or_404(Compound, slug=compound_slug)
        products = Product.objects.filter(category=category, oiltype=oil_type, viscosity=visc, compound=comp,
                                          available=True)
    if fuel_slug:
        fuel = get_object_or_404(Fuel, slug=fuel_slug)
        products = Product.objects.filter(category=category, oiltype=oil_type, viscosity=visc, compound=comp, fuel=fuel,
                                          available=True)
    if transmission_slug:
        transmission = get_object_or_404(Transmission, slug=transmission_slug)
        products = Product.objects.filter(category=category, oiltype=oil_type, viscosity=visc, compound=comp, fuel=fuel,
                                          transmission=transmission,
                                          available=True)

    data = {
        'category': category,
        'oil_type': oil_type,
        'visc': visc,
        'comp': comp,
        'fuel': fuel,
        'transmission': transmission,
        'products': products,

    }
    return render(request, f'shop/product_list.html', data)


def show_product_detail(request, product_code: str):
    product = get_object_or_404(Product, code=product_code)
    cart_product_form = CartAddProductForm()
    data = {
        'product': product,
        'cart_product_form': cart_product_form
    }

    return render(request, 'shop/product_detail.html', data)


def show_contact_page(request):
    error = ''
    if request.method == 'POST':
        contact_form = User_RequestForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('contacts')
        else:
            error = 'Данные введены некорректно'
    contact_form = User_RequestForm()
    data = {
        'contact_form': contact_form
    }
    return render(request, 'shop/contact_us.html', data)


def show_about_page(request):
    return render(request, 'shop/about.html')


def show_partners(request):
    partners = Partner.objects.all()
    data = {
        'partners': partners,
    }
    return render(request, 'shop/partners.html', data)


def show_one_partner(request, partner_id: int):
    partner = get_object_or_404(Partner, id=partner_id)
    img = get_object_or_404(PartnerImage, id=partner_id)
    data = {
        'partner': partner,
        'partner_img': img,
    }
    return render(request, 'shop/one_partner.html', data)


class Search(ListView):
    model = Product
    template_name = 'shop/search_results.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            queryset = Product.objects.filter(
                Q(name__icontains = query)|Q(viscosity__name__icontains=query)
            )
        else:
            queryset = Product.objects.none()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context
