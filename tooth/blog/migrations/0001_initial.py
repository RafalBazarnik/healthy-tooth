# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0015_office_dentists'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=40, null=True, unique=True, blank=True)),
            ],
            options={
                'verbose_name': 'Blog Posts Categories',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True, blank=True)),
                ('pub_date', models.DateTimeField(null=True, blank=True)),
                ('published', models.BooleanField(default=False)),
                ('text', django_markdown.models.MarkdownField(null=True)),
                ('slug', models.SlugField(max_length=40, null=True, unique=True)),
                ('other_author', models.CharField(max_length=100, null=True, blank=True)),
                ('category', models.ForeignKey(null=True, to='blog.Category', blank=True)),
                ('dentist', models.ForeignKey(null=True, to='main_page.Dentist', blank=True)),
                ('office', models.ForeignKey(null=True, to='main_page.Office', blank=True)),
            ],
            options={
                'verbose_name': 'Blog Post',
                'ordering': ['-pub_date'],
                'verbose_name_plural': 'Blog Posts',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('slug', models.SlugField(null=True, unique=True, blank=True)),
            ],
            options={
                'verbose_name': 'Blog Posts Tags',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(null=True, to='blog.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='upload_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
