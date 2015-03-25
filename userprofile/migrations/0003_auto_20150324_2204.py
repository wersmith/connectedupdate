# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_remove_appliancepreferences_appliancesupplierid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentappliances',
            name='applianceSupplierID',
        ),
        migrations.AddField(
            model_name='currentappliances',
            name='applianceID',
            field=models.ForeignKey(default=2, to='userprofile.AppliancePreferences'),
            preserve_default=False,
        ),
    ]
