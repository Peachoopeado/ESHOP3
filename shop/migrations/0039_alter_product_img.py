# Generated by Django 4.1.7 on 2023-03-12 12:48

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0038_product_img_delete_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='shop/img/products'),
        ),
    ]