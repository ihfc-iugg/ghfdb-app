# Generated by Django 4.2.1 on 2023-05-15 14:31

import django.core.validators
from django.db import migrations
import geoluminate.db.fields


class Migration(migrations.Migration):
    dependencies = [
        ("ghfdb", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="interval",
            name="historic_id",
        ),
        migrations.AlterField(
            model_name="heatflow",
            name="borehole_depth",
            field=geoluminate.db.fields.QuantityField(
                base_units="m",
                blank=True,
                help_text="Specification of the total drilling depth below ground surface level.",
                null=True,
                unit_choices=["m"],
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(15000),
                ],
                verbose_name="total borehole depth",
            ),
        ),
        migrations.AlterField(
            model_name="heatflow",
            name="q",
            field=geoluminate.db.fields.QuantityField(
                base_units="mW / m^2",
                help_text="site heat flow value",
                unit_choices=["mW / m^2"],
                validators=[
                    django.core.validators.MinValueValidator(-1000000),
                    django.core.validators.MaxValueValidator(1000000),
                ],
                verbose_name="heat flow",
            ),
        ),
        migrations.AlterField(
            model_name="heatflow",
            name="q_unc",
            field=geoluminate.db.fields.QuantityField(
                base_units="mW / m^2",
                blank=True,
                help_text=(
                    "uncertainty standard deviation of the reported heat-flow value as estimated by an error"
                    " propagation from uncertainty in thermal conductivity and temperature gradient (corrected"
                    " preferred over measured gradient)."
                ),
                null=True,
                unit_choices=["mW / m^2"],
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1000000),
                ],
                verbose_name="heat flow uncertainty",
            ),
        ),
        migrations.AlterField(
            model_name="heatflow",
            name="water_temp",
            field=geoluminate.db.fields.QuantityField(
                base_units="°C",
                blank=True,
                help_text="Seafloor temperature where heat-flow measurements were taken.",
                null=True,
                unit_choices=["°C", "K"],
                verbose_name="bottom water temperature",
            ),
        ),
        migrations.AlterField(
            model_name="interval",
            name="hf_pen",
            field=geoluminate.db.fields.QuantityField(
                base_units="m",
                blank=True,
                help_text="Depth of penetration of marine probe into the sediment.",
                null=True,
                unit_choices=["m"],
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)],
                verbose_name="penetration depth",
            ),
        ),
        migrations.AlterField(
            model_name="interval",
            name="hf_probeL",
            field=geoluminate.db.fields.QuantityField(
                base_units="m",
                blank=True,
                help_text="length of the marine probe.",
                null=True,
                unit_choices=["m"],
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)],
                verbose_name="probe length",
            ),
        ),
        migrations.AlterField(
            model_name="interval",
            name="probe_tilt",
            field=geoluminate.db.fields.QuantityField(
                base_units="degree",
                blank=True,
                help_text="Tilt of the marine probe.",
                null=True,
                unit_choices=["degree"],
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(90)],
                verbose_name="tilt",
            ),
        ),
        migrations.AlterField(
            model_name="interval",
            name="q_bot",
            field=geoluminate.db.fields.QuantityField(
                base_units="m",
                blank=True,
                help_text=(
                    "Describes the true vertical depth of the bottom end of the heat-flow determination interval"
                    " relative to the land surface/ocean bottom."
                ),
                null=True,
                unit_choices=["m"],
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10000),
                ],
                verbose_name="interval bottom",
            ),
        ),
        migrations.AlterField(
            model_name="interval",
            name="q_top",
            field=geoluminate.db.fields.QuantityField(
                base_units="m",
                blank=True,
                help_text=(
                    "Specifies the true vertical depth at the top of the heat-flow interval relative to land"
                    " surface/ocean bottom."
                ),
                null=True,
                unit_choices=["m"],
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10000),
                ],
                verbose_name="interval top",
            ),
        ),
        migrations.AlterField(
            model_name="interval",
            name="qc",
            field=geoluminate.db.fields.QuantityField(
                base_units="mW / m^2",
                help_text="child heat flow value",
                unit_choices=["mW / m^2"],
                validators=[
                    django.core.validators.MinValueValidator(-1000000),
                    django.core.validators.MaxValueValidator(1000000),
                ],
                verbose_name="heat flow",
            ),
        ),
        migrations.AlterField(
            model_name="interval",
            name="qc_unc",
            field=geoluminate.db.fields.QuantityField(
                base_units="mW / m^2",
                blank=True,
                help_text=(
                    "uncertainty standard deviation of the reported heat-flow value as estimated by an error"
                    " propagation from uncertainty in thermal conductivity and temperature gradient (corrected"
                    " preferred over measured gradient)."
                ),
                null=True,
                unit_choices=["mW / m^2"],
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1000000),
                ],
                verbose_name="heat flow uncertainty",
            ),
        ),
        migrations.AlterField(
            model_name="interval",
            name="tc_mean",
            field=geoluminate.db.fields.QuantityField(
                base_units="W/mK",
                blank=True,
                help_text=(
                    "Mean conductivity in the vertical direction representative for the heat-flow determination"
                    " interval. Value should reflect true in-situ conditions for the interval."
                ),
                null=True,
                unit_choices=["W/mK"],
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)],
                verbose_name="Mean conductivity",
            ),
        ),
        migrations.AlterField(
            model_name="interval",
            name="tc_uncertainty",
            field=geoluminate.db.fields.QuantityField(
                base_units="W/mK",
                blank=True,
                help_text="Uncertainty of the mean thermal conductivity given as one-sigma standard deviation.",
                null=True,
                unit_choices=["W/mK"],
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)],
                verbose_name="uncertainty",
            ),
        ),
        migrations.AlterField(
            model_name="temperature",
            name="grad_mean",
            field=geoluminate.db.fields.QuantityField(
                base_units="K/km",
                blank=True,
                help_text="measured temperature gradient for the heat-flow determination interval.",
                null=True,
                unit_choices=["K/km"],
                verbose_name="measured gradient",
            ),
        ),
        migrations.AlterField(
            model_name="temperature",
            name="grad_mean_cor",
            field=geoluminate.db.fields.QuantityField(
                base_units="K/km",
                blank=True,
                help_text=(
                    "temperature gradient corrected for borehole and environmental effects. Correction method should be"
                    " recorded in the relevant field."
                ),
                null=True,
                unit_choices=["K/km"],
                verbose_name="corrected gradient",
            ),
        ),
        migrations.AlterField(
            model_name="temperature",
            name="grad_uncertainty",
            field=geoluminate.db.fields.QuantityField(
                base_units="K/km",
                blank=True,
                help_text=(
                    "uncertainty (standard deviation) of the measured temperature gradient estimated by error"
                    " propagation from uncertainty in the top and bottom interval temperatures."
                ),
                null=True,
                unit_choices=["K/km"],
                verbose_name="uncertainty",
            ),
        ),
        migrations.AlterField(
            model_name="temperature",
            name="grad_uncertainty_cor",
            field=geoluminate.db.fields.QuantityField(
                base_units="K/km",
                blank=True,
                help_text=(
                    "uncertainty (standard deviation) of the corrected temperature gradient estimated by error"
                    " propagation from uncertainty of the measured gradient and the applied correction approaches."
                ),
                null=True,
                unit_choices=["K/km"],
                verbose_name="uncertainty",
            ),
        ),
        migrations.AlterField(
            model_name="temperature",
            name="shutin_bottom",
            field=geoluminate.db.fields.PositiveIntegerQuantityField(
                base_units="hour",
                blank=True,
                help_text=(
                    "Time of measurement at the interval bottom in relation to the end of drilling/end of mud"
                    " circulation. Positive values are measured after the drilling, 0 represents temperatures measured"
                    " during the drilling."
                ),
                null=True,
                unit_choices=["hour"],
                verbose_name="Shut-in time (bottom; hrs)",
            ),
        ),
        migrations.AlterField(
            model_name="temperature",
            name="shutin_top",
            field=geoluminate.db.fields.PositiveIntegerQuantityField(
                base_units="hour",
                blank=True,
                help_text=(
                    "Time of measurement at the interval top in relation to the end of drilling/end of mud circulation."
                    " Positive values are measured after the drilling, 0 represents temperatures measured during the"
                    " drilling."
                ),
                null=True,
                unit_choices=["hour"],
                verbose_name="Shut-in time (top)",
            ),
        ),
    ]
