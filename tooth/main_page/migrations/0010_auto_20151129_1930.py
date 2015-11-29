# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0009_auto_20151129_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='price_list',
            field=django_markdown.models.MarkdownField(help_text='Cennik', null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='text',
            field=django_markdown.models.MarkdownField(help_text='Informacje o gabiencie', null=True),
        ),
    ]
