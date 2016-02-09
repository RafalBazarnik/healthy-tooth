# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0029_auto_20160123_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='profile_image',
            field=models.ImageField(blank=True, help_text='Zdjęcie', upload_to='', null=True),
        ),
    ]
