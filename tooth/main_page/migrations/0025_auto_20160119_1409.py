# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0024_auto_20160115_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(max_length=15, blank=True, validators=[django.core.validators.RegexValidator(message='Niepoprawny numer telefonu. Powinien mieć minimum 9 i maksymalnie 15 cyfr', regex='^\\+?1?\\d{9,15}$')], help_text='Numer telefonu'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phone_number_alt',
            field=models.CharField(max_length=15, blank=True, validators=[django.core.validators.RegexValidator(message='Niepoprawny numer telefonu. Powinien mieć minimum 9 i maksymalnie 15 cyfr', regex='^\\+?1?\\d{9,15}$')], help_text='Alternatywny numer telefonu'),
        ),
        migrations.AlterField(
            model_name='dentist',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='', null=True, help_text='Zdjęcie'),
        ),
        migrations.AlterField(
            model_name='dentist',
            name='slug',
            field=models.SlugField(max_length=40, unique=True, null=True, help_text='Nazwa linku w postaci - nazwisko-imie-pwz - male litery, bez polskich znaków'),
        ),
        migrations.AlterField(
            model_name='office',
            name='phone_number',
            field=models.CharField(max_length=15, blank=True, validators=[django.core.validators.RegexValidator(message='Niepoprawny numer telefonu. Powinien mieć minimum 9 i maksymalnie 15 cyfr', regex='^\\+?1?\\d{9,15}$')], help_text='Numer telefonu'),
        ),
        migrations.AlterField(
            model_name='office',
            name='phone_number_alt',
            field=models.CharField(max_length=15, blank=True, validators=[django.core.validators.RegexValidator(message='Niepoprawny numer telefonu. Powinien mieć minimum 9 i maksymalnie 15 cyfr', regex='^\\+?1?\\d{9,15}$')], help_text='Alternatywny numer telefonu'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(max_length=15, blank=True, validators=[django.core.validators.RegexValidator(message='Niepoprawny numer telefonu. Powinien mieć minimum 9 i maksymalnie 15 cyfr', regex='^\\+?1?\\d{9,15}$')], help_text='Numer telefonu'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number_alt',
            field=models.CharField(max_length=15, blank=True, validators=[django.core.validators.RegexValidator(message='Niepoprawny numer telefonu. Powinien mieć minimum 9 i maksymalnie 15 cyfr', regex='^\\+?1?\\d{9,15}$')], help_text='Alternatywny numer telefonu'),
        ),
    ]
