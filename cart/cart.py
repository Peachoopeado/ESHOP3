from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):
    def __init__(self, request):

        """

        Инициализируем корзину

        """

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохранить пустую коризну в сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
            self.cart = cart
    def add(self, product, quantity = 1, update_quantity=False):
        """

        Добавить продукт в коризну или обновить его количество
        """

        product_code= str(product.code)
        if product_code not in self.cart:
            self.cart[product_code] = {'quantity': 0,
                                       'price': str(product.price)}
        if update_quantity:
            self.cart[product_code]['quantity'] = quantity
        else:
            self.cart[product_code]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        """

        удаление товара из корзины
        """
        product_code = str(product.code)
        if product_code in self.cart:
            del self.cart[product_code]
            self.save()
    def __iter__(self):
        """

        перебор элементов в корзине и получение продуктов из базы данных
        """
        product_codes = self.cart.keys()
        # Получение объектов product и добавление их в корзину
        products = Product.objects.filter(code__in=product_codes)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """

        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """

        подсчет стоимости товаров корзине
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True



