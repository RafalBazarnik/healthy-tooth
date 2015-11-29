# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0007_office_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='price_list',
            field=models.CharField(max_length=1000, help_text='Cennik', null=True),
        ),
        migrations.AddField(
            model_name='office',
            name='text',
            field=django_markdown.models.MarkdownField(null=True),
        ),
        migrations.AlterField(
            model_name='dentist',
            name='pwz_number',
            field=models.CharField(max_length=87, validators=[django.core.validators.MaxLengthValidator(11), django.core.validators.MinLengthValidator(11)], null=True, help_text='7-cyfrowy numer prawa wykonywania zawodu (PWZ)'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pesel',
            field=models.CharField(max_length=11, validators=[django.core.validators.MaxLengthValidator(11), django.core.validators.MinLengthValidator(11)], null=True, help_text='Numer PESEL'),
        ),
    ]
