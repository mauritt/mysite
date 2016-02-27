# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_auto_20150820_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
