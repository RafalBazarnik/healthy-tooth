# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0015_office_dentists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='city',
            field=models.CharField(null=True, max_length=100, help_text='Miasto/Miejscowość'),
        ),
        migrations.AlterField(
            model_name='office',
            name='email',
            field=models.EmailField(null=True, max_length=254, help_text='Adres email'),
        ),
        migrations.AlterField(
            model_name='office',
            name='street',
            field=models.CharField(null=True, max_length=100, help_text='Ulica'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='city',
            field=models.CharField(null=True, max_length=100, help_text='Miasto/Miejscowość'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(null=True, max_length=254, help_text='Adres email'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='slug',
            field=models.SlugField(blank=True, max_length=40, null=True, unique=True, help_text='Nazwa linku w postaci - nazwisko-imie-pesel - male litery, bez polskich znaków'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='street',
            field=models.CharField(null=True, max_length=100, help_text='Ulica'),
        ),
    ]
