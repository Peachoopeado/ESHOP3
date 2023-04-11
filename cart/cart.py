from decimal import Decimal
from django.conf import settings
from shop.models import Product
from django.http import JsonResponse


class Cart(object):
    def get_delivery_choices(self):
        return [
            ('delivery', 'Доставка (+600 руб.)'),
            ('pickup', 'Самовывоз')
        ]

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
        self.delivery = 'delivery'

    def add(self, product, quantity=1, update_quantity=False):
        """

        Добавить продукт в коризну или обновить его количество
        """

        product_code = str(product.code)
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
    def add_one(self, product):
        """
        Добавление одной единицы товара
        """
        product_code = str(product.code)
        if product_code in self.cart:
            if self.cart[product_code]['quantity'] > 0:
                self.cart[product_code]['quantity'] += 1
                self.save()
            else:
                self.add(product, quantity=1)
    def delete_one(self, product):
        """
        Удаление одной единицы товара из корзины
        """
        product_code = str(product.code)
        if product_code in self.cart:
            if self.cart[product_code]['quantity'] > 1:
                self.cart[product_code]['quantity'] -= 1
            else:
                del self.cart[product_code]
            self.save()
    def remove(self, product):
        """

        Удаление товара из корзины
        """
        product_code = str(product.code)
        if product_code in self.cart:
            del self.cart[product_code]
            self.save()

    def __iter__(self):
        """

        Перебор элементов в корзине и получение продуктов из базы данных
        """
        product_codes = self.cart.keys()
        # Получение объектов product и добавление их в корзину
        products = Product.objects.filter(code__in=product_codes)
        for product in products:
            self.cart[str(product.code)]['product'] = product

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

    def set_delivery(self, delivery):
        self.delivery = delivery
    def get_delivery(self):
        return self.delivery

    def get_delivery_price(self):
        if self.delivery == 'delivery':
            return Decimal('600.00')
        elif self.delivery == 'pickup':
            return Decimal('0.00')
        else:
            return Decimal('0.00')

    def get_total_price_with_delivery(self):
        delivery_price = self.get_delivery_price()
        total = self.get_total_price()
        return float(total + delivery_price)

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
