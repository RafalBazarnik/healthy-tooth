# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_auto_20151127_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='dentist',
            name='specialties',
            field=models.CharField(null=True, help_text='Specjalizacja', max_length=50),
        ),
        migrations.AlterField(
            model_name='office',
            name='number',
            field=models.CharField(null=True, help_text='Numer domu/mieszkania', max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='number',
            field=models.CharField(null=True, help_text='Numer domu/mieszkania', max_length=20),
        ),
    ]
