# Generated by Django 4.1.7 on 2023-02-25 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_vehicletype'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicletype',
            name='category',
            field=models.ManyToManyField(to='shop.category'),
        ),
    ]
