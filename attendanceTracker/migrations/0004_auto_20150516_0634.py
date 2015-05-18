# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceTracker', '0003_auto_20150516_0629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='subject_id_5_to_5',
            new_name='subject_id_5_to_6',
        ),
    ]
