# Generated by Django 4.1.7 on 2023-03-06 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_partnerimage_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='describtion',
            field=models.TextField(null=True),
        ),
    ]
