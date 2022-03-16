from rest_framework import generics, permissions

from commerce.models.category import Category, Model, Brand
from commerce.serializers.category_serializer import CategorySerializer, ModelSerializer, BrandSerializer


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
    permission_classes = (permissions.IsAuthenticated,)


class ModelUpdateDeleteView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class BrandCrateListAPIView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (permissions.IsAdminUser,)


class BrandUpdateDeleteView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (permissions.IsAdminUser,)
