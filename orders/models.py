from django.db import models
from shop.models import Product
from django.contrib.auth.models import User


# Create your models here.

STATUS_CHOICES = (
        ('new', 'Новый'),
        ('processing', 'В обработке'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменен'),
)
class Order(models.Model):
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='new')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    type = models.CharField('Тип клиента', max_length=200, null=True)
    full_name = models.CharField('Ф.И.О.', max_length=200, null=True)
    phone = models.CharField('Телефон', max_length=200, null=True)
    email = models.EmailField('Email', null=True)
    address = models.CharField('Адрес', max_length=250)
    postal_code = models.CharField('Почтовый индекс', max_length=20)
    way_to_get = models.CharField('Способ получения', max_length=200, null=True, blank=True)
    comment = models.TextField('Комментарий', null=True, blank=True)
    # items = models.ManyToManyField(Product)
    created = models.DateTimeField('Создано',auto_now_add=True)
    updated = models.DateTimeField('Обновлено', auto_now=True)
    paid = models.BooleanField('Оплачено', default=False)
    manager_status = models.BooleanField('Рассмотрено', default=False, blank=False)
    total_cost = models.DecimalField('Итоговая стоимость', max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return 'Заказ {}'.format(self.id)
    
    def save(self, *args, **kwargs):
        self.total_cost = self.get_total_cost()
        super().save(*args, **kwargs)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Кол-во', default=1)

    

    def __str__(self):
        return '{}'.format(self.id)


    def get_cost(self):
        return self.price * self.quantity
    
    
