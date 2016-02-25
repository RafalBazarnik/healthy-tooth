# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0033_event_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dentist',
            name='slug',
            field=models.SlugField(unique=True, max_length=100, null=True, help_text='Nazwa linku w postaci - nazwisko-imie-pwz - male litery, bez polskich znaków'),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, unique=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='slug',
            field=models.SlugField(blank=True, unique=True, max_length=100, null=True, help_text='Nazwa linku w postaci - nazwisko-imie-pesel - male litery, bez polskich znaków'),
        ),
    ]
