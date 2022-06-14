from cms_base.models import Tag
from cms_base.serializers import TagSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

class TagViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving operations on tag object.
    """
    def list(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Tag.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = TagSerializer(user)
        return Response(serializer.data)
