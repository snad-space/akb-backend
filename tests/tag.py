from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from akb.models import Tag

class TagTest(TestCase):
	def setUp(self):
		self.client = APIClient()

	def test_tag_create1(self):
		url = reverse('tag-list')
		response = self.client.post(url, {
			'name': 'thetag'}, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		tag = Tag.objects.get(name='thetag')
