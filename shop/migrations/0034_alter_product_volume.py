# Generated by Django 4.1.7 on 2023-03-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0033_alter_product_fuel_alter_product_transmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
