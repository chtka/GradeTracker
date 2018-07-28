from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from professors.models import Professor

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

PROFESSOR_1_DATA = {
    'first_name': 'Gary',
    'last_name': 'Gillespie',
    'biography': 'Professor for CSE 12, CSE 15L, and CSE 110.'
}

PROFESSOR_2_DATA = {
    'first_name': 'Rick',
    'last_name': 'Ord',
    'biography': 'Professor for CSE 11 and CSE 30.'
}

class ProfessorAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):

        cls.client = APIClient()

        cls.admin_user = User(**ADMIN_USER_DATA)
        cls.admin_user.is_staff = True
        cls.admin_user.save()
        
        cls.user = User(**USER_DATA)
        cls.user.save()

        cls.professor_1 = Professor(**PROFESSOR_1_DATA)
        cls.professor_1.save()

    def test_post_professor_list_admin(self):

        self.client.force_authenticate(self.admin_user)

        response = self.client.post(reverse('professor_list'), PROFESSOR_2_DATA)
        professor = get_or_none(Professor, **PROFESSOR_2_DATA)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(professor, None)
        self.client.logout()

    def test_post_professor_list_no_admin(self):

        self.client.force_authenticate(self.user)

        response = self.client.post(reverse('professor_list'), PROFESSOR_2_DATA)
        professor = get_or_none(Professor, **PROFESSOR_2_DATA)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(professor, None)
        self.client.logout()

    def test_get_professor_list_admin(self):

        self.client.force_authenticate(self.admin_user)

        response = self.client.get(reverse('professor_list'))

        self.assertEqual(len(response.data['results']), 1)

    def test_get_professore_list_no_admin(self):

        self.client.force_authenticate(self.user)

        response = self.client.get(reverse('professor_list'))
        
        self.assertEqual(len(response.data['results']), 1)