# Generated by Django 4.1.7 on 2023-03-06 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='shop/img/partners')),
            ],
        ),
    ]
