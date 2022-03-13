from rest_framework import generics, status
from rest_framework.response import Response

from commerce.models.product import Product
from commerce.serializers.product_serializer import ProductSerializer
from commerce.utils.response import prepare_create_success_response, prepare_success_response


class CreateListProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(owner=self.request.user)
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        product = Product.objects.filter(owner=self.request.user)
        serializer = ProductSerializer(product, many=True)
        return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
