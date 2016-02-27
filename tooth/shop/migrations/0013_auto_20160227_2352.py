# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20160227_2317'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'verbose_name': 'Shop Purchase', 'verbose_name_plural': 'Shop Purchases'},
        ),
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.CharField(choices=[('A', 'zamówione'), ('B', 'opłacone'), ('C', 'zwrócone'), ('D', 'reklamacja'), ('E', 'potwierdzone'), ('F', 'wysłane'), ('G', 'gotowe do odbioru'), ('H', 'odebrane'), ('I', 'nieopłacone'), ('J', 'nieodebrane'), ('K', 'zarchiwizowane')], blank=True, max_length=20, null=True),
        ),
    ]
