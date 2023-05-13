# Generated by Django 4.1.7 on 2023-02-25 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_fuel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('stock', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
                ('compound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.compound')),
                ('oiltype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.oiltype')),
                ('viscosity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.viscosity')),
            ],
        ),
    ]
