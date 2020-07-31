from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

class WhoamiTest(TestCase):
	def test_whoami_unauthorized(self):
		url = reverse('whoami')
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
	def test_whoami_authorized(self):
		user, _ = User.objects.get_or_create(username='test')
		token = Token.objects.create(user=user)
		client = APIClient()
		client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

		url = reverse('whoami')
		response = client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.json()['username'], user.username)
