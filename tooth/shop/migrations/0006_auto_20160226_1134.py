# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20160225_2213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='tx',
            new_name='additional_info',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='quantity',
            new_name='quantity_1',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='product',
        ),
        migrations.AddField(
            model_name='purchase',
            name='product_1',
            field=models.ForeignKey(null=True, to='shop.Product', related_name='product_slot_1', blank=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='product_2',
            field=models.ForeignKey(null=True, to='shop.Product', related_name='product_slot_2', blank=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='product_3',
            field=models.ForeignKey(null=True, to='shop.Product', related_name='product_slot_3', blank=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='product_4',
            field=models.ForeignKey(null=True, to='shop.Product', related_name='product_slot_4', blank=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='product_5',
            field=models.ForeignKey(null=True, to='shop.Product', related_name='product_slot_5', blank=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='quantity_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='purchase',
            name='quantity_3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='purchase',
            name='quantity_4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='purchase',
            name='quantity_5',
            field=models.IntegerField(default=0),
        ),
    ]
