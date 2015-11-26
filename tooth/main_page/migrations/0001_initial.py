# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import main_page.models
import django_markdown.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dentist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('biography', models.CharField(max_length=5000)),
                ('profile_image', models.ImageField(upload_to=main_page.models.get_image_path, null=True, blank=True)),
                ('slug', models.SlugField(max_length=40, unique=True, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Dentist',
                'verbose_name_plural': 'Dentists',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('text', django_markdown.models.MarkdownField()),
                ('slug', models.SlugField(max_length=40, unique=True, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('province', models.CharField(max_length=20, choices=[('DS', 'dolnośląskie'), ('KP', 'kujawsko-pomorskie'), ('LU', 'lubelskie'), ('LB', 'lubuskie'), ('LD', 'łódzkie'), ('MA', 'małopolskie'), ('MZ', 'mazowieckie'), ('OP', 'opolskie'), ('PK', 'podkarpackie'), ('PD', 'podlaskie'), ('PM', 'pomorskie'), ('SL', 'śląskie'), ('SK', 'świętokrzyskie'), ('WN', 'warmińsko-mazurskie'), ('WP', 'wielkopolskie'), ('ZP', 'zachodniopomorskie')])),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=20)),
                ('phone_number', models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")], max_length=20, blank=True)),
                ('phone_number_alt', models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")], max_length=20, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=150)),
                ('office_id', models.CharField(max_length=10)),
                ('slug', models.SlugField(max_length=40, unique=True, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Office',
                'verbose_name_plural': 'Offices',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=40, unique=True, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Our Patient',
                'verbose_name_plural': 'Our Patients',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='subject',
            field=models.ForeignKey(to='main_page.Patient', blank=True, null=True),
        ),
    ]
