# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0008_auto_20151129_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dentist',
            name='pwz_number',
            field=models.CharField(max_length=87, help_text='7-cyfrowy numer prawa wykonywania zawodu (PWZ)', validators=[django.core.validators.MaxLengthValidator(7), django.core.validators.MinLengthValidator(7)], null=True),
        ),
    ]
