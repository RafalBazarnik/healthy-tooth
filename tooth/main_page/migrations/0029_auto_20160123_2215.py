# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0028_auto_20160123_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
    ]
