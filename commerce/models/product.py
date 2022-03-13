from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save

from commerce.models import Category, Tag
from commerce.models.core import CoreEntity
from commerce.utils.enum import TYPES


class Product(CoreEntity):
    item_name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='item_shop')
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='item_category')
    tags = models.ManyToManyField(Tag, related_name='item_tag')
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=7)
    discount_price = models.DecimalField(max_digits=10, decimal_places=7)
    short_description = models.TextField(default='')
    model = models.CharField(max_length=60, blank=True, null=True)
    serial_number = models.CharField(max_length=90, blank=True, null=True)
    item_type = models.IntegerField(choices=TYPES.select_types(), default=TYPES.KG.value)
    item_image = models.ImageField(upload_to='item/%y/%m', blank=True, null=True)
    galley_image = models.ImageField(upload_to='item/gallery/%y/%m', blank=True, null=True)
    galley_image2 = models.ImageField(upload_to='item/gallery/%y/%m', blank=True, null=True)
    galley_image3 = models.ImageField(upload_to='item/gallery/%y/%m', blank=True, null=True)

    def __str__(self):
        return self.item_name[:50]

    def save(self, *args, **kwargs):
        value = self.item_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


@receiver(pre_save, sender=Product)
def store_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.item_name)
