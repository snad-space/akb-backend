from akb import models, serializers
from rest_framework import generics, viewsets
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class TagViewSet(viewsets.ModelViewSet):
	queryset = models.Tag.objects.all()
	serializer_class = serializers.TagSerializer
	lookup_field = 'name'

class ObjectViewSet(viewsets.ModelViewSet):
	queryset = models.Object.objects
	serializer_class = serializers.ObjectSerializer
	lookup_field = 'oid'

class RevisionViewSet(viewsets.ModelViewSet):
	queryset = models.Revision.objects.prefetch_related('tags').prefetch_related('object').all()
	serializer_class = serializers.RevisionSerializer

class RevisionObjectViewSet(generics.ListAPIView):
	queryset = models.Revision.objects.prefetch_related('tags').prefetch_related('object').all()
	serializer_class = serializers.RevisionSerializer

	def get_queryset(self):
		oid = self.kwargs['oid']
		object = models.Object.objects.get(oid=oid)
		return models.Revision.objects.filter(object=object)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def whoami(request):
	return Response(serializers.UserSerializer(request.user).data)
