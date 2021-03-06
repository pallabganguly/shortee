# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlShortManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='urlshort',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='urlshort',
            name='shortcode',
            field=models.CharField(blank=True, max_length=64, unique=True),
        ),
    ]
