from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ArticleView, SingleArticleView, ArticleViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='user')

urlpatterns = router.urls