from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

class DumpdataTest(TestCase):
	def test_dumpdata_unauthorized(self):
		url = reverse('dumpdata')
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_dumpdata_authorized(self):
		user, _ = User.objects.get_or_create(username='test')
		token = Token.objects.create(user=user)
		client = APIClient()
		client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

		url = reverse('dumpdata')
		response = client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertIsInstance(response.json(), list)
