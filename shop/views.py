from django.shortcuts import render, get_object_or_404
from .models import Category

# Create your views here.
def show_categories(request):
    categories = Category.objects.all()
    data = {
        'categories': categories,
    }
    return render(request, 'shop/categories.html', data)

def show_category_assortment(request, category_slug = None):
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)

    data = {
        'category': category,
    }
    return render(request, f'shop/product_list.html', data)
