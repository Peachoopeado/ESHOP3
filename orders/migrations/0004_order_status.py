# Generated by Django 4.2.1 on 2023-05-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'Новый'), ('processing', 'В обработке'), ('shipped', 'Отправлен'), ('delivered', 'Доставлен'), ('cancelled', 'Отменен')], default='new', max_length=20, verbose_name='Статус'),
        ),
    ]