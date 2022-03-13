from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from commerce.models import Category, Tag
from commerce.models.core import CoreEntity
from commerce.utils.enum import TYPES


class Product(CoreEntity):
    item_name = models.CharField(max_length=120)
    # slug = models.AutoSlugField(populate_from='item_name')
    slug = models.SlugField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='item_shop')
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='item_category')
    tags = models.ManyToManyField(Tag, related_name='item_tag')
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    discount_price = models.DecimalField(max_digits=20, decimal_places=10)
    short_description = models.TextField(default='')
    model = models.TextField(max_length=60, blank=True, null=True)
    serial_number = models.TextField(max_length=90, blank=True, null=True)
    item_type = models.IntegerField(choices=TYPES.select_types(), default=TYPES.KG.value)
    item_image = models.ImageField(upload_to='item/%y/%m', blank=True, null=True)
    galley_image = models.ImageField(upload_to='item/gallery/%y/%m', blank=True, null=True)
    galley_image2 = models.ImageField(upload_to='item/gallery/%y/%m', blank=True, null=True)
    galley_image3 = models.ImageField(upload_to='item/gallery/%y/%m', blank=True, null=True)

    def __str__(self):
        return self.item_name[:50]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.item_name)
        super(Product, self).save(*args, **kwargs)
