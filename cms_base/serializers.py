from rest_framework import serializers
from cms_base.models import Article, Resource, Tag
from django.contrib.auth.models import User

class UserWithLimitedInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'short_name', 'url', 'resource_type']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag_name']

class ArticleListSerializer(serializers.ModelSerializer):
    author = UserWithLimitedInfoSerializer()
    tag = TagSerializer(many=True)
    class Meta:
        model = Article
        fields = ['title', 'author', 'header_image_src', 'updated_at', 'tag']

class ArticleDetailSerializer(serializers.ModelSerializer):
    author = UserWithLimitedInfoSerializer()
    tag = TagSerializer(many=True)
    resources = ResourceSerializer(many=True)
    class Meta:
        model = Article
        fields = ['title', 'author', 'header_image_src', 'content', 'updated_at', 'tag', 'resources']