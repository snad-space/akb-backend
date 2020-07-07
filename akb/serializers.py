from akb import models
from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Tag
		fields = ('id', 'name')

class ObjectSerializer(serializers.ModelSerializer):
	tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=models.Tag.objects, default=[])

	class Meta:
		model = models.Object
		fields = ('id', 'oid', 'description', 'tags')
