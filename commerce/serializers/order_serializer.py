from rest_framework import serializers

from commerce.models.order import Order, OrderItem
from commerce.serializers.product_serializer import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ('user',)
        model = OrderItem
        fields = (
            'id', 'user', 'ordered', 'item', 'quantity', 'get_total_price',
            'get_total_discounted_price', 'get_amount_saved', 'get_final_price',
            'created_at', 'updated_at',
        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['item'] = ProductSerializer(instance.item).data
        return response


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
