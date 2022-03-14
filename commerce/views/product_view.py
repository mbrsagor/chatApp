from rest_framework import generics, status
from rest_framework.response import Response

from commerce.models.product import Product
from commerce.serializers.product_serializer import ProductSerializer
from commerce.utils.response import prepare_create_success_response, prepare_success_response, prepare_error_response


class CreateListProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(owner=self.request.user)
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        else:
            return Response(prepare_error_response('You have no permission to add product'),
                            status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        product = Product.objects.filter(owner=self.request.user)
        if product:
            serializer = ProductSerializer(product, many=True)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        else:
            return Response(prepare_error_response('No Product found'), status=status.HTTP_400_BAD_REQUEST)


class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    # def get_product(self, pk):
    #     try:
    #         return Product.objects.get(id=pk)
    #     except Product.DoesNotExist:
    #         return None

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response(prepare_success_response('Data deleted successfully'), status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(prepare_error_response('Content Not found'), status=status.HTTP_400_BAD_REQUEST)
