# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_purchase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='time',
            new_name='date',
        ),
        migrations.AddField(
            model_name='purchase',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='purchase',
            name='status',
            field=models.CharField(null=True, choices=[('A', 'zamówione'), ('B', 'opłacone'), ('C', 'zwrócone'), ('D', 'w reklamacji'), ('E', 'potwierdzone'), ('F', 'wysłane'), ('G', 'gotowe do odbioru'), ('H', 'odebrane'), ('I', 'nieopłacone'), ('J', 'nieodebrane')], max_length=20),
        ),
    ]
