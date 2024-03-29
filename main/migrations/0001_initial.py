# Generated by Django 4.2.1 on 2023-05-21 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quote', models.CharField(max_length=500)),
                ('short_video_link', models.CharField(max_length=500)),
                ('long_video_link', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='MainPartnerImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='main/img/partners')),
                ('partner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.mainpartner')),
            ],
        ),
    ]
