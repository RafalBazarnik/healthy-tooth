# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_page', '0020_patient_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='DentistDay',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('dentist', models.ForeignKey(to='main_page.Dentist')),
                ('office', models.ForeignKey(to='main_page.Office')),
                ('slot10_11', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='hours_1000_1100', default=1)),
                ('slot11_12', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='hours_1100_1200', default=1)),
                ('slot12_13', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='hours_1200_1300', default=1)),
                ('slot13_14', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='hours_1300_1400', default=1)),
                ('slot14_15', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='hours_1400_1500', default=1)),
                ('slot15_16', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='hours_1500_1600', default=1)),
                ('slot16_17', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='hours_1600_1700', default=1)),
                ('slot17_18', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='hours_1700_1800', default=1)),
                ('slot18_19', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='hours_1800_1900', default=1)),
                ('slot19_20', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='hours_1900_2000', default=1)),
            ],
            options={
                'verbose_name_plural': 'Schedules',
                'verbose_name': 'Schedule',
            },
        ),
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
    ]
