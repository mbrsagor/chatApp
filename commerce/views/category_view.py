from rest_framework import generics, permissions

from commerce.models.category import Category, Model
from commerce.serializers.category_serializer import CategorySerializer, ModelSerializer


class CategoryCrateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAdminUser,)


class CategoryUpdateDeleteView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAdminUser,)


class ModelAPIView(generics.ListCreateAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    # permission_classes = (permissions.IsAdminUser,)
