# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0035_auto_20160227_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='office',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]
