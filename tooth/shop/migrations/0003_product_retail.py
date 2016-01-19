# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20160119_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='retail',
            field=models.BooleanField(default=True, help_text='Do sprzedaży detalicznej = True, Do sprzedaży hurtowej - False'),
        ),
    ]
