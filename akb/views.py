from akb import models, serializers
from rest_framework import viewsets
from rest_framework.settings import api_settings

class TagViewSet(viewsets.ModelViewSet):
	queryset = models.Tag.objects.all()
	serializer_class = serializers.TagSerializer
	lookup_field = 'name'

class ObjectViewSet(viewsets.ModelViewSet):
	queryset = models.Object.objects.prefetch_related('tags').all()
	serializer_class = serializers.ObjectSerializer
	lookup_field = 'oid'
