# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20160226_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='purchase_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.CharField(choices=[('A', 'zamówione'), ('B', 'opłacone'), ('C', 'zwrócone'), ('D', 'reklamacja'), ('E', 'potwierdzone'), ('F', 'wysłane'), ('G', 'gotowe do odbioru'), ('H', 'odebrane'), ('I', 'nieopłacone'), ('J', 'nieodebrane')], max_length=20, blank=True, null=True),
        ),
    ]
