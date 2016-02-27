# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20150818_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='embed',
        ),
        migrations.AddField(
            model_name='video',
            name='key',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
