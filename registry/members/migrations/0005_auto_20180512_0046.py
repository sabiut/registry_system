# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-12 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20180424_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='Comments',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='contacts',
            name='Congregation',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='contacts',
            name='Middle_Name',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='contacts',
            name='Status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('Missing', 'Missing'), ('Unknown', 'Unknow'), ('Transfer', 'Transfer')], default='', max_length=100),
        ),
    ]