# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('guestBook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestlog',
            name='access_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Access Time'),
            preserve_default=True,
        ),
    ]
