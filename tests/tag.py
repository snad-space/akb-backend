from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from akb.models import Tag

class TagTest(TestCase):
	def setUp(self):
		self.user, _ = User.objects.get_or_create(username='test')
		self.token = Token.objects.create(user=self.user)
		self.client = APIClient()
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

	def test_tag_create1(self):
		url = reverse('tag-list')
		response = self.client.post(url, {
			'name': 'thetag', 'priority': 1}, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		tag = Tag.objects.get(name='thetag')

	def test_tag_order1(self):
		url = reverse('tag-list')
		response = self.client.post(url, {
			'name': 'thetag', 'priority': 42}, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		response = self.client.post(url, {
			'name': 'mytag', 'priority': 1}, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.json()[0]['id'], 2)
		self.assertEqual(response.json()[1]['id'], 1)
