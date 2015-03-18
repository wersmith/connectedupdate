# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiledata',
            name='displayname',
            field=models.CharField(default=datetime.datetime(2015, 2, 28, 18, 13, 18, 722000, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]
