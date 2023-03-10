# Generated by Django 4.1.7 on 2023-02-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(db_index=True, default=0, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_m',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor_code',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True, unique=True),
        ),
    ]
