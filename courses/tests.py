from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from courses.models import Course

def get_or_none(Model, **conditions):
    try:
        model = Model.objects.get(**conditions)
    except Model.DoesNotExist:
        model = None

    return model

ADMIN_USER_DATA = {
    'username': 'fake-admin-user',
    'password': 'fake-admin-user'
}

USER_DATA = {
    'username': 'fake-user',
    'password': 'fake-user'
}

COURSE_1_DATA = {
    'department': 'CSE',
    'number': '110',
    'verbose_name': 'Software Engineering'
}

COURSE_2_DATA = {
    'department': 'CSE',
    'number': '100',
    'verbose_name': 'Advanced Data Structures'
}

class CourseAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):

        cls.client = APIClient()

        cls.admin_user = User(**ADMIN_USER_DATA)
        cls.admin_user.is_staff = True
        cls.admin_user.save()
        
        cls.user = User(**USER_DATA)
        cls.user.save()

        cls.course_1 = Course(**COURSE_1_DATA)
        cls.course_1.save()

    def test_post_course_list_admin(self):

        self.client.force_authenticate(self.admin_user)

        response = self.client.post(reverse('course_list'), COURSE_2_DATA)
        course = get_or_none(Course, **COURSE_2_DATA)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(course, None)
        self.client.logout()

    def test_post_course_list_no_admin(self):

        self.client.force_authenticate(self.user)

        response = self.client.post(reverse('course_list'), COURSE_2_DATA)
        course = get_or_none(Course, **COURSE_2_DATA)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(course, None)
        self.client.logout()

    def test_get_course_list_admin(self):

        self.client.force_authenticate(self.admin_user)

        response = self.client.get(reverse('course_list'))

        self.assertEqual(len(response.data['results']), 1)

    def test_get_course_list_no_admin(self):

        self.client.force_authenticate(self.user)

        response = self.client.get(reverse('course_list'))
        
        self.assertEqual(len(response.data['results']), 1)