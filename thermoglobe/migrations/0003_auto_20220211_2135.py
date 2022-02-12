# Generated by Django 3.2.12 on 2022-02-11 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0006_plate'),
        ('thermoglobe', '0002_auto_20220211_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsite',
            name='plate',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='tectonic plate', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mapping.plate', verbose_name='plate'),
        ),
        migrations.AddField(
            model_name='site',
            name='plate',
            field=models.ForeignKey(blank=True, help_text='tectonic plate', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to='mapping.plate', verbose_name='plate'),
        ),
    ]
