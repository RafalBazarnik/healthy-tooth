# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_auto_20151126_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='dentist',
            name='pwz_number',
            field=models.CharField(max_length=87, null=True),
        ),
    ]
