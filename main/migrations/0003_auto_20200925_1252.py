# Generated by Django 3.1.1 on 2020-09-25 03:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200911_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=ckeditor.fields.RichTextField(help_text='The answer to the question.', verbose_name='answer'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(help_text='Input the question here.', max_length=100, verbose_name='question'),
        ),
    ]
