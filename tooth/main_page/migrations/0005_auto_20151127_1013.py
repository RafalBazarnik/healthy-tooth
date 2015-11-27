# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_auto_20151126_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('A1', 'wizyta kontrolna'), ('A2', 'leczenie kanałowe'), ('A3', 'plombowanie'), ('A4', 'inne')], max_length=20, default='A4', help_text='Rodzaj wizyty'),
        ),
        migrations.AddField(
            model_name='patient',
            name='city',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(null=True, max_length=254),
        ),
        migrations.AddField(
            model_name='patient',
            name='number',
            field=models.CharField(null=True, max_length=20),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(max_length=15, blank=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], help_text='Numer telefonu'),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_number_alt',
            field=models.CharField(max_length=15, blank=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], help_text='Alternatywny numer telefonu'),
        ),
        migrations.AddField(
            model_name='patient',
            name='province',
            field=models.CharField(choices=[('DS', 'dolnośląskie'), ('KP', 'kujawsko-pomorskie'), ('LU', 'lubelskie'), ('LB', 'lubuskie'), ('LD', 'łódzkie'), ('MA', 'małopolskie'), ('MZ', 'mazowieckie'), ('OP', 'opolskie'), ('PK', 'podkarpackie'), ('PD', 'podlaskie'), ('PM', 'pomorskie'), ('SL', 'śląskie'), ('SK', 'świętokrzyskie'), ('WN', 'warmińsko-mazurskie'), ('WP', 'wielkopolskie'), ('ZP', 'zachodniopomorskie')], null=True, max_length=20, help_text='Województwo'),
        ),
        migrations.AddField(
            model_name='patient',
            name='street',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='dentist',
            name='professional_title',
            field=models.CharField(max_length=50, help_text='Tytuł zawodowy dentysty'),
        ),
        migrations.AlterField(
            model_name='office',
            name='city',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='office',
            name='email',
            field=models.EmailField(null=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='office',
            name='number',
            field=models.CharField(null=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='office',
            name='office_id',
            field=models.CharField(unique=True, max_length=10, help_text='Indywidualna nazwa kodowa gabinetu'),
        ),
        migrations.AlterField(
            model_name='office',
            name='phone_number',
            field=models.CharField(max_length=15, blank=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], help_text='Numer telefonu'),
        ),
        migrations.AlterField(
            model_name='office',
            name='phone_number_alt',
            field=models.CharField(max_length=15, blank=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], help_text='Alternatywny numer telefonu'),
        ),
        migrations.AlterField(
            model_name='office',
            name='province',
            field=models.CharField(choices=[('DS', 'dolnośląskie'), ('KP', 'kujawsko-pomorskie'), ('LU', 'lubelskie'), ('LB', 'lubuskie'), ('LD', 'łódzkie'), ('MA', 'małopolskie'), ('MZ', 'mazowieckie'), ('OP', 'opolskie'), ('PK', 'podkarpackie'), ('PD', 'podlaskie'), ('PM', 'pomorskie'), ('SL', 'śląskie'), ('SK', 'świętokrzyskie'), ('WN', 'warmińsko-mazurskie'), ('WP', 'wielkopolskie'), ('ZP', 'zachodniopomorskie')], null=True, max_length=20, help_text='Województwo'),
        ),
        migrations.AlterField(
            model_name='office',
            name='street',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=100, help_text='Imię'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pesel',
            field=models.CharField(null=True, max_length=11, help_text='Numer PESEL'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='surname',
            field=models.CharField(max_length=100, help_text='Nazwisko'),
        ),
    ]
