# Generated by Django 4.1.7 on 2023-03-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0035_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='security_pasport',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tech_desc',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
