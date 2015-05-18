# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceTracker', '0002_timetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='subject_id_10_to_11',
            field=models.ForeignKey(related_name='subject_id_10_to_11', blank=True, to='attendanceTracker.Subject', null=b'True'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_id_11_to_12',
            field=models.ForeignKey(related_name='subject_id_11_to_12', blank=True, to='attendanceTracker.Subject', null=b'True'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_id_12_to_1',
            field=models.ForeignKey(related_name='subject_id_12_to_11', blank=True, to='attendanceTracker.Subject', null=b'True'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_id_2_to_3',
            field=models.ForeignKey(related_name='subject_id_2_to_3', blank=True, to='attendanceTracker.Subject', null=b'True'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_id_3_to_4',
            field=models.ForeignKey(related_name='subject_id_3_to_4', blank=True, to='attendanceTracker.Subject', null=b'True'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_id_4_to_5',
            field=models.ForeignKey(related_name='subject_id_4_to_5', blank=True, to='attendanceTracker.Subject', null=b'True'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_id_5_to_5',
            field=models.ForeignKey(related_name='subject_id_5_to_6', blank=True, to='attendanceTracker.Subject', null=b'True'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_id_8_to_9',
            field=models.ForeignKey(related_name='subject_id_8_to_9', blank=True, to='attendanceTracker.Subject', null=b'True'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_id_9_to_10',
            field=models.ForeignKey(related_name='subject_id_9_to_10', blank=True, to='attendanceTracker.Subject', null=b'True'),
        ),
    ]
