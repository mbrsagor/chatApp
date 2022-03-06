from django.db import models
from django.contrib.auth.models import User


class DomainEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(DomainEntity):
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='parentCategory', blank=True, null=True)
    image = models.ImageField(upload_to='category', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Tag(DomainEntity):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(DomainEntity):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogCategory')
    tags = models.ManyToManyField(Tag, related_name='tag', blank=True)
    content = models.TextField()
    is_draft = models.BooleanField(default=False)
    is_publish = models.BooleanField(default=True)
    image = models.ImageField(upload_to='blog', blank=True, null=True)

    def __str__(self):
        return self.title[:30]
