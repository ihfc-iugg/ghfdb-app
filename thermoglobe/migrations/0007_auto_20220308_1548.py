# Generated by Django 3.2.12 on 2022-03-08 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thermoglobe', '0006_temperature'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='heatproduction',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='heatproduction',
            name='reference',
        ),
        migrations.RemoveField(
            model_name='heatproduction',
            name='site',
        ),
        migrations.AlterUniqueTogether(
            name='temperature',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='temperature',
            name='meta',
        ),
        migrations.AlterUniqueTogether(
            name='tempmeta',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='tempmeta',
            name='reference',
        ),
        migrations.RemoveField(
            model_name='tempmeta',
            name='site',
        ),
        migrations.DeleteModel(
            name='Conductivity',
        ),
        migrations.DeleteModel(
            name='HeatProduction',
        ),
        migrations.DeleteModel(
            name='Temperature',
        ),
        migrations.DeleteModel(
            name='TempMeta',
        ),
    ]
