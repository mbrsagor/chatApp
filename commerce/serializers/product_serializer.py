from rest_framework import serializers

from commerce.models.product import Product
from commerce.serializers.category_serializer import CategorySerializer, TagSerializer


class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True).data

    class Meta:
        model = Product
        read_only_fields = ('owner',)
        fields = (
            'id', 'item_name', 'owner', 'categories', 'tags', 'is_available', 'price', 'discount_price',
            'short_description', 'model', 'serial_number', 'item_type', 'item_image', 'galley_image',
            'galley_image2', 'galley_image3', 'created_at', 'updated_at'

        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['categories'] = CategorySerializer(instance.categories).data
        return response


class GenericProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        depth = 2
        fields = '__all__'
