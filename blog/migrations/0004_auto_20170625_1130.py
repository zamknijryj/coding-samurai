# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=30),
        ),
    ]
