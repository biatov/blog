# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 16:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal_page', '0002_post_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
    ]
