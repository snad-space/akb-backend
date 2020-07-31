from akb import models, serializers
from rest_framework import viewsets
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class TagViewSet(viewsets.ModelViewSet):
	queryset = models.Tag.objects.all()
	serializer_class = serializers.TagSerializer
	lookup_field = 'name'

class ObjectViewSet(viewsets.ModelViewSet):
	queryset = models.Object.objects.prefetch_related('tags').all()
	serializer_class = serializers.ObjectSerializer
	lookup_field = 'oid'

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def whoami(request):
	return Response(serializers.UserSerializer(request.user).data)
