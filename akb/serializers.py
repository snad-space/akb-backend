from akb import models
from rest_framework import serializers
from django.contrib.auth.models import User

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Tag
		fields = ('id', 'name', 'priority', 'description')

class ObjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Object
		fields = ('id', 'oid')

class RevisionSerializer(serializers.ModelSerializer):
	object = serializers.SlugRelatedField(many=False, slug_field='oid', queryset=models.Object.objects)
	tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=models.Tag.objects, default=[])

	class Meta:
		model = models.Revision
		fields = ('id', 'object', 'date', 'description', 'simbadid', 'tags')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		exclude = ('id', 'password')
