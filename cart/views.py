from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from decimal import Decimal


# Create your views here.
@require_POST
def cart_add(request, product_code):
    cart = Cart(request)
    product = get_object_or_404(Product, code=product_code)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect(request.META.get('HTTP_REFERER'))

def cart_add_one(request, product_code):
    cart = Cart(request)
    product = get_object_or_404(Product, code=product_code)
    if product_code:
        cart.add_one(product)
    return redirect('cart-detail')
def cart_remove_one(request, product_code):
    cart = Cart(request)
    product = get_object_or_404(Product, code=product_code)
    if product_code:
        cart.delete_one(product)
    return redirect('cart-detail')


def cart_remove(request, product_code):
    cart = Cart(request)
    product = get_object_or_404(Product, code=product_code)
    if product.code:
        cart.remove(product)

    return redirect('cart-detail')

def cart_detail(request):
    cart = Cart(request)
    delivery_price = cart.get_delivery_price()
    if request.method == 'POST':
        delivery = request.POST.get('delivery', '')
        cart.set_delivery(delivery)
        delivery_price = cart.get_delivery_price()
    data = {
        'cart': cart,
        'delivery_choices': cart.get_delivery_choices(),
        'delivery_price': delivery_price,

    }
    return render(request, 'cart/detail.html', data)
