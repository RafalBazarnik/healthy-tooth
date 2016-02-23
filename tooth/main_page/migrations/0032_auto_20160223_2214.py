# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0031_remove_event_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='logo_image',
            field=models.ImageField(blank=True, null=True, upload_to='offices', help_text='Logo'),
        ),
        migrations.AlterField(
            model_name='dentist',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='dentists', help_text='Zdjęcie'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='patients', help_text='Zdjęcie'),
        ),
    ]
