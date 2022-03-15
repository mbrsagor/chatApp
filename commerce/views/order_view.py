from rest_framework import generics

from commerce.models.order import Order, OrderItem
from commerce.serializers.order_serializer import OrderSerializer, OrderItemSerializer


class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CreateOrderItemView(generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
