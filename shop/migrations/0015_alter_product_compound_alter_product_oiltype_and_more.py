# Generated by Django 4.1.7 on 2023-02-25 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_product_vendor_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='compound',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.compound'),
        ),
        migrations.AlterField(
            model_name='product',
            name='oiltype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.oiltype'),
        ),
        migrations.AlterField(
            model_name='product',
            name='viscosity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.viscosity'),
        ),
    ]