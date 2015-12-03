# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0017_auto_20151202_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('province', models.CharField(choices=[('DS', 'dolnośląskie'), ('KP', 'kujawsko-pomorskie'), ('LU', 'lubelskie'), ('LB', 'lubuskie'), ('LD', 'łódzkie'), ('MA', 'małopolskie'), ('MZ', 'mazowieckie'), ('OP', 'opolskie'), ('PK', 'podkarpackie'), ('PD', 'podlaskie'), ('PM', 'pomorskie'), ('SL', 'śląskie'), ('SK', 'świętokrzyskie'), ('WN', 'warmińsko-mazurskie'), ('WP', 'wielkopolskie'), ('ZP', 'zachodniopomorskie')], help_text='Województwo', null=True, max_length=20)),
                ('city', models.CharField(help_text='Miasto/Miejscowość', null=True, max_length=100)),
                ('street', models.CharField(help_text='Ulica', null=True, max_length=100)),
                ('number', models.CharField(help_text='Numer domu/mieszkania', null=True, max_length=20)),
                ('phone_number', models.CharField(validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], max_length=15, help_text='Numer telefonu', blank=True)),
                ('phone_number_alt', models.CharField(validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], max_length=15, help_text='Alternatywny numer telefonu', blank=True)),
                ('email', models.EmailField(help_text='Adres email', null=True, max_length=254)),
                ('skype', models.CharField(max_length=50, null=True, blank=True)),
                ('name', models.CharField(help_text='Imię', max_length=100)),
                ('surname', models.CharField(help_text='Nazwisko', max_length=100)),
                ('preferred_date', models.DateTimeField(help_text='Preferowany dzień i godzina wizyty')),
                ('preferred_date_alt', models.DateTimeField(help_text='Preferowany dzień i godzina wizyty - alternatywny', null=True)),
                ('preferred_date_alt2', models.DateTimeField(help_text='Preferowany dzień i godzina wizyty - alternatywny', null=True)),
                ('extra_info', django_markdown.models.MarkdownField(help_text='Dodatkowe informacje', null=True)),
                ('personal_data_agreement', models.BooleanField(default=True, help_text='Zgoda na przechowywanie i pzetwarzanie danych osobowych w celach umówienia wizyty i w celach marketingowych')),
                ('is_active', models.BooleanField(default=True, help_text='Czy prośba o zapis do dentysty jest nadal aktualna? (nie nastąpił kontakt i umówienie wizyty)')),
            ],
            options={
                'verbose_name_plural': 'Appointments',
                'verbose_name': 'Appointment',
            },
        ),
        migrations.AddField(
            model_name='office',
            name='skype',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='skype',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='office',
            field=models.ForeignKey(to='main_page.Office', help_text='Wybierz gabinet'),
        ),
        migrations.AddField(
            model_name='event',
            name='appointment',
            field=models.ForeignKey(to='main_page.Appointment', null=True, blank=True),
        ),
    ]
