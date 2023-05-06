from django.conf import settings
from .models import Favorite, Product


class Favorites:
    def __init__(self, request):
        self.session = request.session
        self.user = request.user
        favorites = self.session.get(settings.FAVORITES_SESSION_ID)
        if not favorites:
            favorites = self.session[settings.FAVORITES_SESSION_ID] = []
        self.favorites = favorites

    def add(self, product):
        if self.user.is_authentificated:
            favorites, created = Favorite.objects.get_or_create(user=self.user)
            favorites.products.add(product)
        else:
            product_code = str(product.code)
            if product_code not in self.favorites:
                self.favorites.append(product_code)
                self.save()

    def remove(self, product):
        if self.user.is_authenticated:
            favorites = Favorite.objects.get(user=self.user)
            favorites.products.remove(product)
        else:
            product_code = str(product.code)
            if product_code in self.favorites:
                self.favorites.remove(product_code)
                self.save()

    def save(self):
        self.session[settings.FAVORITES_SESSION_ID] = self.favorites
