from rest_framework import serializers

from .models import Category, Article, Tag, Comment


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id', 'name'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        depth = 1
        fields = [
            'id',
            'user',
            'slug',
            'title',
            'categories',
            'tags',
            'content',
            'is_draft',
            'is_publish',
            'total_articles',
            'total_publish_articles',
            'total_draft_articles',
            'image',
            'created_at',
            'updated_at',
        ]


class ArticleCreateSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True).data

    def get_or_create_tag(self, tags):
        tag_ids = []
        for tag in tags:
            tag_instance, create = Tag.objects.get_or_create(pk=tag.get('id'), defaults=tag)
            tag_ids.append(tag_instance.pk)
        return tag_ids

    def create_or_update_tag(self, tags):
        tag_ids = []
        for tag in tags:
            tag_instance, create = Tag.objects.update_or_create(pk=tag.get('id'), defaults=tag)
            tag_ids.append(tag_instance.pk)
        return tag_ids

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        item = Article.objects.create(**validated_data)
        item.tags.set(self.get_or_create_tag(tags))
        return item

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', [])
        instance.tags.set(self.create_or_update_tag(tags))
        return instance

    class Meta:
        model = Article
        read_only_fields = ('author',)
        fields = [
            'id',
            'user',
            'slug',
            'title',
            'categories',
            'tags',
            'content',
            'is_draft',
            'is_publish',
            'image',
            'created_at',
            'updated_at',
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
