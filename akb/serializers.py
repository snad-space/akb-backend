from akb import models
from rest_framework import serializers
from django.contrib.auth.models import User

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Tag
		fields = ('id', 'name', 'priority', 'description')

class ObjectSerializer(serializers.ModelSerializer):
	tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=models.Tag.objects, default=[])
	changed_by = serializers.SlugRelatedField(many=False, slug_field='username', allow_null=False, read_only=True)

	def save(self):
		self.validated_data['changed_by'] = self.context['request'].user
		super(ObjectSerializer, self).save()

	class Meta:
		model = models.Object
		fields = ('oid', 'description', 'simbadid', 'tags', 'changed_by', 'changed_at')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		exclude = ('id', 'password')
