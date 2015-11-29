# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0013_auto_20151129_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.CharField(null=True, max_length=3, help_text='Wiek'),
        ),
        migrations.AddField(
            model_name='patient',
            name='sex',
            field=models.CharField(null=True, choices=[('F', 'kobieta'), ('M', 'mężczyzna')], max_length=20, help_text='Płeć'),
        ),
    ]
