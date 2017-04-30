# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0004_myuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='t',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
