# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180627_0617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='order',
        ),
    ]
