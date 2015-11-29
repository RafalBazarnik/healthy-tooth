# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0012_auto_20151129_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='dentist',
            field=models.ForeignKey(to='main_page.Dentist', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='office',
            field=models.ForeignKey(to='main_page.Office', null=True, blank=True),
        ),
    ]
