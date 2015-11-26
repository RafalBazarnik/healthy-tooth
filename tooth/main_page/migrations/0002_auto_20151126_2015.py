# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='pesel',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='office_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
