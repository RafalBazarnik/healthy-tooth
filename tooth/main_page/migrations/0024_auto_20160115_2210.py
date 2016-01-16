# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0023_auto_20160115_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dentistday',
            name='slot10_11',
            field=models.ForeignKey(related_name='hours_1000_1100', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot11_12',
            field=models.ForeignKey(related_name='hours_1100_1200', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot12_13',
            field=models.ForeignKey(related_name='hours_1200_1300', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot13_14',
            field=models.ForeignKey(related_name='hours_1300_1400', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot14_15',
            field=models.ForeignKey(related_name='hours_1400_1500', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot15_16',
            field=models.ForeignKey(related_name='hours_1500_1600', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot16_17',
            field=models.ForeignKey(related_name='hours_1600_1700', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot17_18',
            field=models.ForeignKey(related_name='hours_1700_1800', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot18_19',
            field=models.ForeignKey(related_name='hours_1800_1900', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot19_20',
            field=models.ForeignKey(related_name='hours_1900_2000', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
