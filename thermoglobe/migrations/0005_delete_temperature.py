# Generated by Django 3.2.12 on 2022-03-08 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thermoglobe', '0004_remove_tempmeta_depth'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Temperature',
        ),
    ]
