# Generated by Django 3.2.15 on 2022-09-27 16:05

import core.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publications', '0001_initial'),
        ('well_logs', '0001_initial'),
        ('database', '0002_initial'),
        ('earth_science', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('data_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='well_logs.data')),
            ],
            options={
                'verbose_name': 'temperature',
                'verbose_name_plural': 'temperature data',
                'db_table': 'temperature',
            },
            bases=('well_logs.data',),
        ),
        migrations.CreateModel(
            name='TemperatureLog',
            fields=[
                ('log_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='temperature_logs', to='well_logs.log')),
                ('source', models.CharField(blank=True, help_text='Where the data came from', max_length=50, null=True, verbose_name='original source')),
                ('source_id', models.CharField(blank=True, help_text='ID from data source', max_length=64, null=True, verbose_name='original source ID')),
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='23456789ABCDEFGHJKLMNPQRSTUVWXYZ', length=8, max_length=13, prefix='GHFT-', primary_key=True, serialize=False)),
                ('method', models.CharField(blank=True, max_length=200, null=True, verbose_name='method')),
                ('circ_time', models.FloatField(blank=True, null=True, verbose_name='circulation time (hrs)')),
                ('lag_time', models.FloatField(blank=True, null=True, verbose_name='lag time (hrs)')),
                ('correction', models.CharField(blank=True, max_length=150, null=True, verbose_name='correction type')),
                ('reference', models.ForeignKey(blank=True, help_text='The publications or other reference from which the measurement was reported.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='temperature_logs', to='publications.publication', verbose_name='reference')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='temperature_logs', to='database.site', verbose_name='site')),
            ],
            options={
                'verbose_name': 'thermal log',
                'verbose_name_plural': 'thermal logs',
                'db_table': 'temp_meta',
                'ordering': ['added'],
                'default_related_name': 'temperature_logs',
            },
            bases=('well_logs.log', models.Model),
        ),
        migrations.CreateModel(
            name='ConductivityLog',
            fields=[
                ('log_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='conductivity_logs', to='well_logs.log')),
                ('method', models.CharField(blank=True, max_length=200, null=True, verbose_name='method')),
                ('source', models.CharField(blank=True, help_text='Where the data came from', max_length=50, null=True, verbose_name='original source')),
                ('source_id', models.CharField(blank=True, help_text='ID from data source', max_length=64, null=True, verbose_name='original source ID')),
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='23456789ABCDEFGHJKLMNPQRSTUVWXYZ', length=10, max_length=15, prefix='GHFLOG-TC', primary_key=True, serialize=False)),
                ('reference', models.ForeignKey(blank=True, help_text='The publications or other reference from which the measurement was reported.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conductivity_logs', to='publications.publication', verbose_name='reference')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conductivity_logs', to='database.site', verbose_name='site')),
            ],
            options={
                'verbose_name': 'conductivity log',
                'verbose_name_plural': 'conductivity logs',
                'db_table': 'thermal_conductivity_log',
                'default_related_name': 'conductivity_logs',
            },
            bases=('well_logs.log', models.Model),
        ),
        migrations.CreateModel(
            name='Conductivity',
            fields=[
                ('data_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='well_logs.data')),
                ('sample_type', models.CharField(choices=[('outcrop samples', 'Outcrop samples'), ('core samples', 'Core samples'), ('cutting samples', 'Cutting samples'), ('mineral computation', 'Mineral computation'), ('well log interpretation', 'Well log interpretation'), ('core-log integration', 'Core-log integration'), ('in-situ probe', 'In-situ probe'), ('other', 'Other (specify in comments field)'), ('unspecified', 'Unspecified')], help_text='Type of sample used to determine conductivity', max_length=23, verbose_name='sample_type')),
                ('method', models.CharField(blank=True, help_text='Method used to determine the mean thermal conductivity over the given interval', max_length=100, null=True, verbose_name='thermal conductivity method')),
                ('saturation_state', models.CharField(help_text='Saturation state of the sample', max_length=100, verbose_name='thermal conductivity saturation')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='sample name/ID')),
                ('length', models.FloatField(blank=True, null=True, verbose_name='length (cm)')),
                ('width', models.FloatField(blank=True, null=True, verbose_name='width (cm)')),
                ('diameter', models.FloatField(blank=True, null=True, verbose_name='diameter (cm)')),
                ('thickness', models.FloatField(blank=True, null=True, verbose_name='thickness (cm)')),
                ('orientation', core.fields.RangeField(blank=True, help_text='Angle relative to the foliation/bedding where 0 is parallel and 90 is perpendicular', null=True, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(0)], verbose_name='orientation')),
                ('IGSN', models.CharField(help_text='International Geo Sample Numbers (IGSN, semicolon separated) for rock samples used for laboratory measurements of thermal conductivity', max_length=100, verbose_name='IGSN sample number')),
                ('lithology', models.OneToOneField(blank=True, help_text='BGS rock classification.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='earth_science.earthmaterial', verbose_name='lithology')),
            ],
            options={
                'db_table': 'thermal_conductivity',
                'ordering': ['depth'],
            },
            bases=('well_logs.data',),
        ),
    ]
