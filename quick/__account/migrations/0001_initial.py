# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('first_name', models.CharField(default=b'', max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(default=b'', max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='email')),
                ('phone', models.CharField(default=b'', max_length=30, verbose_name='phone', blank=True)),
                ('profit', models.CharField(default=b'', max_length=2, verbose_name='profit', blank=True)),
                ('joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='joined')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('avatar', models.ImageField(upload_to=b'%Y/%m/%d', verbose_name='photo', blank=True)),
            ],
            options={
                'ordering': ('joined',),
            },
            bases=(models.Model,),
        ),
    ]
