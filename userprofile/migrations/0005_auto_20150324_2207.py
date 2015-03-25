# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20150324_2204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currentappliances',
            old_name='applianceID',
            new_name='applianceName',
        ),
    ]
