# Generated by Django 3.2.15 on 2022-09-07 13:11

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConductivitySource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Conductivity Source',
                'verbose_name_plural': 'Conductivity Source',
            },
        ),
        migrations.CreateModel(
            name='Correction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Correction Type',
                'verbose_name_plural': 'Correction Type',
            },
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Geographic Environment',
                'verbose_name_plural': 'Geographic Environment',
            },
        ),
        migrations.CreateModel(
            name='ExplorationMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Exploration Method',
                'verbose_name_plural': 'Exploration Method',
            },
        ),
        migrations.CreateModel(
            name='ExplorationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Exploration Purpose',
                'verbose_name_plural': 'Exploration Purpose',
            },
        ),
        migrations.CreateModel(
            name='HeatFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Heat Flow Method',
                'verbose_name_plural': 'Heat Flow Method',
            },
        ),
        migrations.CreateModel(
            name='HeatTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Heat Transfer Type',
                'verbose_name_plural': 'Heat Transfer Type',
            },
        ),
        migrations.CreateModel(
            name='MeasurementCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Conductivity PT Condition',
                'verbose_name_plural': 'Conductivity PT Condition',
            },
        ),
        migrations.CreateModel(
            name='Probe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Probe Type',
                'verbose_name_plural': 'Probe Type',
            },
        ),
        migrations.CreateModel(
            name='Saturation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'TC Saturation Method',
                'verbose_name_plural': 'TC Saturation Method',
            },
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Temperature Method',
                'verbose_name_plural': 'Temperature Method',
            },
        ),
        migrations.CreateModel(
            name='TemperatureCorrection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Temperature Correction Method',
                'verbose_name_plural': 'Temperature Correction Method',
            },
        ),
    ]
