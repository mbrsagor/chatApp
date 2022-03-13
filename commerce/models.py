from django.db import models


class CoreEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(CoreEntity):
    name = models.CharField(max_length=70, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, related_name='parentCategory')
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='category', blank=True, null=True, default='/static/category.svg')

    def __str__(self):
        return self.name


class Tag(CoreEntity):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
