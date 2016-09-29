# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_signed', models.BooleanField(default=False)),
                ('qr_code', models.ImageField(upload_to=b'')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('signed_at', models.DateTimeField()),
            ],
        ),
    ]
