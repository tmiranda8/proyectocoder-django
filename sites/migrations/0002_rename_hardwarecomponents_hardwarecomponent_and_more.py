# Generated by Django 4.2.6 on 2023-11-13 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HardwareComponents',
            new_name='HardwareComponent',
        ),
        migrations.RenameModel(
            old_name='IoTDevices',
            new_name='IoTDevice',
        ),
        migrations.RenameModel(
            old_name='NetworkDevices',
            new_name='NetworkDevice',
        ),
    ]