# Generated by Django 3.2.12 on 2022-03-10 06:52

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import meta.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publications', '0001_initial'),
        ('mapping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('site_name', models.CharField(help_text='The name given to the site.', max_length=200, null=True, verbose_name='site name')),
                ('latitude', models.FloatField(db_index=True, help_text='Latitude in decimal degrees', validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='latitude')),
                ('longitude', models.FloatField(db_index=True, help_text='Longitude in decimal degrees', validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)], verbose_name='longitude')),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, srid=4326)),
                ('elevation', models.FloatField(blank=True, help_text='Site elevation', null=True, verbose_name='elevation')),
                ('well_depth', models.FloatField(blank=True, help_text='Total depth of the hole in metres.', null=True, validators=[django.core.validators.MaxValueValidator(12500), django.core.validators.MinValueValidator(0)], verbose_name='well depth')),
                ('cruise', models.CharField(blank=True, help_text='For oceanic measurements - the name of the cruise on which the measurements were taken.', max_length=150, null=True, verbose_name='name of cruise')),
                ('seafloor_age', models.FloatField(blank=True, help_text='Age of the sea floor', null=True, validators=[django.core.validators.MaxValueValidator(220), django.core.validators.MinValueValidator(0)], verbose_name='sea floor age')),
                ('sediment_thickness', models.FloatField(blank=True, help_text='Sediment thickness at the site.', null=True, verbose_name='calculated sediment thickness')),
                ('sediment_thickness_type', models.CharField(blank=True, help_text='How sediment thickness was determined.', max_length=250, null=True, verbose_name='type of sediment thickness')),
                ('seamount_distance', models.FloatField(blank=True, help_text='Distance in Km to the nearest seamount.', null=True, verbose_name='distance to seamount')),
                ('outcrop_distance', models.FloatField(blank=True, help_text='Distance in Km to the nearest outcrop.', null=True, verbose_name='distance to outcrop')),
                ('crustal_thickness', models.FloatField(blank=True, help_text='Calculated crustal thickness at the site.', null=True, verbose_name='calculated crustal thickness')),
                ('bottom_water_temp', models.FloatField(blank=True, help_text='Temperature at the bottom of the water column.', null=True, verbose_name='bottom_water_temperature')),
                ('year_drilled', models.IntegerField(blank=True, null=True, verbose_name='year drilled')),
                ('description', models.TextField(blank=True, null=True, verbose_name='site description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['site_name', 'latitude', 'longitude'])),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added to ThermoGlobe')),
                ('continent', models.ForeignKey(blank=True, help_text='Continent land boundaries', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to='mapping.continent', verbose_name='continent')),
                ('country', models.ForeignKey(blank=True, help_text='Country land boundaries', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to='mapping.country', verbose_name='country')),
                ('ocean', models.ForeignKey(blank=True, help_text='Global oceans and seas', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to='mapping.ocean', verbose_name='ocean')),
                ('plate', models.ForeignKey(blank=True, help_text='tectonic plate', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to='mapping.plate', verbose_name='plate')),
                ('political', models.ForeignKey(blank=True, help_text='Countries inclusive of exclusive marine economic zones', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to='mapping.political', verbose_name='political region')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to='mapping.province', verbose_name='geological province')),
                ('reference', models.ManyToManyField(blank=True, help_text='The reference or publication from which the data were sourced. Each site may have multiple references.', related_name='sites', to='publications.Publication', verbose_name='references')),
            ],
            options={
                'db_table': 'site',
                'ordering': ['-date_added'],
                'unique_together': {('site_name', 'latitude', 'longitude')},
            },
            bases=(meta.models.ModelMeta, models.Model),
        ),
        migrations.CreateModel(
            name='Interval',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reliability', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('R', 'R'), ('Z', 'Z')], help_text='Heat flow reliability code', max_length=1, null=True, verbose_name='reliability')),
                ('tilt', models.FloatField(blank=True, help_text='Angle between vertical and the orientation of the probe.', null=True, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(0)], verbose_name='probe tilt')),
                ('depth_min', models.FloatField(blank=True, help_text='Minimum depth of the measurement interval.', null=True, validators=[django.core.validators.MaxValueValidator(12500, 'Maximum depth may not exceed 12,500m.'), django.core.validators.MinValueValidator(0, 'Depth cannot be less than 0m.')], verbose_name='depth min')),
                ('depth_max', models.FloatField(blank=True, help_text='Maximum depth of the measurement interval.', null=True, validators=[django.core.validators.MaxValueValidator(12500, 'Maximum depth may not exceed 12,500m.'), django.core.validators.MinValueValidator(0, 'Depth cannot be less than 0m.')], verbose_name='depth max')),
                ('number_of_temperatures', models.IntegerField(blank=True, help_text='Number of temperatures used to determine the estimate.', null=True, verbose_name='number of temperatures')),
                ('temp_method', models.CharField(blank=True, help_text='The method used to obtain temperature values.', max_length=200, verbose_name='temperature method')),
                ('heat_flow_corrected', models.FloatField(blank=True, help_text='The corrected value.', null=True, verbose_name='corrected heat flow')),
                ('heat_flow_corrected_uncertainty', models.FloatField(blank=True, help_text='Uncertainty on the corrected value.', null=True, verbose_name='corrected uncertainty')),
                ('heat_flow_uncorrected', models.FloatField(blank=True, help_text='The uncorrected value.', null=True, verbose_name='uncorrected heat flow')),
                ('heat_flow_uncorrected_uncertainty', models.FloatField(blank=True, help_text='Uncertainty on the uncorrected value.', null=True, verbose_name='uncorrected uncertainty')),
                ('gradient_corrected', models.FloatField(blank=True, help_text='The corrected value.', null=True, verbose_name='corrected gradient')),
                ('gradient_corrected_uncertainty', models.FloatField(blank=True, help_text='Uncertainty on the corrected value.', null=True, verbose_name='corrected uncertainty')),
                ('gradient_uncorrected', models.FloatField(blank=True, help_text='The uncorrected value.', null=True, verbose_name='uncorrected gradient')),
                ('gradient_uncorrected_uncertainty', models.FloatField(blank=True, help_text='Uncertainty on the uncorrected value.', null=True, verbose_name='uncorrected uncertainty')),
                ('average_conductivity', models.FloatField(blank=True, help_text='Reported thermal conductivity to accompany the heat flow estimate.', null=True, verbose_name='therm. cond.')),
                ('conductivity_uncertainty', models.FloatField(blank=True, help_text='Uncertainty of the reported thermal conductivity.', null=True, verbose_name='thermal conductivity uncertainty')),
                ('number_of_conductivities', models.FloatField(blank=True, help_text='Number of thermal conductivities from which the reported thermal conductivity was derived.', null=True, verbose_name='number of conductivity measurements')),
                ('conductivity_method', models.CharField(blank=True, help_text='Method used to measure or derive thermal conductivity.', max_length=150, null=True, verbose_name='cond. method')),
                ('heat_production', models.FloatField(blank=True, help_text='Average heat production to accompany the heat flow estimate.', null=True, verbose_name='heat prod.')),
                ('heat_production_uncertainty', models.FloatField(blank=True, help_text='Uncertainty of the reported heat production.', null=True, verbose_name='heat production uncertainty')),
                ('number_of_heat_gen', models.FloatField(blank=True, help_text='Number of heat production values from which the average heat production was derived.', null=True, verbose_name='number of heat production measurements')),
                ('heat_production_method', models.CharField(blank=True, help_text='Method used to measure or derive heat production.', max_length=150, null=True, verbose_name='heat production method')),
                ('comment', models.TextField(blank=True, help_text='Information supplied with the measurement either by the original author/researcher or the compiler.', null=True, verbose_name='comment')),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
                ('global_flag', models.BooleanField(default=False, help_text='Measurement is suitable for use in global modelling.', null=True, verbose_name='global flag')),
                ('global_reason', models.CharField(blank=True, help_text='reason for denoting this measurement as suitable for global modelling', max_length=200, null=True, verbose_name='reason')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='added')),
                ('global_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='declared_global', to=settings.AUTH_USER_MODEL)),
                ('reference', models.ForeignKey(blank=True, help_text='The publication or other reference from which the measurement was reported.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intervals', to='publications.Publication', verbose_name='reference')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intervals', to='thermoglobe.site', verbose_name='site')),
            ],
            options={
                'db_table': 'interval',
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalSite',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('site_name', models.CharField(help_text='The name given to the site.', max_length=200, null=True, verbose_name='site name')),
                ('latitude', models.FloatField(db_index=True, help_text='Latitude in decimal degrees', validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='latitude')),
                ('longitude', models.FloatField(db_index=True, help_text='Longitude in decimal degrees', validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)], verbose_name='longitude')),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, srid=4326)),
                ('elevation', models.FloatField(blank=True, help_text='Site elevation', null=True, verbose_name='elevation')),
                ('well_depth', models.FloatField(blank=True, help_text='Total depth of the hole in metres.', null=True, validators=[django.core.validators.MaxValueValidator(12500), django.core.validators.MinValueValidator(0)], verbose_name='well depth')),
                ('cruise', models.CharField(blank=True, help_text='For oceanic measurements - the name of the cruise on which the measurements were taken.', max_length=150, null=True, verbose_name='name of cruise')),
                ('seafloor_age', models.FloatField(blank=True, help_text='Age of the sea floor', null=True, validators=[django.core.validators.MaxValueValidator(220), django.core.validators.MinValueValidator(0)], verbose_name='sea floor age')),
                ('sediment_thickness', models.FloatField(blank=True, help_text='Sediment thickness at the site.', null=True, verbose_name='calculated sediment thickness')),
                ('sediment_thickness_type', models.CharField(blank=True, help_text='How sediment thickness was determined.', max_length=250, null=True, verbose_name='type of sediment thickness')),
                ('seamount_distance', models.FloatField(blank=True, help_text='Distance in Km to the nearest seamount.', null=True, verbose_name='distance to seamount')),
                ('outcrop_distance', models.FloatField(blank=True, help_text='Distance in Km to the nearest outcrop.', null=True, verbose_name='distance to outcrop')),
                ('crustal_thickness', models.FloatField(blank=True, help_text='Calculated crustal thickness at the site.', null=True, verbose_name='calculated crustal thickness')),
                ('bottom_water_temp', models.FloatField(blank=True, help_text='Temperature at the bottom of the water column.', null=True, verbose_name='bottom_water_temperature')),
                ('year_drilled', models.IntegerField(blank=True, null=True, verbose_name='year drilled')),
                ('description', models.TextField(blank=True, null=True, verbose_name='site description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['site_name', 'latitude', 'longitude'])),
                ('date_added', models.DateTimeField(blank=True, editable=False, verbose_name='date added to ThermoGlobe')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('continent', models.ForeignKey(blank=True, db_constraint=False, help_text='Continent land boundaries', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mapping.continent', verbose_name='continent')),
                ('country', models.ForeignKey(blank=True, db_constraint=False, help_text='Country land boundaries', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mapping.country', verbose_name='country')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('ocean', models.ForeignKey(blank=True, db_constraint=False, help_text='Global oceans and seas', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mapping.ocean', verbose_name='ocean')),
                ('plate', models.ForeignKey(blank=True, db_constraint=False, help_text='tectonic plate', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mapping.plate', verbose_name='plate')),
                ('political', models.ForeignKey(blank=True, db_constraint=False, help_text='Countries inclusive of exclusive marine economic zones', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mapping.political', verbose_name='political region')),
                ('province', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mapping.province', verbose_name='geological province')),
            ],
            options={
                'verbose_name': 'historical site',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='Correction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CLIM', 'Climate'), ('TOPO', 'Topographic'), ('REFR', 'Refraction'), ('FLUI', 'Fluid'), ('BWV', 'Bottom Water Variation'), ('EROS', 'Erosion'), ('COMP', 'Compaction'), ('OTH', 'Other'), ('CMPS', 'composite'), ('TILT', 'tilt')], max_length=4, verbose_name='correction type')),
                ('value', models.FloatField(blank=True, null=True, verbose_name='value')),
                ('interval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='corrections', to='thermoglobe.interval', verbose_name='interval')),
            ],
            options={
                'db_table': 'heat_flow_correction',
            },
        ),
        migrations.CreateModel(
            name='Gradient',
            fields=[
            ],
            options={
                'verbose_name': 'thermal gradient',
                'verbose_name_plural': 'thermal gradients',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('thermoglobe.interval',),
        ),
        migrations.CreateModel(
            name='HeatFlow',
            fields=[
            ],
            options={
                'verbose_name': 'heat flow',
                'verbose_name_plural': 'heat flow',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('thermoglobe.interval',),
        ),
    ]
