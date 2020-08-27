# Generated by Django 3.0.8 on 2020-08-25 06:21

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basin',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100, null=True)),
                ('max_fill', models.FloatField()),
                ('exploration_status', models.CharField(max_length=25)),
                ('location', models.CharField(max_length=50)),
                ('sub_regime_group', models.CharField(max_length=100, null=True)),
                ('sub_regime', models.CharField(max_length=100, null=True)),
                ('petsys_status', models.CharField(max_length=50, null=True)),
                ('poly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=3857)),
            ],
            options={
                'db_table': 'CGG_basin',
            },
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.BigIntegerField()),
                ('name', models.CharField(max_length=13)),
                ('sqmi', models.FloatField()),
                ('sqkm', models.FloatField()),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('poly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fips', models.CharField(max_length=2, null=True)),
                ('iso2', models.CharField(max_length=2)),
                ('iso3', models.CharField(max_length=3)),
                ('un', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('area', models.IntegerField()),
                ('pop2005', models.BigIntegerField()),
                ('region', models.IntegerField(choices=[(2, 'Africa'), (19, 'Americas'), (142, 'Asia'), (150, 'Europe'), (9, 'Oceania')])),
                ('subregion', models.IntegerField(choices=[(14, 'Eastern Africa'), (17, 'Middle Africa'), (15, 'Northern Africa'), (18, 'Southern Africa'), (11, 'Western Africa'), (29, 'Caribbean'), (13, 'Central America'), (5, 'South America'), (21, 'Northern America'), (143, 'Central Asia'), (30, 'Eastern Asia'), (34, 'Southern Asia'), (35, 'South-Eastern Asia'), (145, 'Western Asia'), (151, 'Eastern Europe'), (154, 'Northern Europe'), (39, 'Southern Europe'), (155, 'Western Europe'), (53, 'Australia and New Zealand'), (54, 'Melanesia'), (57, 'Micronesia'), (61, 'Polynesia')])),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('poly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'countries',
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='Margin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('area', models.FloatField()),
                ('perimetre', models.FloatField()),
                ('superficie', models.FloatField()),
                ('poly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Political',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('territory', models.CharField(max_length=254)),
                ('iso_territory', models.CharField(blank=True, max_length=254, null=True)),
                ('un_territory', models.BigIntegerField(blank=True, null=True)),
                ('sovereign', models.CharField(max_length=254)),
                ('iso_sovereign', models.CharField(blank=True, max_length=254, null=True)),
                ('un_sovereign', models.BigIntegerField(blank=True, null=True)),
                ('area_km2', models.BigIntegerField(blank=True, null=True)),
                ('poly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Sea',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('min_x', models.FloatField()),
                ('min_y', models.FloatField()),
                ('max_x', models.FloatField()),
                ('max_y', models.FloatField()),
                ('area', models.BigIntegerField()),
                ('mrgid', models.BigIntegerField()),
                ('poly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'db_table': 'sea',
                'ordering': ['name'],
            },
        ),
    ]
