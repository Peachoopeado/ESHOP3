# Generated by Django 4.1.7 on 2023-06-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0041_alter_product_compound_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='related_products',
            field=models.ManyToManyField(blank=True, to='shop.product'),
        ),
    ]