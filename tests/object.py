from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from akb.models import Object, Tag

class ObjectTest(TestCase):
	def setUp(self):
		self.user, _ = User.objects.get_or_create(username='test')
		self.token = Token.objects.create(user=self.user)
		self.client = APIClient()
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

	def test_object_create1(self):
		url = reverse('object-list')
		response = self.client.post(url, {
			'oid': 695211400132640,
			'description': 'text'}, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		pk = response.json()['id']
		o = Object.objects.get(pk=pk)
		self.assertEqual(o.oid, 695211400132640)
		self.assertEqual(o.description, 'text')

	def test_object_create2(self):
		tags = [Tag.objects.create(name="thetag", priority=1), Tag.objects.create(name="othertag", priority=2)]
		url = reverse('object-list')
		response = self.client.post(url, {
			'oid': 695211400132640,
			'description': 'text',
			'tags': ["thetag", "othertag"]}, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		pk = response.json()['id']
		o = Object.objects.get(pk=pk)
		self.assertEqual(o.oid, 695211400132640)
		self.assertEqual(o.description, 'text')
		self.assertListEqual(list(o.tags.all()), tags)
		self.assertListEqual(list(tags[0].tagged_objects.all()), [o,])
		self.assertListEqual(list(tags[1].tagged_objects.all()), [o,])

	def test_object_lookup1(self):
		tags = [Tag.objects.create(name="thetag", priority=1), Tag.objects.create(name="othertag", priority=2)]
		o = Object.objects.create(oid = 695211400132640, description = 'description')
		o.tags.set(tags)
		o.save()
		url = reverse('object-detail', args=[695211400132640])
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.json()["oid"], 695211400132640)
