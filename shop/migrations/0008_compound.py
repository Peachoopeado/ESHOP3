# Generated by Django 4.1.7 on 2023-02-25 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_viscosity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('category', models.ManyToManyField(to='shop.category')),
                ('oiltype', models.ManyToManyField(to='shop.oiltype')),
                ('viscosity', models.ManyToManyField(to='shop.viscosity')),
            ],
        ),
    ]
