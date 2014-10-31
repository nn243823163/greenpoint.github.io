# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osb', '0005_auto_20141031_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=128, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1'),
            preserve_default=True,
        ),
    ]
