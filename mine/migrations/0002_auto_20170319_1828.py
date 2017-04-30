# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='contact',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='address',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
