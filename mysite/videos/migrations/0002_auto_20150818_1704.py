# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='id',
        ),
        migrations.AddField(
            model_name='video',
            name='hidden',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(default='Temp', primary_key=True, unique=True, serialize=False),
            preserve_default=False,
        ),
    ]
