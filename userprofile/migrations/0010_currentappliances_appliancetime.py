# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_remove_currentappliances_appliancetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentappliances',
            name='applianceTime',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
