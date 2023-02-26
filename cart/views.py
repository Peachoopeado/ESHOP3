from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


# Create your views here.
@require_POST
def cart_add(request, product_code):
    cart = Cart(request)
    product = get_object_or_404(Product, code=product_code)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product = product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, product_code):
    cart = Cart(request)
    product = get_object_or_404(Product, code=product_code)
    cart.remove(product)
    return redirect('cart-detail')


def cart_detail(request):
    cart = Cart(request)
    data = {
        'cart': cart,
    }
    return render(request, 'cart/detail.html', data)
