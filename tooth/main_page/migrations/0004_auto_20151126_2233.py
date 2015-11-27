# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_dentist_pwz_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dentist',
            old_name='title',
            new_name='professional_title',
        ),
        migrations.AlterField(
            model_name='dentist',
            name='pwz_number',
            field=models.CharField(help_text='7-cyfrowy numer prawa wykonywania zawodu (PWZ)', max_length=87, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='office',
            name='phone_number_alt',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
