from rest_framework import generics, permissions

from commerce.models.category import Category
from commerce.serializers.category_serializer import CategorySerializer


class CategoryCrateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAdminUser,)


class CategoryUpdateDeleteView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAdminUser,)
