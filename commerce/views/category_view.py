from rest_framework import generics

from commerce.models.category import Category
from commerce.serializers.category_serializer import CategorySerializer


class CategoryCrateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def list(self, request, *args, **kwargs):
    #     pass
