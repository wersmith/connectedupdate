# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20150324_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentappliances',
            name='applianceEndTime',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
