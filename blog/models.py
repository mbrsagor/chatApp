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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
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

    @property
    def total_articles(self):
        return Article.objects.count()

    @property
    def total_publish_articles(self):
        return Article.objects.filter(is_publish=True).count()

    @property
    def total_draft_articles(self):
        return Article.objects.filter(is_draft=True).count()


class Comment(DomainEntity):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentUser')
    text = models.TextField()
    articles = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentArticle')

    def __str__(self): return self.text
