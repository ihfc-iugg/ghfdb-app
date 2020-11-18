# Generated by Django 3.1.1 on 2020-09-25 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0002_province'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='area_km2',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='comments',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='conjugate_province',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='continent',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='group',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='juvenile_age_max',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='juvenile_age_min',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='juvenile_age_ref',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='last_orogen',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='plate',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='reference',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='tectonic_age_max',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='tectonic_age_min',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='tectonic_age_ref',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='type',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
