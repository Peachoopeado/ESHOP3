from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from shop.models import Product
from favorites.favorites import Favorites
from cart.cart import Cart
from orders import models


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    favorite_products = Product.objects.filter(favorite__user=request.user)
    orders = models.Order.objects.filter(user=request.user)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            
            form.save()
    else:
        form = UserChangeForm(instance=request.user)
    data = {
        'favorite_products': favorite_products,
        'orders': orders,
        'form': form,
        'user': request.user,
        'section': 'dashboard',
    }
    return render(request, 'account/dashboard.html', data)


@login_required
def delete_favorite(request, product_code: str):
    favorite_product = Favorites(request)
    product = get_object_or_404(Product, code=product_code)
    if product_code:
        favorite_product.remove(product)
    return redirect('dashboard')


def add_fav_to_cart(request, product_code: str):
    cart = Cart(request)
    product = get_object_or_404(Product, code=product_code)
    if product_code:
        cart.add(product)
    return redirect('dashboard')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def order_detail(request, order_id: int):
    order = get_object_or_404(models.Order, id=order_id)
    if order.user != request.user:
        return redirect('login')
    data = {
        'order': order,
    }
    return render(request, 'orders/order/order_detail.html', data)
