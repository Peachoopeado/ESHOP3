# Generated by Django 4.2.1 on 2023-05-15 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_comment_alter_order_way_to_get'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='manager_status',
            field=models.BooleanField(default=False, verbose_name='Рассмотрено'),
        ),
    ]
