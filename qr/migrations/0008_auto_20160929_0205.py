# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0007_auto_20160929_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file_id',
        ),
        migrations.AddField(
            model_name='file',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
