# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=150)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Shop Product Category',
                'verbose_name_plural': 'Shop Product Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=150)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='product_photo', blank=True)),
                ('manufacturer', models.CharField(max_length=300, blank=True)),
                ('price_in_PLN', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Shop Product',
                'verbose_name_plural': 'Shop Products',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('slug', models.SlugField(null=True, unique=True, blank=True)),
            ],
            options={
                'verbose_name': 'Shop Product Tag',
                'verbose_name_plural': 'Shop Product Tags',
            },
        ),
    ]
