from rest_framework import generics, status, permissions
from rest_framework.response import Response

from .models import Category, Article
from .serializers import CategorySerializer, ArticleSerializer


class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.filter(is_publish=True, is_draft=False)
    serializer_class = ArticleSerializer
    permission_classes = (permissions.AllowAny,)
