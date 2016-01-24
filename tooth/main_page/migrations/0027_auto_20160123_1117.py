# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0026_auto_20160121_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dentistday',
            name='slot10_11',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='hours_1000_1100', help_text='10:00-11.00'),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot11_12',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='hours_1100_1200', help_text='11:00-12.00'),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot12_13',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='hours_1200_1300', help_text='12:00-13.00'),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot13_14',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='hours_1300_1400', help_text='13:00-14.00'),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot14_15',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='hours_1400_1500', help_text='14:00-15.00'),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot15_16',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='hours_1500_1600', help_text='15:00-16.00'),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot16_17',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='hours_1600_1700', help_text='16:00-17.00'),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot17_18',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='hours_1700_1800', help_text='17:00-18.00'),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot18_19',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='hours_1800_1900', help_text='18:00-19.00'),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='slot19_20',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='hours_1900_2000', help_text='19:00-20.00'),
        ),
        migrations.AlterUniqueTogether(
            name='dentistday',
            unique_together=set([('date', 'dentist')]),
        ),
    ]
