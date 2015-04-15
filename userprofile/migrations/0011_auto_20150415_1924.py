# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_currentappliances_appliancetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentappliances',
            name='applianceTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 15, 23, 24, 51, 621000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
