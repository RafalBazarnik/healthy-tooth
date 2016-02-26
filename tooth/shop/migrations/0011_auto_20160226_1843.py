# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20160226_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_id',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
    ]
