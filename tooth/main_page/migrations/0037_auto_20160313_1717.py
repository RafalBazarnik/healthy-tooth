# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0036_auto_20160302_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dentist',
            name='pwz_number',
            field=models.CharField(max_length=7, validators=[django.core.validators.MaxLengthValidator(7), django.core.validators.MinLengthValidator(7)], help_text='7-cyfrowy numer prawa wykonywania zawodu (PWZ)', null=True),
        ),
        migrations.AlterField(
            model_name='dentist',
            name='specialties',
            field=models.CharField(max_length=100, help_text='Specjalizacja', null=True),
        ),
    ]
