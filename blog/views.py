from rest_framework import generics, status, permissions
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer


class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)
