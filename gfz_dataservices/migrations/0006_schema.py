# Generated by Django 3.2.15 on 2022-08-30 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gfz_dataservices', '0005_auto_20220829_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=32, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('schema', models.JSONField()),
            ],
        ),
    ]
