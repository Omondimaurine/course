from django.test import TestCase
from courses.models import Course,Subject
from django.utils import timezone
from courses.models import Module
# from django.core import serializers
from django.contrib.auth.models import User
import sys
# from django.core.urlresolvers import reverse


class CourseModelTests(TestCase):
    def setUp(self):
        pass
    
    def test_course_creation(self):
        subject = Subject.objects.create()
        user = User.objects.create()
        course=Course.objects.create(
            owner=user,
            subject=subject
        )
        self.assertEqual(course.owner.id, user.id)



        






        

    
    
    
