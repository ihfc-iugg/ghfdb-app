# Generated by Django 2.2.1 on 2019-10-02 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0009_auto_20191002_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='abstract',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='reference',
            name='bib_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
