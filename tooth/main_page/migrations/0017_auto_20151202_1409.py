# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import main_page.models
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0016_auto_20151202_0945'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'Patient', 'verbose_name_plural': 'Patients'},
        ),
        migrations.AlterField(
            model_name='dentist',
            name='biography',
            field=django_markdown.models.MarkdownField(help_text='Biografia', null=True),
        ),
        migrations.AlterField(
            model_name='dentist',
            name='name',
            field=models.CharField(help_text='Imię', max_length=100),
        ),
        migrations.AlterField(
            model_name='dentist',
            name='profile_image',
            field=models.ImageField(blank=True, help_text='Zdjęcie', null=True, upload_to=main_page.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='dentist',
            name='slug',
            field=models.SlugField(help_text='Nazwa linku w postaci - nazwisko-imie-pwz - male litery, bez polskich znaków', unique=True, blank=True, null=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='dentist',
            name='surname',
            field=models.CharField(help_text='Nazwisko', max_length=100),
        ),
    ]
