from cms_base.models import Tag, Article
from cms_base.serializers import TagSerializer, ArticleListSerializer, ArticleDetailSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import viewsets, mixins
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
        tag = get_object_or_404(queryset, pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)


class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    A simple ViewSet for listing or retrieving operations on article object.
    """
    serializer_class = ArticleListSerializer

    def list(self, request):
        """
        In our mobile application or website we need only published articles.
        Also need to order queryset for newest to older.
        """

        # Status 'Published' is my prequisite 
        query = Q(status='P')

        # If there is parameter in get request as tag, need to query on results
        if request.GET.get('tag') is not None:
            query = query & Q(tag=request.GET.get('tag'))

        queryset =self.filter_queryset(Article.objects.filter(query).order_by('-updated_at'))

        # Get page param from request
        page = request.GET.get('page')

        # Try to paginate results
        try: 
            page = self.paginate_queryset(queryset)
        except Exception as e:
            page = []
            data = page
            return Response({
                "status": 400,
                "message": "Please contact system admin",
                "data" : data
                })

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = serializer.data
            return self.get_paginated_response(data)
        else:
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "status": 200,
                "data" : data
            })

    def retrieve(self, request, pk=None):
        # User can't get details of unpublished article with id request
        queryset = Article.objects.filter(status='P')
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)
