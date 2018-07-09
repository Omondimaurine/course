# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='module',
            field=models.ForeignKey(to='courses.Module', null=True, related_name='contents', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='courses_created', blank=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='file_related', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='image_related', blank=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='course',
            field=models.ForeignKey(to='courses.Course', null=True, related_name='modules', blank=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='text_related', blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='video_related', blank=True),
        ),
    ]
