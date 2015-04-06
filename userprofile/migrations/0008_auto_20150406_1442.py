# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_auto_20150405_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentappliances',
            name='applianceName',
            field=models.ForeignKey(related_name='appliance', to='userprofile.AppliancePreferences'),
            preserve_default=True,
        ),
    ]
