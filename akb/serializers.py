from akb import models
from rest_framework import serializers
from django.contrib.auth.models import User

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Tag
		fields = ('id', 'name', 'priority', 'description')

class ObjectSerializer(serializers.ModelSerializer):
	tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=models.Tag.objects, default=[])

	class Meta:
		model = models.Object
		fields = ('id', 'oid', 'description', 'simbadid', 'tags')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		exclude = ('id', 'password')
