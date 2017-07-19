# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-19 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('weight', models.DecimalField(decimal_places=3, max_digits=7)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('category', models.CharField(max_length=20)),
            ],
        ),
    ]
