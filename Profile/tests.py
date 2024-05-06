from django.test import TestCase
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, \
    HTTP_404_NOT_FOUND
from djangoProject.settings.base import API_VERSION
from .models import Profile


class TestSetup(APITestCase):
    def setUp(self):
        self.existing_profile = Profile.objects.create(
            first_name="name",
            last_name="last_name",
            email="email1@gmail.com",
            phone_number="628461779",
            hobbies="eat potato chips and play skirym"
        )
        return super().setUp()

    def tearDown(self):
        self.existing_profile.delete()
        return super().tearDown()


class TestViews(TestSetup):
    def test_get_profile(self):
        resp = self.client.get(f'/api/{API_VERSION}/profile/1/',
                               {}, format="json")
        self.assertEqual(resp.status_code, HTTP_200_OK)

    def test_get_non_existing_profile(self):
        resp = self.client.get(f'/api/{API_VERSION}/profile/99/',
                               {}, format="json")
        self.assertEqual(resp.status_code, HTTP_404_NOT_FOUND)

    def test_create_new_profile(self):
        response = self.client.post(f'/api/{API_VERSION}/signup/',
                                    data={'first_name': "name",
                                          'last_name': "last_name",
                                          'email': "email2@gmail.com",
                                          'phone_number': "628661777",
                                          'hobbies': "play skirym"}, format="json")
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_create_new_profile_with_same_email(self):
        response = self.client.post(f'/api/{API_VERSION}/signup/',
                                    data={'first_name': "name",
                                          'last_name': "last_name",
                                          'email': "email1@gmail.com",
                                          'phone_number': "628661777",
                                          'hobbies': "play skirym"}, format="json")
        self.assertEqual(response.data.get('email'), [ErrorDetail(string='This field must be unique.', code='unique')])
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_create_new_profile_with_same_phone(self):
        response = self.client.post(f'/api/{API_VERSION}/signup/',
                                    data={'first_name': "name",
                                          'last_name': "last_name",
                                          'email': "email1@gmail.com",
                                          'phone_number': "628461779",
                                          'hobbies': "play skirym"}, format="json")
        self.assertEqual(response.data.get('phone_number'),
                         [ErrorDetail(string='This field must be unique.', code='unique')])
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_create_new_profile_without_phone_number(self):
        response = self.client.post(f'/api/{API_VERSION}/signup/',
                                    data={'first_name': "name",
                                          'last_name': "last_name",
                                          'email': "e5@gmail.com",
                                          'hobbies': "play skirym"}, format="json")
        self.assertEqual(response.data.get('phone_number'),
                         [ErrorDetail(string='This field is required.', code='required')])
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_create_new_profile_without_email(self):
        response = self.client.post(f'/api/{API_VERSION}/signup/',
                                    data={'first_name': "name",
                                          'last_name': "last_name",
                                          'phone_number': "628661777",
                                          'hobbies': "play skirym"}, format="json")
        self.assertEqual(response.data.get('email'), [ErrorDetail(string='This field is required.', code='required')])
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_create_new_profile_with_wrong_format_phone_number(self):
        response = self.client.post(f'/api/{API_VERSION}/signup/',
                                    data={'first_name': "name",
                                          'last_name': "last_name",
                                          'email': "e5@gmail.com",
                                          'phone_number': "628777",
                                          'hobbies': "play skirym"}, format="json")
        self.assertEqual(response.data.get('phone_number'),
                         [ErrorDetail(string='Enter a valid phone number.', code='invalid')])
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
