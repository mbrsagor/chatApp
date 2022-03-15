from rest_framework import generics, status
from rest_framework.response import Response

from commerce.models.order import Order, OrderItem
from commerce.serializers.order_serializer import OrderSerializer, OrderItemSerializer
from commerce.utils.response import prepare_create_success_response, prepare_success_response, prepare_error_response


class CreateListOrderItemView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.filter(ordered=False)
    serializer_class = OrderItemSerializer

    def post(self, request, *args, **kwargs):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=self.request.user)
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            order_item = OrderItem.objects.filter(user=self.request.user)
            serializer = OrderItemSerializer(order_item, many=True)
            return Response(prepare_success_response(serializer.data))
        else:
            order_item = OrderItem.objects.all()
            serializer = OrderItemSerializer(order_item, many=True)
            return Response(prepare_success_response(serializer.data))


class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
