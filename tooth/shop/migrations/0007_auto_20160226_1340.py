# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20160226_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='total_price',
            field=models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=6),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity_1',
            field=models.PositiveIntegerField(default=1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity_2',
            field=models.PositiveIntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity_3',
            field=models.PositiveIntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity_4',
            field=models.PositiveIntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity_5',
            field=models.PositiveIntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.CharField(choices=[('A', 'zamówione'), ('B', 'opłacone'), ('C', 'zwrócone'), ('D', 'w reklamacji'), ('E', 'potwierdzone'), ('F', 'wysłane'), ('G', 'gotowe do odbioru'), ('H', 'odebrane'), ('I', 'nieopłacone'), ('J', 'nieodebrane')], null=True, blank=True, max_length=20),
        ),
    ]
