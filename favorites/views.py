from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from shop.models import Product
from favorites.models import Favorite
from django.contrib import messages


# Create your views here.
@login_required
def add_to_favorites(request, product_code: str):
    product = Product.objects.get(code=product_code)
    try:
        favorite = Favorite.objects.get(user=request.user)
        favorite.products.add(product)
        messages.warning(request, 'Этот продукт уже добавлен в избранное.')
    except Favorite.DoesNotExist:
        favorite = Favorite(user=request.user)
        favorite.save()
        favorite.products.add(product)
        messages.success(request, 'Продукт был успешно добавлен в избранное')

    return redirect('product-detail', product_code=product_code)


@login_required
def show_favorites_list(request):
    favorites = Favorite.objects.get(user=request.user)
    data = {
        'favorites': favorites,
    }
    return render(request, 'favorites_list.html', data)
