# Generated by Django 4.2.7 on 2023-11-09 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HardwareComponents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('product_model', models.CharField(max_length=32)),
                ('product_type', models.CharField(max_length=32)),
                ('price', models.IntegerField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='IoTDevices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('product_model', models.CharField(max_length=32)),
                ('product_type', models.CharField(max_length=32)),
                ('price', models.IntegerField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='NetworkDevices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('product_model', models.CharField(max_length=32)),
                ('product_type', models.CharField(max_length=32)),
                ('price', models.IntegerField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
