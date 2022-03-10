# Generated by Django 3.2.12 on 2022-02-19 05:31

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import meta.models
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mapping', '0001_initial'),
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('site_name', models.CharField(help_text='The name given to the site.', max_length=200, null=True, verbose_name='site name')),
                ('latitude', models.FloatField(db_index=True, help_text='Latitude in decimal degrees. WGS84 preferred but not enforced.', validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='latitude')),
                ('longitude', models.FloatField(db_index=True, help_text='Longitude in decimal degrees. WGS84 preferred but not enforced.', validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)], verbose_name='longitude')),
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
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added to ThermoGlobe')),
                ('global_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='declared_global', to=settings.AUTH_USER_MODEL)),
                ('reference', models.ForeignKey(blank=True, help_text='The publication or other reference from which the measurement was reported.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intervals', to='publications.publication', verbose_name='reference')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intervals', to='thermoglobe.site', verbose_name='site')),
            ],
            options={
                'db_table': 'interval',
            },
        ),
        migrations.CreateModel(
            name='HistoricalSite',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('site_name', models.CharField(help_text='The name given to the site.', max_length=200, null=True, verbose_name='site name')),
                ('latitude', models.FloatField(db_index=True, help_text='Latitude in decimal degrees. WGS84 preferred but not enforced.', validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='latitude')),
                ('longitude', models.FloatField(db_index=True, help_text='Longitude in decimal degrees. WGS84 preferred but not enforced.', validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)], verbose_name='longitude')),
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
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Correction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('climate_flag', models.BooleanField(default=None, null=True, verbose_name='climate corrected')),
                ('climate', models.FloatField(blank=True, help_text='Value of a climatic correction applied to the associated heat flow and thermal gradient estimates.', null=True, verbose_name='value')),
                ('topographic_flag', models.BooleanField(default=None, null=True, verbose_name='topographic corrected')),
                ('topographic', models.FloatField(blank=True, help_text='Value of a topographic correction applied to the associated heat flow and thermal gradient estimates.', null=True, verbose_name='value')),
                ('refraction_flag', models.BooleanField(default=None, null=True, verbose_name='refraction corrected')),
                ('refraction', models.FloatField(blank=True, help_text='Value of a refraction correction applied to the associated heat flow and thermal gradient estimates.', null=True, verbose_name='value')),
                ('sed_erosion_flag', models.BooleanField(default=None, null=True, verbose_name='sedimentation corrected')),
                ('sed_erosion', models.FloatField(blank=True, help_text='Value of a sedimentation correction applied to the associated heat flow and thermal gradient estimates.', null=True, verbose_name='value')),
                ('fluid_flag', models.BooleanField(default=None, null=True, verbose_name='fluid corrected')),
                ('fluid', models.FloatField(blank=True, help_text='Value of a fluid correction applied to the associated heat flow and thermal gradient estimates.', null=True, verbose_name='value')),
                ('bwv_flag', models.BooleanField(default=None, null=True, verbose_name='BWV corrected')),
                ('bwv', models.FloatField(blank=True, help_text='Value of a bottom water variation correction applied to the associated heat flow and thermal gradient estimates.', null=True, verbose_name='value')),
                ('compaction_flag', models.BooleanField(default=None, null=True, verbose_name='compaction corrected')),
                ('compaction', models.FloatField(blank=True, help_text='Value of a compaction correction applied to the associated heat flow and thermal gradient estimates.', null=True, verbose_name='value')),
                ('other_flag', models.BooleanField(default=None, null=True, verbose_name='other')),
                ('other_type', models.CharField(blank=True, help_text='Specifies the type of correction if the type does not belong to one of the other categories.', max_length=100, null=True, verbose_name='type of correction')),
                ('other', models.FloatField(blank=True, help_text='Value of any other correction applied to the associated heat flow and thermal gradient estimates.', null=True, verbose_name='value')),
                ('heatflow', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='corrections', to='thermoglobe.interval')),
            ],
            options={
                'db_table': 'correction',
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
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('formation', models.CharField(blank=True, help_text='The name of the sampled geological formation.', max_length=200, verbose_name='formation name')),
                ('depth', models.FloatField(blank=True, help_text='The depth at which the measurement was taken (if applicable).', null=True, verbose_name='depth')),
                ('method', models.CharField(blank=True, help_text='The method used to obtain the reported value.', max_length=200, verbose_name='method')),
                ('operator', models.CharField(blank=True, help_text='The operator collecting the measurements', max_length=150, null=True, verbose_name='operator')),
                ('comment', models.TextField(blank=True, help_text='Information supplied with the measurement either by the original author/researcher or the compiler.', null=True, verbose_name='comment')),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
                ('source_id', models.CharField(blank=True, help_text='This is the ID for the measurement used by the original source', max_length=150, null=True, verbose_name='source ID')),
                ('log_id', models.CharField(blank=True, help_text='This is required for multiple logs to be stored on the same site.', max_length=64, null=True, verbose_name='log specific ID')),
                ('year_logged', models.PositiveIntegerField(blank=True, help_text='Year the measurement was made.', null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2050)], verbose_name='year logged')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added to ThermoGlobe')),
                ('temperature', models.FloatField(help_text='The reported temperature in at the given depth.', verbose_name='temperature')),
                ('uncertainty', models.FloatField(blank=True, help_text='Uncertainty on the reported temperature.', null=True, verbose_name='uncertainty')),
                ('circ_time', models.FloatField(blank=True, help_text='Circulation time in hours.', null=True, verbose_name='circulation time')),
                ('lag_time', models.FloatField(blank=True, help_text='Hours between drilling and measuring temperature.', null=True, verbose_name='lag time')),
                ('correction', models.CharField(blank=True, help_text='Applied temperature correction type.', max_length=150, null=True, verbose_name='correction')),
                ('reference', models.ForeignKey(blank=True, help_text='The publications or other reference from which the measurement was reported.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='temperature', to='publications.publication', verbose_name='reference')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='temperature', to='thermoglobe.site', verbose_name='site')),
            ],
            options={
                'verbose_name': 'temperature',
                'verbose_name_plural': 'temperature',
                'db_table': 'temperature',
                'ordering': ['log_id', 'depth'],
                'unique_together': {('temperature', 'depth', 'site', 'log_id', 'reference')},
            },
        ),
        migrations.CreateModel(
            name='HeatProduction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('formation', models.CharField(blank=True, help_text='The name of the sampled geological formation.', max_length=200, verbose_name='formation name')),
                ('depth', models.FloatField(blank=True, help_text='The depth at which the measurement was taken (if applicable).', null=True, verbose_name='depth')),
                ('method', models.CharField(blank=True, help_text='The method used to obtain the reported value.', max_length=200, verbose_name='method')),
                ('operator', models.CharField(blank=True, help_text='The operator collecting the measurements', max_length=150, null=True, verbose_name='operator')),
                ('comment', models.TextField(blank=True, help_text='Information supplied with the measurement either by the original author/researcher or the compiler.', null=True, verbose_name='comment')),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
                ('source_id', models.CharField(blank=True, help_text='This is the ID for the measurement used by the original source', max_length=150, null=True, verbose_name='source ID')),
                ('log_id', models.CharField(blank=True, help_text='This is required for multiple logs to be stored on the same site.', max_length=64, null=True, verbose_name='log specific ID')),
                ('year_logged', models.PositiveIntegerField(blank=True, help_text='Year the measurement was made.', null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2050)], verbose_name='year logged')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added to ThermoGlobe')),
                ('rock_type', models.CharField(blank=True, help_text='The reported rock type.', max_length=100, null=True, verbose_name='rock type')),
                ('heat_production', models.FloatField(help_text='The reported value of the sample.', verbose_name='heat production')),
                ('uncertainty', models.FloatField(blank=True, help_text='The uncertainty on the reported value.', null=True, verbose_name='uncertainty')),
                ('k_pc', models.FloatField(blank=True, null=True, verbose_name='K (wt%)')),
                ('th_ppm', models.FloatField(blank=True, null=True, verbose_name='Th (ppm)')),
                ('u_ppm', models.FloatField(blank=True, null=True, verbose_name='U (ppm)')),
                ('reference', models.ForeignKey(blank=True, help_text='The publications or other reference from which the measurement was reported.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='heat_production', to='publications.publication', verbose_name='reference')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='heat_production', to='thermoglobe.site', verbose_name='site')),
            ],
            options={
                'verbose_name': 'heat production',
                'verbose_name_plural': 'heat production',
                'db_table': 'heat_production',
                'ordering': ['log_id', 'depth'],
                'default_related_name': 'heat_production',
                'unique_together': {('log_id', 'heat_production', 'k_pc', 'th_ppm', 'u_ppm', 'depth', 'site', 'reference')},
            },
        ),
        migrations.CreateModel(
            name='Conductivity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('formation', models.CharField(blank=True, help_text='The name of the sampled geological formation.', max_length=200, verbose_name='formation name')),
                ('depth', models.FloatField(blank=True, help_text='The depth at which the measurement was taken (if applicable).', null=True, verbose_name='depth')),
                ('method', models.CharField(blank=True, help_text='The method used to obtain the reported value.', max_length=200, verbose_name='method')),
                ('operator', models.CharField(blank=True, help_text='The operator collecting the measurements', max_length=150, null=True, verbose_name='operator')),
                ('comment', models.TextField(blank=True, help_text='Information supplied with the measurement either by the original author/researcher or the compiler.', null=True, verbose_name='comment')),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
                ('source_id', models.CharField(blank=True, help_text='This is the ID for the measurement used by the original source', max_length=150, null=True, verbose_name='source ID')),
                ('log_id', models.CharField(blank=True, help_text='This is required for multiple logs to be stored on the same site.', max_length=64, null=True, verbose_name='log specific ID')),
                ('year_logged', models.PositiveIntegerField(blank=True, help_text='Year the measurement was made.', null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2050)], verbose_name='year logged')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added to ThermoGlobe')),
                ('sample_name', models.CharField(blank=True, help_text='The reported name of the sample if applicable.', max_length=200, verbose_name='sample name')),
                ('conductivity', models.FloatField(help_text='The reported thermal conductivity in of the sample.', verbose_name='thermal conductivity')),
                ('uncertainty', models.FloatField(blank=True, help_text='The uncertainty on the reported value.', null=True, verbose_name='uncertainty')),
                ('rock_type', models.CharField(blank=True, help_text='The reported rock type.', max_length=100, null=True, verbose_name='rock type')),
                ('sample_length', models.FloatField(blank=True, help_text='Length of the sample.', null=True, verbose_name='sample length')),
                ('sample_width', models.FloatField(blank=True, help_text='Width of the sample.', null=True, verbose_name='sample width')),
                ('sample_diameter', models.FloatField(blank=True, help_text='Diameter of the sample.', null=True, verbose_name='sample diameter')),
                ('sample_thickness', models.FloatField(blank=True, help_text='Thickness of the sample.', null=True, verbose_name='sample thickness')),
                ('orientation', models.FloatField(blank=True, help_text='The angle relative to the foliation or bedding where 0 is along foliation and 90 is perpendicular to foliation. Values can be a floating point number anywhere between 0 and 90.', null=True, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(0)], verbose_name='orientation')),
                ('reference', models.ForeignKey(blank=True, help_text='The publications or other reference from which the measurement was reported.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conductivity', to='publications.publication', verbose_name='reference')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conductivity', to='thermoglobe.site', verbose_name='site')),
            ],
            options={
                'verbose_name': 'thermal conductivity',
                'verbose_name_plural': 'thermal conductivity',
                'db_table': 'thermal_conductivity',
                'ordering': ['site__site_name', 'log_id', 'depth'],
                'unique_together': {('conductivity', 'depth', 'site', 'log_id', 'reference')},
            },
        ),
    ]
