# Generated by Django 3.0.8 on 2020-08-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thermoglobe', '0005_auto_20200825_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='sediment_thickness_type',
            field=models.CharField(blank=True, help_text='How sediment thickness was determined.', max_length=250, null=True, verbose_name='type of sediment thickness'),
        ),
    ]
