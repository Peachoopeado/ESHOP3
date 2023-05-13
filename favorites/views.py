from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from shop.models import Product
from favorites.models import Favorite
from django.contrib import messages


# Create your views here.
@login_required
def add_to_favorites(request, product_code: str):
    product = get_object_or_404(Product, code=product_code)
    try:
        favorite = Favorite.objects.get(user=request.user)
        if product in favorite.products.all():
            messages.warning(request, 'Этот продукт уже добавлен в избранное.')
        else:
            favorite.products.add(product)
            product.is_favorite = True
            product.save()
            messages.success(request, 'Продукт был успешно добавлен в избранное')

    except Favorite.DoesNotExist:
        favorite = Favorite(user=request.user)
        favorite.save()
        favorite.products.add(product)
        product.is_favorite = True
        product.save()
        messages.success(request, 'Продукт был успешно добавлен в избранное')

    return redirect('product-detail', product_code=product_code)


@login_required
def show_favorites_list(request):
    favorites = Favorite.objects.get(user=request.user)
    data = {
        'favorites': favorites,
    }
    return render(request, 'favorites_list.html', data)
