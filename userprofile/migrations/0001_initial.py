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
            name='ApplianceInfo',
            fields=[
                ('applianceSupplierID', models.AutoField(serialize=False, primary_key=True)),
                ('applianceNameSupplier', models.CharField(max_length=50)),
                ('applianceDescription', models.TextField(max_length=300)),
                ('applianceHeight', models.IntegerField()),
                ('applianceWidth', models.IntegerField()),
                ('applianceDepth', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AppliancePreferences',
            fields=[
                ('inputID', models.AutoField(serialize=False, primary_key=True)),
                ('applianceName', models.CharField(max_length=50)),
                ('timeLapseAlarm', models.IntegerField()),
                ('applianceSupplierID', models.ForeignKey(to='userprofile.ApplianceInfo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CurrentAppliances',
            fields=[
                ('sessionID', models.AutoField(serialize=False, primary_key=True)),
                ('applianceStartTime', models.TimeField()),
                ('applianceEndTime', models.TimeField()),
                ('applianceSupplierID', models.ForeignKey(to='userprofile.ApplianceInfo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HomeInfo',
            fields=[
                ('homeID', models.AutoField(serialize=False, primary_key=True)),
                ('homeSquareFeet', models.IntegerField()),
                ('homeStreetAddress', models.CharField(max_length=50)),
                ('homeCity', models.CharField(max_length=50)),
                ('homeZIP', models.IntegerField(max_length=5)),
                ('homeState', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoomInfo',
            fields=[
                ('roomID', models.AutoField(serialize=False, primary_key=True)),
                ('roomName', models.CharField(max_length=50)),
                ('homeID', models.ForeignKey(to='userprofile.HomeInfo')),
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
            name='homeID',
            field=models.ForeignKey(to='userprofile.HomeInfo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appliancepreferences',
            name='roomID',
            field=models.ForeignKey(to='userprofile.RoomInfo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appliancepreferences',
            name='userID',
            field=models.ForeignKey(to='userprofile.UserProfileData'),
            preserve_default=True,
        ),
    ]
