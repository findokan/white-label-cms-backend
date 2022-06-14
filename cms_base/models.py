from django.db import models

# imported for WYSIWYG editor
from tinymce.models import HTMLField

# imported for author field in Article object
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(BaseModel):
    tag_name = models.CharField(max_length=30)

    def __str__(self):
        return self.tag_name

class Article(BaseModel):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    header_image_src = models.URLField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=200)
    content = HTMLField()
    tag = models.ManyToManyField(Tag)

    STATUS_TYPES = (
        ('U', 'Unpublished'),
        ('P', 'Published'),
    )
    status = models.CharField(max_length=1, choices=STATUS_TYPES)

    def __str__(self):
        return self.title


class Resource(BaseModel):
    url = models.URLField(max_length=300)
    short_name = models.CharField(max_length=50)
    RESOURCE_TYPES = (
        ('A', 'Article'),
        ('V', 'Video'),
    )
    resource_type = models.CharField(max_length=1, choices=RESOURCE_TYPES)
    owned_article = models.ForeignKey(Article, related_name='resources', on_delete=models.CASCADE)

    def __str__(self):
        return self.short_name
