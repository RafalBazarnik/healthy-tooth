# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0021_auto_20160107_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='dentists',
        ),
        migrations.AddField(
            model_name='dentist',
            name='office',
            field=models.ForeignKey(related_name='workplace', to='main_page.Office', null=True),
        ),
        migrations.AlterField(
            model_name='dentistday',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='user',
            field=models.OneToOneField(related_name='office_user', null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
