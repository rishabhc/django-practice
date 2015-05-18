# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_name', models.CharField(max_length=50)),
                ('classes_held', models.IntegerField(default=0)),
                ('classes_attended', models.IntegerField(default=0)),
                ('percentage_attendance', models.FloatField(default=0)),
            ],
        ),
    ]
