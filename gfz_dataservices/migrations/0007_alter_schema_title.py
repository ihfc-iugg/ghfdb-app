# Generated by Django 3.2.15 on 2022-08-30 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gfz_dataservices', '0006_schema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schema',
            name='title',
            field=models.CharField(blank=True, default=' ', max_length=32),
            preserve_default=False,
        ),
    ]
