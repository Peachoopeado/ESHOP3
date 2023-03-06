from django.db import models
from shop.models import Product

# Create your models here.
class Order(models.Model):
    type = models.CharField(max_length=200, null=True)
    full_name = models.CharField('Ф.И.О.',max_length=200, null=True)
    phone = models.CharField('Телефон',max_length=200, null=True)
    email = models.EmailField('Email',null=True)
    address = models.CharField('Адрес', max_length=250)
    postal_code = models.CharField('Почтовый индекс',max_length=20)
    way_to_get = models.CharField(max_length=200, null=True)
    # items = models.ManyToManyField(Product)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return 'Заказ {}'.format(self.id)
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)
    def get_cost(self):
        return self.price * self.quantity

