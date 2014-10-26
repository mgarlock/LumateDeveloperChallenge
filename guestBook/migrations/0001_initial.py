# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_address', models.CharField(max_length=45, verbose_name=b'IP Address')),
                ('access_date', models.DateTimeField(verbose_name=b'Access Time')),
                ('f_name', models.CharField(max_length=30, verbose_name=b'First Name')),
                ('l_name', models.CharField(max_length=30, verbose_name=b'Last Name')),
                ('favorite_dino', models.CharField(max_length=50, verbose_name=b'Favorite Dinosaur')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
