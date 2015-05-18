# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceTracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(max_length=8)),
                ('subject_id_10_to_11', models.ForeignKey(related_name='subject_id_10_to_11', to='attendanceTracker.Subject', null=b'True')),
                ('subject_id_11_to_12', models.ForeignKey(related_name='subject_id_11_to_12', to='attendanceTracker.Subject', null=b'True')),
                ('subject_id_12_to_1', models.ForeignKey(related_name='subject_id_12_to_11', to='attendanceTracker.Subject', null=b'True')),
                ('subject_id_2_to_3', models.ForeignKey(related_name='subject_id_2_to_3', to='attendanceTracker.Subject', null=b'True')),
                ('subject_id_3_to_4', models.ForeignKey(related_name='subject_id_3_to_4', to='attendanceTracker.Subject', null=b'True')),
                ('subject_id_4_to_5', models.ForeignKey(related_name='subject_id_4_to_5', to='attendanceTracker.Subject', null=b'True')),
                ('subject_id_5_to_5', models.ForeignKey(related_name='subject_id_5_to_6', to='attendanceTracker.Subject', null=b'True')),
                ('subject_id_8_to_9', models.ForeignKey(related_name='subject_id_8_to_9', to='attendanceTracker.Subject', null=b'True')),
                ('subject_id_9_to_10', models.ForeignKey(related_name='subject_id_9_to_10', to='attendanceTracker.Subject', null=b'True')),
            ],
        ),
    ]
