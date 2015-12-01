# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0014_auto_20151129_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='dentists',
            field=models.ManyToManyField(to='main_page.Dentist', blank=True),
        ),
    ]
