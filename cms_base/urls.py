from cms_base.views import TagViewSet, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'articles', ArticleViewSet, basename='article')
urlpatterns = router.urls