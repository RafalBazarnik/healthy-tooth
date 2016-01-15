# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0022_auto_20160115_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dentistday',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
