from rest_framework import serializers

from commerce.models.order import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ('user',)
        model = OrderItem
        fields = (
            'id', 'user', 'ordered', 'item', 'quantity', 'created_at', 'updated_at'
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
