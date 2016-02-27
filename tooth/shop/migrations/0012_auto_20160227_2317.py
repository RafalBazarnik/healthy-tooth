# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20160226_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='additional_info',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
