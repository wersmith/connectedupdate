# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_auto_20150324_2208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currentappliances',
            old_name='applianceStartTime',
            new_name='applianceTime',
        ),
        migrations.RemoveField(
            model_name='currentappliances',
            name='applianceEndTime',
        ),
        migrations.AddField(
            model_name='currentappliances',
            name='applianceState',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
