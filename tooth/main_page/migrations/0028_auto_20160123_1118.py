# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0027_auto_20160123_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dentistday',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
