# Generated by Django 3.2.15 on 2022-08-15 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('earth_materials', '0003_auto_20220815_1143'),
        ('well_logs', '0004_auto_20220805_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductivity',
            name='lithology',
            field=models.OneToOneField(blank=True, help_text='BGS rock classification.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='earth_materials.earthmaterial', verbose_name='lithology'),
        ),
    ]
