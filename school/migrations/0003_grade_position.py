# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_subject_teacher_teacherclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='position',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
