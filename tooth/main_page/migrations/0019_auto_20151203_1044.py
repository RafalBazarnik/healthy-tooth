# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0018_auto_20151203_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='office',
            field=models.ForeignKey(related_name='appointment', to='main_page.Office', help_text='Wybierz gabinet'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='preferred_date_alt',
            field=models.DateTimeField(blank=True, help_text='Preferowany dzień i godzina wizyty - alternatywny', null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='preferred_date_alt2',
            field=models.DateTimeField(blank=True, help_text='Preferowany dzień i godzina wizyty - alternatywny', null=True),
        ),
    ]
