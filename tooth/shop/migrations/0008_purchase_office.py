# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0034_auto_20160225_0909'),
        ('shop', '0007_auto_20160226_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='office',
            field=models.ForeignKey(to='main_page.Office', default=1),
            preserve_default=False,
        ),
    ]
