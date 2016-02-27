# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0034_auto_20160225_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='age',
        ),
        migrations.AddField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(null=True, help_text='Data Urodzenia', blank=True),
        ),
    ]
