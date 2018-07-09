# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20180703_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(null=True, to='courses.Subject', blank=True, related_name='subject'),
        ),
    ]
