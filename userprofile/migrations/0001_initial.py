# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppliancePreferences',
            fields=[
                ('homeID', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('applianceID', models.IntegerField()),
                ('applianceName', models.CharField(max_length=50)),
                ('timeLapseAlarm', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfileData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dob', models.DateField()),
                ('dateJoined', models.DateField(auto_now_add=True)),
                ('userID', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='appliancepreferences',
            name='userID',
            field=models.ForeignKey(to='userprofile.UserProfileData'),
            preserve_default=True,
        ),
    ]
