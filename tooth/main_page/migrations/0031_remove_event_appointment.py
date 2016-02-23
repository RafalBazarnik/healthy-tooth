# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0030_patient_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='appointment',
        ),
    ]
