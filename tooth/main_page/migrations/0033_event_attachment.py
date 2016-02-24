# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0032_auto_20160223_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attachment',
            field=models.FileField(upload_to='documents', null=True, blank=True),
        ),
    ]
