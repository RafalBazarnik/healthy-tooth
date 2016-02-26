# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_purchase_office'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='quantity_2',
            field=models.PositiveIntegerField(null=True, blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity_3',
            field=models.PositiveIntegerField(null=True, blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity_4',
            field=models.PositiveIntegerField(null=True, blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity_5',
            field=models.PositiveIntegerField(null=True, blank=True, default=1),
        ),
    ]
