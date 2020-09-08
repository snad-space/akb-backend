from akb import models, serializers
from django.utils.encoding import force_str
from json import JSONDecoder
from rest_framework import viewsets, status
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from reversion.models import Version

class TagViewSet(viewsets.ModelViewSet):
	queryset = models.Tag.objects.all()
	serializer_class = serializers.TagSerializer
	lookup_field = 'name'

class ObjectViewSet(viewsets.ModelViewSet):
	queryset = models.Object.objects.prefetch_related('tags').all()
	serializer_class = serializers.ObjectSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]
	lookup_field = 'oid'

	@action(detail=True, methods=['GET'])
	def log(self, request, oid=None):
		decoder = JSONDecoder()

		def decode(x):
			obj = decoder.decode(force_str(x.serialized_data.encode("utf8")))[0]
			return obj['fields']

		o = self.get_object()
		entries = [decode(x) for x in Version.objects.get_for_object(o)]

		return Response(entries, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def whoami(request):
	return Response(serializers.UserSerializer(request.user).data)
