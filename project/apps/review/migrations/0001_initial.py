# Generated by Django 3.2.18 on 2023-03-23 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ghfdb', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('literature', '0002_alter_literature_authors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominated', models.DateTimeField(auto_now_add=True, help_text='Date the user nominated themselves to review this publication', verbose_name='reviewer nominated')),
                ('accepted', models.DateTimeField(blank=True, help_text='Date the review was accepted by site admins and incorporated into the production database', null=True, verbose_name='review accepted')),
                ('submitted', models.DateTimeField(blank=True, help_text='Date the user submitted correction for final approval by site admins', null=True, verbose_name='review submitted')),
                ('publication', models.OneToOneField(help_text='Publication being reviewed', null=True, on_delete=django.db.models.deletion.SET_NULL, to='literature.literature')),
                ('reviewer', models.ForeignKey(help_text='User reviewing this publication', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IntervalReview',
            fields=[
                ('interval_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ghfdb.interval')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.review')),
                ('review_of', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='revised', to='ghfdb.interval')),
            ],
            options={
                'db_table': 'interval_review',
            },
            bases=('ghfdb.interval',),
        ),
        migrations.CreateModel(
            name='HeatFlowReview',
            fields=[
                ('heatflow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ghfdb.heatflow')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.review')),
                ('review_of', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='revised', to='ghfdb.heatflow')),
            ],
            options={
                'db_table': 'heat_flow_review',
            },
            bases=('ghfdb.heatflow',),
        ),
    ]
