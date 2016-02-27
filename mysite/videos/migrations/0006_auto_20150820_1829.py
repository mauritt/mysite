# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20150820_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
