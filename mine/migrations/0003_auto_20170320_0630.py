# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0002_auto_20170319_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]
