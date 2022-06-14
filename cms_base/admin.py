from django.contrib import admin
from cms_base.models import Article, Resource, Tag

class ResourcesInline(admin.TabularInline):
    model = Resource
    fk_name = 'owned_article'

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ResourcesInline]
    readonly_fields=('author',)
    list_display = ('title', 'created_at')
    list_filter = ('tag', 'status', 'author')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)

