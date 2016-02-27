# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_auto_20150818_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='slug',
            field=models.SlugField(default='temp'),
        ),
        migrations.AddField(
            model_name='role',
            name='slug',
            field=models.SlugField(default='temp'),
        ),
    ]
